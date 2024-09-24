---
created: 2024-09-09
lastmod: 2024-09-24
---

Berry-Esseen bounds typically refer to any non-asymptotic bound on the deviation between a sum of random variables $\sum_i X_i$ and a target random variable $X_\infty$. They are often instrumental in proving [[central limit theorems]] and usually stated in terms of the [[KS distance]], $\rho_\ks$. 

The classic Berry-Esseen bound, proved independently by both of them in 1945 is the following. Suppose $X_1,\dots,X_n$ are independent with mean $\mu_i$, variance $\sigma_i^2 = \E[(X_i-\mu_i)^2]$ and $B_n^2 = \sum_{i\leq n} \sigma_i^2$. Then, 
$$
\rho_{\ks}\left(\frac{1}{B_n} \sum_{i\leq n}(X_i-\mu_i), N(0,1)\right) \leq  \frac{C\sum_{i\leq n}\E|X_i - \mu_i|^3}{(B_n^2)^{3/2}}.
$$
for some universal constant $C$. Note that this assumes the existence of a third moment.

For iid observations, this reduces to
$$
\rho_{\ks}\left(\frac{\sqrt{n}}{\sigma}(\overline{X}_n - \mu) , N(0,1)\right) \leq \frac{C \E|X-\mu|^3}{\sqrt{n}\sigma},
$$
which is perhaps the more common form. 

The best known constants $C$ are 0.5583 for independent rvs and 0.4690 for iid rvs. A lower bound (proved by Esseen is 0.4097). [This thesis](https://ubt.opus.hbz-nrw.de/opus45-ubtr/frontdoor/deliver/index/docId/732/file/Dissertation_Schulz.pdf) gives the optimal Berry-Esseen constant in the binomial case. 

The convergence to 0 of the right hand side of the Berry-Esseen bound implies convergence of the Lindeberg function ([[Lindeberg-Feller CLT]]). 

