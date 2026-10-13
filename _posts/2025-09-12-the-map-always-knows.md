---
layout: post
title: "Edges, Vertices, and the Limits of Routing"
date: 2025-09-12
categories: algorithms networks
---

## From Roads to Routes

Can you draw this figure in one continuous stroke without lifting your pen, and without retracing any line?

{% include figure.html src="the-map-always-knows-house.svg" alt="A square with both diagonals and a triangular roof on top: five points joined by eight lines." %}

What looks like a children's puzzle is one of the oldest problems in graph theory. It's also the question facing every street sweeper, snowplow driver, and mail carrier: how do you cover every road at least once, with the fewest repeated stretches?

The city of Königsberg was built across two islands connected by seven bridges, and its residents had a puzzle: could you walk across each bridge exactly once and return home? In 1736, Leonhard Euler answered the question. Euler's answer reduced the problem to counting. The possibility depends only on the number of "odd" intersections, nodes with an odd number of edges. A connected graph has a trail using every edge exactly once if and only if the number of odd-degree nodes is $0$ or $2$. Counting degrees takes seconds.

---

## The Chinese Postman

Euler's result was elegant but limited: it tells you whether a perfect route exists, not what to do when one doesn't. In 1962, Mei-Ko Kwan extended the idea to practical routing.

He asked: what if a network has many odd intersections? Instead of giving up, you can "fix" the graph by pairing odd nodes and adding the cheapest extra links until every degree becomes even. The result is an Eulerian tour in the augmented graph: a walk covering every street exactly once, with repeats chosen as efficiently as possible.

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

This forms a parallelogram: $\lvert ab\rvert=\lvert cd\rvert=3$ and $\lvert ac\rvert=\lvert bd\rvert=4$.

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

{% include figure.html src="the-map-always-knows-matchings.svg" alt="Three copies of the parallelogram a, b, c, d with all six connections drawn in gray; each copy highlights one perfect matching in black, (a,b)+(c,d), (a,c)+(b,d) and (a,d)+(b,c), with extra distances 6.00, 8.00 and 9.69 and totals 48.00, 50.00 and 51.69" %}

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

Two classic ways to walk a graph, and they differ enormously in difficulty.

**Eulerian path**: use every *edge* exactly once. The rule is precise: a connected graph has such a path only when the number of odd-degree nodes is $0$ or $2$. This is the world of street sweepers and snowplows. If more intersections are odd, the Chinese Postman approach fixes it by pairing them with the cheapest extra links.

**Hamiltonian path**: visit every *vertex* exactly once. At first glance it looks similar. But the difficulty is far greater. No simple counting rule applies. Deciding whether such a path exists is NP-hard. Sales rounds and sightseeing tours fall here, where heuristics and approximations are the tools of choice.

---

## Networks: Packets and Tours

The same edge-versus-vertex split appears in computer networks.

At the simplest level, moving a packet from one machine to another is a shortest-path problem. Routers treat the internet like a graph: machines are nodes, links are edges, weights come from bandwidth, latency, or administrative cost. Protocols like OSPF (Open Shortest Path First) maintain a live map and update routes using Dijkstra's algorithm.

Every time you send an email or load a webpage, a shortest-path calculation runs in the background.

The importance of these ideas became obvious in the early days of ARPANET. In 1969 the network launched with four nodes. Each node kept a table of distances and swapped it with its neighbours, a distributed form of the Bellman-Ford shortest-path method, and when delays changed quickly, packets could loop. In May 1979 the network switched to a scheme in which every node kept the whole map and ran Dijkstra's algorithm on it, which gave loop-free and more stable routes. Routers running OSPF still work this way.

---

## Beyond Point-to-Point

Not all communication is one-to-one. A video stream or software update may need to reach thousands of recipients. Sending packets separately would be wasteful, so networks build shared delivery structures.

The problem shifts from finding the shortest path between two machines to finding the cheapest tree connecting many machines. This is the **Steiner Tree Problem**, and it's NP-hard. No fast exact solution exists for large networks, so engineers use heuristics that work well enough in practice.

Another challenge: traffic that must visit a particular set of machines in sequence, forcing packets through firewalls or content filters. This begins to resemble Hamiltonian tours, where each required stop must be visited exactly once. These variants inherit the hardness of the Traveling Salesman Problem.

At the level of everyday internet traffic, packets follow Euler-style edges with polynomial-time algorithms. At the level of distribution and control, networks face Hamiltonian-style vertex constraints, where NP-hardness takes over and heuristics become the only workable approach.

A navigation app finds the fastest route between two points in milliseconds because shortest-path algorithms run in polynomial time. Planning an optimal delivery sequence through twenty stops is a different problem entirely: $(n-1)!$ grows so fast that brute-force search becomes intractable around $n = 20$.
