---
layout: post
title: "The Map Always Knows… Or Does It?"
date: 2025-09-12
categories: algorithms networks
---

## From Roads to Routes

It begins with a puzzle you may have tried as a child: can you draw a figure in one continuous stroke without lifting your pen, and without retracing any line unless you have to? What looks like a doodle challenge is in fact one of the oldest problems in graph theory.

The same question shows up in real life on city streets. Imagine a street sweeper, snowplow, or postman. Their job is to cover every road at least once, but every repeated stretch wastes fuel and time. How do you design the most efficient walk? This is the **Chinese Postman** problem.

The story stretches back to 1736, when Leonhard Euler, working in St. Petersburg, tackled the famous bridges of Königsberg. The city was built across two islands connected by seven bridges, and the residents wondered: could you stroll across each bridge exactly once and return home? Euler’s answer was simple but groundbreaking: the possibility depends only on the number of “odd” intersections (nodes with an odd degree). A connected graph has a trail that uses every edge once if and only if the number of odd-degree intersections is either $0$ or $2$. Counting degrees takes only seconds, and suddenly a centuries-old riddle had a crisp mathematical rule.

More than two centuries later, in 1962, Chinese mathematician Mei-Ko Kwan extended Euler’s idea to practical routing. He asked: what if a network has many odd intersections? Instead of giving up, you can “fix” the graph by pairing odd nodes and adding the cheapest extra links until every degree becomes even. The result is an Eulerian tour in the augmented graph, a walk that covers every street exactly once, with the repeats chosen as efficiently as possible. Kwan’s formulation became known as the **Chinese Postman Problem**, in honor of the everyday urban scenario that inspired it.

Formally, the cost is 

$$
\text{CPP}=\sum_{e\in E} w(e)\;+\;\min_{M}\ \sum_{(u,v)\in M}\operatorname{dist}(u,v),
$$  

where $M$ is a perfect matching of the odd nodes, and $\operatorname{dist}(u,v)$ is the shortest path distance between them in the original network.
---

<!-- CPP Worked Example — Euclidean coordinates with exact distances and live pairing cost -->
<div id="cpp-visual" style="margin:1rem 0;">
  <!-- Controls -->
  <div class="cpp-controls" style="margin-bottom:0.5rem;">
    <strong style="display:block;margin-bottom:0.5rem;">Pair odd nodes:</strong>

    <div style="margin-bottom:0.25rem;">
      <label style="cursor:pointer;">
        <input type="radio" name="cpp-pair" value="ab-cd" checked>
        (a,b) + (c,d)
      </label>
    </div>

    <div style="margin-bottom:0.25rem;">
      <label style="cursor:pointer;">
        <input type="radio" name="cpp-pair" value="ac-bd">
        (a,c) + (b,d)
      </label>
    </div>

    <div>
      <label style="cursor:pointer;">
        <input type="radio" name="cpp-pair" value="ad-bc">
        (a,d) + (b,c)
      </label>
    </div>
  </div>

  <!-- Summary line -->
  <div class="cpp-summary" style="font-family:system-ui,Segoe UI,Roboto,Helvetica,Arial,sans-serif;margin-bottom:0.5rem;">
    Extra distance to add: <strong><span id="cpp-extra">6.000</span></strong>
    | Base street length: <strong>42</strong>
    | Chinese Postman total: <strong><span id="cpp-total">48.000</span></strong>
  </div>

  <!-- Diagram -->
  <div class="cpp-svgwrap" style="max-width:640px;border:1px solid #ddd;border-radius:8px;overflow:hidden;">
    <svg id="cpp-svg" viewBox="0 0 520 300" width="100%" height="auto" aria-labelledby="cpp-title cpp-desc" role="img">
      <title id="cpp-title">Odd-node pair distances and selected pairings</title>
      <desc id="cpp-desc">All six pair distances are shown from Euclidean coordinates. Selecting a pairing highlights its two edges and recomputes the extra cost.</desc>

      <!-- Subtle grid -->
      <defs>
        <pattern id="grid" width="20" height="20" patternUnits="userSpaceOnUse">
          <path d="M20 0 L0 0 0 20" fill="none" stroke="#eee" stroke-width="1"/>
        </pattern>
        <marker id="dot" markerWidth="4" markerHeight="4" refX="2" refY="2">
          <circle cx="2" cy="2" r="2" fill="#111"></circle>
        </marker>
      </defs>
      <rect x="0" y="0" width="100%" height="100%" fill="url(#grid)"></rect>

      <!-- All six edges (light gray by default) -->
      <g id="edges" stroke="#bbb" stroke-width="3" opacity="1">
        <line id="e-ab" data-a="a" data-b="b" />
        <line id="e-ac" data-a="a" data-b="c" />
        <line id="e-ad" data-a="a" data-b="d" />
        <line id="e-bc" data-a="b" data-b="c" />
        <line id="e-bd" data-a="b" data-b="d" />
        <line id="e-cd" data-a="c" data-b="d" />
      </g>

      <!-- Distance labels -->
      <g id="labels" fill="#111" font-size="13" font-family="system-ui,Segoe UI,Roboto,Helvetica,Arial,sans-serif"></g>

      <!-- Nodes -->
      <g id="nodes" fill="#111" font-size="16" font-family="system-ui,Segoe UI,Roboto,Helvetica,Arial,sans-serif">
        <circle id="n-a" r="8"></circle><text id="t-a" text-anchor="middle">a</text>
        <circle id="n-b" r="8"></circle><text id="t-b" text-anchor="middle">b</text>
        <circle id="n-c" r="8"></circle><text id="t-c" text-anchor="middle">c</text>
        <circle id="n-d" r="8"></circle><text id="t-d" text-anchor="middle">d</text>
      </g>
    </svg>
  </div>
