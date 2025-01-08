---
created: 2024-08-29
lastmod: 2025-01-08
---

The total variation distance between two measures $\mu$ and $\nu$ on a measurable space $(\Omega, \calF)$ is 
$$
D_\tv(\rho\|\nu) := \sup_{A\in \calF} |\mu(A) - \nu(A)|.
$$
This can also be written as 
$$
D_\tv(\rho\|\nu) = \sup_{\norm{f}_\infty \leq 1} |\E_\mu[f(X)] - \E_\nu[f(X)]|,
$$
which turns out to be a useful representation for [[robust statistics]]. Eg, this representation was used to construct Huber robust (see [[Huber contamination model]]) [[confidence sequences]] [here](https://proceedings.mlr.press/v206/wang23p/wang23p.pdf).  

If $\mu$ and $\nu$ admit densities $\d \mu$ and $\d\nu$ then we can also write the TV distance as 
$$
D_\tv(\mu\|\nu) = \frac{1}{2}\int |\d\mu(x) - \d\nu(x)|\d x.
$$
The TV distance is an [[f-divergence]].  