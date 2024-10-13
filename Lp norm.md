---
created: 2024-08-29
lastmod: 2024-09-02
---

Intuitively, $L^p$ spaces are a generalization of finite dimensional Euclidean spaces. In particular, the $L^p$ norm generalizes the $\ell_p$ norm to infinite dimensional spaces. $L^p$ spaces are sometimes called Lebesgue spaces.  

Formally, for a measure space $(\Omega, \calF, \mu)$, the $L^p$ norm for $1\leq p<\infty$ is defined as 
$$
\norm{f}_p = \int_\Omega |f|^p\d\mu.
$$
The set of all functions $f$ such that $\norm{f}_p$ is finite is an $L^p$ space. For $p=\infty$, we instead define $$
\norm{f}_\infty = \ess\sup |f|.
$$
Lp norms and spaces are generalized by [[Orlicz norm|Orlicz norms and spaces]].


Notes: 
- For $0\leq p<1$ one can use the same definition, but the resulting "norm" is a not a true norm—it does not obey the triangle inequality. It is sometimes called a "quasi-norm". 
- $L^2$ is the only [[Hilbert space]] among all $L^p$ spaces. 