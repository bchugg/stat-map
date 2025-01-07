---
lastmod: 2025-01-07
created: 2025-01-07
---

A stochastic process $\{X_\theta\}_{\theta\in\Theta}$ where any finite collection of random variables follows a Gaussian distribution. That is, for any collection, $X_{\theta_1}, \dots, X_{\theta_k}$, we require that 
$$
(X_{\theta_1},\dots,X_{\theta_k}) \sim N(\mu,\Sigma),
$$
where $\mu$ and $\Sigma$ can (and will) depend on the specific collection of random variables. In fact, the mean is 
$$
\mu = (\E X_{\theta_1}, \dots, \E X_{\theta_k}),
$$
and the covariance matrix is defined by $\Sigma(s,t) = \Cov(X_{\theta_s},X_{\theta_t})$. If the means are constant and $\Cov(X_{\theta_s},X_{\theta_t})$ depends only on some notion of distance between $\theta_s$ and $\theta_t$ then we call the process stationary. 

Gaussian processes are elegant because they are completely defined by the means and covariances: once you know those, you know how the process behaves. 

Gaussian processes play an important role in [[Bayesian nonparametrics]] via [[Gaussian process regression]]. 

Gaussian processes are distinct (and more strict) than [[sub-Gaussian process|sub-Gaussian processes]], which require only pairwise [[sub-Gaussian distributions|sub-Gaussian behavior]]. 