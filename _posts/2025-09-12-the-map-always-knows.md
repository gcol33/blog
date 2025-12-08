---
layout: post
title: "The Map Always Knows… Or Does It?"
date: 2025-09-12
categories: algorithms networks
---

## From Roads to Routes

Can you draw this figure in one continuous stroke without lifting your pen, and without retracing any line?

What looks like a children's puzzle is one of the oldest problems in graph theory. It's also the question facing every street sweeper, snowplow driver, and mail carrier: how do you cover every road at least once, with the fewest repeated stretches?

The story begins in 1736, when Leonhard Euler tackled the bridges of Königsberg. The city was built across two islands connected by seven bridges. Residents wondered: could you stroll across each bridge exactly once and return home?

Euler's answer was groundbreaking in its simplicity. The possibility depends only on the number of "odd" intersections—nodes with an odd number of edges. A connected graph has a trail using every edge exactly once if and only if the number of odd-degree nodes is $0$ or $2$. Counting degrees takes seconds. A centuries-old riddle suddenly had a crisp mathematical rule.

---

## The Chinese Postman

More than two centuries later, in 1962, Chinese mathematician Mei-Ko Kwan extended Euler's idea to practical routing.

He asked: what if a network has many odd intersections? Instead of giving up, you can "fix" the graph by pairing odd nodes and adding the cheapest extra links until every degree becomes even. The result is an Eulerian tour in the augmented graph—a walk covering every street exactly once, with repeats chosen as efficiently as possible.

Kwan's formulation became known as the **Chinese Postman Problem**, after the everyday scenario that inspired it.

Formally, the cost is:

$$
\text{CPP}=\sum_{e\in E} w(e)\;+\;\min_{M}\ \sum_{(u,v)\in M}\operatorname{dist}(u,v)
$$

where $M$ is a perfect matching of the odd nodes, and $\operatorname{dist}(u,v)$ is the shortest path distance between them.

---

### Worked Example

Place four odd intersections at:

$$
a=(0,0),\quad b=(3,0),\quad c=\!\bigl(2,\,2\sqrt{3}\bigr),\quad d=\!\bigl(5,\,2\sqrt{3}\bigr)
$$

This forms a parallelogram: $|ab|=|cd|=3$ and $|ac|=|bd|=4$.

The diagonals differ:

$$
|ad|=\sqrt{37},\qquad |bc|=\sqrt{13}
$$

Three possible matchings:

$$
\begin{aligned}
(a,b)+(c,d) &: 3+3=6\\
(a,c)+(b,d) &: 4+4=8\\
(a,d)+(b,c) &: \sqrt{37}+\sqrt{13}\approx 9.69
\end{aligned}
$$

The minimum extra cost is $6$. If the total length of all original streets is $42$:

$$
\text{CPP}=42+6=48
$$

The postman covers every road with only $6$ units of extra distance.

