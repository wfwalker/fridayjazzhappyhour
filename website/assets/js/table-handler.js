document.addEventListener('DOMContentLoaded', function() {
  const searchInput = document.getElementById('songSearch');
  const styleFilter = document.getElementById('styleFilter');
  const tableBody = document.getElementById('songsTableBody');
  if (!tableBody) return; // Exit if table is not present on this page
  
  const rows = Array.from(tableBody.querySelectorAll('.song-row'));
  const headers = document.querySelectorAll('.songs-table th.sortable');
  
  // Find which column is sorted by default (usually title)
  let activeHeader = document.querySelector('.songs-table th.sortable.active-sort');
  let currentSort = {
    key: activeHeader ? activeHeader.getAttribute('data-sort') : 'title',
    direction: 'asc'
  };
  
  // Initialize default active sort header if not already set by template
  if (!activeHeader) {
    headers.forEach(h => {
      if (h.getAttribute('data-sort') === 'title') {
        h.classList.add('active-sort');
        const icon = h.querySelector('.sort-icon');
        if (icon) icon.textContent = ' ∧';
      }
    });
  }
  
  function filterTable() {
    const searchQuery = searchInput ? searchInput.value.toLowerCase().trim() : '';
    const selectedStyle = styleFilter ? styleFilter.value : '';
    
    rows.forEach(row => {
      const title = (row.getAttribute('data-title') || '').toLowerCase();
      const composer = (row.getAttribute('data-composer') || '').toLowerCase();
      const style = (row.getAttribute('data-style') || '').toLowerCase();
      const textContent = row.textContent.toLowerCase();
      
      const matchesSearch = !searchQuery || 
                            title.includes(searchQuery) || 
                            composer.includes(searchQuery) || 
                            style.includes(searchQuery) ||
                            textContent.includes(searchQuery);
                            
      const matchesStyle = !selectedStyle || style === selectedStyle.toLowerCase();
      
      row.style.display = (matchesSearch && matchesStyle) ? '' : 'none';
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
    
    // Update header icons and active styling
    headers.forEach(h => {
      const icon = h.querySelector('.sort-icon');
      const hKey = h.getAttribute('data-sort');
      if (hKey === key) {
        if (icon) icon.textContent = direction === 'asc' ? ' ∧' : ' ∨';
        h.classList.add('active-sort');
      } else {
        if (icon) icon.textContent = '';
        h.classList.remove('active-sort');
      }
    });
    
    // Perform sort
    const sortedRows = rows.sort((a, b) => {
      let valA = a.getAttribute(`data-${key}`) || '';
      let valB = b.getAttribute(`data-${key}`) || '';
      
      // Auto-detect numeric columns (plays, tempo, episode number)
      const numA = Number(valA);
      const numB = Number(valB);
      
      if (valA !== '' && valB !== '' && !isNaN(numA) && !isNaN(numB)) {
        return direction === 'asc' ? numA - numB : numB - numA;
      } else {
        // Fallback to alphabetical sorting
        return direction === 'asc' ? valA.localeCompare(valB) : valB.localeCompare(valA);
      }
    });
    
    // Re-append rows in sorted order
    sortedRows.forEach(row => tableBody.appendChild(row));
  }
  
  // Wire up event listeners
  if (searchInput) {
    searchInput.addEventListener('input', filterTable);
  }
  if (styleFilter) {
    styleFilter.addEventListener('change', filterTable);
  }
  
  headers.forEach(header => {
    const key = header.getAttribute('data-sort');
    const defaultDir = header.getAttribute('data-default') || 'asc';
    header.addEventListener('click', () => sortTable(key, defaultDir));
  });
});
