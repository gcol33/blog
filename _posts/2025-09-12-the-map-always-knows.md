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

### Worked example

Suppose the odd intersections are $a,b,c,d$, and the shortest-path distances between them are  

$$
\operatorname{dist}(a,b)=3,\quad \operatorname{dist}(a,c)=4,\quad \operatorname{dist}(a,d)=6, \\
\operatorname{dist}(b,c)=5,\quad \operatorname{dist}(b,d)=2,\quad \operatorname{dist}(c,d)=3.
$$  

To fix the graph, we must pair up the odd nodes. The possible perfect matchings and their added costs are  

$$
(a,b)+(c,d):\ 3+3=6, \qquad
(a,c)+(b,d):\ 4+2=6, \qquad
(a,d)+(b,c):\ 6+5=11.
$$  

The minimum extra cost is $6$. If the total length of all original streets is $42$, then the Chinese Postman solution has  

$$
\text{CPP} = 42 + 6 = 48.
$$  

So the postman covers every road, with only $6$ units of extra distance beyond the raw street network.

<!-- CPP Worked Example — inline SVG visual with toggleable pairings -->
<div id="cpp-visual" style="margin:1rem 0;">
  <!-- Controls -->
  <div class="cpp-controls" style="display:flex;gap:1rem;align-items:center;flex-wrap:wrap;margin-bottom:0.5rem;">
    <strong style="margin-right:0.5rem;">Pair odd nodes:</strong>

    <label style="cursor:pointer;">
      <input type="radio" name="cpp-pair" id="cpp-opt1" data-extra="6" checked>
      (a,b) + (c,d) — cost 3 + 3
    </label>

    <label style="cursor:pointer;">
      <input type="radio" name="cpp-pair" id="cpp-opt2" data-extra="6">
      (a,c) + (b,d) — cost 4 + 2
    </label>

    <label style="cursor:pointer;">
      <input type="radio" name="cpp-pair" id="cpp-opt3" data-extra="11">
      (a,d) + (b,c) — cost 6 + 5
    </label>
  </div>

  <!-- Summary line (auto-updates) -->
  <div class="cpp-summary" style="font-family:system-ui,Segoe UI,Roboto,Helvetica,Arial,sans-serif;margin-bottom:0.5rem;">
    Extra distance to add: <strong><span id="cpp-extra">6</span></strong>  
    | Base street length: <strong>42</strong>  
    | Chinese Postman total: <strong><span id="cpp-total">48</span></strong>
  </div>

  <!-- Diagram -->
  <div class="cpp-svgwrap" style="max-width:640px;border:1px solid #ddd;border-radius:8px;overflow:hidden;">
    <svg viewBox="0 0 520 300" width="100%" height="auto" aria-labelledby="cpp-title cpp-desc" role="img">
      <title id="cpp-title">Pairings between odd intersections a, b, c, d</title>
      <desc id="cpp-desc">Toggle the radio buttons to highlight which odd nodes are paired. Labels show the pair costs.</desc>

      <!-- Background grid (subtle) -->
      <defs>
        <pattern id="grid" width="20" height="20" patternUnits="userSpaceOnUse">
          <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#eee" stroke-width="1"/>
        </pattern>
      </defs>
      <rect x="0" y="0" width="100%" height="100%" fill="url(#grid)"></rect>

      <!-- Node positions -->
      <!-- a(80,60)  b(440,60)  c(120,240)  d(400,240) -->
      <!-- Base nodes & labels -->
      <g fill="#111" font-family="system-ui,Segoe UI,Roboto,Helvetica,Arial,sans-serif" font-size="16">
        <circle cx="80" cy="60" r="8" fill="#111"></circle>
        <text x="80" y="45" text-anchor="middle">a</text>

        <circle cx="440" cy="60" r="8" fill="#111"></circle>
        <text x="440" y="45" text-anchor="middle">b</text>

        <circle cx="120" cy="240" r="8" fill="#111"></circle>
        <text x="120" y="265" text-anchor="middle">c</text>

        <circle cx="400" cy="240" r="8" fill="#111"></circle>
        <text x="400" y="265" text-anchor="middle">d</text>
      </g>

      <!-- Pairings (only one group visible at a time via CSS) -->
      <!-- (a,b) + (c,d) => costs 3 and 3 -->
      <g class="pairing pairing-ab-cd">
        <line x1="80" y1="60" x2="440" y2="60" stroke="currentColor" stroke-width="5" opacity="0.9"/>
        <line x1="120" y1="240" x2="400" y2="240" stroke="currentColor" stroke-width="5" opacity="0.9"/>
        <g fill="#111" font-family="system-ui,Segoe UI,Roboto,Helvetica,Arial,sans-serif" font-size="14">
          <text x="260" y="40" text-anchor="middle">3</text>
          <text x="260" y="260" text-anchor="middle">3</text>
        </g>
      </g>

      <!-- (a,c) + (b,d) => costs 4 and 2 -->
      <g class="pairing pairing-ac-bd">
        <line x1="80" y1="60" x2="120" y2="240" stroke="currentColor" stroke-width="5" opacity="0.9"/>
        <line x1="440" y1="60" x2="400" y2="240" stroke="currentColor" stroke-width="5" opacity="0.9"/>
        <g fill="#111" font-family="system-ui,Segoe UI,Roboto,Helvetica,Arial,sans-serif" font-size="14">
          <text x="100" y="150" text-anchor="middle">4</text>
          <text x="420" y="150" text-anchor="middle">2</text>
        </g>
      </g>

      <!-- (a,d) + (b,c) => costs 6 and 5 -->
      <g class="pairing pairing-ad-bc">
        <line x1="80" y1="60" x2="400" y2="240" stroke="currentColor" stroke-width="5" opacity="0.9"/>
        <line x1="440" y1="60" x2="120" y2="240" stroke="currentColor" stroke-width="5" opacity="0.9"/>
        <g fill="#111" font-family="system-ui,Segoe UI,Roboto,Helvetica,Arial,sans-serif" font-size="14">
          <text x="240" y="150" text-anchor="middle">6</text>
          <text x="280" y="150" text-anchor="middle">5</text>
        </g>
      </g>
    </svg>
  </div>
</div>

<style>
  /* Only show the selected pairing */
  #cpp-visual .pairing { display: none; }
  #cpp-opt1:checked ~ .cpp-summary ~ .cpp-svgwrap .pairing-ab-cd { display: block; }
  #cpp-opt2:checked ~ .cpp-summary ~ .cpp-svgwrap .pairing-ac-bd { display: block; }
  #cpp-opt3:checked ~ .cpp-summary ~ .cpp-svgwrap .pairing-ad-bc { display: block; }

  /* Color the active pairing line using the current text color; tweak here if you want a brand color */
  #cpp-visual .pairing line { color: #0a7; } /* change to your accent color */
</style>

<script>
  (function () {
    var base = 42; // total length of all original streets
    var extraSpan = document.getElementById('cpp-extra');
    var totalSpan = document.getElementById('cpp-total');
    function update() {
      var checked = document.querySelector('input[name="cpp-pair"]:checked');
      var extra = Number(checked.getAttribute('data-extra') || 0);
      extraSpan.textContent = String(extra);
      totalSpan.textContent = String(base + extra);
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
