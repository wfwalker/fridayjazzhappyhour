import os
import sys
import re
import csv

# Add current directory to path to import archive_utils
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from archive_utils import parse_archive_csv, slugify

csv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "FJHH songs - Songs.csv")
images_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "website", "assets", "images", "title-slides")

# Step 1: Read the CSV directly to map ALL dates (including empty song rows like Episode 261) to their Episode #
date_to_epi_raw = {}
with open(csv_path, mode='r', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    header = next(reader)
    header_lower = [h.strip().lower() for h in header]
    date_idx = header_lower.index('date') if 'date' in header_lower else 0
    epi_idx = header_lower.index('epi #') if 'epi #' in header_lower else 1
    
    for row in reader:
        if len(row) > max(date_idx, epi_idx):
            d = row[date_idx].strip()
            e = row[epi_idx].strip()
            if d and e:
                # Normalize date format to M/D/YYYY
                parts = d.split('/')
                if len(parts) == 3:
                    normalized_date = f"{int(parts[0])}/{int(parts[1])}/{parts[2]}"
                    date_to_epi_raw[normalized_date] = e

# Step 2: Load the full archive data using archive_utils to get rerun information
archive_data = parse_archive_csv(csv_path)
episodes_data = archive_data["episodes_data"]
rerun_keys = archive_data["rerun_keys"]
canonical_dates = archive_data["canonical_dates"]

# Month mapping for parsing filename strings
month_map = {
    "jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6, "june": 6,
    "jul": 7, "july": 7, "aug": 8, "sep": 9, "sept": 9, "oct": 10, "nov": 11, "dec": 12
}

# Explicit date corrections for known typos/timezone shifts in image filenames
manual_date_corrections = {
    "4/23/2026": "4/24/2026",  # Episode 296 (was off by 1 day)
    "1/6/2022": "1/7/2022",    # Episode 95 (was off by 1 day)
    "3/18/2022": "3/17/2022",  # Episode 105 (was off by 1 day)
    "9/6/2024": "9/7/2024",    # Episode 223 (was off by 1 day)
    "11/2/2021": "11/5/2021",  # Episode 86 (was off by 3 days)
}

# Regex to match filenames like FJHH-titlecard-monthDay-year.ext (year optional)
filename_regex = re.compile(
    r"^FJHH-titlecard-([a-zA-Z]+)(\d+)(?:st|nd|rd|th)?(?:-(\d{4}))?\.(jpg|png|jpeg)$",
    re.IGNORECASE
)

renamed_count = 0
unmatched_files = []

for filename in sorted(os.listdir(images_dir)):
    # Keep dateless utility slides as-is
    if filename in ["FJHH-titlecard-dateless.jpg", "FJHH-titlecard-howitworks.png", "FJHH-titlecard-nodate.jpg", "FJHH-titlecard-apr17-videoblack.png"]:
        continue
        
    match = filename_regex.match(filename)
    if not match:
        unmatched_files.append((filename, "Does not match date pattern"))
        continue
        
    month_str, day_str, year_str, ext = match.groups()
    month_key = month_str.lower()
    if month_key not in month_map:
        unmatched_files.append((filename, f"Unknown month abbreviation: {month_str}"))
        continue
        
    month = month_map[month_key]
    day = int(day_str)
    
    # Resolve year
    if year_str:
        year = int(year_str)
    else:
        # Fallback: find year by matching month/day in the CSV
        matching_years = []
        for (epi, d_str) in episodes_data.keys():
            parts = d_str.split('/')
            if len(parts) == 3 and int(parts[0]) == month and int(parts[1]) == day:
                matching_years.append(int(parts[2]))
        if len(matching_years) == 1:
            year = matching_years[0]
        else:
            unmatched_files.append((filename, f"Ambiguous year for {month}/{day}"))
            continue
            
    date_key = f"{month}/{day}/{year}"
    
    # Apply manual date corrections
    if date_key in manual_date_corrections:
        date_key = manual_date_corrections[date_key]
        
    # Determine the Episode # and Slug
    epi = date_to_epi_raw.get(date_key, None)
    
    # If the episode wasn't in raw mapping, try finding it in episodes_data
    if not epi:
        for (e_num, d_str), data in episodes_data.items():
            if d_str == date_key:
                epi = e_num
                break
                
    # Generate the standard slug
    is_rerun = (epi, date_key) in rerun_keys
    if epi:
        if is_rerun:
            slug = f"episode-{slugify(epi)}-rerun-{slugify(date_key)}"
        else:
            slug = f"episode-{slugify(epi)}"
    else:
        slug = f"show-{slugify(date_key)}"
        
    new_filename = f"{slug}.{ext.lower()}"
    
    old_path = os.path.join(images_dir, filename)
    new_path = os.path.join(images_dir, new_filename)
    
    # Perform the rename
    try:
        os.rename(old_path, new_path)
        print(f"Renamed: {filename} -> {new_filename} (Resolved Date: {date_key})")
        renamed_count += 1
    except Exception as e:
        print(f"Error renaming {filename}: {e}")

print(f"\nSuccessfully renamed {renamed_count} files.")
if unmatched_files:
    print(f"\nLeft {len(unmatched_files)} files unchanged:")
    for fn, reason in unmatched_files:
        print(f"  - {fn}: {reason}")
