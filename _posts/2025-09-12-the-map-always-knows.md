---
layout: post
title: "The Map Always Knows… Or Does It?"
date: 2025-09-12
categories: algorithms networks
---

## From Roads to Routes

A navigation app feels solved. Enter two places and it returns the best way in seconds. The naive view is that computers just calculate the best path.

For a single trip this is mostly true. Model streets as a graph. Intersections are nodes. Roads are edges with weights for time or distance. Shortest path is efficient.

Change the task to visiting many stops once each and the difficulty jumps. The input is similar. The question is different.

---

## One Trip: Dijkstra and A*

Shortest path keeps a running cost and relaxes edges:

$$
d[v] \leftarrow \min\{d[v],\ d[u] + w(u,v)\}.
$$

A* adds a heuristic $h(v)$ and expands nodes with minimal

$$
f(v) = g(v) + h(v).
$$

If $h$ never overestimates then A* still finds the optimal path and usually explores far fewer nodes.

## Many Stops: Hamilton and the Explosion

Now require a route that visits every chosen stop exactly once. This is a Hamiltonian path or a Traveling Salesman tour.

The number of orders for $n$ stops is

$$
(n-1)!.
$$

For $n = 10$ this is $9! = 362{,}880$. For $n = 20$ it becomes $19! \approx 1.2\times 10^{17}$. No general fast method is known.

## The Fun Link: One-Stroke Drawings

People know the puzzle about drawing a figure without lifting the pen. That is not Hamiltonian. It is Eulerian.

An Eulerian trail uses every edge exactly once. A Hamiltonian path visits every vertex exactly once. They sound close. They are not.

Euler gave a crisp test. A connected graph has an Eulerian trail if and only if the number of odd-degree vertices is in $\{0,2\}$. Degrees are easy to count. The test is fast.

So:

- Street sweeping and snow plows want to use every road once with minimal repeats. This is the Chinese Postman problem. It reduces to pairing odd-degree intersections with a minimum-weight matching and is solvable in polynomial time.
- Sales rounds and sightseeing tours want to visit each location once. This is Hamiltonian and is hard in general.

Same streets. Different rules. Opposite difficulty.

## Networks: Packets vs Tours

The same split appears in computer networks.

- Packet routing sends data from one node to another. Link-state protocols compute shortest paths with Dijkstra-like updates. This is efficient.
- Multicast design and network tours connect many receivers with minimal total cost or visit a set of nodes once. Steiner trees and Hamiltonian variants appear. These are NP hard in general.

## Worked Example

Ten deliveries from one depot:

- Orders to try:

$$
9! = 362{,}880.
$$

At twenty stops the count jumps to

$$
19! \approx 1.2\times 10^{17}.
$$

Heuristics help in practice. The worst-case guarantee does not change.

One-stroke street cleaning on a small grid:

- Count odd-degree intersections. Suppose there are $2$. Then an Eulerian trail exists. Build the minimum matching on those odd nodes, duplicate those matched edges, and traverse all streets once. Each step runs in polynomial time.

Same city. Two formulations. One is fast. One is not.

## The Scorecard

- Shortest path: polynomial time. Dijkstra or A*.  
- Eulerian trail and Postman: polynomial time. Degree parity and matching.  
- Hamiltonian path and TSP: exponential search in general. Guarantees do not scale.