</div>

<script>
  (function () {
    // Euclidean coordinates (scale + offset to fit viewBox)
    // world coords: a(0,0), b(3,0), c(0,4), d(1.8,1.6)
    // SVG mapping: x = x0 + s*X, y = y0 - s*Y
    var s = 50, x0 = 60, y0 = 260;
    var pts = {
      a: {X:0,   Y:0},
      b: {X:3,   Y:0},
      c: {X:0,   Y:4},
      d: {X:1.8, Y:1.6}
    };
    function map(P){ return {x: x0 + s*P.X, y: y0 - s*P.Y}; }
    function dist(P,Q){ var dx=P.X-Q.X, dy=P.Y-Q.Y; return Math.hypot(dx,dy); }

    // Place nodes and labels
    [['a','n-a','t-a'],['b','n-b','t-b'],['c','n-c','t-c'],['d','n-d','t-d']].forEach(function(row){
      var k=row[0], cn=row[1], tn=row[2], p=map(pts[k]);
      var cEl=document.getElementById(cn), tEl=document.getElementById(tn);
      cEl.setAttribute('cx', p.x); cEl.setAttribute('cy', p.y);
      tEl.setAttribute('x', p.x);  tEl.setAttribute('y', p.y + (k==='c'||k==='d'? 25 : -15));
    });

    // Edge list
    var pairs = [
      ['ab','a','b'],
      ['ac','a','c'],
      ['ad','a','d'],
      ['bc','b','c'],
      ['bd','b','d'],
      ['cd','c','d']
    ];

    // Draw edges and compute exact weights from coords
    var labelsGroup = document.getElementById('labels');
    pairs.forEach(function([id,u,v]){
      var e=document.getElementById('e-'+id);
      var Pu=map(pts[u]), Pv=map(pts[v]);
      e.setAttribute('x1', Pu.x); e.setAttribute('y1', Pu.y);
      e.setAttribute('x2', Pv.x); e.setAttribute('y2', Pv.y);
      var w = dist(pts[u], pts[v]); // exact Euclidean
      e.setAttribute('data-weight', w.toString());

      // label at midpoint, with a tiny offset
      var mx=(Pu.x+Pv.x)/2, my=(Pu.y+Pv.y)/2;
      var t=document.createElementNS('http://www.w3.org/2000/svg','text');
      t.setAttribute('x', mx+6);
      t.setAttribute('y', my-6);
      t.setAttribute('text-anchor','start');
      t.setAttribute('fill', '#111');
      var txt = (id==='ad') ? '√5.8 ≈ ' + w.toFixed(3) : w.toFixed(3);
      t.textContent = txt;
      labelsGroup.appendChild(t);
    });

    // Highlight function for selected pairing
    var accent = '#0a7';
    function setStroke(el, color, width, opacity){
      el.setAttribute('stroke', color);
      el.setAttribute('stroke-width', width);
      el.setAttribute('opacity', opacity);
    }
    function highlight(val){
      // reset all to light gray
      pairs.forEach(function([id]){
        setStroke(document.getElementById('e-'+id), '#bbb', 3, 1);
      });
      // pick which two edges
      var choose = {
        'ab-cd': ['ab','cd'],
        'ac-bd': ['ac','bd'],
        'ad-bc': ['ad','bc']
      }[val] || [];
      var extra = 0;
      choose.forEach(function(id){
        var e = document.getElementById('e-'+id);
        setStroke(e, accent, 5, 0.95);
        extra += Number(e.getAttribute('data-weight'));
      });
      // update summary
      document.getElementById('cpp-extra').textContent = extra.toFixed(3);
      document.getElementById('cpp-total').textContent = (42 + extra).toFixed(3);
    }

    // Wire up radios
    function update(){
      var checked = document.querySelector('input[name="cpp-pair"]:checked');
      highlight(checked.value);
    }
    document.querySelectorAll('input[name="cpp-pair"]').forEach(function (el) {
      el.addEventListener('change', update);
    });
    update();
  })();
