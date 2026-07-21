import os
import sys
import re
import csv
import xml.etree.ElementTree as ET
import difflib

# Common Ableton section cues and structural labels to ignore as song starts
CUE_BLACKLIST = {
    "INTRO", "VERSE", "CHORUS", "LAST CHORUS", "HEAD", "LAST HEAD", 
    "BREAK", "PICKUP", "BOMP", "VCV OFF", "MELODICER", "OUTRO", "SOLO"
}

def is_valid_song_name(name):
    """Filters out cued markers, cased numbers, and structural track section labels."""
    name = name.strip()
    
    # 1. Must be in ALL CAPS
    if not name.isupper():
        return False
        
    # 2. Filter out single-word structural cues
    if name in CUE_BLACKLIST:
        return False
        
    # 3. Filter out structural markers like A 1, B 2, C 12 (Letter + space + digit)
    if re.match(r'^[A-Z]\s+\d+$', name):
        return False
        
    # 4. Skip single-character labels
    if len(name) <= 1:
        return False
        
    return True

def clean_song_name(name):
    """Normalizes song names for comparison (strips punctuation, common prefixes, expansions)."""
    name = name.strip().upper()
    # Expand common Ableton titles shorthand
    name = name.replace("TWNB", "THERE WILL NEVER BE")
    name = name.replace("LOFI", "")
    name = name.replace("XMAS", "CHRISTMAS")
    # Remove leading A, An, The
    name = re.sub(r'^(A|AN|THE)\s+', '', name)
    # Remove non-alphanumeric chars
    name = re.sub(r'[^A-Z0-9\s]', '', name)
    # Collapse multiple spaces
    name = re.sub(r'\s+', ' ', name).strip()
    return name

def load_csv_songs(csv_path):
    songs = []
    if not os.path.exists(csv_path):
        print(f"Error: CSV file not found at {csv_path}", file=sys.stderr)
        sys.exit(1)
        
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        try:
            header = next(reader)
        except StopIteration:
            print("Error: Empty CSV file", file=sys.stderr)
            sys.exit(1)
            
        # Find Title column index
        title_idx = 1 # Default fallback
        for idx, col in enumerate(header):
            if col.strip().lower() == "title":
                title_idx = idx
                break
                
        for row in reader:
            if len(row) > title_idx:
                title = row[title_idx].strip()
                if title and title.lower() != "title":
                    songs.append(title)
    return songs

def load_xml_songs(xml_path):
    """Extracts song names directly from the Ableton XML file."""
    if not os.path.exists(xml_path):
        print(f"Error: XML file not found at {xml_path}", file=sys.stderr)
        sys.exit(1)
        
    songs = set()
    try:
        context = ET.iterparse(xml_path, events=("end",))
        for event, elem in context:
            if elem.tag == "Scene":
                name_elem = elem.find("Name")
                if name_elem is not None:
                    name_val = name_elem.get("Value")
                    if name_val:
                        name_clean = name_val.strip()
                        if is_valid_song_name(name_clean):
                            songs.add(name_clean)
                elem.clear()
    except Exception as e:
        print(f"Error parsing XML: {e}", file=sys.stderr)
        sys.exit(1)
    return list(songs)

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(script_dir, "FJHH songs - Hall of Fame.csv")
    xml_path = os.path.join(script_dir, "tmp-xml-extract.xml")
    
    csv_songs = load_csv_songs(csv_path)
    xml_songs = load_xml_songs(xml_path)
    
    print(f"Loaded {len(csv_songs)} songs from CSV.")
    print(f"Loaded {len(xml_songs)} songs from Ableton XML.\n")
    
    # 1. Exact case-insensitive sets
    csv_upper = {s.upper() for s in csv_songs}
    xml_upper = {s.upper() for s in xml_songs}
    
    only_in_xml = xml_upper - csv_upper
    only_in_csv = csv_upper - xml_upper
    
    # 2. Find matches using normalization & fuzzy matching
    resolved_xml = set()
    resolved_csv = set()
    close_matches = []
    
    for x_song in sorted(only_in_xml):
        x_clean = clean_song_name(x_song)
        match_found = None
        
        # Only search from CSV songs that haven't been matched yet
        available_csv = only_in_csv - resolved_csv
        
        for c_song in available_csv:
            c_clean = clean_song_name(c_song)
            
            # Substring checks or direct normalized matches
            if x_clean == c_clean or (len(x_clean) > 4 and (x_clean in c_clean or c_clean in x_clean)):
                match_found = c_song
                break
                
        if not match_found:
            # difflib fallback on available candidates (increased cutoff to 0.70)
            matches = difflib.get_close_matches(x_song, list(available_csv), n=1, cutoff=0.70)
            if matches:
                match_found = matches[0]
                
        if match_found:
            close_matches.append((x_song, match_found))
            resolved_xml.add(x_song)
            resolved_csv.add(match_found)
            
    # Subtract resolved matches to get true mismatches
    unresolved_xml = only_in_xml - resolved_xml
    unresolved_csv = only_in_csv - resolved_csv
    
    print("=" * 75)
    print(" 1. POTENTIAL MATCHES (Likely the same song, different names/spellings)")
    print("=" * 75)
    if close_matches:
        for x, c in sorted(close_matches):
            original_csv_case = next((orig for orig in csv_songs if orig.upper() == c), c)
            print(f"  Ableton: {x:<32} ↔   CSV: {original_csv_case}")
    else:
        print("  None")
        
    print("\n" + "=" * 75)
    print(" 2. IN ABLETON SET BUT NOT IN CSV")
    print("=" * 75)
    if unresolved_xml:
        for s in sorted(unresolved_xml):
            print(f"  - {s}")
    else:
        print("  None")
        
    print("\n" + "=" * 75)
    print(" 3. IN CSV BUT NOT IN ABLETON SET")
    print("=" * 75)
    if unresolved_csv:
        for s in sorted(unresolved_csv):
            # Print with original casing from CSV
            original_case = next((orig for orig in csv_songs if orig.upper() == s), s)
            print(f"  - {original_case}")
    else:
        print("  None")
        
    print("\n" + "=" * 75)

if __name__ == "__main__":
    main()
