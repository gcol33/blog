---
layout: default
title: Search
permalink: /search/
---

<h1>Search</h1>
<input type="text" id="search-box" placeholder="Type to search..." style="width:100%;padding:8px;font-size:16px;">

<ul id="results"></ul>

<script>
  async function fetchIndex() {
    const res = await fetch('{{ "/search.json" | relative_url }}');
    return await res.json();
  }

  function searchPosts(posts, query) {
    query = query.toLowerCase();
    return posts.filter(p => 
      p.title.toLowerCase().includes(query) ||
      p.content.toLowerCase().includes(query)
    );
  }

  (async function() {
    const posts = await fetchIndex();
    const box = document.getElementById('search-box');
    const results = document.getElementById('results');
    box.addEventListener('input', () => {
      const matches = searchPosts(posts, box.value);
      results.innerHTML = matches.map(m => 
        `<li><a href="${m.url}">${m.title}</a></li>`
      ).join('');
    });
  })();
</script>
