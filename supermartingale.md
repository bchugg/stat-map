---
created: 2024-08-29
lastmod: 2024-12-21
---

A stochastic process $(S_t)$ is a supermartingale with respect to a filtration $(\calF_t)$ if
$$
\E[S_t|\calF_{t-1}] \leq S_{t-1},\quad \forall t.
$$
Supermartingales are thus decreasing over time in expectation. If $\leq$ is replaced by an equality then we have a martingale and, if in addition $\E[S_0]=1$ then we have a [[test-martingale]]. If $\leq$ is swapped with $\geq$ then we have a [[submartingale]]. 

Supermartingales obey [[Ville's inequality]] which makes them useful tools in [[game-theoretic statistics]]. They also define betting strategies in [[game-theoretic probability]]. 

Supermartingales obey the optional stopping theorem, which states that $\E[S_\tau]\leq \E S_0$ for stopping times $\tau$, under certain conditions on the process and the stopping time. They also obey the martingale convergence theorem, which states that if $S_t$ is nonnegative, then $S_t\to S$ a.s. to some random variable $S$ and $\E S\leq \E S_0$. 
