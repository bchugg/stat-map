---
created: 2024-08-29
lastmod: 2024-10-07
---

Wasserstein distances are a class of [[distributional distance|distributional metrics]] between distributions $\mu$ and $\nu$ over some common space $\calX$. They come from considering the [[optimal transport]] cost when the cost function is a metric. In particular, if $d:\calX\times\calX\to\Re$ is a metric, set 
$$
W_p(\mu,\nu) = \bigg(\min_{\pi\in \Gamma(\mu,\nu)} \E_{X,Y\sim \pi} [d(X,Y)^p]\bigg)^{1/p},
$$
where $\Gamma(\mu,\nu)$ is the set of joint distributions on $\calX\times\calX$ who marginals are $\mu$ and $\nu$, that is 
$$
\Gamma(\mu,\nu) = \bigg\{\pi: \int \pi(x,y)dy = \mu(x),\;\int \pi(x,y)dx = \nu(y)\bigg\}.
$$
Wasserstein distances are an optimal class of distances because they take advantage of the underlying geometry of the space $\calX$ (as induced by $d$). This is contradistinction to, e.g., the [[KL divergence]] and the [[total variation distance]]. 

For distributions over $\Re$, the 1-Wasserstein distance is 
$$
W_1(\mu, \nu) = \int|F_\mu(x) - F_\mu(x)|\d x,
$$
where $F_\mu$ and $F_\nu$ are the cdfs of $\mu$ and $\nu$. 

The Wasserstein distance is an [[ideal metrics|ideal metric]] of order 1, and useful for proving [[central limit theorems]]. 
