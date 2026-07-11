import csv
import os
import re

csv_path = "/Users/walker/Dropbox/youtube-chapters/FJHH songs - Songs.csv"
hof_csv_path = "/Users/walker/Dropbox/youtube-chapters/FJHH songs - Hall of Fame.csv"
output_dir = "/Users/walker/Dropbox/youtube-chapters/website/_songs"

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

def read_hall_of_fame(path):
    """Read the Hall of Fame CSV and map slugified titles to metadata."""
    hof = {}
    if not os.path.exists(path):
        print(f"Warning: Hall of Fame CSV not found at {path}")
        return hof
        
    print(f"Reading Hall of Fame CSV from: {path}")
    with open(path, mode='r', encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        header = next(reader)
        header = [h.strip().lower() for h in header]
        
        title_idx = header.index('title') if 'title' in header else 1
        ready_idx = header.index('ready') if 'ready' in header else 2
        style_idx = header.index('style') if 'style' in header else 6
        
        for row in reader:
            if not row or len(row) <= max(title_idx, ready_idx, style_idx):
                continue
            title = row[title_idx].strip()
            ready = row[ready_idx].strip()
            style = row[style_idx].strip()
            if title:
                slug = slugify(title)
                hof[slug] = {
                    "title": title,
                    "ready": ready,
                    "style": style
                }
    print(f"Loaded {len(hof)} songs from Hall of Fame.")
    return hof

def parse_csv(path):
    songs_data = {}
    epi_dates_map = {}
    
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
        
        rows = list(reader)
        
        # Pass 1: Gather all dates per episode number
        for row in rows:
            if not row or len(row) <= name_idx:
                continue
            date = row[date_idx].strip()
            epi = row[epi_idx].strip()
            if epi and date:
                if epi not in epi_dates_map:
                    epi_dates_map[epi] = set()
                epi_dates_map[epi].add(date)
                
        # Resolve canonical dates and rerun dates
        canonical_dates = {}
        for epi, dates in epi_dates_map.items():
            dates_list = list(dates)
            canonical_dates[epi] = max(dates_list, key=lambda d: dates_list.count(d))
            
        rerun_keys = set()
        for epi, dates in epi_dates_map.items():
            if len(dates) > 1:
                sorted_dates = sorted(list(dates), key=parse_date_key)
                for rerun_date in sorted_dates[1:]:
                    rerun_keys.add((epi, rerun_date))
                    
        # Pass 2: Build song data
        for row in rows:
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
            
    return songs_data, rerun_keys, canonical_dates

def get_episode_link(epi, date, rerun_keys, canonical_dates):
    if not date and epi in canonical_dates:
        date = canonical_dates[epi]
    if not date:
        return "#%s" % epi if epi else "Show"
        
    if epi:
        is_rerun = (epi, date) in rerun_keys
        if is_rerun:
            slug = f"episode-{slugify(epi)}-rerun-{slugify(date)}"
        else:
            slug = f"episode-{slugify(epi)}"
        return '<a href="{{ \'/episodes/\' | relative_url }}%s/">#%s</a>' % (slug, epi)
    else:
        slug = f"show-{slugify(date)}"
        return '<a href="{{ \'/episodes/\' | relative_url }}%s/">Show</a>' % slug

def generate_markdown(songs_data, hof, rerun_keys, canonical_dates, out_dir):
    # Clean out the songs directory to avoid orphan files
    if os.path.exists(out_dir):
        for f in os.listdir(out_dir):
            if f.endswith('.md'):
                os.remove(os.path.join(out_dir, f))
    else:
        os.makedirs(out_dir, exist_ok=True)
        
    one_offs_performances = []
    one_offs_meta = {} # slug -> {title, composer, style, count}
    multi_play_count = 0
    
    data_dir = "/Users/walker/Dropbox/youtube-chapters/website/_data"
    os.makedirs(data_dir, exist_ok=True)
    
    # Sort songs alphabetically by key
    for slug in sorted(songs_data.keys()):
        data = songs_data[slug]
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
        
        # Check if song is in Hall of Fame
        if slug in hof:
            multi_play_count += 1
            hof_data = hof[slug]
            
            # Style override from Hall of Fame CSV
            if hof_data["style"]:
                style = hof_data["style"]
                
            ready_rating = hof_data["ready"] or "0"
            title_escaped = title.replace('"', '\\"')
            composer_escaped = composer.replace('"', '\\"')
            style_escaped = style.replace('"', '\\"')
            
            md_content = f"""---
layout: song
title: "{title_escaped}"
composer: "{composer_escaped}"
style: "{style_escaped}"
play_count: {count}
hall_of_fame: true
ready_rating: {ready_rating}
---

# {title}

Played **{count}** times in the live shows.

| Date | Episode | Tempo | Notes |
| --- | --- | --- | --- |
"""
            for perf in performances:
                date_link = f"[{perf['date']}]({perf['url']})" if perf['url'] else perf['date']
                epi_link = get_episode_link(perf['episode'], perf['date'], rerun_keys, canonical_dates)
                md_content += f"| {date_link} | {epi_link} | {perf['tempo']} | {perf['notes']} |\n"
                
            file_path = os.path.join(out_dir, f"{slug}.md")
            with open(file_path, mode='w', encoding='utf-8') as f:
                f.write(md_content)
        else:
            # Song is NOT in Hall of Fame: treat as one-off / non-regular-rotation
            if count > 1:
                print(f"Warning: Song '{title}' was played {count} times but is not in the Hall of Fame.")
                
            # Log all performances to list
            for perf in performances:
                one_offs_performances.append({
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
                
            # Log song aggregate metadata for the homepage feed
            if slug not in one_offs_meta:
                one_offs_meta[slug] = {
                    "title": title,
                    "composer": composer,
                    "style": style,
                    "play_count": count
                }
                
    # Sort one-off performances alphabetically by song title, then by date
    def parse_one_off_key(x):
        return x["title"].lower(), parse_perf_date_key(x)
    one_offs_performances.sort(key=parse_one_off_key)
    
    # 2. Generate website/one-off-songs.md
    one_offs_path = "/Users/walker/Dropbox/youtube-chapters/website/one-off-songs.md"
    
    unique_styles = sorted(list(set(song["style"] for song in one_offs_performances if song["style"])))
    style_options = "\n      ".join(f'<option value="{style.lower()}">{style}</option>' for style in unique_styles)
    
    table_rows = ""
    for song in one_offs_performances:
        date_parts = song["date"].split('/')
        date_sort_key = "2000-01-01"
        if len(date_parts) == 3:
            try:
                date_sort_key = f"{int(date_parts[2]):04d}-{int(date_parts[0]):02d}-{int(date_parts[1]):02d}"
            except ValueError:
                pass
                
        try:
            # Strip non-digits from episode (e.g. 299D -> 299)
            epi_digits = re.sub(r'\D', '', song["episode"])
            epi_sort_key = int(epi_digits) if epi_digits else 9999
        except ValueError:
            epi_sort_key = 9999
            
        title_tag = f'<span id="{song["slug"]}"><strong>{song["title"]}</strong></span>'
        if song["composer"]:
            title_tag += f'<br><small style="color:var(--text-secondary);">by {song["composer"]}</small>'
            
        date_link = f'<a href="{song["url"]}" target="_blank" class="song-title-link" onclick="event.stopPropagation();">{song["date"]}</a>' if song["url"] else song["date"]
        epi_link = get_episode_link(song["episode"], song["date"], rerun_keys, canonical_dates)
        
        style_badge = f'<span class="badge-style">{song["style"]}</span>' if song["style"] else "-"
        tempo_val = song["tempo"] if song["tempo"] else "-"
        notes_val = song["notes"] if song["notes"] else ""
        
        title_esc = song["title"].lower().replace('"', '&quot;')
        composer_esc = song["composer"].lower().replace('"', '&quot;')
        style_esc = song["style"].lower().replace('"', '&quot;')
        
        table_rows += f"""        <tr class="song-row"
            data-title="{title_esc}"
            data-composer="{composer_esc}"
            data-style="{style_esc}"
            data-date="{date_sort_key}"
            data-episode="{epi_sort_key}"
            data-tempo="{tempo_val}">
          <td>{title_tag}</td>
          <td>{date_link}</td>
          <td>{epi_link}</td>
          <td>{style_badge}</td>
          <td style="text-align: right;">{tempo_val}</td>
          <td>{notes_val}</td>
        </tr>
"""
        
    one_offs_md_template = """---
layout: default
title: "One-Off Songs"
---

<style>
  .hero-section {
    text-align: center;
    margin-bottom: 3rem;
    padding: 3rem 1rem;
  }
  
  .hero-title {
    font-family: 'Outfit', sans-serif;
    font-weight: 800;
    font-size: 3.5rem;
    margin: 0 0 1rem 0;
    background: var(--accent-gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    letter-spacing: -0.03em;
    line-height: 1.1;
  }
  
  .hero-subtitle {
    color: var(--text-secondary);
    font-size: 1.2rem;
    max-width: 600px;
    margin: 0 auto;
    font-weight: 400;
  }
  
  /* Filter Container Styles */
  .search-filter-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 1.5rem;
    margin-bottom: 2.5rem;
    flex-wrap: wrap;
  }
  
  .search-wrapper {
    position: relative;
    flex: 1;
    min-width: 300px;
  }
  
  .search-icon {
    position: absolute;
    left: 1.2rem;
    top: 50%;
    transform: translateY(-50%);
    color: var(--text-secondary);
    font-size: 1.1rem;
    pointer-events: none;
  }
  
  #songSearch {
    width: 100%;
    padding: 0.85rem 1rem 0.85rem 2.8rem;
    background: var(--card-bg);
    border: 1px solid var(--border-color);
    border-radius: 14px;
    color: var(--text-primary);
    font-family: inherit;
    font-size: 0.95rem;
    outline: none;
    box-sizing: border-box;
    transition: all 0.2s ease;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
  }
  
  #songSearch:focus {
    border-color: var(--accent-color);
    box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.15), 0 4px 20px rgba(0, 0, 0, 0.1);
  }
  
  .filters-wrapper {
    display: flex;
    gap: 1rem;
    flex-wrap: wrap;
  }
  
  .filters-wrapper select {
    padding: 0.85rem 1.2rem;
    background: var(--card-bg);
    border: 1px solid var(--border-color);
    border-radius: 14px;
    color: var(--text-primary);
    font-family: inherit;
    font-size: 0.95rem;
    outline: none;
    cursor: pointer;
    transition: all 0.2s ease;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
  }
  
  .filters-wrapper select:focus {
    border-color: var(--accent-color);
  }
  
  /* Table Grid Card Styles */
  .songs-table-container {
    overflow-x: auto;
    margin-bottom: 5rem;
  }
  
  .songs-table {
    width: 100%;
    border-collapse: separate;
    border-spacing: 0 12px;
  }
  
  .songs-table th {
    text-align: left;
    color: var(--text-secondary);
    font-weight: 600;
    font-size: 0.8rem;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    padding: 0.5rem 1.5rem;
    border: none;
  }
  
  .songs-table th.sortable {
    cursor: pointer;
    user-select: none;
    transition: color 0.15s ease;
  }
  
  .songs-table th.sortable:hover {
    color: var(--text-primary);
  }
  
  .songs-table th.active-sort {
    color: var(--accent-hover);
  }
  
  .sort-icon {
    font-size: 0.75rem;
    display: inline-block;
    width: 12px;
  }
  
  .song-row {
    transition: transform 0.2s cubic-bezier(0.16, 1, 0.3, 1);
  }
  
  .song-row td {
    background: var(--card-bg);
    border-top: 1px solid var(--border-color);
    border-bottom: 1px solid var(--border-color);
    padding: 1.3rem 1.5rem;
    color: var(--text-primary);
    transition: all 0.2s ease;
  }
  
  .song-row td:first-child {
    border-left: 1px solid var(--border-color);
    border-top-left-radius: 16px;
    border-bottom-left-radius: 16px;
  }
  
  .song-row td:last-child {
    border-right: 1px solid var(--border-color);
    border-top-right-radius: 16px;
    border-bottom-right-radius: 16px;
  }
  
  /* Hover effects */
  .song-row:hover td {
    background: rgba(255, 255, 255, 0.03);
    border-color: var(--accent-color);
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
  }
  
  .song-row:hover {
    transform: translateY(-2px);
  }
  
  .song-title-link {
    font-weight: 600;
    color: var(--accent-hover);
    text-decoration: none;
    transition: color 0.15s ease;
  }
  
  .song-title-link:hover {
    color: var(--text-primary);
    text-decoration: underline;
  }
  
  .badge-style {
    background-color: rgba(255, 255, 255, 0.04);
    padding: 0.25rem 0.65rem;
    border-radius: 6px;
    font-size: 0.78rem;
    text-transform: capitalize;
    border: 1px solid rgba(255, 255, 255, 0.04);
  }
</style>

<div class="hero-section">
  <h1 class="hero-title">One-Off Songs</h1>
  <p class="hero-subtitle">These are the unique performances, modular synth improvisations, and special requests played exactly once.</p>
</div>

<div class="search-filter-container">
  <div class="search-wrapper">
    <span class="search-icon">🔍</span>
    <input type="text" id="songSearch" placeholder="Search by song name, composer, style, or notes...">
  </div>
  
  <div class="filters-wrapper">
    <select id="styleFilter">
      <option value="">All Styles</option>
      __STYLE_OPTIONS__
    </select>
  </div>
</div>

<div class="songs-table-container">
  <table class="songs-table">
    <thead>
      <tr>
        <th class="sortable" data-sort="title">Song <span class="sort-icon"> ▲</span></th>
        <th class="sortable" data-sort="date" data-default="desc">Date <span class="sort-icon"></span></th>
        <th class="sortable" data-sort="episode">Episode <span class="sort-icon"></span></th>
        <th class="sortable" data-sort="style">Style <span class="sort-icon"></span></th>
        <th class="sortable" data-sort="tempo" data-default="desc" style="text-align: right; width: 90px;">Tempo <span class="sort-icon"></span></th>
        <th>Notes</th>
      </tr>
    </thead>
    <tbody id="songsTableBody">
__TABLE_ROWS__    </tbody>
  </table>
</div>

<script>
  document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('songSearch');
    const styleFilter = document.getElementById('styleFilter');
    const tableBody = document.getElementById('songsTableBody');
    const rows = Array.from(tableBody.querySelectorAll('.song-row'));
    const headers = document.querySelectorAll('.songs-table th.sortable');
    
    let currentSort = {
      key: 'title',
      direction: 'asc'
    };
    
    headers.forEach(h => {
      if (h.getAttribute('data-sort') === 'title') {
        h.classList.add('active-sort');
      }
    });
    
    function filterTable() {
      const searchQuery = searchInput.value.toLowerCase().trim();
      const selectedStyle = styleFilter.value;
      
      rows.forEach(row => {
        const title = row.getAttribute('data-title');
        const composer = row.getAttribute('data-composer');
        const style = row.getAttribute('data-style');
        const notes = row.textContent.toLowerCase();
        
        const matchesSearch = !searchQuery || 
                              title.includes(searchQuery) || 
                              composer.includes(searchQuery) || 
                              style.includes(searchQuery) ||
                              notes.includes(searchQuery);
                              
        const matchesStyle = !selectedStyle || style === selectedStyle;
        
        if (matchesSearch && matchesStyle) {
          row.style.display = '';
        } else {
          row.style.display = 'none';
        }
      });
    }
    
    function sortTable(key, defaultDir = 'asc') {
      let direction = 'asc';
      if (currentSort.key === key) {
        direction = currentSort.direction === 'asc' ? 'desc' : 'asc';
      } else {
        direction = defaultDir;
      }
      
      currentSort = { key, direction };
      
      headers.forEach(h => {
        const icon = h.querySelector('.sort-icon');
        const hKey = h.getAttribute('data-sort');
        if (hKey === key) {
          icon.textContent = direction === 'asc' ? ' ▲' : ' ▼';
          h.classList.add('active-sort');
        } else {
          icon.textContent = '';
          h.classList.remove('active-sort');
        }
      });
      
      const sortedRows = rows.sort((a, b) => {
        let valA = a.getAttribute(`data-${key}`);
        let valB = b.getAttribute(`data-${key}`);
        
        if (key === 'tempo' || key === 'episode') {
          valA = parseInt(valA) || 0;
          valB = parseInt(valB) || 0;
          return direction === 'asc' ? valA - valB : valB - valA;
        } else if (key === 'date') {
          return direction === 'asc' ? valA.localeCompare(valB) : valB.localeCompare(valA);
        } else {
          return direction === 'asc' ? valA.localeCompare(valB) : valB.localeCompare(valA);
        }
      });
      
      sortedRows.forEach(row => tableBody.appendChild(row));
    }
    
    searchInput.addEventListener('input', filterTable);
    styleFilter.addEventListener('change', filterTable);
    
    headers.forEach(header => {
      const key = header.getAttribute('data-sort');
      const defaultDir = header.getAttribute('data-default') || 'asc';
      header.addEventListener('click', () => sortTable(key, defaultDir));
    });
  });
</script>
"""
    
    one_offs_md = one_offs_md_template.replace("__STYLE_OPTIONS__", style_options).replace("__TABLE_ROWS__", table_rows)

    with open(one_offs_path, mode='w', encoding='utf-8') as f:
        f.write(one_offs_md)
        
    # 3. Generate website/_data/one_offs.yml
    yaml_path = os.path.join(data_dir, "one_offs.yml")
    
    # Sort the unique one-offs alphabetically for the index
    sorted_one_offs_meta = sorted(one_offs_meta.items(), key=lambda x: x[1]["title"].lower())
    
    with open(yaml_path, mode='w', encoding='utf-8') as f:
        for slug, meta in sorted_one_offs_meta:
            title_esc = meta["title"].replace('"', '\\"')
            comp_esc = meta["composer"].replace('"', '\\"')
            style_esc = meta["style"].replace('"', '\\"')
            f.write(f"- title: \"{title_esc}\"\n")
            f.write(f"  slug: \"{slug}\"\n")
            f.write(f"  composer: \"{comp_esc}\"\n")
            f.write(f"  style: \"{style_esc}\"\n")
            f.write(f"  play_count: {meta['play_count']}\n")
            
    print(f"Generated {multi_play_count} individual Hall of Fame song pages.")
    print(f"Consolidated {len(one_offs_performances)} performances of {len(one_offs_meta)} unique non-rotation songs into website/one-offs.md and website/_data/one_offs.yml.")

if __name__ == "__main__":
    hof = read_hall_of_fame(hof_csv_path)
    songs_data, rerun_keys, canonical_dates = parse_csv(csv_path)
    generate_markdown(songs_data, hof, rerun_keys, canonical_dates, output_dir)
