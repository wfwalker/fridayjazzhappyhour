import csv
import os
import re

def slugify(text):
    """Generates clean url-friendly slugs from song names."""
    text = text.lower().strip()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s-]+', '-', text)
    return text.strip('-')

def parse_date_key(date_str):
    """Helper to parse MM/DD/YYYY date strings into tuples for sorting."""
    parts = date_str.split('/')
    if len(parts) == 3:
        try:
            return int(parts[2]), int(parts[0]), int(parts[1])
        except ValueError:
            pass
    return (0, 0, 0)

def format_offset_time(seconds_str):
    """Converts a seconds offset string into a HH:MM:SS or MM:SS format."""
    try:
        seconds = int(seconds_str)
        h = seconds // 3600
        m = (seconds % 3600) // 60
        s = seconds % 60
        if h > 0:
            return f"{h:02d}:{m:02d}:{s:02d}"
        return f"{m:02d}:{s:02d}"
    except (ValueError, TypeError):
        return seconds_str

def get_episode_link(epi, date, rerun_keys, canonical_dates):
    """Generates the Markdown/Jekyll links for a given episode number and date."""
    if not date and epi in canonical_dates:
        date = canonical_dates[epi]
    if not date:
        return f"#{epi}" if epi else "Show"
        
    if epi:
        is_rerun = (epi, date) in rerun_keys
        if is_rerun:
            slug = f"episode-{slugify(epi)}-rerun-{slugify(date)}"
        else:
            slug = f"episode-{slugify(epi)}"
        return f"[#{epi}]({{{{ '/episodes/' | relative_url }}}}{slug}/)"
    else:
        slug = f"show-{slugify(date)}"
        return f"[Show]({{{{ '/episodes/' | relative_url }}}}{slug}/)"

def format_front_matter(metadata):
    """Formats a dictionary into YAML front matter block."""
    lines = ["---"]
    for key, value in metadata.items():
        if isinstance(value, bool):
            lines.append(f"{key}: {str(value).lower()}")
        elif value is None:
            lines.append(f'{key}: ""')
        else:
            # Escape double quotes
            val_esc = str(value).replace('"', '\\"')
            lines.append(f'{key}: "{val_esc}"')
    lines.append("---")
    return "\n".join(lines) + "\n\n"

def format_markdown_table(headers, rows):
    """Formats a list of headers and rows into a Markdown table."""
    header_row = "| " + " | ".join(headers) + " |"
    separator_row = "| " + " | ".join(["---"] * len(headers)) + " |"
    data_rows = []
    for row in rows:
        data_rows.append("| " + " | ".join(str(cell) for cell in row) + " |")
    return "\n".join([header_row, separator_row] + data_rows) + "\n"

def parse_archive_csv(path):
    """Parses the FJHH songs CSV file and extracts structured data for both episodes and songs."""
    rows = []
    epi_dates_map = {}
    song_counts = {}
    
    with open(path, mode='r', encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        header = next(reader)
        header_lower = [h.strip().lower() for h in header]
        
        # Get column indices (with defaults if not found)
        date_idx = header_lower.index('date') if 'date' in header_lower else 0
        epi_idx = header_lower.index('epi #') if 'epi #' in header_lower else 1
        song_num_idx = header_lower.index('song #') if 'song #' in header_lower else 2
        offset_idx = header_lower.index('offset') if 'offset' in header_lower else 3
        url_idx = header_lower.index('url') if 'url' in header_lower else 4
        name_idx = header_lower.index('name') if 'name' in header_lower else 6
        tempo_idx = header_lower.index('tempo') if 'tempo' in header_lower else 9
        composer_idx = header_lower.index('composer') if 'composer' in header_lower else 10
        style_idx = header_lower.index('style') if 'style' in header_lower else 11
        notes_idx = header_lower.index('notes') if 'notes' in header_lower else 15
        
        for row in reader:
            if not row or len(row) <= name_idx:
                continue
            name = row[name_idx].strip()
            if not name:
                continue
                
            slug = slugify(name)
            date = row[date_idx].strip()
            epi = row[epi_idx].strip()
            
            # Count song plays
            song_counts[slug] = song_counts.get(slug, 0) + 1
            
            # Map episodes to dates
            if epi and date:
                if epi not in epi_dates_map:
                    epi_dates_map[epi] = set()
                epi_dates_map[epi].add(date)
                
            rows.append({
                "date": date,
                "epi": epi,
                "song_num": row[song_num_idx].strip(),
                "offset": row[offset_idx].strip() if offset_idx < len(row) else "",
                "url": row[url_idx].strip() if url_idx < len(row) else "",
                "name": name,
                "slug": slug,
                "tempo": row[tempo_idx].strip() if tempo_idx < len(row) else "",
                "composer": row[composer_idx].strip() if composer_idx < len(row) else "",
                "style": row[style_idx].strip() if style_idx < len(row) else "",
                "notes": row[notes_idx].strip() if notes_idx < len(row) else ""
            })
            
    # Resolve canonical dates for episodes to fix typos
    canonical_dates = {}
    for epi, dates in epi_dates_map.items():
        dates_list = list(dates)
        canonical_dates[epi] = max(dates_list, key=lambda d: dates_list.count(d))
        
    # Chronologically sort dates for each episode to find reruns
    rerun_keys = set()
    for epi, dates in epi_dates_map.items():
        if len(dates) > 1:
            sorted_dates = sorted(list(dates), key=parse_date_key)
            # First date is original; subsequent dates are reruns
            for rerun_date in sorted_dates[1:]:
                rerun_keys.add((epi, rerun_date))
                
    # Group rows by show instance (epi, date) and song instance (slug)
    episodes_data = {}
    songs_data = {}
    
    for item in rows:
        epi = item["epi"]
        date = item["date"]
        slug = item["slug"]
        
        # Impute missing date if possible
        if not date and epi in canonical_dates:
            date = canonical_dates[epi]
            item["date"] = date
            
        show_key = (epi, date)
        
        # 1. Group for episodes
        if show_key not in episodes_data:
            episodes_data[show_key] = {
                "episode": epi,
                "date": date,
                "youtube_url": None,
                "setlist": []
            }
            
        if item["url"] and not episodes_data[show_key]["youtube_url"]:
            # Strip timestamps from URL to get the stream's main URL
            base_url = re.sub(r'\?t=\d+', '', item["url"])
            base_url = re.sub(r'&t=\d+s', '', base_url)
            episodes_data[show_key]["youtube_url"] = base_url
            
        episodes_data[show_key]["setlist"].append(item)
        
        # 2. Group for songs
        if slug not in songs_data:
            songs_data[slug] = {
                "names": [],
                "composer": None,
                "style": None,
                "performances": []
            }
            
        songs_data[slug]["names"].append(item["name"])
        if item["composer"] and not songs_data[slug]["composer"]:
            songs_data[slug]["composer"] = item["composer"]
        if item["style"] and not songs_data[slug]["style"]:
            songs_data[slug]["style"] = item["style"]
            
        songs_data[slug]["performances"].append({
            "date": date,
            "episode": epi,
            "song_num": item["song_num"],
            "url": item["url"],
            "tempo": item["tempo"],
            "notes": item["notes"]
        })
        
    return {
        "song_counts": song_counts,
        "songs_data": songs_data,
        "episodes_data": episodes_data,
        "rerun_keys": rerun_keys,
        "canonical_dates": canonical_dates
    }
