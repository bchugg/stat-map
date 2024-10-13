---
created: 2024-09-03
lastmod: 2024-09-03
---

When trying to estimate an unknown $k$-dimensional parameter $\theta = (\theta_1,\dots,\theta_k)$ ([[statistical inference]]) the method of moments is an old school method (though it's recently seen a revival in interest), which equates the first $k$ theoretical moments with the first $k$ empirical moments. 

That is, we solve $\frac{1}{n}\sum_{i\leq n} X_i^j = \E_{\wh{\theta}}[X^j]$ for $j=1,\dots,k$. Note this is a purely [[frequentist statistics|frequentist approach]] . 

For [[exponential families]], the MoM estimator coincides with the [[MLE]]. 