---
layout: post
title: "The Map Always Knows… Or Does It?"
date: 2025-09-12
categories: algorithms networks
---

## From Roads to Routes

Begin with the classic pen puzzle: can you trace a figure in one stroke without lifting the pen? City streets pose the same question. A street sweeper wants a walk that covers every road once, repeating as little as possible, which leads to the **Chinese Postman** problem.

The story starts with the bridges of Königsberg. Working in St Petersburg, Euler gave a crisp rule: a connected street graph has a trail that uses every edge exactly once if and only if the number of odd-degree intersections is in $\{0,2\}$. Degrees are easy to count, so this decision is fast.

If there are more than two odd intersections, pair the odd nodes and add the cheapest extra links so that all degrees become even. In the augmented graph an Eulerian tour exists and it covers every street exactly once. The total cost is
$$
\text{CPP}=\sum_{e\in E} w(e)\;+\;\min_{M}\ \sum_{(u,v)\in M}\operatorname{dist}(u,v),
$$
where $M$ is a perfect matching on the odd nodes and $\operatorname{dist}$ is the shortest-path distance in the original network.

---

### Worked example

Suppose the odd intersections are $a,b,c,d$ and the distances are
$$
\operatorname{dist}(a,b)=3,\ \operatorname{dist}(a,c)=4,\ \operatorname{dist}(a,d)=6,\\
\operatorname{dist}(b,c)=5,\ \operatorname{dist}(b,d)=2,\ \operatorname{dist}(c,d)=3.
$$
The perfect matchings and their costs are
$$
(a,b)+(c,d):\ 3+3=6,\quad
(a,c)+(b,d):\ 4+2=6,\quad
(a,d)+(b,c):\ 6+5=11.
$$
Choose cost $6$. If the sum of all street lengths is $42$, then
$$
\text{CPP}=42+6=48.
$$
Same city, every road covered, computed in polynomial time.

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

Using every **edge** once is an Eulerian question; visiting every **vertex** once is a Hamiltonian one. The statements sound similar but behave very differently.

For edges the rule is sharp: a connected graph has an Eulerian trail exactly when the count of odd-degree nodes is in $\{0,2\}$. Street sweeping and snow routing follow this edge view, and the Chinese Postman fix—pairing odd nodes with a minimum-weight matching—runs in polynomial time.

Sales rounds and sightseeing tours follow the vertex view. Visiting each location once is Hamiltonian and is NP hard in general.

## Networks: Packets and Tours

Computer networks show the same split. Moving a packet from one machine to another is a shortest-path task, and link-state protocols compute routes with Dijkstra-style updates across the network graph.

Designing structures that reach many receivers at once or forcing traffic to pass through a chosen set of machines mirrors the tour setting. Minimum Steiner trees and Hamiltonian variants appear, they are NP hard in general, and they encourage approximations rather than guaranteed fast solutions.

## The Scorecard

- Shortest path: polynomial time — use Dijkstra or A*.  
- Chinese Postman and Euler trails: polynomial time — degree parity and matching.  
- Hamiltonian path and TSP: exponential families in general — heuristics help, guarantees do not.