<div id="cpp-visual" style="margin:1rem 0;">
  <div class="cpp-controls" style="margin-bottom:0.5rem;">
    <strong style="display:block;margin-bottom:0.5rem;">Pair odd nodes:</strong>
    <div><label><input type="radio" name="cpp-pair" value="ab-cd" checked> (a,b) + (c,d)</label></div>
    <div><label><input type="radio" name="cpp-pair" value="ac-bd"> (a,c) + (b,d)</label></div>
    <div><label><input type="radio" name="cpp-pair" value="ad-bc"> (a,d) + (b,c)</label></div>
  </div>

  <div class="cpp-summary" style="font-family:system-ui,Segoe UI,Roboto,Helvetica,Arial,sans-serif;margin-bottom:0.5rem;">
    Extra distance: <strong><span id="cpp-extra">6.000</span></strong>
    | Base: <strong>42</strong>
    | Total: <strong><span id="cpp-total">48.000</span></strong>
  </div>

  <div class="cpp-svgwrap" style="max-width:720px; margin:0 auto; border:1px solid #000; overflow:hidden;">
    <svg id="cpp-svg" viewBox="0 0 700 420" width="100%" height="auto" aria-labelledby="cpp-title cpp-desc" role="img">
      <title id="cpp-title">Parallelogram layout: sides 3 and 4 at 60°, diagonals √37 and √13</title>
      <desc id="cpp-desc">Interactive CPP matching on a slanted 3×4 parallelogram.</desc>

      <defs>
        <pattern id="grid" width="20" height="20" patternUnits="userSpaceOnUse">
          <path d="M20 0 L0 0 0 20" fill="none" stroke="#eee" stroke-width="1"/>
        </pattern>
        <filter id="labelShadow" x="-50%" y="-50%" width="200%" height="200%">
          <feDropShadow dx="0" dy="0" stdDeviation="1" flood-color="#fff" flood-opacity="0.85"/>
        </filter>
      </defs>

      <rect x="14" y="14" width="672" height="392" fill="url(#grid)"></rect>
      <rect id="inner-frame" x="14" y="14" width="672" height="392" fill="none" stroke="#000" stroke-width="1"></rect>

      <g id="edges" stroke="#bbb" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
        <line id="e-ab" />
        <line id="e-ac" />
        <line id="e-bd" />
        <line id="e-cd" />
        <line id="e-ad" />
        <line id="e-bc" />
      </g>

      <g id="edge-hits" stroke="rgba(0,0,0,0)" stroke-width="24" stroke-linecap="round" stroke-linejoin="round"
         style="pointer-events: stroke;">
        <line data-for="e-ab" />
        <line data-for="e-ac" />
        <line data-for="e-bd" />
        <line data-for="e-cd" />
        <line data-for="e-ad" />
        <line data-for="e-bc" />
      </g>

      <g id="labels" font-family="system-ui,Segoe UI,Roboto,Helvetica,Arial,sans-serif"
         font-size="18" font-weight="600" fill="#111" filter="url(#labelShadow)"></g>

      <g id="nodes" fill="#111">
        <circle id="n-a" r="8"></circle>
        <circle id="n-b" r="8"></circle>
        <circle id="n-c" r="8"></circle>
        <circle id="n-d" r="8"></circle>
      </g>

      <g id="node-labels" font-family="system-ui,Segoe UI,Roboto,Helvetica,Arial,sans-serif"
         font-size="20" font-weight="700" fill="#111" filter="url(#labelShadow)"></g>
    </svg>
  </div>
</div>

<style>
#cpp-visual #edges line{
  transition: stroke 120ms ease, stroke-width 120ms ease, opacity 120ms ease;
}
#cpp-visual #edges line:hover{
  stroke: #0a7;
  opacity: 0.9;
}
#cpp-visual text{ user-select: none; }
</style>

