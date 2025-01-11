---
created: 2024-09-03
lastmod: 2025-01-11
---

Method for [[parametric density estimation]]. We are trying estimate an unknown $k$-dimensional parameter $\theta = (\theta_1,\dots,\theta_k)$ ([[statistical inference]]). The method of moments is an old school method (though it's recently seen a revival in interest, eg for [estimating Gaussian mixtures](https://projecteuclid.org/journals/annals-of-statistics/volume-48/issue-4/Optimal-estimation-of-Gaussian-mixtures-via-denoised-method-of-moments/10.1214/19-AOS1873.full)), which equates the first $k$ theoretical moments with the first $k$ empirical moments. That is, we solve 
$$
\frac{1}{n}\sum_{i\leq n} X_i^j = \E_{\wh{\theta}}[X^j], \quad \text{for }\quad j=1,\dots,k,
$$
(where $\wh{\theta}$ is unknown).  Note this is a purely [[frequentist statistics|frequentist approach]]. Because we're only trying to solve the moment equations, the resulting parameter estimates can be outside of the parameter space. This doesn't happen with the [[MLE]]. 

The MoM is consistent under fairly weak assumptions, and it obeys a [[central limit theorems|CLT]]. It's not guaranteed to be unbiased. For [[exponential families]], the MoM estimator coincides with the [[MLE]]. 