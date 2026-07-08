import os
from archive_utils import (
    parse_archive_csv,
    slugify,
    format_offset_time,
    format_front_matter,
    format_markdown_table
)

csv_path = "/Users/walker/Dropbox/youtube-chapters/FJHH songs - Songs.csv"
output_dir = "/Users/walker/Dropbox/youtube-chapters/website/_episodes"

def generate_episodes(song_counts, episodes_data, rerun_keys, out_dir):
    """Generates Markdown files for all episodes from parsed data."""
    # Clean output directory to avoid orphan files
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
            
        # Check if title slide image exists
        image_url = None
        for ext in ["jpg", "png", "jpeg"]:
            img_rel_path = f"assets/images/title-slides/{slug}.{ext}"
            img_abs_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "website", img_rel_path)
            if os.path.exists(img_abs_path):
                image_url = f"/{img_rel_path}"
                break

        metadata = {
            "layout": "episode",
            "title": title,
            "episode_number": epi,
            "date_string": date,
            "date": date_formatted,
            "song_count": len(setlist),
            "rerun": is_rerun,
            "youtube_url": yt_url
        }
        if image_url:
            metadata["image"] = image_url
        
        # Build table rows
        rows = []
        for item in setlist:
            slug_song = item["slug"]
            if song_counts.get(slug_song, 0) > 1:
                song_link = f"[{item['name']}]({{{{ '/songs/' | relative_url }}}}{slug_song}/)"
            else:
                song_link = f"[{item['name']}]({{{{ '/one-off-songs.html' | relative_url }}}}#{slug_song})"
                
            time_str = format_offset_time(item["offset"])
            time_link = f"[{time_str}]({item['url']})" if item['url'] else time_str
            
            style_str = item["style"]
            if item["composer"]:
                style_str += f"<br><small style='color:var(--text-secondary);'>by {item['composer']}</small>"
                
            rows.append([item["song_num"], song_link, time_link, style_str, item["notes"]])
            
        # Compose Markdown content
        md_content = format_front_matter(metadata)
        md_content += f"# {title}\n\n"
        if yt_url:
            md_content += f"[Watch Full Stream on YouTube &rarr;]({yt_url})\n\n"
            
        md_content += "### Set List\n\n"
        md_content += format_markdown_table(["#", "Song", "Time", "Style", "Notes"], rows)
        
        file_path = os.path.join(out_dir, f"{slug}.md")
        with open(file_path, mode='w', encoding='utf-8') as f:
            f.write(md_content)
            
    print(f"Generated {len(episodes_data)} episode files.")

if __name__ == "__main__":
    archive_data = parse_archive_csv(csv_path)
    generate_episodes(
        archive_data["song_counts"],
        archive_data["episodes_data"],
        archive_data["rerun_keys"],
        output_dir
    )
