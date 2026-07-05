import csv
import os
import re

csv_path = "/Users/walker/Dropbox/youtube-chapters/FJHH songs - Songs.csv"
output_dir = "/Users/walker/Dropbox/youtube-chapters/website/_songs"

def slugify(text):
    text = text.lower().strip()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s-]+', '-', text)
    return text.strip('-')

def parse_csv(path):
    songs_data = {}
    
    with open(path, mode='r', encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        header = next(reader)
        
        # Clean headers
        header = [h.strip().lower() for h in header]
        
        # Map headers to indices
        date_idx = header.index('date') if 'date' in header else 0
        epi_idx = header.index('epi #') if 'epi #' in header else 1
        song_num_idx = header.index('song #') if 'song #' in header else 2
        url_idx = header.index('url') if 'url' in header else 4
        name_idx = header.index('name') if 'name' in header else 6
        tempo_idx = header.index('tempo') if 'tempo' in header else 9
        composer_idx = header.index('composer') if 'composer' in header else 10
        style_idx = header.index('style') if 'style' in header else 11
        notes_idx = header.index('notes') if 'notes' in header else 15
        
        for row in reader:
            if not row or len(row) <= max(name_idx, date_idx):
                continue
                
            name = row[name_idx].strip()
            if not name:
                continue
                
            slug = slugify(name)
            if not slug:
                continue
                
            date = row[date_idx].strip()
            epi = row[epi_idx].strip()
            song_num = row[song_num_idx].strip()
            url = row[url_idx].strip()
            tempo = row[tempo_idx].strip()
            composer = row[composer_idx].strip()
            style = row[style_idx].strip()
            notes = row[notes_idx].strip()
            
            if slug not in songs_data:
                songs_data[slug] = {
                    "names": [],
                    "composer": None,
                    "style": None,
                    "performances": []
                }
                
            songs_data[slug]["names"].append(name)
            if composer and not songs_data[slug]["composer"]:
                songs_data[slug]["composer"] = composer
            if style and not songs_data[slug]["style"]:
                songs_data[slug]["style"] = style
                
            songs_data[slug]["performances"].append({
                "date": date,
                "episode": epi,
                "song_num": song_num,
                "url": url,
                "tempo": tempo,
                "notes": notes
            })
            
    return songs_data

def generate_markdown(songs_data, out_dir):
    # 1. Clean out the songs directory to avoid orphan files
    if os.path.exists(out_dir):
        for f in os.listdir(out_dir):
            if f.endswith('.md'):
                os.remove(os.path.join(out_dir, f))
    else:
        os.makedirs(out_dir, exist_ok=True)
        
    one_offs = []
    multi_play_count = 0
    
    # Ensure _data directory exists
    data_dir = "/Users/walker/Dropbox/youtube-chapters/website/_data"
    os.makedirs(data_dir, exist_ok=True)
    
    for slug, data in songs_data.items():
        title = max(set(data["names"]), key=data["names"].count)
        composer = data["composer"] or ""
        style = data["style"] or ""
        performances = data["performances"]
        
        # Sort performances by date
        def parse_date_key(perf):
            parts = perf["date"].split('/')
            if len(parts) == 3:
                try:
                    return int(parts[2]), int(parts[0]), int(parts[1])
                except ValueError:
                    pass
            return (0, 0, 0)
            
        performances.sort(key=parse_date_key)
        count = len(performances)
        
        if count == 1:
            perf = performances[0]
            one_offs.append({
                "slug": slug,
                "title": title,
                "composer": composer,
                "style": style,
                "date": perf["date"],
                "episode": perf["episode"],
                "song_num": perf["song_num"],
                "url": perf["url"],
                "tempo": perf["tempo"],
                "notes": perf["notes"]
            })
            continue
            
        # Multi-play song: generate individual page
        multi_play_count += 1
        title_escaped = title.replace('"', '\\"')
        composer_escaped = composer.replace('"', '\\"')
        style_escaped = style.replace('"', '\\"')
        
        md_content = f"""---
layout: song
title: "{title_escaped}"
composer: "{composer_escaped}"
style: "{style_escaped}"
play_count: {count}
---

# {title}

Played **{count}** times in the live shows.

| Date | Episode | Tempo | Notes |
| --- | --- | --- | --- |
"""
        for perf in performances:
            date_link = f"[{perf['date']}]({perf['url']})" if perf['url'] else perf['date']
            md_content += f"| {date_link} | #{perf['episode']} | {perf['tempo']} | {perf['notes']} |\n"
            
        file_path = os.path.join(out_dir, f"{slug}.md")
        with open(file_path, mode='w', encoding='utf-8') as f:
            f.write(md_content)
            
    # Sort one-offs alphabetically by song title
    one_offs.sort(key=lambda s: s["title"].lower())
    
    # 2. Generate website/one-offs.md
    one_offs_path = "/Users/walker/Dropbox/youtube-chapters/website/one-offs.md"
    one_offs_md = f"""---
layout: default
title: "One-Off Songs"
---

# One-Off Songs

These are the songs that have been performed exactly once during the live streams.

| Song | Date | Episode | Tempo | Notes |
| --- | --- | --- | --- | --- |
"""
    for song in one_offs:
        title_tag = f'<span id="{song["slug"]}">**{song["title"]}**</span>'
        if song["composer"]:
            title_tag += f'<br><small style="color:var(--text-secondary);">by {song["composer"]}</small>'
            
        date_link = f"[{song['date']}]({song['url']})" if song['url'] else song['date']
        style_col = f" ({song['style']})" if song['style'] else ""
        
        one_offs_md += f"| {title_tag} | {date_link} | #{song['episode']}{style_col} | {song['tempo']} | {song['notes']} |\n"
        
    with open(one_offs_path, mode='w', encoding='utf-8') as f:
        f.write(one_offs_md)
        
    # 3. Generate website/_data/one_offs.yml
    yaml_path = os.path.join(data_dir, "one_offs.yml")
    with open(yaml_path, mode='w', encoding='utf-8') as f:
        for song in one_offs:
            title_esc = song["title"].replace('"', '\\"')
            comp_esc = song["composer"].replace('"', '\\"')
            style_esc = song["style"].replace('"', '\\"')
            f.write(f"- title: \"{title_esc}\"\n")
            f.write(f"  slug: \"{song['slug']}\"\n")
            f.write(f"  composer: \"{comp_esc}\"\n")
            f.write(f"  style: \"{style_esc}\"\n")
            
    print(f"Generated {multi_play_count} individual song pages.")
    print(f"Consolidated {len(one_offs)} one-offs into website/one-offs.md and website/_data/one_offs.yml.")

if __name__ == "__main__":
    data = parse_csv(csv_path)
    generate_markdown(data, output_dir)

