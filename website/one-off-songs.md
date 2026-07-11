---
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
      <option value="accordion">Accordion</option>
      <option value="ballad">Ballad</option>
      <option value="bossa">Bossa</option>
      <option value="pop">Pop</option>
      <option value="swing">Swing</option>
      <option value="techno">Techno</option>
      <option value="vocal">VOCAL</option>
      <option value="waltz">Waltz</option>
      <option value="accordion">accordion</option>
      <option value="ballad">ballad</option>
      <option value="bossa">bossa</option>
      <option value="funk">funk</option>
      <option value="pop">pop</option>
      <option value="samba">samba</option>
      <option value="spoken">spoken</option>
      <option value="swing">swing</option>
      <option value="techno">techno</option>
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
        <tr class="song-row"
            data-title="a night in tunisia"
            data-composer=""
            data-style=""
            data-date="2023-03-17"
            data-episode="154"
            data-tempo="-">
          <td><span id="a-night-in-tunisia"><strong>A night in Tunisia</strong></span></td>
          <td><a href="https://youtube.com/live/iD4kGZuXLYA?t=1158" target="_blank" class="song-title-link" onclick="event.stopPropagation();">3/17/2023</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-154/">#154</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="accordion ambient closer"
            data-composer=""
            data-style=""
            data-date="2024-10-04"
            data-episode="227"
            data-tempo="-">
          <td><span id="accordion-ambient-closer"><strong>accordion ambient closer</strong></span></td>
          <td>10/4/2024</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-227/">#227</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="accordion ambient closer"
            data-composer=""
            data-style=""
            data-date="2025-05-30"
            data-episode="258"
            data-tempo="-">
          <td><span id="accordion-ambient-closer"><strong>accordion ambient closer</strong></span></td>
          <td>5/30/2025</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-258/">#258</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="albatross at night"
            data-composer=""
            data-style=""
            data-date="2026-04-03"
            data-episode="293"
            data-tempo="-">
          <td><span id="albatross-at-night"><strong>Albatross at Night</strong></span></td>
          <td>4/3/2026</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-293/">#293</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="all you fascists bound to lose"
            data-composer=""
            data-style=""
            data-date="2021-01-08"
            data-episode="43"
            data-tempo="97">
          <td><span id="all-you-fascists-bound-to-lose"><strong>All You Fascists Bound to Lose</strong></span></td>
          <td><a href="https://youtu.be/PcZFKARMaQo?t=3165" target="_blank" class="song-title-link" onclick="event.stopPropagation();">1/8/2021</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-43/">#43</a></td>
          <td>-</td>
          <td style="text-align: right;">97</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="alphabet exercise"
            data-composer=""
            data-style=""
            data-date="2022-09-23"
            data-episode="132"
            data-tempo="-">
          <td><span id="alphabet-exercise"><strong>Alphabet Exercise</strong></span></td>
          <td><a href="https://youtu.be/ngSqqLNxvgo?t=3483" target="_blank" class="song-title-link" onclick="event.stopPropagation();">9/23/2022</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-132/">#132</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td>GAFFE CAGED</td>
        </tr>
        <tr class="song-row"
            data-title="alphabet game"
            data-composer=""
            data-style=""
            data-date="2024-03-01"
            data-episode="200"
            data-tempo="-">
          <td><span id="alphabet-game"><strong>Alphabet Game</strong></span></td>
          <td>3/1/2024</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-200/">#200</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="alphabet improv"
            data-composer=""
            data-style=""
            data-date="2023-06-09"
            data-episode="166"
            data-tempo="-">
          <td><span id="alphabet-improv"><strong>Alphabet Improv</strong></span></td>
          <td><a href="https://youtube.com/live/zxBeVU3jcP8?t=3023" target="_blank" class="song-title-link" onclick="event.stopPropagation();">6/9/2023</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-166/">#166</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="alphabet improv 2"
            data-composer=""
            data-style=""
            data-date="2021-12-03"
            data-episode="90"
            data-tempo="-">
          <td><span id="alphabet-improv-2"><strong>Alphabet Improv 2</strong></span></td>
          <td><a href="https://youtu.be/cwkUkcDyfaw?t=3070" target="_blank" class="song-title-link" onclick="event.stopPropagation();">12/3/2021</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-90/">#90</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="always"
            data-composer=""
            data-style=""
            data-date="2021-01-22"
            data-episode="45"
            data-tempo="-">
          <td><span id="always"><strong>Always</strong></span></td>
          <td><a href="https://youtu.be/9MPZ7yfdE6o?t=3177" target="_blank" class="song-title-link" onclick="event.stopPropagation();">1/22/2021</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-45/">#45</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="ambient accordion closer aug 2"
            data-composer=""
            data-style=""
            data-date="2024-08-02"
            data-episode="219"
            data-tempo="-">
          <td><span id="ambient-accordion-closer-aug-2"><strong>ambient accordion closer Aug 2</strong></span></td>
          <td>8/2/2024</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-219/">#219</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="ambient melodica closer"
            data-composer=""
            data-style=""
            data-date="2025-05-23"
            data-episode="257"
            data-tempo="-">
          <td><span id="ambient-melodica-closer"><strong>ambient melodica closer</strong></span></td>
          <td>5/23/2025</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-257/">#257</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="ambient set cnps"
            data-composer=""
            data-style=""
            data-date="2025-05-02"
            data-episode="254"
            data-tempo="-">
          <td><span id="ambient-set-cnps"><strong>Ambient Set CNPS</strong></span></td>
          <td>5/2/2025</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-254/">#254</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="ambient tuesday"
            data-composer=""
            data-style=""
            data-date="2021-02-12"
            data-episode="48"
            data-tempo="110">
          <td><span id="ambient-tuesday"><strong>Ambient Tuesday</strong></span></td>
          <td><a href="https://youtu.be/qK4QPjXbR7g?t=1830" target="_blank" class="song-title-link" onclick="event.stopPropagation();">2/12/2021</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-48/">#48</a></td>
          <td>-</td>
          <td style="text-align: right;">110</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="antelope valley closer"
            data-composer=""
            data-style=""
            data-date="2024-10-04"
            data-episode="227"
            data-tempo="-">
          <td><span id="antelope-valley-closer"><strong>Antelope Valley closer</strong></span></td>
          <td>10/4/2024</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-227/">#227</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="apollo 17"
            data-composer=""
            data-style=""
            data-date="2024-10-04"
            data-episode="227"
            data-tempo="-">
          <td><span id="apollo-17"><strong>Apollo 17</strong></span></td>
          <td>10/4/2024</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-227/">#227</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="april 11 closer"
            data-composer=""
            data-style=""
            data-date="2025-04-11"
            data-episode="251"
            data-tempo="-">
          <td><span id="april-11-closer"><strong>April 11 closer</strong></span></td>
          <td>4/11/2025</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-251/">#251</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="arpeggio improv"
            data-composer=""
            data-style="techno"
            data-date="2021-04-02"
            data-episode="55"
            data-tempo="-">
          <td><span id="arpeggio-improv"><strong>Arpeggio Improv</strong></span></td>
          <td><a href="https://youtu.be/brtK3KrZ6Io?t=2208" target="_blank" class="song-title-link" onclick="event.stopPropagation();">4/2/2021</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-55/">#55</a></td>
          <td><span class="badge-style">Techno</span></td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="arpeggio improv"
            data-composer=""
            data-style="techno"
            data-date="2021-07-02"
            data-episode="68"
            data-tempo="-">
          <td><span id="arpeggio-improv"><strong>Arpeggio Improv</strong></span></td>
          <td><a href="https://youtu.be/eJgSZO-IkTg?t=2482" target="_blank" class="song-title-link" onclick="event.stopPropagation();">7/2/2021</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-68/">#68</a></td>
          <td><span class="badge-style">Techno</span></td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="arpeggio improv"
            data-composer=""
            data-style="techno"
            data-date="2024-03-29"
            data-episode="55"
            data-tempo="-">
          <td><span id="arpeggio-improv"><strong>Arpeggio Improv</strong></span></td>
          <td><a href="https://youtu.be/brtK3KrZ6Io?t=1859" target="_blank" class="song-title-link" onclick="event.stopPropagation();">3/29/2024</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-55-rerun-3292024/">#55</a></td>
          <td><span class="badge-style">Techno</span></td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="arpeggio improvisation"
            data-composer=""
            data-style=""
            data-date="2020-10-02"
            data-episode="29"
            data-tempo="120">
          <td><span id="arpeggio-improvisation"><strong>Arpeggio Improvisation</strong></span></td>
          <td><a href="https://youtu.be/5H3aJ1p02Qo?t=2852" target="_blank" class="song-title-link" onclick="event.stopPropagation();">10/2/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-29/">#29</a></td>
          <td>-</td>
          <td style="text-align: right;">120</td>
          <td>arpeggio + random bass</td>
        </tr>
        <tr class="song-row"
            data-title="arpeggios for lent, meditation on &quot;wilderness&quot;"
            data-composer=""
            data-style=""
            data-date="2026-03-13"
            data-episode="9999"
            data-tempo="-">
          <td><span id="arpeggios-for-lent-meditation-on-wilderness"><strong>Arpeggios for Lent, meditation on "Wilderness"</strong></span></td>
          <td>3/13/2026</td>
          <td><a href="{{ '/episodes/' | relative_url }}show-3132026/">Show</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="autumn in new york"
            data-composer=""
            data-style=""
            data-date="2020-07-31"
            data-episode="20"
            data-tempo="-">
          <td><span id="autumn-in-new-york"><strong>Autumn in New York</strong></span></td>
          <td><a href="https://youtu.be/sTwgRPVLycU?t=3476" target="_blank" class="song-title-link" onclick="event.stopPropagation();">7/31/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-20/">#20</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="back in black"
            data-composer=""
            data-style="pop"
            data-date="2021-05-28"
            data-episode="63"
            data-tempo="-">
          <td><span id="back-in-black"><strong>Back in Black</strong></span></td>
          <td><a href="https://youtu.be/m7hZS9rLGO0?t=2120" target="_blank" class="song-title-link" onclick="event.stopPropagation();">5/28/2021</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-63/">#63</a></td>
          <td><span class="badge-style">Pop</span></td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="bathing exercise 1"
            data-composer=""
            data-style=""
            data-date="2023-03-03"
            data-episode="152"
            data-tempo="-">
          <td><span id="bathing-exercise-1"><strong>Bathing Exercise 1</strong></span></td>
          <td><a href="https://youtube.com/live/sRh_m871lEU?t=3023" target="_blank" class="song-title-link" onclick="event.stopPropagation();">3/3/2023</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-152/">#152</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="belet's last tape piece"
            data-composer=""
            data-style=""
            data-date="2022-02-25"
            data-episode="102"
            data-tempo="-">
          <td><span id="belets-last-tape-piece"><strong>Belet's Last Tape Piece</strong></span></td>
          <td><a href="https://youtu.be/f8SEdxjiIMM?t=1810" target="_blank" class="song-title-link" onclick="event.stopPropagation();">2/25/2022</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-102/">#102</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td>Belet liked it!</td>
        </tr>
        <tr class="song-row"
            data-title="berlin streetscape closer"
            data-composer=""
            data-style=""
            data-date="2025-05-16"
            data-episode="256"
            data-tempo="-">
          <td><span id="berlin-streetscape-closer"><strong>Berlin Streetscape closer</strong></span></td>
          <td>5/16/2025</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-256/">#256</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="berlin streetscape closer"
            data-composer=""
            data-style=""
            data-date="2026-06-05"
            data-episode="256"
            data-tempo="-">
          <td><span id="berlin-streetscape-closer"><strong>Berlin Streetscape closer</strong></span></td>
          <td>6/5/2026</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-256-rerun-652026/">#256</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="birding down under soundtrack"
            data-composer=""
            data-style=""
            data-date="2025-01-03"
            data-episode="241"
            data-tempo="-">
          <td><span id="birding-down-under-soundtrack"><strong>Birding Down Under Soundtrack</strong></span></td>
          <td>1/3/2025</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-241/">#241</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="bladerunner improv march 22"
            data-composer=""
            data-style=""
            data-date="2024-03-22"
            data-episode="203"
            data-tempo="-">
          <td><span id="bladerunner-improv-march-22"><strong>Bladerunner improv march 22</strong></span></td>
          <td><a href="https://youtube.com/live/kPqhJAREXfo?t=3023" target="_blank" class="song-title-link" onclick="event.stopPropagation();">3/22/2024</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-203/">#203</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="bladerunner midnight"
            data-composer=""
            data-style=""
            data-date="2020-10-30"
            data-episode="33"
            data-tempo="-">
          <td><span id="bladerunner-midnight"><strong>Bladerunner Midnight</strong></span></td>
          <td><a href="https://youtu.be/kRuS4bBAE_s?t=1064" target="_blank" class="song-title-link" onclick="event.stopPropagation();">10/30/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-33/">#33</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="blue bossa"
            data-composer="kenny dorham"
            data-style="bossa"
            data-date="2020-06-26"
            data-episode="15"
            data-tempo="136">
          <td><span id="blue-bossa"><strong>Blue Bossa</strong></span><br><small style="color:var(--text-secondary);">by Kenny Dorham</small></td>
          <td><a href="https://youtu.be/LCcBhJKB8YA?t=825" target="_blank" class="song-title-link" onclick="event.stopPropagation();">6/26/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-15/">#15</a></td>
          <td><span class="badge-style">bossa</span></td>
          <td style="text-align: right;">136</td>
          <td>(see Week14 file on disk</td>
        </tr>
        <tr class="song-row"
            data-title="blue bossa"
            data-composer="kenny dorham"
            data-style="bossa"
            data-date="2021-01-22"
            data-episode="45"
            data-tempo="190">
          <td><span id="blue-bossa"><strong>Blue Bossa</strong></span><br><small style="color:var(--text-secondary);">by Kenny Dorham</small></td>
          <td><a href="https://youtu.be/9MPZ7yfdE6o?t=1750" target="_blank" class="song-title-link" onclick="event.stopPropagation();">1/22/2021</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-45/">#45</a></td>
          <td><span class="badge-style">bossa</span></td>
          <td style="text-align: right;">190</td>
          <td>needs drum fills and comping? proper horns?</td>
        </tr>
        <tr class="song-row"
            data-title="blue bossa"
            data-composer="kenny dorham"
            data-style="bossa"
            data-date="2021-04-23"
            data-episode="58"
            data-tempo="-">
          <td><span id="blue-bossa"><strong>Blue Bossa</strong></span><br><small style="color:var(--text-secondary);">by Kenny Dorham</small></td>
          <td><a href="https://youtu.be/yYYl7DQc0K0?t=1150" target="_blank" class="song-title-link" onclick="event.stopPropagation();">4/23/2021</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-58/">#58</a></td>
          <td><span class="badge-style">bossa</span></td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="blues in f"
            data-composer=""
            data-style=""
            data-date="2020-10-09"
            data-episode="30"
            data-tempo="-">
          <td><span id="blues-in-f"><strong>Blues in F</strong></span></td>
          <td><a href="https://youtu.be/BOcDB0UTT54?t=628" target="_blank" class="song-title-link" onclick="event.stopPropagation();">10/9/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-30/">#30</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="boc closer apr 24"
            data-composer=""
            data-style=""
            data-date="2026-04-24"
            data-episode="296"
            data-tempo="-">
          <td><span id="boc-closer-apr-24"><strong>BoC closer apr 24</strong></span></td>
          <td>4/24/2026</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-296/">#296</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="break bread together"
            data-composer=""
            data-style=""
            data-date="2022-02-11"
            data-episode="100"
            data-tempo="-">
          <td><span id="break-bread-together"><strong>Break Bread Together</strong></span></td>
          <td><a href="https://youtu.be/6Wlh1-UXkrs?t=4230" target="_blank" class="song-title-link" onclick="event.stopPropagation();">2/11/2022</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-100/">#100</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="brother, can you spare a dime?"
            data-composer=""
            data-style="ballad"
            data-date="2021-07-23"
            data-episode="71"
            data-tempo="-">
          <td><span id="brother-can-you-spare-a-dime"><strong>Brother, Can you Spare a Dime?</strong></span></td>
          <td><a href="https://youtu.be/8xnSYgneRlI?t=235" target="_blank" class="song-title-link" onclick="event.stopPropagation();">7/23/2021</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-71/">#71</a></td>
          <td><span class="badge-style">Ballad</span></td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="buffering"
            data-composer=""
            data-style=""
            data-date="2021-09-24"
            data-episode="80"
            data-tempo="-">
          <td><span id="buffering"><strong>Buffering</strong></span></td>
          <td><a href="https://youtu.be/HM_6QdDeBy4?t=2387" target="_blank" class="song-title-link" onclick="event.stopPropagation();">9/24/2021</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-80/">#80</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="but beautiful"
            data-composer="jimmy van heusen"
            data-style="ballad"
            data-date="2020-07-03"
            data-episode="16"
            data-tempo="-">
          <td><span id="but-beautiful"><strong>But Beautiful</strong></span><br><small style="color:var(--text-secondary);">by Jimmy Van Heusen</small></td>
          <td><a href="https://youtu.be/pX-E6ZVGrpA?t=3314" target="_blank" class="song-title-link" onclick="event.stopPropagation();">7/3/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-16/">#16</a></td>
          <td><span class="badge-style">ballad</span></td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="but beautiful"
            data-composer="jimmy van heusen"
            data-style="ballad"
            data-date="2021-03-26"
            data-episode="54"
            data-tempo="-">
          <td><span id="but-beautiful"><strong>But Beautiful</strong></span><br><small style="color:var(--text-secondary);">by Jimmy Van Heusen</small></td>
          <td><a href="https://youtu.be/L9jDIlX7bjs?t=3553" target="_blank" class="song-title-link" onclick="event.stopPropagation();">3/26/2021</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-54/">#54</a></td>
          <td><span class="badge-style">ballad</span></td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="but not for me"
            data-composer=""
            data-style=""
            data-date="2020-09-11"
            data-episode="26"
            data-tempo="-">
          <td><span id="but-not-for-me"><strong>But Not For Me</strong></span></td>
          <td><a href="https://youtu.be/texnvgIfzO8?t=144" target="_blank" class="song-title-link" onclick="event.stopPropagation();">9/11/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-26/">#26</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="c jam blues"
            data-composer=""
            data-style="swing"
            data-date="2021-07-23"
            data-episode="71"
            data-tempo="-">
          <td><span id="c-jam-blues"><strong>C Jam Blues</strong></span></td>
          <td><a href="https://youtu.be/8xnSYgneRlI?t=2990" target="_blank" class="song-title-link" onclick="event.stopPropagation();">7/23/2021</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-71/">#71</a></td>
          <td><span class="badge-style">Swing</span></td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="christmas is coming"
            data-composer=""
            data-style=""
            data-date="2020-12-18"
            data-episode="40"
            data-tempo="144">
          <td><span id="christmas-is-coming"><strong>Christmas is Coming</strong></span></td>
          <td><a href="https://youtu.be/yhWB3cwCzOI?t=880" target="_blank" class="song-title-link" onclick="event.stopPropagation();">12/18/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-40/">#40</a></td>
          <td>-</td>
          <td style="text-align: right;">144</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="christmas is coming"
            data-composer=""
            data-style=""
            data-date="2020-12-25"
            data-episode="41"
            data-tempo="150">
          <td><span id="christmas-is-coming"><strong>Christmas is Coming</strong></span></td>
          <td><a href="https://youtu.be/G-HJYWxotdo?t=3030" target="_blank" class="song-title-link" onclick="event.stopPropagation();">12/25/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-41/">#41</a></td>
          <td>-</td>
          <td style="text-align: right;">150</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="christmas is coming"
            data-composer=""
            data-style=""
            data-date="2021-12-17"
            data-episode="92"
            data-tempo="-">
          <td><span id="christmas-is-coming"><strong>Christmas is Coming</strong></span></td>
          <td><a href="https://youtu.be/-MgcGR7PIMg?t=1308" target="_blank" class="song-title-link" onclick="event.stopPropagation();">12/17/2021</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-92/">#92</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="christmas is coming"
            data-composer=""
            data-style=""
            data-date="2021-12-24"
            data-episode="93"
            data-tempo="-">
          <td><span id="christmas-is-coming"><strong>Christmas is Coming</strong></span></td>
          <td><a href="https://youtu.be/oIJ5iubhwRg?t=2973" target="_blank" class="song-title-link" onclick="event.stopPropagation();">12/24/2021</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-93/">#93</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="christmas is coming"
            data-composer=""
            data-style=""
            data-date="2022-12-16"
            data-episode="141"
            data-tempo="-">
          <td><span id="christmas-is-coming"><strong>Christmas is Coming</strong></span></td>
          <td><a href="https://youtube.com/live/676nV2NzygY?t=950" target="_blank" class="song-title-link" onclick="event.stopPropagation();">12/16/2022</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-141/">#141</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="christmas is coming"
            data-composer=""
            data-style=""
            data-date="2023-12-01"
            data-episode="189"
            data-tempo="-">
          <td><span id="christmas-is-coming"><strong>Christmas is Coming</strong></span></td>
          <td>12/1/2023</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-189/">#189</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="christmas is coming"
            data-composer=""
            data-style=""
            data-date="2024-11-29"
            data-episode="235"
            data-tempo="-">
          <td><span id="christmas-is-coming"><strong>Christmas is Coming</strong></span></td>
          <td>11/29/2024</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-235/">#235</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="christmas is coming"
            data-composer=""
            data-style=""
            data-date="2025-12-19"
            data-episode="282"
            data-tempo="-">
          <td><span id="christmas-is-coming"><strong>Christmas is Coming</strong></span></td>
          <td>12/19/2025</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-282/">#282</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="christmastime is here"
            data-composer=""
            data-style=""
            data-date="2020-12-18"
            data-episode="40"
            data-tempo="80">
          <td><span id="christmastime-is-here"><strong>Christmastime is Here</strong></span></td>
          <td><a href="https://youtu.be/yhWB3cwCzOI?t=220" target="_blank" class="song-title-link" onclick="event.stopPropagation();">12/18/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-40/">#40</a></td>
          <td>-</td>
          <td style="text-align: right;">80</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="christmastime is here"
            data-composer=""
            data-style=""
            data-date="2020-12-25"
            data-episode="41"
            data-tempo="80">
          <td><span id="christmastime-is-here"><strong>Christmastime is Here</strong></span></td>
          <td><a href="https://youtu.be/G-HJYWxotdo?t=1069" target="_blank" class="song-title-link" onclick="event.stopPropagation();">12/25/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-41/">#41</a></td>
          <td>-</td>
          <td style="text-align: right;">80</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="christmastime is here"
            data-composer=""
            data-style=""
            data-date="2021-12-03"
            data-episode="90"
            data-tempo="-">
          <td><span id="christmastime-is-here"><strong>Christmastime is Here</strong></span></td>
          <td><a href="https://youtu.be/cwkUkcDyfaw?t=693" target="_blank" class="song-title-link" onclick="event.stopPropagation();">12/3/2021</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-90/">#90</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td>BASS FAIL</td>
        </tr>
        <tr class="song-row"
            data-title="christmastime is here"
            data-composer=""
            data-style=""
            data-date="2022-12-02"
            data-episode="139"
            data-tempo="-">
          <td><span id="christmastime-is-here"><strong>Christmastime is Here</strong></span></td>
          <td><a href="https://youtube.com/live/ezlBzx7DvTU?t=1321" target="_blank" class="song-title-link" onclick="event.stopPropagation();">12/2/2022</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-139/">#139</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="christmastime is here"
            data-composer=""
            data-style=""
            data-date="2023-12-01"
            data-episode="189"
            data-tempo="-">
          <td><span id="christmastime-is-here"><strong>Christmastime is Here</strong></span></td>
          <td>12/1/2023</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-189/">#189</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="christmastime is here"
            data-composer=""
            data-style=""
            data-date="2024-11-29"
            data-episode="235"
            data-tempo="-">
          <td><span id="christmastime-is-here"><strong>Christmastime is Here</strong></span></td>
          <td>11/29/2024</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-235/">#235</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="christmastime is here"
            data-composer=""
            data-style=""
            data-date="2024-12-20"
            data-episode="238"
            data-tempo="-">
          <td><span id="christmastime-is-here"><strong>Christmastime is Here</strong></span></td>
          <td>12/20/2024</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-238/">#238</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="christmastime is here"
            data-composer=""
            data-style=""
            data-date="2025-12-05"
            data-episode="280"
            data-tempo="-">
          <td><span id="christmastime-is-here"><strong>Christmastime is Here</strong></span></td>
          <td>12/5/2025</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-280/">#280</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="closer"
            data-composer=""
            data-style=""
            data-date="2025-10-24"
            data-episode="276"
            data-tempo="-">
          <td><span id="closer"><strong>Closer</strong></span></td>
          <td>10/24/2025</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-276/">#276</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="closer (when i fall) july 26"
            data-composer=""
            data-style=""
            data-date="2024-07-26"
            data-episode="218"
            data-tempo="-">
          <td><span id="closer-when-i-fall-july-26"><strong>Closer (When I Fall) July 26</strong></span></td>
          <td>7/26/2024</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-218/">#218</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="closer april 21"
            data-composer=""
            data-style=""
            data-date="2023-04-21"
            data-episode="159"
            data-tempo="-">
          <td><span id="closer-april-21"><strong>Closer April 21</strong></span></td>
          <td>4/21/2023</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-159/">#159</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="closer april 26"
            data-composer=""
            data-style=""
            data-date="2024-04-26"
            data-episode="206"
            data-tempo="-">
          <td><span id="closer-april-26"><strong>closer april 26</strong></span></td>
          <td>4/26/2024</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-206/">#206</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="closer april 8"
            data-composer=""
            data-style=""
            data-date="2022-04-08"
            data-episode="108"
            data-tempo="-">
          <td><span id="closer-april-8"><strong>Closer April 8</strong></span></td>
          <td><a href="https://youtu.be/47KbvV1znH8?t=3620" target="_blank" class="song-title-link" onclick="event.stopPropagation();">4/8/2022</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-108/">#108</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="closer aug 16"
            data-composer=""
            data-style=""
            data-date="2024-08-16"
            data-episode="221"
            data-tempo="-">
          <td><span id="closer-aug-16"><strong>Closer Aug 16</strong></span></td>
          <td>8/16/2024</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-221/">#221</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="closer aug 18"
            data-composer=""
            data-style=""
            data-date="2023-08-18"
            data-episode="176"
            data-tempo="-">
          <td><span id="closer-aug-18"><strong>Closer Aug 18</strong></span></td>
          <td>8/18/2023</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-176/">#176</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="closer aug 19"
            data-composer=""
            data-style=""
            data-date="2022-08-19"
            data-episode="127"
            data-tempo="-">
          <td><span id="closer-aug-19"><strong>Closer Aug 19</strong></span></td>
          <td><a href="https://youtu.be/VXmjfiJz2ZM?t=3175" target="_blank" class="song-title-link" onclick="event.stopPropagation();">8/19/2022</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-127/">#127</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="closer aug 19"
            data-composer=""
            data-style=""
            data-date="2025-04-04"
            data-episode="127"
            data-tempo="-">
          <td><span id="closer-aug-19"><strong>Closer Aug 19</strong></span></td>
          <td>4/4/2025</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-127-rerun-442025/">#127</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="closer aug 25"
            data-composer=""
            data-style=""
            data-date="2023-08-25"
            data-episode="177"
            data-tempo="-">
          <td><span id="closer-aug-25"><strong>Closer Aug 25</strong></span></td>
          <td><a href="https://youtube.com/live/jdMrvP3YOOo?t=3023" target="_blank" class="song-title-link" onclick="event.stopPropagation();">8/25/2023</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-177/">#177</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="closer aug 9"
            data-composer=""
            data-style=""
            data-date="2023-08-11"
            data-episode="175"
            data-tempo="-">
          <td><span id="closer-aug-9"><strong>Closer Aug 9</strong></span></td>
          <td><a href="https://youtu.be/c0po_X-AAOc?t=3023" target="_blank" class="song-title-link" onclick="event.stopPropagation();">8/11/2023</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-175/">#175</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="closer dec 10"
            data-composer=""
            data-style=""
            data-date="2021-12-10"
            data-episode="91"
            data-tempo="-">
          <td><span id="closer-dec-10"><strong>Closer Dec 10</strong></span></td>
          <td><a href="https://youtu.be/vr3lHzT6u9s?t=2545" target="_blank" class="song-title-link" onclick="event.stopPropagation();">12/10/2021</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-91/">#91</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="closer dec 13"
            data-composer=""
            data-style=""
            data-date="2024-12-13"
            data-episode="237"
            data-tempo="-">
          <td><span id="closer-dec-13"><strong>closer dec 13</strong></span></td>
          <td>12/13/2024</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-237/">#237</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="closer dec 17"
            data-composer=""
            data-style=""
            data-date="2021-12-17"
            data-episode="92"
            data-tempo="-">
          <td><span id="closer-dec-17"><strong>Closer Dec 17</strong></span></td>
          <td><a href="https://youtu.be/-MgcGR7PIMg?t=3065" target="_blank" class="song-title-link" onclick="event.stopPropagation();">12/17/2021</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-92/">#92</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="closer feb 3"
            data-composer=""
            data-style=""
            data-date="2023-02-03"
            data-episode="148"
            data-tempo="-">
          <td><span id="closer-feb-3"><strong>Closer Feb 3</strong></span></td>
          <td><a href="https://youtube.com/live/kyx5vcS24Tk?t=3200" target="_blank" class="song-title-link" onclick="event.stopPropagation();">2/3/2023</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-148/">#148</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td>swingy!</td>
        </tr>
        <tr class="song-row"
            data-title="closer improv oct 1"
            data-composer=""
            data-style=""
            data-date="2021-10-01"
            data-episode="81"
            data-tempo="-">
          <td><span id="closer-improv-oct-1"><strong>Closer Improv Oct 1</strong></span></td>
          <td><a href="https://youtu.be/xQLCSsoW8d8?t=3285" target="_blank" class="song-title-link" onclick="event.stopPropagation();">10/1/2021</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-81/">#81</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="closer improv oct 15"
            data-composer=""
            data-style=""
            data-date="2021-10-15"
            data-episode="83"
            data-tempo="-">
          <td><span id="closer-improv-oct-15"><strong>Closer Improv Oct 15</strong></span></td>
          <td><a href="https://youtu.be/txLo5jOwNGU?t=2870" target="_blank" class="song-title-link" onclick="event.stopPropagation();">10/15/2021</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-83/">#83</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="closer improv oct 22"
            data-composer=""
            data-style=""
            data-date="2021-10-22"
            data-episode="84"
            data-tempo="-">
          <td><span id="closer-improv-oct-22"><strong>Closer Improv Oct 22</strong></span></td>
          <td><a href="https://youtu.be/reLwPwmrFZk?t=3063" target="_blank" class="song-title-link" onclick="event.stopPropagation();">10/22/2021</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-84/">#84</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="closer improv oct 8"
            data-composer=""
            data-style=""
            data-date="2021-10-08"
            data-episode="82"
            data-tempo="-">
          <td><span id="closer-improv-oct-8"><strong>Closer Improv Oct 8</strong></span></td>
          <td><a href="https://youtu.be/y6pNfq5ndEU?t=3258" target="_blank" class="song-title-link" onclick="event.stopPropagation();">10/8/2021</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-82/">#82</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="closer improvise jan 28"
            data-composer=""
            data-style=""
            data-date="2022-01-28"
            data-episode="98"
            data-tempo="-">
          <td><span id="closer-improvise-jan-28"><strong>Closer improvise jan 28</strong></span></td>
          <td><a href="https://youtu.be/zEpV0UCl2es?t=2592" target="_blank" class="song-title-link" onclick="event.stopPropagation();">1/28/2022</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-98/">#98</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="closer jan 13"
            data-composer=""
            data-style=""
            data-date="2023-01-13"
            data-episode="145"
            data-tempo="-">
          <td><span id="closer-jan-13"><strong>Closer Jan 13</strong></span></td>
          <td><a href="https://youtube.com/live/twnyETfghJY?t=3200" target="_blank" class="song-title-link" onclick="event.stopPropagation();">1/13/2023</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-145/">#145</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="closer jan 6"
            data-composer=""
            data-style=""
            data-date="2023-01-06"
            data-episode="144"
            data-tempo="-">
          <td><span id="closer-jan-6"><strong>Closer Jan 6</strong></span></td>
          <td><a href="https://youtube.com/live/AgOf7ObdkGY?t=3207" target="_blank" class="song-title-link" onclick="event.stopPropagation();">1/6/2023</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-144/">#144</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="closer jan 9"
            data-composer=""
            data-style=""
            data-date="2026-01-09"
            data-episode="285"
            data-tempo="-">
          <td><span id="closer-jan-9"><strong>closer jan 9</strong></span></td>
          <td>1/9/2026</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-285/">#285</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="closer july 12 (inchworm)"
            data-composer=""
            data-style=""
            data-date="2024-07-12"
            data-episode="217"
            data-tempo="-">
          <td><span id="closer-july-12-inchworm"><strong>Closer July 12 (inchworm)</strong></span></td>
          <td>7/12/2024</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-217/">#217</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="closer july 15"
            data-composer=""
            data-style=""
            data-date="2022-07-15"
            data-episode="122"
            data-tempo="-">
          <td><span id="closer-july-15"><strong>Closer July 15</strong></span></td>
          <td><a href="https://youtu.be/vl789QxMIG4?t=2833" target="_blank" class="song-title-link" onclick="event.stopPropagation();">7/15/2022</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-122/">#122</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="closer july 15"
            data-composer=""
            data-style=""
            data-date="2026-03-13"
            data-episode="122"
            data-tempo="-">
          <td><span id="closer-july-15"><strong>Closer July 15</strong></span></td>
          <td>3/13/2026</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-122-rerun-3132026/">#122</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="closer july 18"
            data-composer=""
            data-style=""
            data-date="2025-07-18"
            data-episode="264"
            data-tempo="-">
          <td><span id="closer-july-18"><strong>Closer July 18</strong></span></td>
          <td>7/18/2025</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-264/">#264</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="closer july 6"
            data-composer=""
            data-style=""
            data-date="2024-07-05"
            data-episode="216"
            data-tempo="-">
          <td><span id="closer-july-6"><strong>Closer July 6</strong></span></td>
          <td>7/5/2024</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-216/">#216</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="closer june 17"
            data-composer=""
            data-style=""
            data-date="2022-06-17"
            data-episode="118"
            data-tempo="-">
          <td><span id="closer-june-17"><strong>Closer June 17</strong></span></td>
          <td><a href="https://youtu.be/xBJwSJ8nljM?t=3340" target="_blank" class="song-title-link" onclick="event.stopPropagation();">6/17/2022</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-118/">#118</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="closer june 24"
            data-composer=""
            data-style=""
            data-date="2022-06-24"
            data-episode="119"
            data-tempo="-">
          <td><span id="closer-june-24"><strong>Closer June 24</strong></span></td>
          <td><a href="https://youtu.be/XiFXST5UZ0E?t=3015" target="_blank" class="song-title-link" onclick="event.stopPropagation();">6/24/2022</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-119/">#119</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="closer june 3"
            data-composer=""
            data-style=""
            data-date="2022-06-03"
            data-episode="116"
            data-tempo="-">
          <td><span id="closer-june-3"><strong>Closer June 3</strong></span></td>
          <td><a href="https://youtu.be/58cVCBMx1oI?t=3295" target="_blank" class="song-title-link" onclick="event.stopPropagation();">6/3/2022</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-116/">#116</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td>keeper, add to collection</td>
        </tr>
        <tr class="song-row"
            data-title="closer june 7"
            data-composer=""
            data-style=""
            data-date="2024-06-07"
            data-episode="212"
            data-tempo="-">
          <td><span id="closer-june-7"><strong>Closer June 7</strong></span></td>
          <td>6/7/2024</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-212/">#212</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="closer march 11 (inchworm)"
            data-composer=""
            data-style=""
            data-date="2022-03-11"
            data-episode="104"
            data-tempo="-">
          <td><span id="closer-march-11-inchworm"><strong>Closer March 11 (inchworm)</strong></span></td>
          <td><a href="https://youtu.be/9YCarBEto_w?t=3180" target="_blank" class="song-title-link" onclick="event.stopPropagation();">3/11/2022</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-104/">#104</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td>one of the best closers</td>
        </tr>
        <tr class="song-row"
            data-title="closer march 18"
            data-composer=""
            data-style=""
            data-date="2022-03-17"
            data-episode="105"
            data-tempo="-">
          <td><span id="closer-march-18"><strong>Closer March 18</strong></span></td>
          <td><a href="https://youtu.be/BddGe4Ag9_M?t=3203" target="_blank" class="song-title-link" onclick="event.stopPropagation();">3/17/2022</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-105/">#105</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="closer march 18"
            data-composer=""
            data-style=""
            data-date="2025-07-11"
            data-episode="105"
            data-tempo="-">
          <td><span id="closer-march-18"><strong>Closer March 18</strong></span></td>
          <td>7/11/2025</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-105-rerun-7112025/">#105</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="closer march 25"
            data-composer=""
            data-style=""
            data-date="2022-03-25"
            data-episode="106"
            data-tempo="-">
          <td><span id="closer-march-25"><strong>Closer March 25</strong></span></td>
          <td><a href="https://youtu.be/-yO13Zr2O50?t=2548" target="_blank" class="song-title-link" onclick="event.stopPropagation();">3/25/2022</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-106/">#106</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="closer march 27"
            data-composer=""
            data-style=""
            data-date="2026-03-27"
            data-episode="292"
            data-tempo="-">
          <td><span id="closer-march-27"><strong>Closer March 27</strong></span></td>
          <td>3/27/2026</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-292/">#292</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="closer march 30"
            data-composer=""
            data-style=""
            data-date="2023-03-24"
            data-episode="155"
            data-tempo="-">
          <td><span id="closer-march-30"><strong>Closer March 30</strong></span></td>
          <td><a href="https://youtu.be/5m_WeGR1fNA?t=3023" target="_blank" class="song-title-link" onclick="event.stopPropagation();">3/24/2023</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-155/">#155</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="closer march 4"
            data-composer=""
            data-style=""
            data-date="2022-03-04"
            data-episode="103"
            data-tempo="-">
          <td><span id="closer-march-4"><strong>Closer March 4</strong></span></td>
          <td><a href="https://youtu.be/FJztyT2596g?t=3290" target="_blank" class="song-title-link" onclick="event.stopPropagation();">3/4/2022</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-103/">#103</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="closer may 19"
            data-composer=""
            data-style=""
            data-date="2023-05-19"
            data-episode="163"
            data-tempo="-">
          <td><span id="closer-may-19"><strong>Closer May 19</strong></span></td>
          <td>5/19/2023</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-163/">#163</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="closer may 3"
            data-composer=""
            data-style=""
            data-date="2024-05-03"
            data-episode="207"
            data-tempo="-">
          <td><span id="closer-may-3"><strong>closer may 3</strong></span></td>
          <td>5/3/2024</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-207/">#207</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="closer may 6"
            data-composer=""
            data-style=""
            data-date="2022-05-06"
            data-episode="112"
            data-tempo="-">
          <td><span id="closer-may-6"><strong>Closer May 6</strong></span></td>
          <td><a href="https://youtu.be/EnurztZItgI?t=3423" target="_blank" class="song-title-link" onclick="event.stopPropagation();">5/6/2022</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-112/">#112</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td>nice, add to collection</td>
        </tr>
        <tr class="song-row"
            data-title="closer nov 17"
            data-composer=""
            data-style=""
            data-date="2023-11-17"
            data-episode="187"
            data-tempo="-">
          <td><span id="closer-nov-17"><strong>Closer Nov 17</strong></span></td>
          <td>11/17/2023</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-187/">#187</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="closer nov 19"
            data-composer=""
            data-style=""
            data-date="2021-11-26"
            data-episode="89"
            data-tempo="-">
          <td><span id="closer-nov-19"><strong>Closer Nov 19</strong></span></td>
          <td><a href="https://youtu.be/gojpuqP3s6A?t=2793" target="_blank" class="song-title-link" onclick="event.stopPropagation();">11/26/2021</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-89/">#89</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="closer nov 29"
            data-composer=""
            data-style=""
            data-date="2024-11-29"
            data-episode="235"
            data-tempo="-">
          <td><span id="closer-nov-29"><strong>Closer Nov 29</strong></span></td>
          <td>11/29/2024</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-235/">#235</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="closer nov 4"
            data-composer=""
            data-style=""
            data-date="2022-11-04"
            data-episode="138"
            data-tempo="-">
          <td><span id="closer-nov-4"><strong>Closer Nov 4</strong></span></td>
          <td><a href="https://youtu.be/8XM8B7y4T_Q?t=2665" target="_blank" class="song-title-link" onclick="event.stopPropagation();">11/4/2022</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-138/">#138</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td>organ!</td>
        </tr>
        <tr class="song-row"
            data-title="closer oct 14"
            data-composer=""
            data-style=""
            data-date="2022-10-14"
            data-episode="135"
            data-tempo="-">
          <td><span id="closer-oct-14"><strong>Closer Oct 14</strong></span></td>
          <td><a href="https://youtu.be/hs2qWsSLfxY?t=3483" target="_blank" class="song-title-link" onclick="event.stopPropagation();">10/14/2022</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-135/">#135</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td>jarrett esque</td>
        </tr>
        <tr class="song-row"
            data-title="closer oct 22"
            data-composer=""
            data-style=""
            data-date="2024-10-18"
            data-episode="229"
            data-tempo="-">
          <td><span id="closer-oct-22"><strong>closer oct 22</strong></span></td>
          <td>10/18/2024</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-229/">#229</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="closer oct 31"
            data-composer=""
            data-style=""
            data-date="2025-10-31"
            data-episode="277"
            data-tempo="-">
          <td><span id="closer-oct-31"><strong>Closer Oct 31</strong></span></td>
          <td>10/31/2025</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-277/">#277</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="closer waltz"
            data-composer=""
            data-style=""
            data-date="2024-11-08"
            data-episode="232"
            data-tempo="-">
          <td><span id="closer-waltz"><strong>closer waltz</strong></span></td>
          <td>11/8/2024</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-232/">#232</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="closer white christmas"
            data-composer=""
            data-style=""
            data-date="2024-12-06"
            data-episode="236"
            data-tempo="-">
          <td><span id="closer-white-christmas"><strong>closer white christmas</strong></span></td>
          <td>12/6/2024</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-236/">#236</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="closing improv"
            data-composer=""
            data-style=""
            data-date="2021-09-10"
            data-episode="78"
            data-tempo="-">
          <td><span id="closing-improv"><strong>Closing Improv</strong></span></td>
          <td><a href="https://youtu.be/NuXghDNajFw?t=3618" target="_blank" class="song-title-link" onclick="event.stopPropagation();">9/10/2021</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-78/">#78</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="crane concréte"
            data-composer=""
            data-style=""
            data-date="2026-06-26"
            data-episode="299"
            data-tempo="-">
          <td><span id="crane-concrte"><strong>Crane Concréte</strong></span></td>
          <td>6/26/2026</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-299d/">#299D</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="crystal silence"
            data-composer="chick corea"
            data-style="ballad"
            data-date="2020-05-29"
            data-episode="11"
            data-tempo="-">
          <td><span id="crystal-silence"><strong>Crystal Silence</strong></span><br><small style="color:var(--text-secondary);">by Chick Corea</small></td>
          <td><a href="https://youtu.be/4UMdp7mQUrM?t=224" target="_blank" class="song-title-link" onclick="event.stopPropagation();">5/29/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-11/">#11</a></td>
          <td><span class="badge-style">ballad</span></td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="crystal silence"
            data-composer="chick corea"
            data-style="ballad"
            data-date="2021-02-12"
            data-episode="48"
            data-tempo="180">
          <td><span id="crystal-silence"><strong>Crystal Silence</strong></span><br><small style="color:var(--text-secondary);">by Chick Corea</small></td>
          <td><a href="https://youtu.be/qK4QPjXbR7g?t=849" target="_blank" class="song-title-link" onclick="event.stopPropagation();">2/12/2021</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-48/">#48</a></td>
          <td><span class="badge-style">ballad</span></td>
          <td style="text-align: right;">180</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="crystal silence"
            data-composer="chick corea"
            data-style="ballad"
            data-date="2023-04-14"
            data-episode="158"
            data-tempo="-">
          <td><span id="crystal-silence"><strong>Crystal Silence</strong></span><br><small style="color:var(--text-secondary);">by Chick Corea</small></td>
          <td><a href="https://youtube.com/live/dXjYvp477_M?t=3023" target="_blank" class="song-title-link" onclick="event.stopPropagation();">4/14/2023</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-158/">#158</a></td>
          <td><span class="badge-style">ballad</span></td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="dawless closer"
            data-composer=""
            data-style=""
            data-date="2025-09-12"
            data-episode="271"
            data-tempo="-">
          <td><span id="dawless-closer"><strong>DAWless closer</strong></span></td>
          <td>9/12/2025</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-271/">#271</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="dinosaur night"
            data-composer="bill walker"
            data-style="accordion"
            data-date="2020-04-03"
            data-episode="3"
            data-tempo="98">
          <td><span id="dinosaur-night"><strong>Dinosaur Night</strong></span><br><small style="color:var(--text-secondary);">by Bill Walker</small></td>
          <td><a href="https://youtu.be/s0MwmoMYKj8?t=2242" target="_blank" class="song-title-link" onclick="event.stopPropagation();">4/3/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-3/">#3</a></td>
          <td><span class="badge-style">accordion</span></td>
          <td style="text-align: right;">98</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="dinosaur night"
            data-composer="bill walker"
            data-style="accordion"
            data-date="2021-01-01"
            data-episode="42"
            data-tempo="98">
          <td><span id="dinosaur-night"><strong>Dinosaur Night</strong></span><br><small style="color:var(--text-secondary);">by Bill Walker</small></td>
          <td><a href="https://youtu.be/i7H03-9N1As?t=3350" target="_blank" class="song-title-link" onclick="event.stopPropagation();">1/1/2021</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-42/">#42</a></td>
          <td><span class="badge-style">accordion</span></td>
          <td style="text-align: right;">98</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="dinosaur night"
            data-composer="bill walker"
            data-style="accordion"
            data-date="2022-02-11"
            data-episode="100"
            data-tempo="-">
          <td><span id="dinosaur-night"><strong>Dinosaur Night</strong></span><br><small style="color:var(--text-secondary);">by Bill Walker</small></td>
          <td><a href="https://youtu.be/6Wlh1-UXkrs?t=1834" target="_blank" class="song-title-link" onclick="event.stopPropagation();">2/11/2022</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-100/">#100</a></td>
          <td><span class="badge-style">accordion</span></td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="don't get around much anymore"
            data-composer="duke ellington"
            data-style="swing"
            data-date="2020-08-07"
            data-episode="21"
            data-tempo="-">
          <td><span id="dont-get-around-much-anymore"><strong>Don't Get Around Much Anymore</strong></span><br><small style="color:var(--text-secondary);">by Duke Ellington</small></td>
          <td><a href="https://youtu.be/jqycjkIUaCs?t=168" target="_blank" class="song-title-link" onclick="event.stopPropagation();">8/7/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-21/">#21</a></td>
          <td><span class="badge-style">swing</span></td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="dub techno arpeggios"
            data-composer=""
            data-style=""
            data-date="2026-02-27"
            data-episode="291"
            data-tempo="-">
          <td><span id="dub-techno-arpeggios"><strong>Dub Techno Arpeggios</strong></span></td>
          <td>2/27/2026</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-291/">#291</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="dulcimers in space"
            data-composer=""
            data-style=""
            data-date="2021-02-26"
            data-episode="50"
            data-tempo="115">
          <td><span id="dulcimers-in-space"><strong>Dulcimers in Space</strong></span></td>
          <td><a href="https://youtu.be/TKoh0MrsGgs?t=1475" target="_blank" class="song-title-link" onclick="event.stopPropagation();">2/26/2021</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-50/">#50</a></td>
          <td>-</td>
          <td style="text-align: right;">115</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="dust makes rain with accordion"
            data-composer=""
            data-style=""
            data-date="2024-01-05"
            data-episode="194"
            data-tempo="-">
          <td><span id="dust-makes-rain-with-accordion"><strong>Dust makes Rain with Accordion</strong></span></td>
          <td>1/5/2024</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-194/">#194</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="edm02"
            data-composer=""
            data-style=""
            data-date="2026-01-02"
            data-episode="284"
            data-tempo="-">
          <td><span id="edm02"><strong>EDM02</strong></span></td>
          <td>1/2/2026</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-284/">#284</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="emom sc set"
            data-composer=""
            data-style=""
            data-date="2026-01-23"
            data-episode="286"
            data-tempo="-">
          <td><span id="emom-sc-set"><strong>EMOM SC set</strong></span></td>
          <td>1/23/2026</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-286/">#286</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="emotional weather report"
            data-composer="tom waits"
            data-style="swing"
            data-date="2020-04-17"
            data-episode="5"
            data-tempo="105">
          <td><span id="emotional-weather-report"><strong>Emotional Weather Report</strong></span><br><small style="color:var(--text-secondary);">by Tom Waits</small></td>
          <td><a href="https://youtu.be/mlWuikMRDGo?t=335" target="_blank" class="song-title-link" onclick="event.stopPropagation();">4/17/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-5/">#5</a></td>
          <td><span class="badge-style">swing</span></td>
          <td style="text-align: right;">105</td>
          <td>REDO with jazz dummer</td>
        </tr>
        <tr class="song-row"
            data-title="emotional weather report"
            data-composer="tom waits"
            data-style="swing"
            data-date="2021-05-21"
            data-episode="62"
            data-tempo="-">
          <td><span id="emotional-weather-report"><strong>Emotional Weather Report</strong></span><br><small style="color:var(--text-secondary);">by Tom Waits</small></td>
          <td><a href="https://youtu.be/tB5vd6dRUS4?t=1680" target="_blank" class="song-title-link" onclick="event.stopPropagation();">5/21/2021</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-62/">#62</a></td>
          <td><span class="badge-style">swing</span></td>
          <td style="text-align: right;">-</td>
          <td>what is your voice? trying to sound black?</td>
        </tr>
        <tr class="song-row"
            data-title="epiano closer aug 1"
            data-composer=""
            data-style=""
            data-date="2025-08-01"
            data-episode="266"
            data-tempo="-">
          <td><span id="epiano-closer-aug-1"><strong>epiano closer aug 1</strong></span></td>
          <td>8/1/2025</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-266/">#266</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="euclidian dub techno"
            data-composer=""
            data-style=""
            data-date="2026-03-20"
            data-episode="9999"
            data-tempo="-">
          <td><span id="euclidian-dub-techno"><strong>Euclidian Dub Techno</strong></span></td>
          <td>3/20/2026</td>
          <td><a href="{{ '/episodes/' | relative_url }}show-3202026/">Show</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="euro closer euclid"
            data-composer=""
            data-style=""
            data-date="2025-12-12"
            data-episode="281"
            data-tempo="-">
          <td><span id="euro-closer-euclid"><strong>Euro Closer Euclid</strong></span></td>
          <td>12/12/2025</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-281/">#281</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="eurorack closer feb 6"
            data-composer=""
            data-style=""
            data-date="2026-02-06"
            data-episode="288"
            data-tempo="-">
          <td><span id="eurorack-closer-feb-6"><strong>EuroRack closer feb 6</strong></span></td>
          <td>2/6/2026</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-288/">#288</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="eurorack jam 1"
            data-composer=""
            data-style=""
            data-date="2021-10-08"
            data-episode="82"
            data-tempo="-">
          <td><span id="eurorack-jam-1"><strong>EuroRack Jam 1</strong></span></td>
          <td><a href="https://youtu.be/y6pNfq5ndEU?t=2450" target="_blank" class="song-title-link" onclick="event.stopPropagation();">10/8/2021</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-82/">#82</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td>practice</td>
        </tr>
        <tr class="song-row"
            data-title="eurorack piano 1"
            data-composer=""
            data-style=""
            data-date="2025-08-15"
            data-episode="268"
            data-tempo="-">
          <td><span id="eurorack-piano-1"><strong>EuroRack Piano 1</strong></span></td>
          <td>8/15/2025</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-268/">#268</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="eurorack piano 2"
            data-composer=""
            data-style=""
            data-date="2025-08-15"
            data-episode="268"
            data-tempo="-">
          <td><span id="eurorack-piano-2"><strong>EuroRack Piano 2</strong></span></td>
          <td>8/15/2025</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-268/">#268</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="eurorack piano 3"
            data-composer=""
            data-style=""
            data-date="2025-08-15"
            data-episode="268"
            data-tempo="-">
          <td><span id="eurorack-piano-3"><strong>EuroRack Piano 3</strong></span></td>
          <td>8/15/2025</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-268/">#268</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="eye in the sky"
            data-composer="alan parsons"
            data-style="pop"
            data-date="2020-04-17"
            data-episode="5"
            data-tempo="90">
          <td><span id="eye-in-the-sky"><strong>Eye in the Sky</strong></span><br><small style="color:var(--text-secondary);">by Alan Parsons</small></td>
          <td><a href="https://youtu.be/mlWuikMRDGo?t=655" target="_blank" class="song-title-link" onclick="event.stopPropagation();">4/17/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-5/">#5</a></td>
          <td><span class="badge-style">pop</span></td>
          <td style="text-align: right;">90</td>
          <td>REDO</td>
        </tr>
        <tr class="song-row"
            data-title="feb 20 rhodes closer"
            data-composer=""
            data-style=""
            data-date="2026-02-20"
            data-episode="290"
            data-tempo="-">
          <td><span id="feb-20-rhodes-closer"><strong>feb 20 rhodes closer</strong></span></td>
          <td>2/20/2026</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-290/">#290</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="feb 25 closer"
            data-composer=""
            data-style=""
            data-date="2022-02-25"
            data-episode="102"
            data-tempo="-">
          <td><span id="feb-25-closer"><strong>Feb 25 Closer</strong></span></td>
          <td><a href="https://youtu.be/f8SEdxjiIMM?t=3191" target="_blank" class="song-title-link" onclick="event.stopPropagation();">2/25/2022</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-102/">#102</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td>waltz!</td>
        </tr>
        <tr class="song-row"
            data-title="feel like going home closer"
            data-composer=""
            data-style=""
            data-date="2024-08-30"
            data-episode="222"
            data-tempo="-">
          <td><span id="feel-like-going-home-closer"><strong>Feel like going home closer</strong></span></td>
          <td>8/30/2024</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-222/">#222</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="feel like going home closer"
            data-composer=""
            data-style=""
            data-date="2025-08-29"
            data-episode="9999"
            data-tempo="-">
          <td><span id="feel-like-going-home-closer"><strong>Feel like going home closer</strong></span></td>
          <td>8/29/2025</td>
          <td><a href="{{ '/episodes/' | relative_url }}show-8292025/">Show</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="forty days"
            data-composer=""
            data-style="swing"
            data-date="2021-04-02"
            data-episode="55"
            data-tempo="-">
          <td><span id="forty-days"><strong>Forty Days</strong></span></td>
          <td><a href="https://youtu.be/brtK3KrZ6Io?t=290" target="_blank" class="song-title-link" onclick="event.stopPropagation();">4/2/2021</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-55/">#55</a></td>
          <td><span class="badge-style">Swing</span></td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="forty days"
            data-composer=""
            data-style="swing"
            data-date="2024-03-29"
            data-episode="55"
            data-tempo="-">
          <td><span id="forty-days"><strong>Forty Days</strong></span></td>
          <td><a href="https://youtu.be/brtK3KrZ6Io?t=268" target="_blank" class="song-title-link" onclick="event.stopPropagation();">3/29/2024</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-55-rerun-3292024/">#55</a></td>
          <td><span class="badge-style">Swing</span></td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="four on six"
            data-composer="wes montgomery"
            data-style=""
            data-date="2020-06-19"
            data-episode="14"
            data-tempo="189">
          <td><span id="four-on-six"><strong>Four on Six</strong></span><br><small style="color:var(--text-secondary);">by Wes Montgomery</small></td>
          <td><a href="https://youtu.be/JFFsTahEkzg?t=2784" target="_blank" class="song-title-link" onclick="event.stopPropagation();">6/19/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-14/">#14</a></td>
          <td>-</td>
          <td style="text-align: right;">189</td>
          <td>REDO more comping</td>
        </tr>
        <tr class="song-row"
            data-title="four on six"
            data-composer="wes montgomery"
            data-style=""
            data-date="2021-02-12"
            data-episode="48"
            data-tempo="210">
          <td><span id="four-on-six"><strong>Four on Six</strong></span><br><small style="color:var(--text-secondary);">by Wes Montgomery</small></td>
          <td><a href="https://youtu.be/qK4QPjXbR7g?t=2614" target="_blank" class="song-title-link" onclick="event.stopPropagation();">2/12/2021</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-48/">#48</a></td>
          <td>-</td>
          <td style="text-align: right;">210</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="free improv (captain's log)"
            data-composer=""
            data-style="techno"
            data-date="2021-06-04"
            data-episode="64"
            data-tempo="-">
          <td><span id="free-improv-captains-log"><strong>free improv (captain's log)</strong></span></td>
          <td><a href="https://youtu.be/S_oefge4qcQ?t=1581" target="_blank" class="song-title-link" onclick="event.stopPropagation();">6/4/2021</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-64/">#64</a></td>
          <td><span class="badge-style">Techno</span></td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="fretless improvisation"
            data-composer="bill walker"
            data-style=""
            data-date="2020-08-07"
            data-episode="21"
            data-tempo="-">
          <td><span id="fretless-improvisation"><strong>Fretless Improvisation</strong></span><br><small style="color:var(--text-secondary);">by Bill Walker</small></td>
          <td><a href="https://youtu.be/jqycjkIUaCs?t=2473" target="_blank" class="song-title-link" onclick="event.stopPropagation();">8/7/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-21/">#21</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td>rhodes + fretless</td>
        </tr>
        <tr class="song-row"
            data-title="frippertronics improv"
            data-composer=""
            data-style="techno"
            data-date="2021-05-21"
            data-episode="62"
            data-tempo="-">
          <td><span id="frippertronics-improv"><strong>Frippertronics improv</strong></span></td>
          <td><a href="https://youtu.be/tB5vd6dRUS4?t=3412" target="_blank" class="song-title-link" onclick="event.stopPropagation();">5/21/2021</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-62/">#62</a></td>
          <td><span class="badge-style">Techno</span></td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="frisell vcv closer april 19"
            data-composer=""
            data-style=""
            data-date="2024-04-19"
            data-episode="205"
            data-tempo="-">
          <td><span id="frisell-vcv-closer-april-19"><strong>Frisell VCV closer April 19</strong></span></td>
          <td>4/19/2024</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-205/">#205</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="fuzzy vcv chord closer"
            data-composer=""
            data-style=""
            data-date="2024-06-28"
            data-episode="215"
            data-tempo="-">
          <td><span id="fuzzy-vcv-chord-closer"><strong>fuzzy vcv chord closer</strong></span></td>
          <td>6/28/2024</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-215/">#215</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="gentle rain improv"
            data-composer=""
            data-style=""
            data-date="2023-09-01"
            data-episode="178"
            data-tempo="-">
          <td><span id="gentle-rain-improv"><strong>Gentle Rain Improv</strong></span></td>
          <td><a href="https://youtu.be/zxhyx-uWlJQ?t=3023" target="_blank" class="song-title-link" onclick="event.stopPropagation();">9/1/2023</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-178/">#178</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="get up, stand up"
            data-composer="bob marley"
            data-style=""
            data-date="2020-08-28"
            data-episode="24"
            data-tempo="155">
          <td><span id="get-up-stand-up"><strong>Get Up, Stand Up</strong></span><br><small style="color:var(--text-secondary);">by Bob Marley</small></td>
          <td><a href="https://youtu.be/oLyXU2T1ZuA?t=3175" target="_blank" class="song-title-link" onclick="event.stopPropagation();">8/28/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-24/">#24</a></td>
          <td>-</td>
          <td style="text-align: right;">155</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="girl on fire"
            data-composer=""
            data-style=""
            data-date="2026-02-13"
            data-episode="289"
            data-tempo="-">
          <td><span id="girl-on-fire"><strong>Girl on Fire</strong></span></td>
          <td>2/13/2026</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-289/">#289</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="go tell it on the mountain"
            data-composer=""
            data-style=""
            data-date="2020-12-25"
            data-episode="41"
            data-tempo="135">
          <td><span id="go-tell-it-on-the-mountain"><strong>Go Tell it on the Mountain</strong></span></td>
          <td><a href="https://youtu.be/G-HJYWxotdo?t=3345" target="_blank" class="song-title-link" onclick="event.stopPropagation();">12/25/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-41/">#41</a></td>
          <td>-</td>
          <td style="text-align: right;">135</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="go tell it on the mountain"
            data-composer=""
            data-style=""
            data-date="2021-12-24"
            data-episode="93"
            data-tempo="-">
          <td><span id="go-tell-it-on-the-mountain"><strong>Go Tell it on the Mountain</strong></span></td>
          <td><a href="https://youtu.be/oIJ5iubhwRg?t=288" target="_blank" class="song-title-link" onclick="event.stopPropagation();">12/24/2021</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-93/">#93</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="go tell it on the mountain"
            data-composer=""
            data-style=""
            data-date="2022-12-23"
            data-episode="142"
            data-tempo="-">
          <td><span id="go-tell-it-on-the-mountain"><strong>Go Tell it on the Mountain</strong></span></td>
          <td><a href="https://youtube.com/live/iH6lwOJ7Gb4?t=846" target="_blank" class="song-title-link" onclick="event.stopPropagation();">12/23/2022</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-142/">#142</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="go tell it on the mountain"
            data-composer=""
            data-style=""
            data-date="2023-12-22"
            data-episode="192"
            data-tempo="-">
          <td><span id="go-tell-it-on-the-mountain"><strong>Go Tell it on the Mountain</strong></span></td>
          <td>12/22/2023</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-192/">#192</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="go tell it on the mountain"
            data-composer=""
            data-style=""
            data-date="2025-12-26"
            data-episode="283"
            data-tempo="-">
          <td><span id="go-tell-it-on-the-mountain"><strong>Go Tell it on the Mountain</strong></span></td>
          <td>12/26/2025</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-283/">#283</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="god rest ye merry gentlemen"
            data-composer=""
            data-style=""
            data-date="2020-12-25"
            data-episode="41"
            data-tempo="200">
          <td><span id="god-rest-ye-merry-gentlemen"><strong>God Rest Ye Merry Gentlemen</strong></span></td>
          <td><a href="https://youtu.be/G-HJYWxotdo?t=2267" target="_blank" class="song-title-link" onclick="event.stopPropagation();">12/25/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-41/">#41</a></td>
          <td>-</td>
          <td style="text-align: right;">200</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="god rest ye merry gentlemen"
            data-composer=""
            data-style=""
            data-date="2021-12-24"
            data-episode="93"
            data-tempo="-">
          <td><span id="god-rest-ye-merry-gentlemen"><strong>God Rest Ye Merry Gentlemen</strong></span></td>
          <td><a href="https://youtu.be/oIJ5iubhwRg?t=2234" target="_blank" class="song-title-link" onclick="event.stopPropagation();">12/24/2021</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-93/">#93</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="god rest ye merry gentlemen"
            data-composer=""
            data-style=""
            data-date="2022-12-23"
            data-episode="142"
            data-tempo="-">
          <td><span id="god-rest-ye-merry-gentlemen"><strong>God Rest Ye Merry Gentlemen</strong></span></td>
          <td><a href="https://youtube.com/live/iH6lwOJ7Gb4?t=1137" target="_blank" class="song-title-link" onclick="event.stopPropagation();">12/23/2022</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-142/">#142</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="god rest ye merry gentlemen"
            data-composer=""
            data-style=""
            data-date="2023-12-22"
            data-episode="192"
            data-tempo="-">
          <td><span id="god-rest-ye-merry-gentlemen"><strong>God Rest Ye Merry Gentlemen</strong></span></td>
          <td>12/22/2023</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-192/">#192</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="gratitude euorack closer"
            data-composer=""
            data-style=""
            data-date="2025-11-28"
            data-episode="279"
            data-tempo="-">
          <td><span id="gratitude-euorack-closer"><strong>Gratitude euorack closer</strong></span></td>
          <td>11/28/2025</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-279/">#279</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="greensleeves closer"
            data-composer=""
            data-style=""
            data-date="2025-12-26"
            data-episode="283"
            data-tempo="-">
          <td><span id="greensleeves-closer"><strong>Greensleeves Closer</strong></span></td>
          <td>12/26/2025</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-283/">#283</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="have yourself a merry little christmas"
            data-composer=""
            data-style=""
            data-date="2020-12-11"
            data-episode="39"
            data-tempo="91">
          <td><span id="have-yourself-a-merry-little-christmas"><strong>Have yourself a Merry Little Christmas</strong></span></td>
          <td><a href="https://youtu.be/hfljJ87kgbs?t=2390" target="_blank" class="song-title-link" onclick="event.stopPropagation();">12/11/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-39/">#39</a></td>
          <td>-</td>
          <td style="text-align: right;">91</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="have yourself a merry little christmas"
            data-composer=""
            data-style=""
            data-date="2020-12-25"
            data-episode="41"
            data-tempo="91">
          <td><span id="have-yourself-a-merry-little-christmas"><strong>Have yourself a Merry Little Christmas</strong></span></td>
          <td><a href="https://youtu.be/G-HJYWxotdo?t=260" target="_blank" class="song-title-link" onclick="event.stopPropagation();">12/25/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-41/">#41</a></td>
          <td>-</td>
          <td style="text-align: right;">91</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="have yourself a merry little christmas"
            data-composer=""
            data-style=""
            data-date="2021-12-24"
            data-episode="93"
            data-tempo="-">
          <td><span id="have-yourself-a-merry-little-christmas"><strong>Have yourself a Merry Little Christmas</strong></span></td>
          <td><a href="https://youtu.be/oIJ5iubhwRg?t=600" target="_blank" class="song-title-link" onclick="event.stopPropagation();">12/24/2021</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-93/">#93</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="have yourself a merry little christmas"
            data-composer=""
            data-style=""
            data-date="2023-12-15"
            data-episode="191"
            data-tempo="-">
          <td><span id="have-yourself-a-merry-little-christmas"><strong>Have yourself a Merry Little Christmas</strong></span></td>
          <td>12/15/2023</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-191/">#191</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="have yourself a merry little christmas"
            data-composer=""
            data-style=""
            data-date="2024-12-20"
            data-episode="238"
            data-tempo="-">
          <td><span id="have-yourself-a-merry-little-christmas"><strong>Have yourself a Merry Little Christmas</strong></span></td>
          <td>12/20/2024</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-238/">#238</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="heather closer"
            data-composer=""
            data-style=""
            data-date="2024-09-07"
            data-episode="223"
            data-tempo="-">
          <td><span id="heather-closer"><strong>Heather closer</strong></span></td>
          <td>9/7/2024</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-223/">#223</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="hippies on a corner"
            data-composer="joe sample"
            data-style="funk"
            data-date="2020-05-29"
            data-episode="11"
            data-tempo="122">
          <td><span id="hippies-on-a-corner"><strong>Hippies on a Corner</strong></span><br><small style="color:var(--text-secondary);">by Joe Sample</small></td>
          <td><a href="https://youtu.be/4UMdp7mQUrM?t=3105" target="_blank" class="song-title-link" onclick="event.stopPropagation();">5/29/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-11/">#11</a></td>
          <td><span class="badge-style">funk</span></td>
          <td style="text-align: right;">122</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="holly and the ivy"
            data-composer=""
            data-style=""
            data-date="2021-12-03"
            data-episode="90"
            data-tempo="-">
          <td><span id="holly-and-the-ivy"><strong>Holly and the Ivy</strong></span></td>
          <td><a href="https://youtu.be/cwkUkcDyfaw?t=2288" target="_blank" class="song-title-link" onclick="event.stopPropagation();">12/3/2021</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-90/">#90</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td>bah. why fall behind?</td>
        </tr>
        <tr class="song-row"
            data-title="holly and the ivy"
            data-composer=""
            data-style=""
            data-date="2022-12-09"
            data-episode="140"
            data-tempo="-">
          <td><span id="holly-and-the-ivy"><strong>Holly and the Ivy</strong></span></td>
          <td><a href="https://youtube.com/live/2vM_dR9jpjk?t=151" target="_blank" class="song-title-link" onclick="event.stopPropagation();">12/9/2022</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-140/">#140</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="holly and the ivy"
            data-composer=""
            data-style=""
            data-date="2023-12-15"
            data-episode="191"
            data-tempo="-">
          <td><span id="holly-and-the-ivy"><strong>Holly and the Ivy</strong></span></td>
          <td>12/15/2023</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-191/">#191</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="homage to eno"
            data-composer=""
            data-style=""
            data-date="2026-04-03"
            data-episode="293"
            data-tempo="-">
          <td><span id="homage-to-eno"><strong>Homage to Eno</strong></span></td>
          <td>4/3/2026</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-293/">#293</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="how insensitive closer"
            data-composer=""
            data-style=""
            data-date="2025-09-05"
            data-episode="270"
            data-tempo="-">
          <td><span id="how-insensitive-closer"><strong>How Insensitive closer</strong></span></td>
          <td>9/5/2025</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-270/">#270</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="how my heart sings"
            data-composer=""
            data-style=""
            data-date="2020-09-04"
            data-episode="25"
            data-tempo="-">
          <td><span id="how-my-heart-sings"><strong>How My Heart Sings</strong></span></td>
          <td><a href="https://youtu.be/tCGZLZnLvh4?t=2803" target="_blank" class="song-title-link" onclick="event.stopPropagation();">9/4/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-25/">#25</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="hullo, bolinas"
            data-composer="steve swallow"
            data-style=""
            data-date="2020-07-24"
            data-episode="19"
            data-tempo="-">
          <td><span id="hullo-bolinas"><strong>Hullo, Bolinas</strong></span><br><small style="color:var(--text-secondary);">by Steve Swallow</small></td>
          <td><a href="https://youtu.be/nNbXig2F9Lc?t=775" target="_blank" class="song-title-link" onclick="event.stopPropagation();">7/24/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-19/">#19</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="hullo, bolinas"
            data-composer="steve swallow"
            data-style=""
            data-date="2020-11-27"
            data-episode="37"
            data-tempo="-">
          <td><span id="hullo-bolinas"><strong>Hullo, Bolinas</strong></span><br><small style="color:var(--text-secondary);">by Steve Swallow</small></td>
          <td><a href="https://youtu.be/8W4XQTLdajk?t=2100" target="_blank" class="song-title-link" onclick="event.stopPropagation();">11/27/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-37/">#37</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="hullo, bolinas"
            data-composer="steve swallow"
            data-style=""
            data-date="2021-08-13"
            data-episode="74"
            data-tempo="-">
          <td><span id="hullo-bolinas"><strong>Hullo, Bolinas</strong></span><br><small style="color:var(--text-secondary);">by Steve Swallow</small></td>
          <td><a href="https://youtu.be/jOeFADhEs7c?t=3210" target="_blank" class="song-title-link" onclick="event.stopPropagation();">8/13/2021</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-74/">#74</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="hymn to freedom"
            data-composer=""
            data-style=""
            data-date="2020-07-31"
            data-episode="20"
            data-tempo="-">
          <td><span id="hymn-to-freedom"><strong>Hymn to Freedom</strong></span></td>
          <td><a href="https://youtu.be/sTwgRPVLycU?t=1590" target="_blank" class="song-title-link" onclick="event.stopPropagation();">7/31/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-20/">#20</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="i could write a book"
            data-composer="rogers and hart"
            data-style=""
            data-date="2020-05-29"
            data-episode="11"
            data-tempo="115">
          <td><span id="i-could-write-a-book"><strong>I could write a book</strong></span><br><small style="color:var(--text-secondary);">by Rogers and Hart</small></td>
          <td><a href="https://youtu.be/4UMdp7mQUrM?t=693" target="_blank" class="song-title-link" onclick="event.stopPropagation();">5/29/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-11/">#11</a></td>
          <td>-</td>
          <td style="text-align: right;">115</td>
          <td>in week 12 file</td>
        </tr>
        <tr class="song-row"
            data-title="i could write a book"
            data-composer="rogers and hart"
            data-style=""
            data-date="2020-10-23"
            data-episode="32"
            data-tempo="-">
          <td><span id="i-could-write-a-book"><strong>I could write a book</strong></span><br><small style="color:var(--text-secondary);">by Rogers and Hart</small></td>
          <td><a href="https://youtu.be/fk8JSTyNEfM?t=282" target="_blank" class="song-title-link" onclick="event.stopPropagation();">10/23/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-32/">#32</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="i love you"
            data-composer=""
            data-style=""
            data-date="2020-08-28"
            data-episode="24"
            data-tempo="155">
          <td><span id="i-love-you"><strong>I Love You</strong></span></td>
          <td><a href="https://youtu.be/oLyXU2T1ZuA?t=1550" target="_blank" class="song-title-link" onclick="event.stopPropagation();">8/28/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-24/">#24</a></td>
          <td>-</td>
          <td style="text-align: right;">155</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="i'll be home for christmas"
            data-composer=""
            data-style=""
            data-date="2020-12-04"
            data-episode="38"
            data-tempo="-">
          <td><span id="ill-be-home-for-christmas"><strong>I'll be home for Christmas</strong></span></td>
          <td><a href="https://youtu.be/8ALGHR-ErS0?t=3325" target="_blank" class="song-title-link" onclick="event.stopPropagation();">12/4/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-38/">#38</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="i'll be home for christmas"
            data-composer=""
            data-style=""
            data-date="2020-12-25"
            data-episode="41"
            data-tempo="-">
          <td><span id="ill-be-home-for-christmas"><strong>I'll be home for Christmas</strong></span></td>
          <td><a href="https://youtu.be/G-HJYWxotdo?t=2677" target="_blank" class="song-title-link" onclick="event.stopPropagation();">12/25/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-41/">#41</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="i'll be home for christmas"
            data-composer=""
            data-style=""
            data-date="2021-12-24"
            data-episode="93"
            data-tempo="-">
          <td><span id="ill-be-home-for-christmas"><strong>I'll be home for Christmas</strong></span></td>
          <td><a href="https://youtu.be/oIJ5iubhwRg?t=2610" target="_blank" class="song-title-link" onclick="event.stopPropagation();">12/24/2021</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-93/">#93</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="i'll be home for christmas"
            data-composer=""
            data-style=""
            data-date="2023-12-08"
            data-episode="190"
            data-tempo="-">
          <td><span id="ill-be-home-for-christmas"><strong>I'll be home for Christmas</strong></span></td>
          <td>12/8/2023</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-190/">#190</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="i'll be home for christmas"
            data-composer=""
            data-style=""
            data-date="2024-12-20"
            data-episode="238"
            data-tempo="-">
          <td><span id="ill-be-home-for-christmas"><strong>I'll be home for Christmas</strong></span></td>
          <td>12/20/2024</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-238/">#238</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="ice closer vcv video"
            data-composer=""
            data-style=""
            data-date="2023-09-15"
            data-episode="179"
            data-tempo="-">
          <td><span id="ice-closer-vcv-video"><strong>Ice Closer VCV video</strong></span></td>
          <td><a href="https://youtube.com/live/NfYxpQ1E1Ms?t=3023" target="_blank" class="song-title-link" onclick="event.stopPropagation();">9/15/2023</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-179/">#179</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="imagination"
            data-composer=""
            data-style=""
            data-date="2020-10-16"
            data-episode="31"
            data-tempo="-">
          <td><span id="imagination"><strong>Imagination</strong></span></td>
          <td><a href="https://youtu.be/QeraCjgLykE?t=432" target="_blank" class="song-title-link" onclick="event.stopPropagation();">10/16/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-31/">#31</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="improv closer apr 12"
            data-composer=""
            data-style=""
            data-date="2024-04-12"
            data-episode="204"
            data-tempo="-">
          <td><span id="improv-closer-apr-12"><strong>improv closer apr 12</strong></span></td>
          <td>4/12/2024</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-204/">#204</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="improv closer may 24"
            data-composer=""
            data-style=""
            data-date="2024-05-24"
            data-episode="210"
            data-tempo="-">
          <td><span id="improv-closer-may-24"><strong>Improv Closer may 24</strong></span></td>
          <td>5/24/2024</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-210/">#210</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="improv closer oct 17"
            data-composer=""
            data-style=""
            data-date="2025-10-17"
            data-episode="275"
            data-tempo="-">
          <td><span id="improv-closer-oct-17"><strong>Improv Closer Oct 17</strong></span></td>
          <td>10/17/2025</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-275/">#275</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="improv feb 16"
            data-composer=""
            data-style=""
            data-date="2024-02-16"
            data-episode="199"
            data-tempo="-">
          <td><span id="improv-feb-16"><strong>Improv Feb 16</strong></span></td>
          <td>2/16/2024</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-199a/">#199A</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="improv on look of love"
            data-composer=""
            data-style=""
            data-date="2024-01-19"
            data-episode="196"
            data-tempo="-">
          <td><span id="improv-on-look-of-love"><strong>improv on Look of Love</strong></span></td>
          <td>1/19/2024</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-196/">#196</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="in the meadow"
            data-composer=""
            data-style=""
            data-date="2026-04-03"
            data-episode="293"
            data-tempo="-">
          <td><span id="in-the-meadow"><strong>In the Meadow</strong></span></td>
          <td>4/3/2026</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-293/">#293</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="in the wee small hours of the morning"
            data-composer=""
            data-style="ballad"
            data-date="2020-05-15"
            data-episode="9"
            data-tempo="-">
          <td><span id="in-the-wee-small-hours-of-the-morning"><strong>In the wee small hours of the morning</strong></span></td>
          <td><a href="https://youtu.be/nAk_30ixPvc?t=2463" target="_blank" class="song-title-link" onclick="event.stopPropagation();">5/15/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-9/">#9</a></td>
          <td><span class="badge-style">ballad</span></td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="in the wee small hours of the morning"
            data-composer=""
            data-style="ballad"
            data-date="2020-09-25"
            data-episode="28"
            data-tempo="-">
          <td><span id="in-the-wee-small-hours-of-the-morning"><strong>In the wee small hours of the morning</strong></span></td>
          <td><a href="https://youtu.be/GA-3QzzX3m4?t=3580" target="_blank" class="song-title-link" onclick="event.stopPropagation();">9/25/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-28/">#28</a></td>
          <td><span class="badge-style">ballad</span></td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="in walked bud"
            data-composer="thelonius monk"
            data-style="funk"
            data-date="2020-04-17"
            data-episode="5"
            data-tempo="54">
          <td><span id="in-walked-bud"><strong>In walked Bud</strong></span><br><small style="color:var(--text-secondary);">by Thelonius Monk</small></td>
          <td><a href="https://youtu.be/mlWuikMRDGo?t=1860" target="_blank" class="song-title-link" onclick="event.stopPropagation();">4/17/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-5/">#5</a></td>
          <td><span class="badge-style">funk</span></td>
          <td style="text-align: right;">54</td>
          <td>REDO (fuzz gtr?)</td>
        </tr>
        <tr class="song-row"
            data-title="in walked bud"
            data-composer="thelonius monk"
            data-style="funk"
            data-date="2021-03-05"
            data-episode="51"
            data-tempo="62">
          <td><span id="in-walked-bud"><strong>In walked Bud</strong></span><br><small style="color:var(--text-secondary);">by Thelonius Monk</small></td>
          <td><a href="https://youtu.be/Wxw626FLkDw?t=1230" target="_blank" class="song-title-link" onclick="event.stopPropagation();">3/5/2021</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-51/">#51</a></td>
          <td><span class="badge-style">funk</span></td>
          <td style="text-align: right;">62</td>
          <td>v messy, organ too loud</td>
        </tr>
        <tr class="song-row"
            data-title="interesting piano closer"
            data-composer=""
            data-style=""
            data-date="2025-06-06"
            data-episode="259"
            data-tempo="-">
          <td><span id="interesting-piano-closer"><strong>interesting piano closer</strong></span></td>
          <td>6/6/2025</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-259/">#259</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="interlude march 10"
            data-composer=""
            data-style=""
            data-date="2023-03-10"
            data-episode="153"
            data-tempo="-">
          <td><span id="interlude-march-10"><strong>Interlude March 10</strong></span></td>
          <td><a href="https://youtube.com/live/4WWV1-H7mrQ?t=2662" target="_blank" class="song-title-link" onclick="event.stopPropagation();">3/10/2023</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-153/">#153</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="jarrettesque piano improv"
            data-composer=""
            data-style=""
            data-date="2021-01-01"
            data-episode="42"
            data-tempo="-">
          <td><span id="jarrettesque-piano-improv"><strong>Jarrettesque Piano Improv</strong></span></td>
          <td><a href="https://youtu.be/i7H03-9N1As?t=2492" target="_blank" class="song-title-link" onclick="event.stopPropagation();">1/1/2021</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-42/">#42</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="kiss him goodbye"
            data-composer=""
            data-style=""
            data-date="2020-11-27"
            data-episode="37"
            data-tempo="126">
          <td><span id="kiss-him-goodbye"><strong>Kiss Him Goodbye</strong></span></td>
          <td><a href="https://youtu.be/8W4XQTLdajk?t=3284" target="_blank" class="song-title-link" onclick="event.stopPropagation();">11/27/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-37/">#37</a></td>
          <td>-</td>
          <td style="text-align: right;">126</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="köpenicker straße"
            data-composer=""
            data-style=""
            data-date="2026-04-03"
            data-episode="293"
            data-tempo="-">
          <td><span id="kpenicker-strae"><strong>Köpenicker Straße</strong></span></td>
          <td>4/3/2026</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-293/">#293</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="l'indifference"
            data-composer=""
            data-style=""
            data-date="2020-07-31"
            data-episode="20"
            data-tempo="-">
          <td><span id="lindifference"><strong>L'Indifference</strong></span></td>
          <td><a href="https://youtu.be/sTwgRPVLycU?t=384" target="_blank" class="song-title-link" onclick="event.stopPropagation();">7/31/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-20/">#20</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td>practice, man, practice</td>
        </tr>
        <tr class="song-row"
            data-title="la mer"
            data-composer=""
            data-style=""
            data-date="2021-03-26"
            data-episode="54"
            data-tempo="-">
          <td><span id="la-mer"><strong>La Mer</strong></span></td>
          <td><a href="https://youtu.be/L9jDIlX7bjs?t=839" target="_blank" class="song-title-link" onclick="event.stopPropagation();">3/26/2021</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-54/">#54</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="larry fast improv"
            data-composer="bill walker"
            data-style=""
            data-date="2020-11-20"
            data-episode="36"
            data-tempo="90">
          <td><span id="larry-fast-improv"><strong>Larry Fast Improv</strong></span><br><small style="color:var(--text-secondary);">by Bill Walker</small></td>
          <td><a href="https://youtu.be/FgUbgdPd9pw?t=1795" target="_blank" class="song-title-link" onclick="event.stopPropagation();">11/20/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-36/">#36</a></td>
          <td>-</td>
          <td style="text-align: right;">90</td>
          <td>needs shape and structure; organ surprisingly good</td>
        </tr>
        <tr class="song-row"
            data-title="lean on me"
            data-composer="bill withers"
            data-style="vocal"
            data-date="2020-06-05"
            data-episode="12"
            data-tempo="78">
          <td><span id="lean-on-me"><strong>Lean on Me</strong></span><br><small style="color:var(--text-secondary);">by Bill Withers</small></td>
          <td><a href="https://youtu.be/8aHUkT2wFNc?t=2890" target="_blank" class="song-title-link" onclick="event.stopPropagation();">6/5/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-12/">#12</a></td>
          <td><span class="badge-style">VOCAL</span></td>
          <td style="text-align: right;">78</td>
          <td>tracks good; singing meh</td>
        </tr>
        <tr class="song-row"
            data-title="let it snow"
            data-composer=""
            data-style=""
            data-date="2020-12-18"
            data-episode="40"
            data-tempo="130">
          <td><span id="let-it-snow"><strong>Let it Snow</strong></span></td>
          <td><a href="https://youtu.be/yhWB3cwCzOI?t=1280" target="_blank" class="song-title-link" onclick="event.stopPropagation();">12/18/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-40/">#40</a></td>
          <td>-</td>
          <td style="text-align: right;">130</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="let it snow"
            data-composer=""
            data-style=""
            data-date="2025-12-26"
            data-episode="283"
            data-tempo="-">
          <td><span id="let-it-snow"><strong>Let it Snow</strong></span></td>
          <td>12/26/2025</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-283/">#283</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="letters of the alphabet improv"
            data-composer=""
            data-style="ballad"
            data-date="2021-06-11"
            data-episode="65"
            data-tempo="-">
          <td><span id="letters-of-the-alphabet-improv"><strong>Letters of the Alphabet improv</strong></span></td>
          <td><a href="https://youtu.be/ZnlVVoHkbCE?t=1730" target="_blank" class="song-title-link" onclick="event.stopPropagation();">6/11/2021</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-65/">#65</a></td>
          <td><span class="badge-style">Ballad</span></td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="little birdie"
            data-composer=""
            data-style=""
            data-date="2020-12-04"
            data-episode="38"
            data-tempo="90">
          <td><span id="little-birdie"><strong>Little Birdie</strong></span></td>
          <td><a href="https://youtu.be/8ALGHR-ErS0?t=1960" target="_blank" class="song-title-link" onclick="event.stopPropagation();">12/4/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-38/">#38</a></td>
          <td>-</td>
          <td style="text-align: right;">90</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="little samba"
            data-composer="bill walker"
            data-style="samba"
            data-date="2020-03-27"
            data-episode="2"
            data-tempo="-">
          <td><span id="little-samba"><strong>Little Samba</strong></span><br><small style="color:var(--text-secondary);">by Bill Walker</small></td>
          <td><a href="https://youtu.be/8OIItLaezQk?t=200" target="_blank" class="song-title-link" onclick="event.stopPropagation();">3/27/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-2/">#2</a></td>
          <td><span class="badge-style">samba</span></td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="little samba"
            data-composer="bill walker"
            data-style="samba"
            data-date="2020-07-03"
            data-episode="16"
            data-tempo="90">
          <td><span id="little-samba"><strong>Little Samba</strong></span><br><small style="color:var(--text-secondary);">by Bill Walker</small></td>
          <td><a href="https://youtu.be/pX-E6ZVGrpA?t=694" target="_blank" class="song-title-link" onclick="event.stopPropagation();">7/3/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-16/">#16</a></td>
          <td><span class="badge-style">samba</span></td>
          <td style="text-align: right;">90</td>
          <td>nice improv</td>
        </tr>
        <tr class="song-row"
            data-title="little samba"
            data-composer="bill walker"
            data-style="samba"
            data-date="2021-01-01"
            data-episode="42"
            data-tempo="90">
          <td><span id="little-samba"><strong>Little Samba</strong></span><br><small style="color:var(--text-secondary);">by Bill Walker</small></td>
          <td><a href="https://youtu.be/i7H03-9N1As?t=578" target="_blank" class="song-title-link" onclick="event.stopPropagation();">1/1/2021</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-42/">#42</a></td>
          <td><span class="badge-style">samba</span></td>
          <td style="text-align: right;">90</td>
          <td>gtr too repetitive; organ + vibes good</td>
        </tr>
        <tr class="song-row"
            data-title="lofi improvisation"
            data-composer=""
            data-style=""
            data-date="2021-01-01"
            data-episode="42"
            data-tempo="72">
          <td><span id="lofi-improvisation"><strong>LOFi Improvisation</strong></span></td>
          <td><a href="https://youtu.be/i7H03-9N1As?t=1767" target="_blank" class="song-title-link" onclick="event.stopPropagation();">1/1/2021</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-42/">#42</a></td>
          <td>-</td>
          <td style="text-align: right;">72</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="lullaby for thursday"
            data-composer=""
            data-style=""
            data-date="2025-01-24"
            data-episode="243"
            data-tempo="-">
          <td><span id="lullaby-for-thursday"><strong>Lullaby for Thursday</strong></span></td>
          <td>1/24/2025</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-243/">#243</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="melodica looper and vcv"
            data-composer=""
            data-style=""
            data-date="2024-01-12"
            data-episode="195"
            data-tempo="-">
          <td><span id="melodica-looper-and-vcv"><strong>Melodica looper and VCV</strong></span></td>
          <td><a href="https://youtube.com/live/dkMgQ_pHYNk?t=3339" target="_blank" class="song-title-link" onclick="event.stopPropagation();">1/12/2024</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-195/">#195</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="melodicer and accordion"
            data-composer=""
            data-style=""
            data-date="2023-11-10"
            data-episode="186"
            data-tempo="-">
          <td><span id="melodicer-and-accordion"><strong>Melodicer and Accordion</strong></span></td>
          <td>11/10/2023</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-186/">#186</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="merry little christmas"
            data-composer=""
            data-style=""
            data-date="2020-12-11"
            data-episode="39"
            data-tempo="91">
          <td><span id="merry-little-christmas"><strong>Merry Little Christmas</strong></span></td>
          <td><a href="https://youtu.be/hfljJ87kgbs?t=2390" target="_blank" class="song-title-link" onclick="event.stopPropagation();">12/11/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-39/">#39</a></td>
          <td>-</td>
          <td style="text-align: right;">91</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="merry little christmas"
            data-composer=""
            data-style=""
            data-date="2021-12-17"
            data-episode="92"
            data-tempo="-">
          <td><span id="merry-little-christmas"><strong>Merry Little Christmas</strong></span></td>
          <td><a href="https://youtu.be/-MgcGR7PIMg?t=200" target="_blank" class="song-title-link" onclick="event.stopPropagation();">12/17/2021</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-92/">#92</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td>swingin'</td>
        </tr>
        <tr class="song-row"
            data-title="merry little christmas"
            data-composer=""
            data-style=""
            data-date="2022-12-16"
            data-episode="141"
            data-tempo="-">
          <td><span id="merry-little-christmas"><strong>Merry Little Christmas</strong></span></td>
          <td><a href="https://youtube.com/live/676nV2NzygY?t=3060" target="_blank" class="song-title-link" onclick="event.stopPropagation();">12/16/2022</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-141/">#141</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td>nice solo</td>
        </tr>
        <tr class="song-row"
            data-title="merry little christmas"
            data-composer=""
            data-style=""
            data-date="2025-12-12"
            data-episode="281"
            data-tempo="-">
          <td><span id="merry-little-christmas"><strong>Merry Little Christmas</strong></span></td>
          <td>12/12/2025</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-281/">#281</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="minor blues improvisation"
            data-composer="bill walker"
            data-style=""
            data-date="2020-07-24"
            data-episode="19"
            data-tempo="-">
          <td><span id="minor-blues-improvisation"><strong>Minor Blues Improvisation</strong></span><br><small style="color:var(--text-secondary);">by Bill Walker</small></td>
          <td><a href="https://youtu.be/nNbXig2F9Lc?t=2038" target="_blank" class="song-title-link" onclick="event.stopPropagation();">7/24/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-19/">#19</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td>TOO LONG, boring</td>
        </tr>
        <tr class="song-row"
            data-title="missing arrangement improvisation"
            data-composer=""
            data-style="ballad"
            data-date="2021-04-23"
            data-episode="58"
            data-tempo="-">
          <td><span id="missing-arrangement-improvisation"><strong>Missing Arrangement Improvisation</strong></span></td>
          <td><a href="https://youtu.be/yYYl7DQc0K0?t=2402" target="_blank" class="song-title-link" onclick="event.stopPropagation();">4/23/2021</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-58/">#58</a></td>
          <td><span class="badge-style">Ballad</span></td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="modular closer"
            data-composer=""
            data-style=""
            data-date="2025-04-25"
            data-episode="253"
            data-tempo="-">
          <td><span id="modular-closer"><strong>Modular Closer</strong></span></td>
          <td>4/25/2025</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-253/">#253</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="modular impov: allegro"
            data-composer=""
            data-style=""
            data-date="2025-10-03"
            data-episode="9999"
            data-tempo="-">
          <td><span id="modular-impov-allegro"><strong>Modular Impov: Allegro</strong></span></td>
          <td>10/3/2025</td>
          <td><a href="{{ '/episodes/' | relative_url }}show-1032025/">Show</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="modular impov: lento"
            data-composer=""
            data-style=""
            data-date="2025-10-03"
            data-episode="9999"
            data-tempo="-">
          <td><span id="modular-impov-lento"><strong>Modular Impov: Lento</strong></span></td>
          <td>10/3/2025</td>
          <td><a href="{{ '/episodes/' | relative_url }}show-1032025/">Show</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="moon river"
            data-composer=""
            data-style=""
            data-date="2024-10-25"
            data-episode="230"
            data-tempo="-">
          <td><span id="moon-river"><strong>Moon River</strong></span></td>
          <td>10/25/2024</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-230/">#230</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="my foolish heart"
            data-composer=""
            data-style="ballad"
            data-date="2020-07-10"
            data-episode="17"
            data-tempo="-">
          <td><span id="my-foolish-heart"><strong>My Foolish Heart</strong></span></td>
          <td><a href="https://youtu.be/pWeOutFnTGs?t=3331" target="_blank" class="song-title-link" onclick="event.stopPropagation();">7/10/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-17/">#17</a></td>
          <td><span class="badge-style">ballad</span></td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="my foolish heart"
            data-composer=""
            data-style="ballad"
            data-date="2020-10-23"
            data-episode="32"
            data-tempo="-">
          <td><span id="my-foolish-heart"><strong>My Foolish Heart</strong></span></td>
          <td><a href="https://youtu.be/fk8JSTyNEfM?t=3318" target="_blank" class="song-title-link" onclick="event.stopPropagation();">10/23/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-32/">#32</a></td>
          <td><span class="badge-style">ballad</span></td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="my foolish heart"
            data-composer=""
            data-style="ballad"
            data-date="2021-07-30"
            data-episode="72"
            data-tempo="-">
          <td><span id="my-foolish-heart"><strong>My Foolish Heart</strong></span></td>
          <td><a href="https://youtu.be/SFHGArSt8qo?t=3450" target="_blank" class="song-title-link" onclick="event.stopPropagation();">7/30/2021</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-72/">#72</a></td>
          <td><span class="badge-style">ballad</span></td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="my lord, what a morning"
            data-composer=""
            data-style="swing"
            data-date="2021-04-02"
            data-episode="55"
            data-tempo="-">
          <td><span id="my-lord-what-a-morning"><strong>My Lord, What a Morning</strong></span></td>
          <td><a href="https://youtu.be/brtK3KrZ6Io?t=3615" target="_blank" class="song-title-link" onclick="event.stopPropagation();">4/2/2021</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-55/">#55</a></td>
          <td><span class="badge-style">Swing</span></td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="my lord, what a morning"
            data-composer=""
            data-style="swing"
            data-date="2021-04-09"
            data-episode="56"
            data-tempo="-">
          <td><span id="my-lord-what-a-morning"><strong>My Lord, What a Morning</strong></span></td>
          <td><a href="https://youtu.be/RVecTJg5GEs?t=1670" target="_blank" class="song-title-link" onclick="event.stopPropagation();">4/9/2021</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-56/">#56</a></td>
          <td><span class="badge-style">Swing</span></td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="my lord, what a morning"
            data-composer=""
            data-style="swing"
            data-date="2024-03-29"
            data-episode="55"
            data-tempo="-">
          <td><span id="my-lord-what-a-morning"><strong>My Lord, What a Morning</strong></span></td>
          <td><a href="https://youtu.be/brtK3KrZ6Io?t=3023" target="_blank" class="song-title-link" onclick="event.stopPropagation();">3/29/2024</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-55-rerun-3292024/">#55</a></td>
          <td><span class="badge-style">Swing</span></td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="new ambient pieces"
            data-composer=""
            data-style=""
            data-date="2026-06-19"
            data-episode="299"
            data-tempo="-">
          <td><span id="new-ambient-pieces"><strong>New Ambient Pieces</strong></span></td>
          <td>6/19/2026</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-299c/">#299C</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="night rhodes"
            data-composer=""
            data-style=""
            data-date="2026-04-03"
            data-episode="293"
            data-tempo="-">
          <td><span id="night-rhodes"><strong>Night Rhodes</strong></span></td>
          <td>4/3/2026</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-293/">#293</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="novemberain"
            data-composer="bill walker"
            data-style=""
            data-date="2020-05-01"
            data-episode="7"
            data-tempo="65">
          <td><span id="novemberain"><strong>NovembeRain</strong></span><br><small style="color:var(--text-secondary);">by Bill Walker</small></td>
          <td><a href="https://youtu.be/QGkAB6VG8VU?t=603" target="_blank" class="song-title-link" onclick="event.stopPropagation();">5/1/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-7/">#7</a></td>
          <td>-</td>
          <td style="text-align: right;">65</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="novemberain"
            data-composer="bill walker"
            data-style=""
            data-date="2020-11-06"
            data-episode="34"
            data-tempo="71">
          <td><span id="novemberain"><strong>NovembeRain</strong></span><br><small style="color:var(--text-secondary);">by Bill Walker</small></td>
          <td><a href="https://youtu.be/EKJT69DCOnA?t=530" target="_blank" class="song-title-link" onclick="event.stopPropagation();">11/6/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-34/">#34</a></td>
          <td>-</td>
          <td style="text-align: right;">71</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="o christmas tree"
            data-composer=""
            data-style=""
            data-date="2020-12-11"
            data-episode="39"
            data-tempo="110">
          <td><span id="o-christmas-tree"><strong>O Christmas Tree</strong></span></td>
          <td><a href="https://youtu.be/hfljJ87kgbs?t=260" target="_blank" class="song-title-link" onclick="event.stopPropagation();">12/11/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-39/">#39</a></td>
          <td>-</td>
          <td style="text-align: right;">110</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="o christmas tree"
            data-composer=""
            data-style=""
            data-date="2020-12-11"
            data-episode="39"
            data-tempo="110">
          <td><span id="o-christmas-tree"><strong>O Christmas Tree</strong></span></td>
          <td><a href="https://youtu.be/hfljJ87kgbs?t=260" target="_blank" class="song-title-link" onclick="event.stopPropagation();">12/11/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-39/">#39</a></td>
          <td>-</td>
          <td style="text-align: right;">110</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="o christmas tree"
            data-composer=""
            data-style=""
            data-date="2020-12-25"
            data-episode="41"
            data-tempo="110">
          <td><span id="o-christmas-tree"><strong>O Christmas Tree</strong></span></td>
          <td><a href="https://youtu.be/G-HJYWxotdo?t=1950" target="_blank" class="song-title-link" onclick="event.stopPropagation();">12/25/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-41/">#41</a></td>
          <td>-</td>
          <td style="text-align: right;">110</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="o christmas tree"
            data-composer=""
            data-style=""
            data-date="2021-12-10"
            data-episode="91"
            data-tempo="-">
          <td><span id="o-christmas-tree"><strong>O Christmas Tree</strong></span></td>
          <td><a href="https://youtu.be/vr3lHzT6u9s?t=1903" target="_blank" class="song-title-link" onclick="event.stopPropagation();">12/10/2021</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-91/">#91</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="o christmas tree"
            data-composer=""
            data-style=""
            data-date="2021-12-24"
            data-episode="93"
            data-tempo="-">
          <td><span id="o-christmas-tree"><strong>O Christmas Tree</strong></span></td>
          <td><a href="https://youtu.be/oIJ5iubhwRg?t=1140" target="_blank" class="song-title-link" onclick="event.stopPropagation();">12/24/2021</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-93/">#93</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="o christmas tree"
            data-composer=""
            data-style=""
            data-date="2022-12-23"
            data-episode="142"
            data-tempo="-">
          <td><span id="o-christmas-tree"><strong>O Christmas Tree</strong></span></td>
          <td><a href="https://youtube.com/live/iH6lwOJ7Gb4?t=201" target="_blank" class="song-title-link" onclick="event.stopPropagation();">12/23/2022</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-142/">#142</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="o christmas tree"
            data-composer=""
            data-style=""
            data-date="2023-12-08"
            data-episode="190"
            data-tempo="-">
          <td><span id="o-christmas-tree"><strong>O Christmas Tree</strong></span></td>
          <td>12/8/2023</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-190/">#190</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="o christmas tree"
            data-composer=""
            data-style=""
            data-date="2024-12-13"
            data-episode="237"
            data-tempo="-">
          <td><span id="o-christmas-tree"><strong>O Christmas Tree</strong></span></td>
          <td>12/13/2024</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-237/">#237</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="o christmas tree"
            data-composer=""
            data-style=""
            data-date="2025-12-05"
            data-episode="280"
            data-tempo="-">
          <td><span id="o-christmas-tree"><strong>O Christmas Tree</strong></span></td>
          <td>12/5/2025</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-280/">#280</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="o come o come emmanuel"
            data-composer=""
            data-style=""
            data-date="2020-12-18"
            data-episode="40"
            data-tempo="130">
          <td><span id="o-come-o-come-emmanuel"><strong>O Come O Come Emmanuel</strong></span></td>
          <td><a href="https://youtu.be/yhWB3cwCzOI?t=1787" target="_blank" class="song-title-link" onclick="event.stopPropagation();">12/18/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-40/">#40</a></td>
          <td>-</td>
          <td style="text-align: right;">130</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="o come o come emmanuel"
            data-composer=""
            data-style=""
            data-date="2021-12-24"
            data-episode="93"
            data-tempo="-">
          <td><span id="o-come-o-come-emmanuel"><strong>O Come O Come Emmanuel</strong></span></td>
          <td><a href="https://youtu.be/oIJ5iubhwRg?t=1530" target="_blank" class="song-title-link" onclick="event.stopPropagation();">12/24/2021</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-93/">#93</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="o come o come emmanuel"
            data-composer=""
            data-style=""
            data-date="2022-12-23"
            data-episode="142"
            data-tempo="-">
          <td><span id="o-come-o-come-emmanuel"><strong>O Come O Come Emmanuel</strong></span></td>
          <td><a href="https://youtube.com/live/iH6lwOJ7Gb4?t=2524" target="_blank" class="song-title-link" onclick="event.stopPropagation();">12/23/2022</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-142/">#142</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="o come o come emmanuel"
            data-composer=""
            data-style=""
            data-date="2023-12-22"
            data-episode="192"
            data-tempo="-">
          <td><span id="o-come-o-come-emmanuel"><strong>O Come O Come Emmanuel</strong></span></td>
          <td>12/22/2023</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-192/">#192</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="o come o come emmanuel"
            data-composer=""
            data-style=""
            data-date="2024-12-13"
            data-episode="237"
            data-tempo="-">
          <td><span id="o-come-o-come-emmanuel"><strong>O Come O Come Emmanuel</strong></span></td>
          <td>12/13/2024</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-237/">#237</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="o come o come emmanuel"
            data-composer=""
            data-style=""
            data-date="2025-12-19"
            data-episode="282"
            data-tempo="-">
          <td><span id="o-come-o-come-emmanuel"><strong>O Come O Come Emmanuel</strong></span></td>
          <td>12/19/2025</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-282/">#282</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="o holy night"
            data-composer=""
            data-style=""
            data-date="2020-12-25"
            data-episode="41"
            data-tempo="-">
          <td><span id="o-holy-night"><strong>O Holy Night</strong></span></td>
          <td><a href="https://youtu.be/G-HJYWxotdo?t=3735" target="_blank" class="song-title-link" onclick="event.stopPropagation();">12/25/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-41/">#41</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="o holy night"
            data-composer=""
            data-style=""
            data-date="2021-12-24"
            data-episode="93"
            data-tempo="-">
          <td><span id="o-holy-night"><strong>O Holy Night</strong></span></td>
          <td><a href="https://youtu.be/oIJ5iubhwRg?t=3240" target="_blank" class="song-title-link" onclick="event.stopPropagation();">12/24/2021</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-93/">#93</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="o holy night"
            data-composer=""
            data-style=""
            data-date="2022-12-09"
            data-episode="140"
            data-tempo="-">
          <td><span id="o-holy-night"><strong>O Holy Night</strong></span></td>
          <td><a href="https://youtube.com/live/2vM_dR9jpjk?t=3420" target="_blank" class="song-title-link" onclick="event.stopPropagation();">12/9/2022</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-140/">#140</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="o nosso amor"
            data-composer=""
            data-style="bossa"
            data-date="2021-05-21"
            data-episode="62"
            data-tempo="-">
          <td><span id="o-nosso-amor"><strong>O Nosso Amor</strong></span></td>
          <td><a href="https://youtu.be/tB5vd6dRUS4?t=1275" target="_blank" class="song-title-link" onclick="event.stopPropagation();">5/21/2021</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-62/">#62</a></td>
          <td><span class="badge-style">Bossa</span></td>
          <td style="text-align: right;">-</td>
          <td>too repetitive</td>
        </tr>
        <tr class="song-row"
            data-title="ocean signals"
            data-composer=""
            data-style=""
            data-date="2026-04-03"
            data-episode="293"
            data-tempo="-">
          <td><span id="ocean-signals"><strong>Ocean Signals</strong></span></td>
          <td>4/3/2026</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-293/">#293</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="ode to missing sustain pedal"
            data-composer=""
            data-style=""
            data-date="2023-06-30"
            data-episode="169"
            data-tempo="-">
          <td><span id="ode-to-missing-sustain-pedal"><strong>Ode to Missing Sustain Pedal</strong></span></td>
          <td>6/30/2023</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-169/">#169</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="oh good grief"
            data-composer=""
            data-style=""
            data-date="2021-02-12"
            data-episode="48"
            data-tempo="128">
          <td><span id="oh-good-grief"><strong>Oh Good Grief</strong></span></td>
          <td><a href="https://youtu.be/qK4QPjXbR7g?t=2270" target="_blank" class="song-title-link" onclick="event.stopPropagation();">2/12/2021</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-48/">#48</a></td>
          <td>-</td>
          <td style="text-align: right;">128</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="on a clear day"
            data-composer=""
            data-style=""
            data-date="2020-10-16"
            data-episode="31"
            data-tempo="-">
          <td><span id="on-a-clear-day"><strong>On a Clear Day</strong></span></td>
          <td><a href="https://youtu.be/QeraCjgLykE?t=1657" target="_blank" class="song-title-link" onclick="event.stopPropagation();">10/16/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-31/">#31</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="on the sunny side of the street"
            data-composer=""
            data-style=""
            data-date="2020-09-11"
            data-episode="26"
            data-tempo="-">
          <td><span id="on-the-sunny-side-of-the-street"><strong>On the Sunny side of the street</strong></span></td>
          <td><a href="https://youtu.be/texnvgIfzO8?t=3106" target="_blank" class="song-title-link" onclick="event.stopPropagation();">9/11/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-26/">#26</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td>try a little faster?</td>
        </tr>
        <tr class="song-row"
            data-title="one note samba"
            data-composer=""
            data-style="bossa"
            data-date="2021-04-30"
            data-episode="59"
            data-tempo="-">
          <td><span id="one-note-samba"><strong>One Note Samba</strong></span></td>
          <td><a href="https://youtu.be/ItLGYec3rkE?t=1107" target="_blank" class="song-title-link" onclick="event.stopPropagation();">4/30/2021</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-59/">#59</a></td>
          <td><span class="badge-style">Bossa</span></td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="orba jam"
            data-composer="bill walker"
            data-style=""
            data-date="2020-11-27"
            data-episode="37"
            data-tempo="60">
          <td><span id="orba-jam"><strong>Orba Jam</strong></span><br><small style="color:var(--text-secondary);">by Bill Walker</small></td>
          <td><a href="https://youtu.be/8W4XQTLdajk?t=1172" target="_blank" class="song-title-link" onclick="event.stopPropagation();">11/27/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-37/">#37</a></td>
          <td>-</td>
          <td style="text-align: right;">60</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="orba with vcv swirling"
            data-composer=""
            data-style=""
            data-date="2024-02-02"
            data-episode="198"
            data-tempo="-">
          <td><span id="orba-with-vcv-swirling"><strong>Orba with VCV swirling</strong></span></td>
          <td>2/2/2024</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-198/">#198</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="other improvisation"
            data-composer="bill walker"
            data-style=""
            data-date="2020-10-30"
            data-episode="33"
            data-tempo="-">
          <td><span id="other-improvisation"><strong>OTHER Improvisation</strong></span><br><small style="color:var(--text-secondary);">by Bill Walker</small></td>
          <td><a href="https://youtu.be/kRuS4bBAE_s?t=1815" target="_blank" class="song-title-link" onclick="event.stopPropagation();">10/30/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-33/">#33</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="our love is here to stay"
            data-composer="george gerswin"
            data-style=""
            data-date="2020-05-01"
            data-episode="7"
            data-tempo="-">
          <td><span id="our-love-is-here-to-stay"><strong>Our Love is here to Stay</strong></span><br><small style="color:var(--text-secondary);">by George Gerswin</small></td>
          <td><a href="https://youtu.be/QGkAB6VG8VU?t=260" target="_blank" class="song-title-link" onclick="event.stopPropagation();">5/1/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-7/">#7</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="our love is here to stay"
            data-composer="george gerswin"
            data-style=""
            data-date="2020-12-18"
            data-episode="40"
            data-tempo="-">
          <td><span id="our-love-is-here-to-stay"><strong>Our Love is here to Stay</strong></span><br><small style="color:var(--text-secondary);">by George Gerswin</small></td>
          <td><a href="https://youtu.be/yhWB3cwCzOI?t=2178" target="_blank" class="song-title-link" onclick="event.stopPropagation();">12/18/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-40/">#40</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="pack ice video"
            data-composer=""
            data-style=""
            data-date="2025-06-27"
            data-episode="262"
            data-tempo="-">
          <td><span id="pack-ice-video"><strong>Pack Ice Video</strong></span></td>
          <td>6/27/2025</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-262/">#262</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="pams pro workout debut closer"
            data-composer=""
            data-style=""
            data-date="2025-11-21"
            data-episode="278"
            data-tempo="-">
          <td><span id="pams-pro-workout-debut-closer"><strong>pams pro workout debut closer</strong></span></td>
          <td>11/21/2025</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-278/">#278</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="paranoimia"
            data-composer=""
            data-style=""
            data-date="2020-07-31"
            data-episode="20"
            data-tempo="110">
          <td><span id="paranoimia"><strong>Paranoimia</strong></span></td>
          <td><a href="https://youtu.be/sTwgRPVLycU?t=1173" target="_blank" class="song-title-link" onclick="event.stopPropagation();">7/31/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-20/">#20</a></td>
          <td>-</td>
          <td style="text-align: right;">110</td>
          <td>live looping! fix it up and try again</td>
        </tr>
        <tr class="song-row"
            data-title="paranoimia"
            data-composer=""
            data-style=""
            data-date="2021-03-12"
            data-episode="52"
            data-tempo="110">
          <td><span id="paranoimia"><strong>Paranoimia</strong></span></td>
          <td><a href="https://youtu.be/lrD9RxOWutM?t=732" target="_blank" class="song-title-link" onclick="event.stopPropagation();">3/12/2021</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-52/">#52</a></td>
          <td>-</td>
          <td style="text-align: right;">110</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="peace piece"
            data-composer="bill evans"
            data-style="ballad"
            data-date="2020-06-05"
            data-episode="12"
            data-tempo="-">
          <td><span id="peace-piece"><strong>Peace Piece</strong></span><br><small style="color:var(--text-secondary);">by Bill Evans</small></td>
          <td><a href="https://youtu.be/8aHUkT2wFNc?t=3253" target="_blank" class="song-title-link" onclick="event.stopPropagation();">6/5/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-12/">#12</a></td>
          <td><span class="badge-style">ballad</span></td>
          <td style="text-align: right;">-</td>
          <td>practice man practice</td>
        </tr>
        <tr class="song-row"
            data-title="peace piece"
            data-composer="bill evans"
            data-style="ballad"
            data-date="2021-04-16"
            data-episode="57"
            data-tempo="-">
          <td><span id="peace-piece"><strong>Peace Piece</strong></span><br><small style="color:var(--text-secondary);">by Bill Evans</small></td>
          <td><a href="https://youtu.be/l0R4TcCeMAY?t=3350" target="_blank" class="song-title-link" onclick="event.stopPropagation();">4/16/2021</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-57/">#57</a></td>
          <td><span class="badge-style">ballad</span></td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="peace piece"
            data-composer="bill evans"
            data-style="ballad"
            data-date="2021-07-16"
            data-episode="70"
            data-tempo="-">
          <td><span id="peace-piece"><strong>Peace Piece</strong></span><br><small style="color:var(--text-secondary);">by Bill Evans</small></td>
          <td><a href="https://youtu.be/yaLXVIw0nxE?t=1632" target="_blank" class="song-title-link" onclick="event.stopPropagation();">7/16/2021</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-70/">#70</a></td>
          <td><span class="badge-style">ballad</span></td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="peace piece"
            data-composer="bill evans"
            data-style="ballad"
            data-date="2022-05-20"
            data-episode="114"
            data-tempo="-">
          <td><span id="peace-piece"><strong>Peace Piece</strong></span><br><small style="color:var(--text-secondary);">by Bill Evans</small></td>
          <td><a href="https://youtu.be/Wmyvd2LlVw0?t=3127" target="_blank" class="song-title-link" onclick="event.stopPropagation();">5/20/2022</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-114/">#114</a></td>
          <td><span class="badge-style">ballad</span></td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="peace piece"
            data-composer="bill evans"
            data-style="ballad"
            data-date="2023-06-23"
            data-episode="168"
            data-tempo="-">
          <td><span id="peace-piece"><strong>Peace Piece</strong></span><br><small style="color:var(--text-secondary);">by Bill Evans</small></td>
          <td><a href="https://www.youtube.com/watch?v=w28RQAWi17U?t=3023" target="_blank" class="song-title-link" onclick="event.stopPropagation();">6/23/2023</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-168/">#168</a></td>
          <td><span class="badge-style">ballad</span></td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="peace piece"
            data-composer="bill evans"
            data-style="ballad"
            data-date="2023-10-27"
            data-episode="184"
            data-tempo="-">
          <td><span id="peace-piece"><strong>Peace Piece</strong></span><br><small style="color:var(--text-secondary);">by Bill Evans</small></td>
          <td><a href="https://youtube.com/live/3TUXOsOjp-U?t=3023" target="_blank" class="song-title-link" onclick="event.stopPropagation();">10/27/2023</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-184/">#184</a></td>
          <td><span class="badge-style">ballad</span></td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="peace piece"
            data-composer="bill evans"
            data-style="ballad"
            data-date="2024-10-11"
            data-episode="228"
            data-tempo="-">
          <td><span id="peace-piece"><strong>Peace Piece</strong></span><br><small style="color:var(--text-secondary);">by Bill Evans</small></td>
          <td>10/11/2024</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-228/">#228</a></td>
          <td><span class="badge-style">ballad</span></td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="peace piece"
            data-composer="bill evans"
            data-style="ballad"
            data-date="2026-05-22"
            data-episode="114"
            data-tempo="-">
          <td><span id="peace-piece"><strong>Peace Piece</strong></span><br><small style="color:var(--text-secondary);">by Bill Evans</small></td>
          <td>5/22/2026</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-114-rerun-5222026/">#114</a></td>
          <td><span class="badge-style">ballad</span></td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="pendulums"
            data-composer=""
            data-style=""
            data-date="2022-02-04"
            data-episode="99"
            data-tempo="-">
          <td><span id="pendulums"><strong>Pendulums</strong></span></td>
          <td><a href="https://youtu.be/gK7O90mHgQ4?t=3626" target="_blank" class="song-title-link" onclick="event.stopPropagation();">2/4/2022</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-99/">#99</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="pendulums"
            data-composer=""
            data-style=""
            data-date="2022-02-18"
            data-episode="101"
            data-tempo="-">
          <td><span id="pendulums"><strong>Pendulums</strong></span></td>
          <td><a href="https://youtu.be/3mAFWZBR_QU?t=2987" target="_blank" class="song-title-link" onclick="event.stopPropagation();">2/18/2022</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-101/">#101</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="people will say we're in love"
            data-composer=""
            data-style=""
            data-date="2021-08-27"
            data-episode="76"
            data-tempo="-">
          <td><span id="people-will-say-were-in-love"><strong>People will say we're in love</strong></span></td>
          <td><a href="https://youtu.be/uMmr2KPqqpk?t=3416" target="_blank" class="song-title-link" onclick="event.stopPropagation();">8/27/2021</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-76/">#76</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td>flute solo worked out well; add horn hits in solo</td>
        </tr>
        <tr class="song-row"
            data-title="peter gunn / trouble comin’ everyday"
            data-composer="henry mancini"
            data-style="funk"
            data-date="2020-04-03"
            data-episode="3"
            data-tempo="90">
          <td><span id="peter-gunn-trouble-comin-everyday"><strong>Peter Gunn / Trouble Comin’ Everyday</strong></span><br><small style="color:var(--text-secondary);">by Henry Mancini</small></td>
          <td><a href="https://youtu.be/s0MwmoMYKj8?t=1130" target="_blank" class="song-title-link" onclick="event.stopPropagation();">4/3/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-3/">#3</a></td>
          <td><span class="badge-style">funk</span></td>
          <td style="text-align: right;">90</td>
          <td>REDO</td>
        </tr>
        <tr class="song-row"
            data-title="piano improv"
            data-composer=""
            data-style=""
            data-date="2021-08-06"
            data-episode="73"
            data-tempo="-">
          <td><span id="piano-improv"><strong>Piano Improv</strong></span></td>
          <td><a href="https://youtu.be/WOvFSmKeHH4?t=2775" target="_blank" class="song-title-link" onclick="event.stopPropagation();">8/6/2021</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-73/">#73</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td>happy accident with spacey pad + piano</td>
        </tr>
        <tr class="song-row"
            data-title="piano improv"
            data-composer=""
            data-style=""
            data-date="2026-03-06"
            data-episode="73"
            data-tempo="-">
          <td><span id="piano-improv"><strong>Piano Improv</strong></span></td>
          <td>3/6/2026</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-73-rerun-362026/">#73</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="piano improv jan 26"
            data-composer=""
            data-style=""
            data-date="2024-01-26"
            data-episode="197"
            data-tempo="-">
          <td><span id="piano-improv-jan-26"><strong>Piano Improv Jan 26</strong></span></td>
          <td>1/26/2024</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-197/">#197</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="piano improv may 12"
            data-composer=""
            data-style=""
            data-date="2023-05-12"
            data-episode="162"
            data-tempo="-">
          <td><span id="piano-improv-may-12"><strong>Piano Improv May 12</strong></span></td>
          <td><a href="https://youtu.be/GGa7s8I0Gzc?t=2164" target="_blank" class="song-title-link" onclick="event.stopPropagation();">5/12/2023</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-162/">#162</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="piano improv may 5"
            data-composer=""
            data-style=""
            data-date="2023-05-05"
            data-episode="161"
            data-tempo="-">
          <td><span id="piano-improv-may-5"><strong>Piano Improv May 5</strong></span></td>
          <td><a href="https://youtube.com/live/iSBCTTvF5RM?t=2863" target="_blank" class="song-title-link" onclick="event.stopPropagation();">5/5/2023</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-161/">#161</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="piano improvisation"
            data-composer="bill walker"
            data-style=""
            data-date="2020-07-17"
            data-episode="18"
            data-tempo="-">
          <td><span id="piano-improvisation"><strong>Piano Improvisation</strong></span><br><small style="color:var(--text-secondary);">by Bill Walker</small></td>
          <td><a href="https://youtu.be/ws1QG2nfN5g?t=2371" target="_blank" class="song-title-link" onclick="event.stopPropagation();">7/17/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-18/">#18</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td>like koln concert</td>
        </tr>
        <tr class="song-row"
            data-title="pinnacles (abscission day)"
            data-composer=""
            data-style=""
            data-date="2024-04-05"
            data-episode="9999"
            data-tempo="-">
          <td><span id="pinnacles-abscission-day"><strong>Pinnacles (Abscission Day)</strong></span></td>
          <td>4/5/2024</td>
          <td><a href="{{ '/episodes/' | relative_url }}show-452024/">Show</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="quiet now"
            data-composer="denny zeitlin"
            data-style="ballad"
            data-date="2020-05-22"
            data-episode="10"
            data-tempo="-">
          <td><span id="quiet-now"><strong>Quiet Now</strong></span><br><small style="color:var(--text-secondary);">by Denny Zeitlin</small></td>
          <td><a href="https://youtu.be/Wa5KVG0iCKM?t=3150" target="_blank" class="song-title-link" onclick="event.stopPropagation();">5/22/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-10/">#10</a></td>
          <td><span class="badge-style">ballad</span></td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="quiet now"
            data-composer="denny zeitlin"
            data-style="ballad"
            data-date="2021-02-12"
            data-episode="48"
            data-tempo="-">
          <td><span id="quiet-now"><strong>Quiet Now</strong></span><br><small style="color:var(--text-secondary);">by Denny Zeitlin</small></td>
          <td><a href="https://youtu.be/qK4QPjXbR7g?t=3266" target="_blank" class="song-title-link" onclick="event.stopPropagation();">2/12/2021</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-48/">#48</a></td>
          <td><span class="badge-style">ballad</span></td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="rainbow connection"
            data-composer="paul williams"
            data-style="pop"
            data-date="2020-05-15"
            data-episode="9"
            data-tempo="117">
          <td><span id="rainbow-connection"><strong>Rainbow Connection</strong></span><br><small style="color:var(--text-secondary);">by Paul Williams</small></td>
          <td><a href="https://youtu.be/nAk_30ixPvc?t=982" target="_blank" class="song-title-link" onclick="event.stopPropagation();">5/15/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-9/">#9</a></td>
          <td><span class="badge-style">pop</span></td>
          <td style="text-align: right;">117</td>
          <td>whiffed start; transpose down?</td>
        </tr>
        <tr class="song-row"
            data-title="rando bass"
            data-composer=""
            data-style=""
            data-date="2020-10-09"
            data-episode="30"
            data-tempo="112">
          <td><span id="rando-bass"><strong>Rando Bass</strong></span></td>
          <td><a href="https://youtu.be/BOcDB0UTT54?t=1445" target="_blank" class="song-title-link" onclick="event.stopPropagation();">10/9/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-30/">#30</a></td>
          <td>-</td>
          <td style="text-align: right;">112</td>
          <td>why didn't midi overdub work?</td>
        </tr>
        <tr class="song-row"
            data-title="re: take five"
            data-composer=""
            data-style=""
            data-date="2026-04-17"
            data-episode="295"
            data-tempo="-">
          <td><span id="re-take-five"><strong>Re: Take Five</strong></span></td>
          <td>4/17/2026</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-295/">#295</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="relembrando"
            data-composer=""
            data-style="accordion"
            data-date="2021-06-25"
            data-episode="67"
            data-tempo="-">
          <td><span id="relembrando"><strong>Relembrando</strong></span></td>
          <td><a href="https://youtu.be/BVJuigptxSA?t=837" target="_blank" class="song-title-link" onclick="event.stopPropagation();">6/25/2021</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-67/">#67</a></td>
          <td><span class="badge-style">Accordion</span></td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="rhodes ambient closer may 15"
            data-composer=""
            data-style=""
            data-date="2026-05-15"
            data-episode="298"
            data-tempo="-">
          <td><span id="rhodes-ambient-closer-may-15"><strong>rhodes ambient closer may 15</strong></span></td>
          <td>5/15/2026</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-298/">#298</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="rhodes and euro closer"
            data-composer=""
            data-style=""
            data-date="2026-06-12"
            data-episode="299"
            data-tempo="-">
          <td><span id="rhodes-and-euro-closer"><strong>Rhodes and Euro closer</strong></span></td>
          <td>6/12/2026</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-299b/">#299B</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="rhodes closer may 29"
            data-composer=""
            data-style=""
            data-date="2026-05-29"
            data-episode="299"
            data-tempo="-">
          <td><span id="rhodes-closer-may-29"><strong>rhodes closer may 29</strong></span></td>
          <td>5/29/2026</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-299/">#299</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="sacto closer"
            data-composer=""
            data-style=""
            data-date="2023-09-22"
            data-episode="180"
            data-tempo="-">
          <td><span id="sacto-closer"><strong>Sacto Closer</strong></span></td>
          <td><a href="https://youtube.com/live/PDFolCHBpes?t=3023" target="_blank" class="song-title-link" onclick="event.stopPropagation();">9/22/2023</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-180/">#180</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="sacto closer"
            data-composer=""
            data-style=""
            data-date="2024-06-14"
            data-episode="213"
            data-tempo="-">
          <td><span id="sacto-closer"><strong>Sacto Closer</strong></span></td>
          <td>6/14/2024</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-213/">#213</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="santa claus is coming to town"
            data-composer=""
            data-style=""
            data-date="2023-12-15"
            data-episode="191"
            data-tempo="-">
          <td><span id="santa-claus-is-coming-to-town"><strong>Santa Claus is Coming to Town</strong></span></td>
          <td>12/15/2023</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-191/">#191</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="santa claus is coming to town"
            data-composer=""
            data-style=""
            data-date="2024-12-13"
            data-episode="237"
            data-tempo="-">
          <td><span id="santa-claus-is-coming-to-town"><strong>Santa Claus is Coming to Town</strong></span></td>
          <td>12/13/2024</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-237/">#237</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="second time around"
            data-composer=""
            data-style=""
            data-date="2020-08-14"
            data-episode="22"
            data-tempo="-">
          <td><span id="second-time-around"><strong>Second Time Around</strong></span></td>
          <td><a href="https://youtu.be/ngdgSgM8f3U?t=2534" target="_blank" class="song-title-link" onclick="event.stopPropagation();">8/14/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-22/">#22</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="second time around"
            data-composer=""
            data-style=""
            data-date="2020-11-27"
            data-episode="37"
            data-tempo="-">
          <td><span id="second-time-around"><strong>Second Time Around</strong></span></td>
          <td><a href="https://youtu.be/8W4XQTLdajk?t=3620" target="_blank" class="song-title-link" onclick="event.stopPropagation();">11/27/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-37/">#37</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="secret love"
            data-composer="sammy fein"
            data-style="pop"
            data-date="2020-05-22"
            data-episode="10"
            data-tempo="140">
          <td><span id="secret-love"><strong>Secret Love</strong></span><br><small style="color:var(--text-secondary);">by Sammy Fein</small></td>
          <td><a href="https://youtu.be/Wa5KVG0iCKM?t=2687" target="_blank" class="song-title-link" onclick="event.stopPropagation();">5/22/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-10/">#10</a></td>
          <td><span class="badge-style">pop</span></td>
          <td style="text-align: right;">140</td>
          <td>REDO</td>
        </tr>
        <tr class="song-row"
            data-title="secret love"
            data-composer="sammy fein"
            data-style="pop"
            data-date="2020-10-23"
            data-episode="32"
            data-tempo="178">
          <td><span id="secret-love"><strong>Secret Love</strong></span><br><small style="color:var(--text-secondary);">by Sammy Fein</small></td>
          <td><a href="https://youtu.be/fk8JSTyNEfM?t=843" target="_blank" class="song-title-link" onclick="event.stopPropagation();">10/23/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-32/">#32</a></td>
          <td><span class="badge-style">pop</span></td>
          <td style="text-align: right;">178</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="secret love"
            data-composer="sammy fein"
            data-style="pop"
            data-date="2021-03-05"
            data-episode="51"
            data-tempo="175">
          <td><span id="secret-love"><strong>Secret Love</strong></span><br><small style="color:var(--text-secondary);">by Sammy Fein</small></td>
          <td><a href="https://youtu.be/Wxw626FLkDw?t=2217" target="_blank" class="song-title-link" onclick="event.stopPropagation();">3/5/2021</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-51/">#51</a></td>
          <td><span class="badge-style">pop</span></td>
          <td style="text-align: right;">175</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="sertao alagoano"
            data-composer=""
            data-style=""
            data-date="2026-02-06"
            data-episode="288"
            data-tempo="-">
          <td><span id="sertao-alagoano"><strong>Sertao Alagoano</strong></span></td>
          <td>2/6/2026</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-288/">#288</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="shake it off"
            data-composer="taylor swift"
            data-style="pop"
            data-date="2020-04-17"
            data-episode="5"
            data-tempo="159">
          <td><span id="shake-it-off"><strong>Shake It Off</strong></span><br><small style="color:var(--text-secondary);">by Taylor Swift</small></td>
          <td><a href="https://youtu.be/mlWuikMRDGo?t=1452" target="_blank" class="song-title-link" onclick="event.stopPropagation();">4/17/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-5/">#5</a></td>
          <td><span class="badge-style">pop</span></td>
          <td style="text-align: right;">159</td>
          <td>sing or dont sing</td>
        </tr>
        <tr class="song-row"
            data-title="shipping news ambient closer"
            data-composer=""
            data-style=""
            data-date="2024-09-13"
            data-episode="224"
            data-tempo="-">
          <td><span id="shipping-news-ambient-closer"><strong>shipping news ambient closer</strong></span></td>
          <td>9/13/2024</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-224/">#224</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="shipping news ambient closer 2"
            data-composer=""
            data-style=""
            data-date="2024-10-04"
            data-episode="227"
            data-tempo="-">
          <td><span id="shipping-news-ambient-closer-2"><strong>shipping news ambient closer 2</strong></span></td>
          <td>10/4/2024</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-227/">#227</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="shipping news closer"
            data-composer=""
            data-style=""
            data-date="2025-07-25"
            data-episode="265"
            data-tempo="-">
          <td><span id="shipping-news-closer"><strong>Shipping News Closer</strong></span></td>
          <td>7/25/2025</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-265/">#265</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="simply the best"
            data-composer=""
            data-style=""
            data-date="2022-10-28"
            data-episode="137"
            data-tempo="-">
          <td><span id="simply-the-best"><strong>Simply the Best</strong></span></td>
          <td><a href="https://youtu.be/Vyo_oTHKhUY?t=3070" target="_blank" class="song-title-link" onclick="event.stopPropagation();">10/28/2022</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-137/">#137</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="skating"
            data-composer=""
            data-style=""
            data-date="2023-12-22"
            data-episode="192"
            data-tempo="-">
          <td><span id="skating"><strong>Skating</strong></span></td>
          <td>12/22/2023</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-192/">#192</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="skating"
            data-composer=""
            data-style=""
            data-date="2024-11-29"
            data-episode="235"
            data-tempo="-">
          <td><span id="skating"><strong>Skating</strong></span></td>
          <td>11/29/2024</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-235/">#235</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="skating"
            data-composer=""
            data-style=""
            data-date="2025-12-19"
            data-episode="282"
            data-tempo="-">
          <td><span id="skating"><strong>Skating</strong></span></td>
          <td>12/19/2025</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-282/">#282</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="skating in central park"
            data-composer=""
            data-style="waltz"
            data-date="2021-02-05"
            data-episode="47"
            data-tempo="-">
          <td><span id="skating-in-central-park"><strong>Skating in Central Park</strong></span></td>
          <td><a href="https://youtu.be/n3dKUHIuIlU?t=3165" target="_blank" class="song-title-link" onclick="event.stopPropagation();">2/5/2021</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-47/">#47</a></td>
          <td><span class="badge-style">Waltz</span></td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="skating in central park"
            data-composer=""
            data-style="waltz"
            data-date="2021-07-09"
            data-episode="69"
            data-tempo="-">
          <td><span id="skating-in-central-park"><strong>Skating in Central Park</strong></span></td>
          <td><a href="https://youtu.be/LcOwt_X_aog?t=2033" target="_blank" class="song-title-link" onclick="event.stopPropagation();">7/9/2021</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-69/">#69</a></td>
          <td><span class="badge-style">Waltz</span></td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="skating in central park"
            data-composer=""
            data-style="waltz"
            data-date="2022-06-10"
            data-episode="117"
            data-tempo="-">
          <td><span id="skating-in-central-park"><strong>Skating in Central Park</strong></span></td>
          <td><a href="https://youtu.be/Um0wMxG_j1k?t=2670" target="_blank" class="song-title-link" onclick="event.stopPropagation();">6/10/2022</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-117/">#117</a></td>
          <td><span class="badge-style">Waltz</span></td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="skylark"
            data-composer=""
            data-style=""
            data-date="2021-01-29"
            data-episode="46"
            data-tempo="-">
          <td><span id="skylark"><strong>Skylark</strong></span></td>
          <td><a href="https://youtu.be/oVtkuUaMHU8?t=290" target="_blank" class="song-title-link" onclick="event.stopPropagation();">1/29/2021</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-46/">#46</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="snfc ambient one"
            data-composer=""
            data-style=""
            data-date="2024-06-21"
            data-episode="214"
            data-tempo="-">
          <td><span id="snfc-ambient-one"><strong>SNFC ambient one</strong></span></td>
          <td>6/21/2024</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-214/">#214</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="snow petrels closer"
            data-composer=""
            data-style=""
            data-date="2022-12-02"
            data-episode="139"
            data-tempo="-">
          <td><span id="snow-petrels-closer"><strong>Snow Petrels Closer</strong></span></td>
          <td><a href="https://youtube.com/live/ezlBzx7DvTU?t=3088" target="_blank" class="song-title-link" onclick="event.stopPropagation();">12/2/2022</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-139/">#139</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="some children him"
            data-composer=""
            data-style=""
            data-date="2023-12-22"
            data-episode="192"
            data-tempo="-">
          <td><span id="some-children-him"><strong>Some Children Him</strong></span></td>
          <td>12/22/2023</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-192/">#192</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="some children see him"
            data-composer=""
            data-style=""
            data-date="2020-12-18"
            data-episode="40"
            data-tempo="-">
          <td><span id="some-children-see-him"><strong>Some Children See Him</strong></span></td>
          <td><a href="https://youtu.be/yhWB3cwCzOI?t=3095" target="_blank" class="song-title-link" onclick="event.stopPropagation();">12/18/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-40/">#40</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="some children see him"
            data-composer=""
            data-style=""
            data-date="2024-12-20"
            data-episode="238"
            data-tempo="-">
          <td><span id="some-children-see-him"><strong>Some Children See Him</strong></span></td>
          <td>12/20/2024</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-238/">#238</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="some children see him"
            data-composer=""
            data-style=""
            data-date="2025-12-19"
            data-episode="282"
            data-tempo="-">
          <td><span id="some-children-see-him"><strong>Some Children See Him</strong></span></td>
          <td>12/19/2025</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-282/">#282</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="somewhere over the rainbow"
            data-composer=""
            data-style=""
            data-date="2025-12-05"
            data-episode="280"
            data-tempo="-">
          <td><span id="somewhere-over-the-rainbow"><strong>Somewhere Over the Rainbow</strong></span></td>
          <td>12/5/2025</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-280/">#280</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="sonic circuits practice april 10"
            data-composer=""
            data-style=""
            data-date="2026-04-10"
            data-episode="294"
            data-tempo="-">
          <td><span id="sonic-circuits-practice-april-10"><strong>Sonic Circuits practice april 10</strong></span></td>
          <td>4/10/2026</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-294/">#294</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="space lion"
            data-composer="seatbelts"
            data-style=""
            data-date="2020-07-17"
            data-episode="18"
            data-tempo="40">
          <td><span id="space-lion"><strong>Space Lion</strong></span><br><small style="color:var(--text-secondary);">by Seatbelts</small></td>
          <td><a href="https://youtu.be/ws1QG2nfN5g?t=2821" target="_blank" class="song-title-link" onclick="event.stopPropagation();">7/17/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-18/">#18</a></td>
          <td>-</td>
          <td style="text-align: right;">40</td>
          <td>redo</td>
        </tr>
        <tr class="song-row"
            data-title="spring can really hang you up the most"
            data-composer="tommy wolf"
            data-style="ballad"
            data-date="2020-05-29"
            data-episode="11"
            data-tempo="-">
          <td><span id="spring-can-really-hang-you-up-the-most"><strong>Spring can really hang you up the most</strong></span><br><small style="color:var(--text-secondary);">by Tommy Wolf</small></td>
          <td><a href="https://youtu.be/4UMdp7mQUrM?t=3427" target="_blank" class="song-title-link" onclick="event.stopPropagation();">5/29/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-11/">#11</a></td>
          <td><span class="badge-style">ballad</span></td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="spring can really hang you up the most"
            data-composer="tommy wolf"
            data-style="ballad"
            data-date="2023-04-21"
            data-episode="159"
            data-tempo="-">
          <td><span id="spring-can-really-hang-you-up-the-most"><strong>Spring can really hang you up the most</strong></span><br><small style="color:var(--text-secondary);">by Tommy Wolf</small></td>
          <td><a href="https://youtube.com/live/YOlVjS1rPFY?t=2662" target="_blank" class="song-title-link" onclick="event.stopPropagation();">4/21/2023</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-159/">#159</a></td>
          <td><span class="badge-style">ballad</span></td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="spring is here"
            data-composer=""
            data-style="ballad"
            data-date="2020-07-10"
            data-episode="17"
            data-tempo="-">
          <td><span id="spring-is-here"><strong>Spring is Here</strong></span></td>
          <td><a href="https://youtu.be/pWeOutFnTGs?t=1830" target="_blank" class="song-title-link" onclick="event.stopPropagation();">7/10/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-17/">#17</a></td>
          <td><span class="badge-style">ballad</span></td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="starshine (fretless improvisation)"
            data-composer="bill walker"
            data-style=""
            data-date="2020-09-18"
            data-episode="27"
            data-tempo="138">
          <td><span id="starshine-fretless-improvisation"><strong>Starshine (Fretless Improvisation)</strong></span><br><small style="color:var(--text-secondary);">by Bill Walker</small></td>
          <td><a href="https://youtu.be/0LJTLQOLZQM?t=198" target="_blank" class="song-title-link" onclick="event.stopPropagation();">9/18/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-27/">#27</a></td>
          <td>-</td>
          <td style="text-align: right;">138</td>
          <td>add one more element, more parameter automation</td>
        </tr>
        <tr class="song-row"
            data-title="starshine (fretless improvisation)"
            data-composer="bill walker"
            data-style=""
            data-date="2021-01-01"
            data-episode="42"
            data-tempo="138">
          <td><span id="starshine-fretless-improvisation"><strong>Starshine (Fretless Improvisation)</strong></span><br><small style="color:var(--text-secondary);">by Bill Walker</small></td>
          <td><a href="https://youtu.be/i7H03-9N1As?t=305" target="_blank" class="song-title-link" onclick="event.stopPropagation();">1/1/2021</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-42/">#42</a></td>
          <td>-</td>
          <td style="text-align: right;">138</td>
          <td>organ is good</td>
        </tr>
        <tr class="song-row"
            data-title="summer rain"
            data-composer=""
            data-style=""
            data-date="2022-09-30"
            data-episode="133"
            data-tempo="-">
          <td><span id="summer-rain"><strong>Summer Rain</strong></span></td>
          <td><a href="https://youtu.be/B3o-4sC6Z6w?t=3120" target="_blank" class="song-title-link" onclick="event.stopPropagation();">9/30/2022</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-133/">#133</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td>VCV random gates thing?</td>
        </tr>
        <tr class="song-row"
            data-title="summer rain"
            data-composer=""
            data-style=""
            data-date="2023-03-17"
            data-episode="154"
            data-tempo="-">
          <td><span id="summer-rain"><strong>Summer Rain</strong></span></td>
          <td>3/17/2023</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-154/">#154</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="surf the fog"
            data-composer=""
            data-style=""
            data-date="2025-02-07"
            data-episode="245"
            data-tempo="-">
          <td><span id="surf-the-fog"><strong>Surf the Fog</strong></span></td>
          <td>2/7/2025</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-245/">#245</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="surrey with the fringe on top"
            data-composer="hammerstein"
            data-style="swing"
            data-date="2020-04-24"
            data-episode="6"
            data-tempo="97">
          <td><span id="surrey-with-the-fringe-on-top"><strong>Surrey with the Fringe on Top</strong></span><br><small style="color:var(--text-secondary);">by Hammerstein</small></td>
          <td><a href="https://youtu.be/9EwAG0vUho8?t=2648" target="_blank" class="song-title-link" onclick="event.stopPropagation();">4/24/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-6/">#6</a></td>
          <td><span class="badge-style">swing</span></td>
          <td style="text-align: right;">97</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="surrey with the fringe on top"
            data-composer="hammerstein"
            data-style="swing"
            data-date="2020-07-17"
            data-episode="18"
            data-tempo="105">
          <td><span id="surrey-with-the-fringe-on-top"><strong>Surrey with the Fringe on Top</strong></span><br><small style="color:var(--text-secondary);">by Hammerstein</small></td>
          <td><a href="https://youtu.be/ws1QG2nfN5g?t=1985" target="_blank" class="song-title-link" onclick="event.stopPropagation();">7/17/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-18/">#18</a></td>
          <td><span class="badge-style">swing</span></td>
          <td style="text-align: right;">105</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="surrey with the fringe on top"
            data-composer="hammerstein"
            data-style="swing"
            data-date="2020-10-30"
            data-episode="33"
            data-tempo="111">
          <td><span id="surrey-with-the-fringe-on-top"><strong>Surrey with the Fringe on Top</strong></span><br><small style="color:var(--text-secondary);">by Hammerstein</small></td>
          <td><a href="https://youtu.be/kRuS4bBAE_s?t=2272" target="_blank" class="song-title-link" onclick="event.stopPropagation();">10/30/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-33/">#33</a></td>
          <td><span class="badge-style">swing</span></td>
          <td style="text-align: right;">111</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="tenderly"
            data-composer=""
            data-style=""
            data-date="2020-08-21"
            data-episode="23"
            data-tempo="-">
          <td><span id="tenderly"><strong>Tenderly</strong></span></td>
          <td><a href="https://youtu.be/m7JFcEdod0E?t=3045" target="_blank" class="song-title-link" onclick="event.stopPropagation();">8/21/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-23/">#23</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="tenderly"
            data-composer=""
            data-style=""
            data-date="2025-11-14"
            data-episode="23"
            data-tempo="-">
          <td><span id="tenderly"><strong>Tenderly</strong></span></td>
          <td>11/14/2025</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-23-rerun-11142025/">#23</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="tenderly"
            data-composer=""
            data-style=""
            data-date="2026-05-08"
            data-episode="23"
            data-tempo="-">
          <td><span id="tenderly"><strong>Tenderly</strong></span></td>
          <td>5/8/2026</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-23-rerun-582026/">#23</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="the bay"
            data-composer=""
            data-style=""
            data-date="2023-10-20"
            data-episode="183"
            data-tempo="-">
          <td><span id="the-bay"><strong>The Bay</strong></span></td>
          <td>10/20/2023</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-183/">#183</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="the christmas song"
            data-composer=""
            data-style=""
            data-date="2020-12-11"
            data-episode="39"
            data-tempo="-">
          <td><span id="the-christmas-song"><strong>The Christmas Song</strong></span></td>
          <td><a href="https://youtu.be/hfljJ87kgbs?t=1625" target="_blank" class="song-title-link" onclick="event.stopPropagation();">12/11/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-39/">#39</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="the christmas song"
            data-composer=""
            data-style=""
            data-date="2023-12-15"
            data-episode="191"
            data-tempo="-">
          <td><span id="the-christmas-song"><strong>The Christmas Song</strong></span></td>
          <td>12/15/2023</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-191/">#191</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="the christmas song (chestnuts...)"
            data-composer=""
            data-style=""
            data-date="2020-12-11"
            data-episode="39"
            data-tempo="-">
          <td><span id="the-christmas-song-chestnuts"><strong>The Christmas Song (Chestnuts...)</strong></span></td>
          <td><a href="https://youtu.be/hfljJ87kgbs?t=1634" target="_blank" class="song-title-link" onclick="event.stopPropagation();">12/11/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-39/">#39</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="the city"
            data-composer=""
            data-style=""
            data-date="2023-10-20"
            data-episode="183"
            data-tempo="-">
          <td><span id="the-city"><strong>The City</strong></span></td>
          <td>10/20/2023</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-183/">#183</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="the holly and the ivy"
            data-composer=""
            data-style=""
            data-date="2020-12-11"
            data-episode="39"
            data-tempo="112">
          <td><span id="the-holly-and-the-ivy"><strong>The Holly and the Ivy</strong></span></td>
          <td><a href="https://youtu.be/hfljJ87kgbs?t=3283" target="_blank" class="song-title-link" onclick="event.stopPropagation();">12/11/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-39/">#39</a></td>
          <td>-</td>
          <td style="text-align: right;">112</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="the holly and the ivy"
            data-composer=""
            data-style=""
            data-date="2020-12-25"
            data-episode="41"
            data-tempo="119">
          <td><span id="the-holly-and-the-ivy"><strong>The Holly and the Ivy</strong></span></td>
          <td><a href="https://youtu.be/G-HJYWxotdo?t=1592" target="_blank" class="song-title-link" onclick="event.stopPropagation();">12/25/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-41/">#41</a></td>
          <td>-</td>
          <td style="text-align: right;">119</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="the holly and the ivy"
            data-composer=""
            data-style=""
            data-date="2024-12-06"
            data-episode="236"
            data-tempo="-">
          <td><span id="the-holly-and-the-ivy"><strong>The Holly and the Ivy</strong></span></td>
          <td>12/6/2024</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-236/">#236</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="the holly and the ivy"
            data-composer=""
            data-style=""
            data-date="2025-12-12"
            data-episode="281"
            data-tempo="-">
          <td><span id="the-holly-and-the-ivy"><strong>The Holly and the Ivy</strong></span></td>
          <td>12/12/2025</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-281/">#281</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="the merry-go-round of life"
            data-composer="joe hisaishi"
            data-style="ballad"
            data-date="2020-05-29"
            data-episode="11"
            data-tempo="-">
          <td><span id="the-merry-go-round-of-life"><strong>The Merry-go-round of Life</strong></span><br><small style="color:var(--text-secondary);">by Joe Hisaishi</small></td>
          <td><a href="https://youtu.be/4UMdp7mQUrM?t=2380" target="_blank" class="song-title-link" onclick="event.stopPropagation();">5/29/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-11/">#11</a></td>
          <td><span class="badge-style">ballad</span></td>
          <td style="text-align: right;">-</td>
          <td>REDO</td>
        </tr>
        <tr class="song-row"
            data-title="the ocean"
            data-composer=""
            data-style=""
            data-date="2023-10-20"
            data-episode="183"
            data-tempo="-">
          <td><span id="the-ocean"><strong>The Ocean</strong></span></td>
          <td>10/20/2023</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-183/">#183</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="there is no greater love"
            data-composer="isham jones"
            data-style="swing"
            data-date="2020-07-03"
            data-episode="16"
            data-tempo="160">
          <td><span id="there-is-no-greater-love"><strong>There is no greater love</strong></span><br><small style="color:var(--text-secondary);">by Isham Jones</small></td>
          <td><a href="https://youtu.be/pX-E6ZVGrpA?t=224" target="_blank" class="song-title-link" onclick="event.stopPropagation();">7/3/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-16/">#16</a></td>
          <td><span class="badge-style">swing</span></td>
          <td style="text-align: right;">160</td>
          <td>drums too loud</td>
        </tr>
        <tr class="song-row"
            data-title="turn out the stars"
            data-composer=""
            data-style=""
            data-date="2020-09-04"
            data-episode="25"
            data-tempo="-">
          <td><span id="turn-out-the-stars"><strong>Turn out the Stars</strong></span></td>
          <td><a href="https://youtu.be/tCGZLZnLvh4?t=3825" target="_blank" class="song-title-link" onclick="event.stopPropagation();">9/4/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-25/">#25</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="tuvan robot closer"
            data-composer=""
            data-style=""
            data-date="2025-07-04"
            data-episode="263"
            data-tempo="-">
          <td><span id="tuvan-robot-closer"><strong>Tuvan robot closer</strong></span></td>
          <td>7/4/2025</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-263/">#263</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="variations on dinosaur night"
            data-composer=""
            data-style=""
            data-date="2022-01-21"
            data-episode="97"
            data-tempo="-">
          <td><span id="variations-on-dinosaur-night"><strong>Variations on Dinosaur Night</strong></span></td>
          <td><a href="https://youtu.be/vFJFp1oRZE8?t=3497" target="_blank" class="song-title-link" onclick="event.stopPropagation();">1/21/2022</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-97/">#97</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td>surprisingly good</td>
        </tr>
        <tr class="song-row"
            data-title="variations on inchworm"
            data-composer=""
            data-style=""
            data-date="2023-10-06"
            data-episode="181"
            data-tempo="-">
          <td><span id="variations-on-inchworm"><strong>variations on inchworm</strong></span></td>
          <td><a href="https://youtube.com/live/72lHM0ID4_8?t=3023" target="_blank" class="song-title-link" onclick="event.stopPropagation();">10/6/2023</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-181/">#181</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="vcv ambient"
            data-composer=""
            data-style=""
            data-date="2022-01-14"
            data-episode="96"
            data-tempo="-">
          <td><span id="vcv-ambient"><strong>VCV Ambient</strong></span></td>
          <td><a href="https://youtu.be/VAUYw5v0RiQ?t=3405" target="_blank" class="song-title-link" onclick="event.stopPropagation();">1/14/2022</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-96/">#96</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="vcv ambient"
            data-composer=""
            data-style=""
            data-date="2022-07-01"
            data-episode="120"
            data-tempo="-">
          <td><span id="vcv-ambient"><strong>VCV Ambient</strong></span></td>
          <td><a href="https://youtu.be/eIUxG9vQkiw?t=3448" target="_blank" class="song-title-link" onclick="event.stopPropagation();">7/1/2022</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-120/">#120</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="vcv arpeggio wash"
            data-composer=""
            data-style=""
            data-date="2024-06-14"
            data-episode="213"
            data-tempo="-">
          <td><span id="vcv-arpeggio-wash"><strong>VCV arpeggio wash</strong></span></td>
          <td>6/14/2024</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-213/">#213</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="vcv closer april 28"
            data-composer=""
            data-style=""
            data-date="2023-04-28"
            data-episode="160"
            data-tempo="-">
          <td><span id="vcv-closer-april-28"><strong>VCV Closer April 28</strong></span></td>
          <td><a href="https://youtube.com/live/McHbN0vAbMA?t=2892" target="_blank" class="song-title-link" onclick="event.stopPropagation();">4/28/2023</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-160/">#160</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="vcv closer nov 3"
            data-composer=""
            data-style=""
            data-date="2023-11-03"
            data-episode="185"
            data-tempo="-">
          <td><span id="vcv-closer-nov-3"><strong>VCV Closer Nov 3</strong></span></td>
          <td><a href="https://youtube.com/live/vpg-dYDIFj0?t=3023" target="_blank" class="song-title-link" onclick="event.stopPropagation();">11/3/2023</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-185/">#185</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="vcv closer nov 3"
            data-composer=""
            data-style=""
            data-date="2025-11-07"
            data-episode="185"
            data-tempo="-">
          <td><span id="vcv-closer-nov-3"><strong>VCV Closer Nov 3</strong></span></td>
          <td>11/7/2025</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-185-rerun-1172025/">#185</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="vcv closer sept 27"
            data-composer=""
            data-style=""
            data-date="2024-09-27"
            data-episode="226"
            data-tempo="-">
          <td><span id="vcv-closer-sept-27"><strong>VCV closer sept 27</strong></span></td>
          <td>9/27/2024</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-226/">#226</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="vcv neutrinode mellowness nov 24"
            data-composer=""
            data-style=""
            data-date="2023-11-24"
            data-episode="188"
            data-tempo="-">
          <td><span id="vcv-neutrinode-mellowness-nov-24"><strong>VCV neutrinode mellowness Nov 24</strong></span></td>
          <td>11/24/2023</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-188/">#188</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td>VERY GOOD! fan fave</td>
        </tr>
        <tr class="song-row"
            data-title="vcv wobbly chords closer"
            data-composer=""
            data-style=""
            data-date="2024-03-08"
            data-episode="201"
            data-tempo="-">
          <td><span id="vcv-wobbly-chords-closer"><strong>VCV wobbly chords closer</strong></span></td>
          <td><a href="https://youtu.be/LbsjAeA49TU?t=3023" target="_blank" class="song-title-link" onclick="event.stopPropagation();">3/8/2024</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-201/">#201</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="vcv wobbly chords closer"
            data-composer=""
            data-style=""
            data-date="2025-01-17"
            data-episode="201"
            data-tempo="-">
          <td><span id="vcv-wobbly-chords-closer"><strong>VCV wobbly chords closer</strong></span></td>
          <td>1/17/2025</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-201-rerun-1172025/">#201</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="vcv wobbly chords closer"
            data-composer=""
            data-style=""
            data-date="2025-03-07"
            data-episode="9999"
            data-tempo="-">
          <td><span id="vcv-wobbly-chords-closer"><strong>VCV wobbly chords closer</strong></span></td>
          <td>3/7/2025</td>
          <td><a href="{{ '/episodes/' | relative_url }}show-372025/">Show</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="walk to the park"
            data-composer=""
            data-style="techno"
            data-date="2020-10-30"
            data-episode="33"
            data-tempo="101">
          <td><span id="walk-to-the-park"><strong>Walk to the Park</strong></span></td>
          <td><a href="https://youtu.be/kRuS4bBAE_s?t=2690" target="_blank" class="song-title-link" onclick="event.stopPropagation();">10/30/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-33/">#33</a></td>
          <td><span class="badge-style">techno</span></td>
          <td style="text-align: right;">101</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="waltz for debby"
            data-composer=""
            data-style=""
            data-date="2021-03-05"
            data-episode="51"
            data-tempo="170">
          <td><span id="waltz-for-debby"><strong>Waltz for Debby</strong></span></td>
          <td><a href="https://youtu.be/Wxw626FLkDw?t=2660" target="_blank" class="song-title-link" onclick="event.stopPropagation();">3/5/2021</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-51/">#51</a></td>
          <td>-</td>
          <td style="text-align: right;">170</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="we shall overcome"
            data-composer=""
            data-style=""
            data-date="2020-08-28"
            data-episode="24"
            data-tempo="-">
          <td><span id="we-shall-overcome"><strong>We Shall Overcome</strong></span></td>
          <td><a href="https://youtu.be/oLyXU2T1ZuA?t=300" target="_blank" class="song-title-link" onclick="event.stopPropagation();">8/28/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-24/">#24</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="we shall overcome"
            data-composer=""
            data-style=""
            data-date="2021-01-08"
            data-episode="43"
            data-tempo="-">
          <td><span id="we-shall-overcome"><strong>We Shall Overcome</strong></span></td>
          <td><a href="https://youtu.be/PcZFKARMaQo?t=237" target="_blank" class="song-title-link" onclick="event.stopPropagation();">1/8/2021</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-43/">#43</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="we'll be together again closer"
            data-composer=""
            data-style=""
            data-date="2025-02-21"
            data-episode="247"
            data-tempo="-">
          <td><span id="well-be-together-again-closer"><strong>We'll be together again closer</strong></span></td>
          <td>2/21/2025</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-247/">#247</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="were you there"
            data-composer="spiritual"
            data-style=""
            data-date="2020-04-10"
            data-episode="4"
            data-tempo="-">
          <td><span id="were-you-there"><strong>Were You There</strong></span><br><small style="color:var(--text-secondary);">by Spiritual</small></td>
          <td><a href="https://youtu.be/a4UEJSQN9Zw?t=1232" target="_blank" class="song-title-link" onclick="event.stopPropagation();">4/10/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-4/">#4</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="were you there"
            data-composer="spiritual"
            data-style=""
            data-date="2023-04-07"
            data-episode="157"
            data-tempo="-">
          <td><span id="were-you-there"><strong>Were You There</strong></span><br><small style="color:var(--text-secondary);">by Spiritual</small></td>
          <td><a href="https://youtu.be/kVbZruEPROM?t=3023" target="_blank" class="song-title-link" onclick="event.stopPropagation();">4/7/2023</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-157/">#157</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="were you there"
            data-composer="spiritual"
            data-style=""
            data-date="2025-04-18"
            data-episode="252"
            data-tempo="-">
          <td><span id="were-you-there"><strong>Were You There</strong></span><br><small style="color:var(--text-secondary);">by Spiritual</small></td>
          <td>4/18/2025</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-252/">#252</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="were you there improv"
            data-composer=""
            data-style=""
            data-date="2024-05-17"
            data-episode="209"
            data-tempo="-">
          <td><span id="were-you-there-improv"><strong>Were you There Improv</strong></span></td>
          <td>5/17/2024</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-209/">#209</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="we’ll be together again"
            data-composer="carl fischer"
            data-style="ballad"
            data-date="2020-05-08"
            data-episode="8"
            data-tempo="-">
          <td><span id="well-be-together-again"><strong>We’ll Be Together Again</strong></span><br><small style="color:var(--text-secondary);">by Carl Fischer</small></td>
          <td><a href="https://youtu.be/ODap9wBMyeU?t=3222" target="_blank" class="song-title-link" onclick="event.stopPropagation();">5/8/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-8/">#8</a></td>
          <td><span class="badge-style">ballad</span></td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="we’ll be together again"
            data-composer="carl fischer"
            data-style="ballad"
            data-date="2020-06-26"
            data-episode="15"
            data-tempo="-">
          <td><span id="well-be-together-again"><strong>We’ll Be Together Again</strong></span><br><small style="color:var(--text-secondary);">by Carl Fischer</small></td>
          <td><a href="https://youtu.be/LCcBhJKB8YA?t=2125" target="_blank" class="song-title-link" onclick="event.stopPropagation();">6/26/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-15/">#15</a></td>
          <td><span class="badge-style">ballad</span></td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="we’ll be together again"
            data-composer="carl fischer"
            data-style="ballad"
            data-date="2021-02-26"
            data-episode="50"
            data-tempo="-">
          <td><span id="well-be-together-again"><strong>We’ll Be Together Again</strong></span><br><small style="color:var(--text-secondary);">by Carl Fischer</small></td>
          <td><a href="https://youtu.be/TKoh0MrsGgs?t=245" target="_blank" class="song-title-link" onclick="event.stopPropagation();">2/26/2021</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-50/">#50</a></td>
          <td><span class="badge-style">ballad</span></td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="we’ll be together again"
            data-composer="carl fischer"
            data-style="ballad"
            data-date="2022-09-02"
            data-episode="129"
            data-tempo="-">
          <td><span id="well-be-together-again"><strong>We’ll Be Together Again</strong></span><br><small style="color:var(--text-secondary);">by Carl Fischer</small></td>
          <td><a href="https://youtu.be/bIdPZtsIf-M?t=3275" target="_blank" class="song-title-link" onclick="event.stopPropagation();">9/2/2022</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-129/">#129</a></td>
          <td><span class="badge-style">ballad</span></td>
          <td style="text-align: right;">-</td>
          <td>nice</td>
        </tr>
        <tr class="song-row"
            data-title="we’ll be together again"
            data-composer="carl fischer"
            data-style="ballad"
            data-date="2023-09-08"
            data-episode="129"
            data-tempo="-">
          <td><span id="well-be-together-again"><strong>We’ll Be Together Again</strong></span><br><small style="color:var(--text-secondary);">by Carl Fischer</small></td>
          <td><a href="https://youtu.be/bIdPZtsIf-M?t=3023" target="_blank" class="song-title-link" onclick="event.stopPropagation();">9/8/2023</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-129-rerun-982023/">#129</a></td>
          <td><span class="badge-style">ballad</span></td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="we’ll be together again"
            data-composer="carl fischer"
            data-style="ballad"
            data-date="2024-10-11"
            data-episode="228"
            data-tempo="-">
          <td><span id="well-be-together-again"><strong>We’ll Be Together Again</strong></span><br><small style="color:var(--text-secondary);">by Carl Fischer</small></td>
          <td>10/11/2024</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-228/">#228</a></td>
          <td><span class="badge-style">ballad</span></td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="what are you doing new year's eve?"
            data-composer=""
            data-style=""
            data-date="2021-12-31"
            data-episode="94"
            data-tempo="-">
          <td><span id="what-are-you-doing-new-years-eve"><strong>What are you doing New Year's Eve?</strong></span></td>
          <td><a href="https://youtu.be/Rcivz__GFo4?t=3017" target="_blank" class="song-title-link" onclick="event.stopPropagation();">12/31/2021</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-94/">#94</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="what are you doing new year's eve?"
            data-composer=""
            data-style=""
            data-date="2022-12-30"
            data-episode="143"
            data-tempo="-">
          <td><span id="what-are-you-doing-new-years-eve"><strong>What are you doing New Year's Eve?</strong></span></td>
          <td><a href="https://youtube.com/live/ayeY3t9WvGA?t=3024" target="_blank" class="song-title-link" onclick="event.stopPropagation();">12/30/2022</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-143/">#143</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="what are you doing new year's eve?"
            data-composer=""
            data-style=""
            data-date="2023-12-29"
            data-episode="193"
            data-tempo="-">
          <td><span id="what-are-you-doing-new-years-eve"><strong>What are you doing New Year's Eve?</strong></span></td>
          <td>12/29/2023</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-193/">#193</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="what are you doing new year's eve?"
            data-composer=""
            data-style=""
            data-date="2024-12-27"
            data-episode="239"
            data-tempo="-">
          <td><span id="what-are-you-doing-new-years-eve"><strong>What are you doing New Year's Eve?</strong></span></td>
          <td>12/27/2024</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-239/">#239</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="what child is this?"
            data-composer=""
            data-style=""
            data-date="2024-12-06"
            data-episode="236"
            data-tempo="-">
          <td><span id="what-child-is-this"><strong>What Child is This?</strong></span></td>
          <td>12/6/2024</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-236/">#236</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="what time is it?"
            data-composer="ken nordine"
            data-style="spoken"
            data-date="2020-06-05"
            data-episode="12"
            data-tempo="-">
          <td><span id="what-time-is-it"><strong>What Time Is It?</strong></span><br><small style="color:var(--text-secondary);">by Ken Nordine</small></td>
          <td><a href="https://youtu.be/8aHUkT2wFNc?t=1810" target="_blank" class="song-title-link" onclick="event.stopPropagation();">6/5/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-12/">#12</a></td>
          <td><span class="badge-style">spoken</span></td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="when in rome"
            data-composer="cy coleman"
            data-style=""
            data-date="2020-07-24"
            data-episode="19"
            data-tempo="-">
          <td><span id="when-in-rome"><strong>When in Rome</strong></span><br><small style="color:var(--text-secondary);">by Cy Coleman</small></td>
          <td><a href="https://youtu.be/nNbXig2F9Lc?t=3261" target="_blank" class="song-title-link" onclick="event.stopPropagation();">7/24/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-19/">#19</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="where or when"
            data-composer="rogers and hart"
            data-style=""
            data-date="2020-05-08"
            data-episode="8"
            data-tempo="110">
          <td><span id="where-or-when"><strong>Where or When</strong></span><br><small style="color:var(--text-secondary);">by Rogers and Hart</small></td>
          <td><a href="https://youtu.be/ODap9wBMyeU?t=1867" target="_blank" class="song-title-link" onclick="event.stopPropagation();">5/8/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-8/">#8</a></td>
          <td>-</td>
          <td style="text-align: right;">110</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="where or when"
            data-composer="rogers and hart"
            data-style=""
            data-date="2020-08-21"
            data-episode="23"
            data-tempo="106">
          <td><span id="where-or-when"><strong>Where or When</strong></span><br><small style="color:var(--text-secondary);">by Rogers and Hart</small></td>
          <td><a href="https://youtu.be/m7JFcEdod0E?t=2160" target="_blank" class="song-title-link" onclick="event.stopPropagation();">8/21/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-23/">#23</a></td>
          <td>-</td>
          <td style="text-align: right;">106</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="where or when"
            data-composer="rogers and hart"
            data-style=""
            data-date="2020-11-20"
            data-episode="36"
            data-tempo="-">
          <td><span id="where-or-when"><strong>Where or When</strong></span><br><small style="color:var(--text-secondary);">by Rogers and Hart</small></td>
          <td><a href="https://youtu.be/FgUbgdPd9pw?t=3060" target="_blank" class="song-title-link" onclick="event.stopPropagation();">11/20/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-36/">#36</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="where or when"
            data-composer="rogers and hart"
            data-style=""
            data-date="2025-11-14"
            data-episode="23"
            data-tempo="-">
          <td><span id="where-or-when"><strong>Where or When</strong></span><br><small style="color:var(--text-secondary);">by Rogers and Hart</small></td>
          <td>11/14/2025</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-23-rerun-11142025/">#23</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="where or when"
            data-composer="rogers and hart"
            data-style=""
            data-date="2026-05-08"
            data-episode="23"
            data-tempo="-">
          <td><span id="where-or-when"><strong>Where or When</strong></span><br><small style="color:var(--text-secondary);">by Rogers and Hart</small></td>
          <td>5/8/2026</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-23-rerun-582026/">#23</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="white christmas"
            data-composer=""
            data-style=""
            data-date="2020-12-04"
            data-episode="38"
            data-tempo="65">
          <td><span id="white-christmas"><strong>White Christmas</strong></span></td>
          <td><a href="https://youtu.be/8ALGHR-ErS0?t=590" target="_blank" class="song-title-link" onclick="event.stopPropagation();">12/4/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-38/">#38</a></td>
          <td>-</td>
          <td style="text-align: right;">65</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="white christmas"
            data-composer=""
            data-style=""
            data-date="2020-12-25"
            data-episode="41"
            data-tempo="65">
          <td><span id="white-christmas"><strong>White Christmas</strong></span></td>
          <td><a href="https://youtu.be/G-HJYWxotdo?t=597" target="_blank" class="song-title-link" onclick="event.stopPropagation();">12/25/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-41/">#41</a></td>
          <td>-</td>
          <td style="text-align: right;">65</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="white christmas"
            data-composer=""
            data-style=""
            data-date="2021-12-10"
            data-episode="91"
            data-tempo="-">
          <td><span id="white-christmas"><strong>White Christmas</strong></span></td>
          <td><a href="https://youtu.be/vr3lHzT6u9s?t=34" target="_blank" class="song-title-link" onclick="event.stopPropagation();">12/10/2021</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-91/">#91</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td>smoove</td>
        </tr>
        <tr class="song-row"
            data-title="white christmas"
            data-composer=""
            data-style=""
            data-date="2021-12-24"
            data-episode="93"
            data-tempo="-">
          <td><span id="white-christmas"><strong>White Christmas</strong></span></td>
          <td><a href="https://youtu.be/oIJ5iubhwRg?t=1880" target="_blank" class="song-title-link" onclick="event.stopPropagation();">12/24/2021</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-93/">#93</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="white christmas"
            data-composer=""
            data-style=""
            data-date="2022-12-23"
            data-episode="142"
            data-tempo="-">
          <td><span id="white-christmas"><strong>White Christmas</strong></span></td>
          <td><a href="https://youtube.com/live/iH6lwOJ7Gb4?t=3428" target="_blank" class="song-title-link" onclick="event.stopPropagation();">12/23/2022</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-142/">#142</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="white christmas"
            data-composer=""
            data-style=""
            data-date="2023-12-08"
            data-episode="190"
            data-tempo="-">
          <td><span id="white-christmas"><strong>White Christmas</strong></span></td>
          <td>12/8/2023</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-190/">#190</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="white christmas"
            data-composer=""
            data-style=""
            data-date="2024-12-06"
            data-episode="236"
            data-tempo="-">
          <td><span id="white-christmas"><strong>White Christmas</strong></span></td>
          <td>12/6/2024</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-236/">#236</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="wood and grassland"
            data-composer=""
            data-style=""
            data-date="2023-10-20"
            data-episode="183"
            data-tempo="-">
          <td><span id="wood-and-grassland"><strong>Wood and Grassland</strong></span></td>
          <td>10/20/2023</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-183/">#183</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="wwv"
            data-composer=""
            data-style=""
            data-date="2024-10-04"
            data-episode="227"
            data-tempo="-">
          <td><span id="wwv"><strong>WWV</strong></span></td>
          <td>10/4/2024</td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-227/">#227</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="young and foolish"
            data-composer=""
            data-style=""
            data-date="2020-09-18"
            data-episode="27"
            data-tempo="-">
          <td><span id="young-and-foolish"><strong>Young and Foolish</strong></span></td>
          <td><a href="https://youtu.be/0LJTLQOLZQM?t=3196" target="_blank" class="song-title-link" onclick="event.stopPropagation();">9/18/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-27/">#27</a></td>
          <td>-</td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
        <tr class="song-row"
            data-title="‘round midnight"
            data-composer=""
            data-style="ballad"
            data-date="2020-07-10"
            data-episode="17"
            data-tempo="-">
          <td><span id="round-midnight"><strong>‘Round Midnight</strong></span></td>
          <td><a href="https://youtu.be/pWeOutFnTGs?t=2548" target="_blank" class="song-title-link" onclick="event.stopPropagation();">7/10/2020</a></td>
          <td><a href="{{ '/episodes/' | relative_url }}episode-17/">#17</a></td>
          <td><span class="badge-style">ballad</span></td>
          <td style="text-align: right;">-</td>
          <td></td>
        </tr>
    </tbody>
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
