---
layout: default
title: "Friday Jazz Happy Hour Archive"
---

<style>
  .dashboard-hero {
    text-align: center;
    margin: 3rem auto 4rem auto;
    padding: 3rem 1.5rem;
    max-width: 800px;
  }
  
  .dashboard-title {
    font-family: 'Outfit', sans-serif;
    font-weight: 800;
    font-size: 4rem;
    margin: 0 0 1rem 0;
    background: var(--accent-gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    letter-spacing: -0.03em;
    line-height: 1.1;
  }
  
  .dashboard-subtitle {
    color: var(--text-secondary);
    font-size: 1.25rem;
    line-height: 1.6;
    font-weight: 400;
  }

  .stats-container {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1.5rem;
    margin-bottom: 4rem;
  }

  .stat-card {
    background: var(--card-bg);
    border: 1px solid var(--border-color);
    border-radius: 20px;
    padding: 2rem;
    text-align: center;
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.15);
  }

  .stat-number {
    font-family: 'Outfit', sans-serif;
    font-size: 3rem;
    font-weight: 800;
    color: var(--text-primary);
    background: linear-gradient(135deg, #f3f4f6, #9ca3af);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0.5rem;
    line-height: 1;
  }

  .stat-label {
    color: var(--text-secondary);
    font-size: 0.95rem;
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: 0.05em;
  }

  .section-title {
    font-family: 'Outfit', sans-serif;
    font-size: 2rem;
    font-weight: 700;
    margin-bottom: 2rem;
    text-align: center;
    letter-spacing: -0.02em;
  }

  .navigation-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1.5rem;
    margin-bottom: 5rem;
  }

  .nav-card {
    background: var(--card-bg);
    border: 1px solid var(--border-color);
    border-radius: 20px;
    padding: 2.2rem;
    text-decoration: none;
    color: var(--text-primary);
    transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.25s ease, box-shadow 0.25s ease;
    display: flex;
    flex-direction: column;
    height: 100%;
    box-sizing: border-box;
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.15);
  }

  .nav-card:hover {
    transform: translateY(-6px);
    border-color: var(--accent-color);
    box-shadow: 0 12px 40px rgba(59, 130, 246, 0.18);
  }

  .nav-card-icon {
    font-size: 2.2rem;
    margin-bottom: 1.2rem;
    display: inline-block;
  }

  .nav-card-title {
    font-family: 'Outfit', sans-serif;
    font-size: 1.45rem;
    font-weight: 700;
    margin: 0 0 0.8rem 0;
    letter-spacing: -0.01em;
  }

  .nav-card-description {
    color: var(--text-secondary);
    font-size: 0.95rem;
    line-height: 1.5;
    margin: 0 0 1.5rem 0;
    flex-grow: 1;
  }

  .nav-card-action {
    color: var(--accent-hover);
    font-size: 0.9rem;
    font-weight: 600;
    display: flex;
    align-items: center;
    gap: 0.25rem;
    transition: gap 0.2s ease;
  }

  .nav-card:hover .nav-card-action {
    gap: 0.5rem;
  }

  @media (max-width: 800px) {
    .stats-container, .navigation-grid {
      grid-template-columns: 1fr;
      gap: 1.2rem;
    }
    
    .dashboard-title {
      font-size: 2.8rem;
    }
  }
</style>

<div class="dashboard-hero">
  <h1 class="dashboard-title">Live Stream Archive</h1>
  <p class="dashboard-subtitle">A chronological record, song index, and setlist explorer for Bill Walker's Friday Jazz Happy Hour live stream improvisations.</p>
</div>

<div class="stats-container">
  <div class="stat-card">
    <div class="stat-number">{{ site.episodes | size }}</div>
    <div class="stat-label">Episodes</div>
  </div>
  <div class="stat-card">
    <div class="stat-number">{{ site.songs | size }}</div>
    <div class="stat-label">Regular Songs</div>
  </div>
  <div class="stat-card">
    <div class="stat-number">{{ site.data.one_offs | size }}</div>
    <div class="stat-label">One-Off Songs</div>
  </div>
</div>

<h2 class="section-title">Explore the Archive</h2>

<div class="navigation-grid">
  <a href="{{ '/regular-songs.html' | relative_url }}" class="nav-card">
    <span class="nav-card-icon">🎷</span>
    <h3 class="nav-card-title">Regular Songs</h3>
    <p class="nav-card-description">Browse the core catalog of jazz standards, ballads, and originals that form the regular rotation of the live streams.</p>
    <span class="nav-card-action">View Songs &rarr;</span>
  </a>

  <a href="{{ '/one-off-songs.html' | relative_url }}" class="nav-card">
    <span class="nav-card-icon">🎹</span>
    <h3 class="nav-card-title">One-Off Songs</h3>
    <p class="nav-card-description">Explore unique performances, modular synth improvisations, and special requests played exactly once.</p>
    <span class="nav-card-action">View One-Offs &rarr;</span>
  </a>

  <a href="{{ '/episodes.html' | relative_url }}" class="nav-card">
    <span class="nav-card-icon">📅</span>
    <h3 class="nav-card-title">Episodes</h3>
    <p class="nav-card-description">Scan the chronological history of all streams to review complete setlists, styles, tempos, and video links.</p>
    <span class="nav-card-action">View Episodes &rarr;</span>
  </a>
</div>
