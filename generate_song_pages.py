import os
from archive_utils import (
    parse_archive_csv,
    get_episode_link,
    format_front_matter,
    format_markdown_table
)

csv_path = "/Users/walker/Dropbox/youtube-chapters/FJHH songs - Songs.csv"
output_dir = "/Users/walker/Dropbox/youtube-chapters/website/_songs"

def generate_markdown(songs_data, rerun_keys, canonical_dates, out_dir):
    """Generates individual song pages and consolidated one-offs lists."""
    # Clean out the songs directory to avoid orphan files
    if os.path.exists(out_dir):
        for f in os.listdir(out_dir):
            if f.endswith('.md'):
                os.remove(os.path.join(out_dir, f))
    else:
        os.makedirs(out_dir, exist_ok=True)
        
    one_offs = []
    multi_play_count = 0
    
    data_dir = "/Users/walker/Dropbox/youtube-chapters/website/_data"
    os.makedirs(data_dir, exist_ok=True)
    
    for slug, data in songs_data.items():
        title = max(set(data["names"]), key=data["names"].count)
        composer = data["composer"] or ""
        style = data["style"] or ""
        performances = data["performances"]
        
        # Sort performances by date
        def parse_perf_date_key(perf):
            parts = perf["date"].split('/')
            if len(parts) == 3:
                try:
                    return int(parts[2]), int(parts[0]), int(parts[1])
                except ValueError:
                    pass
            return (0, 0, 0)
            
        performances.sort(key=parse_perf_date_key)
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
        metadata = {
            "layout": "song",
            "title": title,
            "composer": composer,
            "style": style,
            "play_count": count
        }
        
        # Build table rows
        rows = []
        for perf in performances:
            date_link = f"[{perf['date']}]({perf['url']})" if perf['url'] else perf['date']
            epi_link = get_episode_link(perf['episode'], perf['date'], rerun_keys, canonical_dates)
            rows.append([date_link, epi_link, perf['tempo'], perf['notes']])
            
        md_content = format_front_matter(metadata)
        md_content += f"# {title}\n\n"
        md_content += f"Played **{count}** times in the live shows.\n\n"
        md_content += format_markdown_table(["Date", "Episode", "Tempo", "Notes"], rows)
        
        file_path = os.path.join(out_dir, f"{slug}.md")
        with open(file_path, mode='w', encoding='utf-8') as f:
            f.write(md_content)
            
    # Sort one-offs alphabetically by song title
    one_offs.sort(key=lambda s: s["title"].lower())
    
    # 2. Generate website/one-off-songs.md
    one_offs_path = "/Users/walker/Dropbox/youtube-chapters/website/one-off-songs.md"
    one_offs_metadata = {
        "layout": "default",
        "title": "One-Off Songs"
    }
    
    one_offs_rows = []
    for song in one_offs:
        title_tag = f'<span id="{song["slug"]}">**{song["title"]}**</span>'
        if song["composer"]:
            title_tag += f'<br><small style="color:var(--text-secondary);">by {song["composer"]}</small>'
            
        date_link = f"[{song['date']}]({song['url']})" if song['url'] else song['date']
        style_col = f" ({song['style']})" if song['style'] else ""
        epi_link = get_episode_link(song['episode'], song['date'], rerun_keys, canonical_dates)
        
        one_offs_rows.append([
            title_tag,
            date_link,
            f"{epi_link}{style_col}",
            song["tempo"],
            song["notes"]
        ])
        
    one_offs_md = format_front_matter(one_offs_metadata)
    one_offs_md += "# One-Off Songs\n\nThese are the songs that have been performed exactly once during the live streams.\n\n"
    one_offs_md += format_markdown_table(["Song", "Date", "Episode", "Tempo", "Notes"], one_offs_rows)
        
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
    print(f"Consolidated {len(one_offs)} one-offs into website/one-off-songs.md and website/_data/one_offs.yml.")

if __name__ == "__main__":
    archive_data = parse_archive_csv(csv_path)
    generate_markdown(
        archive_data["songs_data"],
        archive_data["rerun_keys"],
        archive_data["canonical_dates"],
        output_dir
    )
