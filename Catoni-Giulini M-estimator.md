---
lastmod: 2024-10-07
created: 2024-10-07
---

In 2017, [Catoni and Giulini proposed](https://arxiv.org/pdf/1712.02747) to [[multivariate concentration]] based on [[M-estimation]]. Let $\psi$ be any symmetric "influence function" such that
$$
-\log(1 - x + x^2/2)\leq \psi(x) \leq \log(1 + x + x^2/2),\quad \forall x \in\Re.
$$
The motivation behind this condition is to choose a function $\psi$ such that $e^\psi$ is bounded by polynomials. The estimator is then 
$$
\xi(\theta) = \frac{1}{n\lambda}\sum_{i\leq n}\int_{\Re^d}\psi(\lambda \la \vartheta, X_i\ra)\rho_\theta(d\vartheta),
$$
where $\rho_\theta$ is Gaussian with mean $\theta$ and covariance $\beta^{-1}I$ for some $\beta>0$.  This is the estimate of $\la \theta, \E X\ra$. An approximation $\xi(\theta)$ is computationally tractable for certain choices of $\psi$, but still doesn't give a closed-form bound, since you can't compute it for all $\theta$.  

If we have a bound on the raw second moment, $\E\norm{X}^2 \leq v^2$, then choosing $\lambda = \sqrt{2\log(1/\delta)/(nv^2)}$ and $\beta = \lambda\sqrt{n v^2}$ gives the bound 
$$
\sup_{\theta\in\dsphere} |\xi(\theta) - \la \theta, \E X\ra | = O\left(\sqrt{\frac{v^2\log(1/\delta)}{n}}\right).
$$
Again, this is not quite a sub-Gaussian rate. This method can also be extended to matrices (also done by Catoni and Giulini). It is also proved using [[PAC-Bayes]] arguments. 

The same approach can of course be taken in the scalar case. There we can get explicit [[confidence intervals]] using numerical methods. See [Wang and Ramdas](https://arxiv.org/abs/2202.01250) (2023) who obtain [[confidence sequences]] in this way. 