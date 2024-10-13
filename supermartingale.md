---
created: 2024-08-29
lastmod: 2024-09-02
---

A stochastic process $(S_t)$ is a supermartingale with respect to a filtration $(\calF_t)$ if
$$
\E[S_t|\calF_{t-1}] \leq S_{t-1},\quad \forall t.
$$
Supermartingales are thus decreasing over time in expectation. If $\leq$ is replaced by an equality then we have a martingale and, if in addition $\E[S_0]=1$ then we have a [[test-martingale]].

Supermartingales obey [[Ville's inequality]] which makes them useful tools in [[game-theoretic statistics]]. They also define betting strategies in [[game-theoretic probability]]. 
