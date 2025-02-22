---
created: 2024-08-29
lastmod: 2025-01-07
---

> [!note] Definition 
> A collection of zero-mean random variables $\{X_\theta:\theta\in\Theta\}$ is a sub-Gaussian process wrt to a metric $\rho$ if 
> $$
> \E[\exp(\lambda(X_\theta - X_\phi))] \leq \exp(\lambda^2\rho^2(\theta, \phi)/2),
> $$
> for all $\theta,\phi\in\Theta$. 

The Rademacher process and the canonical Gaussian process (see [[Rademacher complexity]] and [[Gaussian complexity]]) are examples of sub-Gaussian processes. 

As in the case of tail bounds for sub-Gaussian random variables ([[bounded scalar concentration]]), using the [[Chernoff method]] we see that the above definition is equivalent to 
$$
\Pr(|X_\theta - X_\phi| \geq \eps) \leq 2\exp\left(-\frac{t^2}{2 \rho^2(\theta, \phi)}\right).
$$
Note that a sub-Gaussian process is distinct from a [[Gaussian process]], which requires Gaussian behavior of any finite collection of random variables. Here we demand only pairwise [[sub-Gaussian distributions|(sub)-Gaussian behavior]]. 
