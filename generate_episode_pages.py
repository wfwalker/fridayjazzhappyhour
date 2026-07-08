import csv
import os
import re

csv_path = "/Users/walker/Dropbox/youtube-chapters/FJHH songs - Songs.csv"
output_dir = "/Users/walker/Dropbox/youtube-chapters/website/_episodes"

def slugify(text):
    text = text.lower().strip()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s-]+', '-', text)
    return text.strip('-')

def parse_date_key(date_str):
    parts = date_str.split('/')
    if len(parts) == 3:
        try:
            return int(parts[2]), int(parts[0]), int(parts[1])
        except ValueError:
            pass
    return (0, 0, 0)

def format_offset_time(seconds_str):
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

def parse_csv(path):
    # First pass: Count play frequency and gather dates per episode number
    song_counts = {}
    epi_dates_map = {}
    rows = []
    
    with open(path, mode='r', encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        header = next(reader)
        header = [h.strip().lower() for h in header]
        
        date_idx = header.index('date') if 'date' in header else 0
        epi_idx = header.index('epi #') if 'epi #' in header else 1
        song_num_idx = header.index('song #') if 'song #' in header else 2
        url_idx = header.index('url') if 'url' in header else 4
        name_idx = header.index('name') if 'name' in header else 6
        tempo_idx = header.index('tempo') if 'tempo' in header else 9
        composer_idx = header.index('composer') if 'composer' in header else 10
        style_idx = header.index('style') if 'style' in header else 11
        notes_idx = header.index('notes') if 'notes' in header else 15
        offset_idx = header.index('offset') if 'offset' in header else 3
        
        for row in reader:
            if not row or len(row) <= name_idx:
                continue
            name = row[name_idx].strip()
            if not name:
                continue
                
            slug = slugify(name)
            song_counts[slug] = song_counts.get(slug, 0) + 1
            
            date = row[date_idx].strip()
            epi = row[epi_idx].strip()
            
            if epi and date:
                if epi not in epi_dates_map:
                    epi_dates_map[epi] = set()
                epi_dates_map[epi].add(date)
                
            rows.append({
                "date": date,
                "epi": epi,
                "song_num": row[song_num_idx].strip(),
                "url": row[url_idx].strip(),
                "name": name,
                "slug": slug,
                "tempo": row[tempo_idx].strip(),
                "composer": row[composer_idx].strip(),
                "style": row[style_idx].strip(),
                "notes": row[notes_idx].strip(),
                "offset": row[offset_idx].strip()
            })
            
    # Resolve canonical dates (most common non-empty date) for episodes to fix typos
    canonical_dates = {}
    for epi, dates in epi_dates_map.items():
        dates_list = list(dates)
        canonical_dates[epi] = max(dates_list, key=lambda d: dates_list.count(d))
        
    # Chronologically sort dates for each episode to find reruns
    rerun_keys = set()
    for epi, dates in epi_dates_map.items():
        if len(dates) > 1:
            sorted_dates = sorted(list(dates), key=parse_date_key)
            # The first date is original; subsequent dates are reruns
            for rerun_date in sorted_dates[1:]:
                rerun_keys.add((epi, rerun_date))
                
    # Group rows by show instance (epi, date)
    episodes_data = {}
    for item in rows:
        epi = item["epi"]
        date = item["date"]
        
        # Impute missing date if possible
        if not date and epi in canonical_dates:
            date = canonical_dates[epi]
            
        show_key = (epi, date)
        if show_key not in episodes_data:
            episodes_data[show_key] = {
                "episode": epi,
                "date": date,
                "youtube_url": None,
                "setlist": []
            }
            
        if item["url"] and not episodes_data[show_key]["youtube_url"]:
            base_url = re.sub(r'\?t=\d+', '', item["url"])
            base_url = re.sub(r'&t=\d+s', '', base_url)
            episodes_data[show_key]["youtube_url"] = base_url
            
        episodes_data[show_key]["setlist"].append(item)
        
    return song_counts, episodes_data, rerun_keys

def generate_episodes(song_counts, episodes_data, rerun_keys, out_dir):
    if os.path.exists(out_dir):
        for f in os.listdir(out_dir):
            if f.endswith('.md'):
                os.remove(os.path.join(out_dir, f))
    else:
        os.makedirs(out_dir, exist_ok=True)
        
    for (epi, date), data in episodes_data.items():
        yt_url = data["youtube_url"] or ""
        setlist = data["setlist"]
        
        # Sort setlist by Song #
        def parse_song_num(item):
            try:
                return int(item["song_num"])
            except ValueError:
                return 999
        setlist.sort(key=parse_song_num)
        
        # Format date as YYYY-MM-DD for Jekyll sorting
        date_formatted = ""
        if date:
            parts = date.split('/')
            if len(parts) == 3:
                try:
                    date_formatted = f"{int(parts[2]):04d}-{int(parts[0]):02d}-{int(parts[1]):02d}"
                except ValueError:
                    pass
        if not date_formatted:
            date_formatted = "2000-01-01"
            
        is_rerun = (epi, date) in rerun_keys
        
        # Generate slug and title
        if epi:
            if is_rerun:
                slug = f"episode-{slugify(epi)}-rerun-{slugify(date)}"
                title = f"Episode {epi} ({date}) (Rerun)"
            else:
                slug = f"episode-{slugify(epi)}"
                title = f"Episode {epi} ({date})"
        else:
            slug = f"show-{slugify(date)}"
            title = f"Show ({date})"
            
        title_escaped = title.replace('"', '\\"')
        
        md_content = f"""---
layout: episode
title: "{title_escaped}"
episode_number: "{epi}"
date_string: "{date}"
date: {date_formatted}
song_count: {len(setlist)}
rerun: {str(is_rerun).lower()}
youtube_url: "{yt_url}"
---

# {title}

"""
        if yt_url:
            md_content += f"[Watch Full Stream on YouTube &rarr;]({yt_url})\n\n"
            
        md_content += """### Set List

| # | Song | Time | Style | Notes |
| --- | --- | --- | --- | --- |
"""
        for item in setlist:
            slug_song = item["slug"]
            if song_counts.get(slug_song, 0) > 1:
                song_link = "[%s]({{ '/songs/' | relative_url }}%s/)" % (item['name'], slug_song)
            else:
                song_link = "[%s]({{ '/one-off-songs.html' | relative_url }}#%s)" % (item['name'], slug_song)
                
            time_str = format_offset_time(item["offset"])
            time_link = f"[{time_str}]({item['url']})" if item['url'] else time_str
            
            style_str = item["style"]
            if item["composer"]:
                style_str += f"<br><small style='color:var(--text-secondary);'>by {item['composer']}</small>"
                
            md_content += f"| {item['song_num']} | {song_link} | {time_link} | {style_str} | {item['notes']} |\n"
            
        file_path = os.path.join(out_dir, f"{slug}.md")
        with open(file_path, mode='w', encoding='utf-8') as f:
            f.write(md_content)
            
    print(f"Generated {len(episodes_data)} episode files.")

if __name__ == "__main__":
    song_counts, episodes_data, rerun_keys = parse_csv(csv_path)
    generate_episodes(song_counts, episodes_data, rerun_keys, output_dir)