<script>
(function(){
  const SQRT3 = Math.sqrt(3);
  const W = {
    a:{X:0, Y:0},
    b:{X:3, Y:0},
    c:{X:2, Y:2*SQRT3},
    d:{X:5, Y:2*SQRT3}
  };

  const s = 90, x0 = 80, y0 = 360;
  function map(P){ return { x: x0 + s*P.X, y: y0 - s*P.Y }; }
  function dist(P,Q){ const dx=P.X-Q.X, dy=P.Y-Q.Y; return Math.hypot(dx,dy); }

  ['a','b','c','d'].forEach(k=>{
    const p = map(W[k]);
    const el = document.getElementById('n-'+k);
    el.setAttribute('cx', p.x);
    el.setAttribute('cy', p.y);
  });

  function addText(parent, x, y, text, fontSize=18){
    const t = document.createElementNS('http://www.w3.org/2000/svg','text');
    t.setAttribute('x', x); t.setAttribute('y', y);
    t.setAttribute('font-size', fontSize);
    t.setAttribute('text-anchor', 'middle');
    t.setAttribute('dominant-baseline', 'middle');
    t.textContent = text;
    parent.appendChild(t);
  }

  function setEdge(id, u, v, label, opts={}){
    const U = map(W[u]), V = map(W[v]);
    const e  = document.getElementById(id);
    e.setAttribute('x1', U.x); e.setAttribute('y1', U.y);
    e.setAttribute('x2', V.x); e.setAttribute('y2', V.y);
    e.dataset.weight = dist(W[u], W[v]);

    const hit = document.querySelector(`#edge-hits line[data-for="${id}"]`);
    hit.setAttribute('x1', U.x); hit.setAttribute('y1', U.y);
    hit.setAttribute('x2', V.x); hit.setAttribute('y2', V.y);

    const dx = V.x - U.x, dy = V.y - U.y;
    const len = Math.hypot(dx, dy) || 1;
    const tx = dx/len, ty = dy/len;
    const nx = -ty, ny = tx;

    const k = (opts.k ?? 20), t = (opts.t ?? 0), side = (opts.side ?? 1);
    const mx = (U.x+V.x)/2, my = (U.y+V.y)/2;
    const lx = mx + side*k*nx + t*tx;
    const ly = my + side*k*ny + t*ty;

    addText(document.getElementById('labels'), lx, ly, label, 20);
  }

  setEdge('e-ab','a','b','3',{k:16});
  setEdge('e-cd','c','d','3',{k:16});
  setEdge('e-ac','a','c','4',{k:16});
  setEdge('e-bd','b','d','4',{k:16});
  setEdge('e-ad','a','d','√37',{k:22,t:24,side:1});
  setEdge('e-bc','b','c','√13',{k:22,t:-24,side:-1});

  (function(){
    const NL=document.getElementById('node-labels');
    const cfg = { a:{dx:0,dy:-28}, b:{dx:0,dy:-28}, c:{dx:0,dy:32}, d:{dx:0,dy:32} };
    ['a','b','c','d'].forEach(k=>{
      const nEl=document.getElementById('n-'+k);
      const x=+nEl.getAttribute('cx')+cfg[k].dx;
      const y=+nEl.getAttribute('cy')+cfg[k].dy;
      addText(NL,x,y,k,22);
    });
  })();

  const accent='#0a7', base=42;
  function resetEdges(){
    document.querySelectorAll('#edges line').forEach(e=>{
      e.setAttribute('stroke','#bbb'); e.setAttribute('stroke-width',3); e.setAttribute('opacity',1);
    });
  }
  function mark(id){
    const e=document.getElementById(id);
    e.setAttribute('stroke',accent); e.setAttribute('stroke-width',5); e.setAttribute('opacity',0.95);
    return +e.dataset.weight;
  }
  function update(){
    resetEdges();
    const val=document.querySelector('input[name="cpp-pair"]:checked').value;
    let extra=0;
    if(val==='ab-cd') extra=mark('e-ab')+mark('e-cd');
    if(val==='ac-bd') extra=mark('e-ac')+mark('e-bd');
    if(val==='ad-bc') extra=mark('e-ad')+mark('e-bc');
    document.getElementById('cpp-extra').textContent=extra.toFixed(3);
    document.getElementById('cpp-total').textContent=(base+extra).toFixed(3);
  }

  const edgeToPair = {
    'e-ab': 'ab-cd', 'e-cd': 'ab-cd',
    'e-ac': 'ac-bd', 'e-bd': 'ac-bd',
    'e-ad': 'ad-bc', 'e-bc': 'ad-bc'
  };

  document.querySelectorAll('#edge-hits line').forEach(hit=>{
    hit.addEventListener('click', ()=>{
      const targetId = hit.getAttribute('data-for');
      const pair = edgeToPair[targetId];
      const radio = document.querySelector(`input[name="cpp-pair"][value="${pair}"]`);
      if(radio){ radio.checked = true; update(); }
    }, {passive:true});
  });

  document.querySelectorAll('input[name="cpp-pair"]').forEach(el=>el.addEventListener('change',update));
  update();
})();
</script>

