---
lastmod: 2024-12-30
created: 2024-12-24
---

Let $\Theta$ be some parameter space and $\calG$ be a family of functions from $\Theta$ to $\Re$. The integral probability metric (IPM) with respect to $\calG$ between two distributions $\rho$ and $\nu$ is the [[distributional distance]] 
$$
\gamma_\calG(\rho,\nu) := \sup_{g\in \calG}|\E_{\theta\sim \rho} g(\theta) - \E_{\theta\sim \nu} g(\theta)|.
$$
IPMs recover the [[total variation distance]], the [[Wasserstein distance]], the [[KS distance]], and the [[kernel MMD]] under different choices of $\calG$. $\calG$ is often taken to be symmetric so that we can get rid of the absolute value above. 

IPMs and [[f-divergence|f-divergences]] intersect (non-trivially) only at the [[total variation distance]]. IPMs are convex and can thus be sequentially estimated by [[confidence sequences for convex functionals]]. See [Sriperumbudur et al](https://arxiv.org/pdf/0901.2698) for more on plug-in estimation. 