</script>


## One Trip: Dijkstra and A*

A single journey fits the shortest-path model: intersections are nodes, roads are edges with weights for time or distance, and we maintain tentative costs that improve by relaxing edges,  

$$
d[v]\leftarrow \min\{\,d[v],\ d[u]+w(u,v)\,\}.
$$  

A* adds an admissible heuristic $h(v)$ and always expands the node with the smallest  

$$
f(v)=g(v)+h(v),
$$  

which keeps the search focused while preserving optimality when $h$ never overestimates.

## Tours: Hamilton and Factorials

When the goal is to visit each chosen stop exactly once, the problem is Hamiltonian. With $n$ stops and a fixed start, the number of possible orders is  

$$
(n-1)!.
$$  

For $n=10$ this is $9!=362{,}880$, and for $n=20$ it is $19!\approx 1.2\times 10^{17}$.

A quick timing thought experiment makes the growth concrete. If scoring one tour takes $1\,\mu s$, then  

$$
9!\Rightarrow 3.6288\times 10^{5}\ \mu s \approx 0.36\ \text{s},
$$  

while  

$$
19!\Rightarrow 1.216\times 10^{17}\ \mu s \approx 3{,}860\ \text{years}.
$$  

Heuristics help in practice on real maps, yet the worst-case remains enormous.

## One Stroke versus One Visit

There are two classic ways to walk a graph. One focuses on edges, the other on vertices.

An **Eulerian path** uses every edge exactly once. The rule is precise: a connected graph has such a path only when the number of odd-degree nodes is $0$ or $2$. This is the world of street sweepers and snowplows. If more intersections are odd, the Chinese Postman approach fixes it by pairing them up with the cheapest extra links, after which the tour can be completed efficiently.

A **Hamiltonian path** visits every vertex exactly once. At first glance it looks similar, but the difficulty is much greater. No simple counting rule applies, and deciding whether such a path exists is NP-hard. Sales rounds and sightseeing tours fall into this category, where heuristics and approximations are the tools of choice.

## Networks: Packets and Tours

The same edge-versus-vertex split appears in computer networks. At the simplest level, moving a packet from one machine to another is a shortest-path problem. Routers and switches treat the internet like a graph: machines are nodes, links are edges, and weights come from bandwidth, latency, or administrative cost. Protocols such as OSPF (Open Shortest Path First) or IS-IS maintain a live map of the network and update routes using Dijkstra’s algorithm. Every time you send an email or load a webpage, a shortest-path calculation is running in the background to decide which wires and fibers your data will actually use.

The importance of these ideas became obvious in the early days of ARPANET, the ancestor of the modern internet. In 1969 the network launched with only four nodes. Routing was initially done with very simple distance tables, and small failures could confuse the system or cause packets to loop endlessly. By the early 1970s the designers adopted shortest-path algorithms to stabilize the network. Without the mathematics of Dijkstra and his successors, packet routing would have collapsed as ARPANET grew.

Not all communication is one-to-one. A video stream, a multiplayer game, or a software update may need to reach hundreds or thousands of recipients at once. Sending packets separately would be wasteful, so networks build shared delivery structures. The problem shifts from finding the shortest path between two machines to finding the cheapest tree that connects many machines together. This is the **Steiner Tree Problem**, and computer scientists quickly discovered it is NP-hard. No fast exact solution exists for large networks, so engineers use heuristics and approximation algorithms that are good enough in practice, even if they cannot promise the absolute best tree.

Another challenge comes when traffic must visit a particular set of machines in sequence, such as forcing packets to pass through firewalls, proxies, or content filters. This begins to resemble Hamiltonian tours, where each required stop must be visited exactly once. These variants inherit the hardness of Hamiltonian paths and the Traveling Salesman Problem: simple to state but resistant to efficient general solutions.

At the level of everyday internet traffic, packets follow Euler-style edges and are routed with polynomial-time algorithms. At the level of distribution and control, the network faces Hamiltonian-style vertex constraints, where NP-hardness takes over and heuristics are the only workable approach.