---

## One Trip: Dijkstra and A*

A single journey fits the shortest-path model. Intersections are nodes, roads are edges with weights for time or distance. Maintain tentative costs that improve by relaxing edges:

$$
d[v]\leftarrow \min\{\,d[v],\ d[u]+w(u,v)\,\}
$$

A* adds an admissible heuristic $h(v)$ and always expands the node with smallest:

$$
f(v)=g(v)+h(v)
$$

This keeps the search focused while preserving optimality when $h$ never overestimates.

---

## Tours: Hamilton and Factorials

When the goal is to visit each chosen stop exactly once, the problem becomes Hamiltonian. With $n$ stops and a fixed start, the number of possible orders is:

$$
(n-1)!
$$

For $n=10$: $9!=362{,}880$. For $n=20$: $19!\approx 1.2\times 10^{17}$.

A timing experiment makes the growth concrete. If scoring one tour takes $1\,\mu s$:

$$
9! \Rightarrow 3.6 \times 10^{5}\ \mu s \approx 0.36\ \text{s}
$$

$$
19! \Rightarrow 1.2 \times 10^{17}\ \mu s \approx 3{,}860\ \text{years}
$$

Heuristics help on real maps. But the worst case remains enormous.

---

## One Stroke versus One Visit

Two classic ways to walk a graph. One focuses on edges. The other on vertices.

**Eulerian path**: use every *edge* exactly once. The rule is precise: a connected graph has such a path only when the number of odd-degree nodes is $0$ or $2$. This is the world of street sweepers and snowplows. If more intersections are odd, the Chinese Postman approach fixes it by pairing them with the cheapest extra links.

**Hamiltonian path**: visit every *vertex* exactly once. At first glance it looks similar. But the difficulty is far greater. No simple counting rule applies. Deciding whether such a path exists is NP-hard. Sales rounds and sightseeing tours fall here, where heuristics and approximations are the tools of choice.

---

## Networks: Packets and Tours

The same edge-versus-vertex split appears in computer networks.

At the simplest level, moving a packet from one machine to another is a shortest-path problem. Routers treat the internet like a graph: machines are nodes, links are edges, weights come from bandwidth, latency, or administrative cost. Protocols like OSPF (Open Shortest Path First) maintain a live map and update routes using Dijkstra's algorithm.

Every time you send an email or load a webpage, a shortest-path calculation runs in the background.

The importance of these ideas became obvious in the early days of ARPANET. In 1969 the network launched with four nodes. Routing was done with simple distance tables, and small failures could cause packets to loop endlessly. By the early 1970s, designers adopted shortest-path algorithms to stabilize the network. Without Dijkstra, packet routing would have collapsed as ARPANET grew.

---

## Beyond Point-to-Point

Not all communication is one-to-one. A video stream or software update may need to reach thousands of recipients. Sending packets separately would be wasteful, so networks build shared delivery structures.

The problem shifts from finding the shortest path between two machines to finding the cheapest tree connecting many machines. This is the **Steiner Tree Problem**—and it's NP-hard. No fast exact solution exists for large networks, so engineers use heuristics that work well enough in practice.

Another challenge: traffic that must visit a particular set of machines in sequence, forcing packets through firewalls or content filters. This begins to resemble Hamiltonian tours, where each required stop must be visited exactly once. These variants inherit the hardness of the Traveling Salesman Problem.

At the level of everyday internet traffic, packets follow Euler-style edges with polynomial-time algorithms. At the level of distribution and control, networks face Hamiltonian-style vertex constraints, where NP-hardness takes over and heuristics become the only workable approach.

Your navigation app finds the fastest route in milliseconds. Planning a delivery sequence through twenty stops could take millennia to optimize exactly. The map always knows—but sometimes, knowing takes longer than the universe has existed.
