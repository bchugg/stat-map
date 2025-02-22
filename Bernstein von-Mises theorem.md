---
created: 2024-08-29
lastmod: 2024-09-02
---

A result about the consistency of [[credible intervals]] in [[Bayesian statistics]]. The theorem states that in a fixed-dimensional problem, if the prior $\pi$ is positive in a neighborhood around the true parameter $\theta^*$, then 
$$
\norm{\pi(\theta|X^n) - N(\wh{\theta}_n, I^{-1}(\wh{\theta}_n)/n)}_{\tv} \to 0,
$$
where $N$ is the normal distribution, $\wh{\theta}_n$ is the [[MLE]], and $I(\wh{\theta}_n)$ is the [[Fisher information]]. Therefore, if the MLE has nice properties for the problem at hand, then so too does the posterior for large enough $n$. 

This BvM theorem as a justification for Bayesian methods in certain problem domains. However, one should always emphasize the assumption that the prior put positive mass on the true parameter. This can be challenging when the dimension is extremely large. 