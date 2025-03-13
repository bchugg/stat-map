---
created: 2024-08-29
lastmod: 2025-03-13
---

A Bayesian (see [[Bayesian statistics]]) approach to [[nonparametric regression]]; see also [[Bayesian nonparametrics]]. 

We have training data $(X_1,Y_1),\dots,(X_n,Y_n)$ and want to model the regression function $f(x) = \E[Y|X=x]$. GP regression assumes that $f$ is a [[Gaussian process]]. That is, there exists a [[Mercer kernel]] $K$ such that for any finite collection $X_1,\dots,X_n$, 
$$
(f(X_1),\dots,f(X_n)) \sim N(\mu,K),
$$
where $K_{i,j} = K(X_i,X_j)$ and $\mu = (f(X_1),\dots,f(X_n))$. Typically we suppose that $\mu=0$ since we can always subtract the mean from the data. 

Note that $N(\mu,K) = N(0,K)$ is a distribution over functions. The shape smoothness of these functions is determined by the kernel $K$. By choosing $K$, we are thus choosing a prior over functions $f$. Assuming $\mu=0$, the prior has density 
$$
\pi(f) = \frac{|K|^{-1/2}}{(2\pi)^{n/2}} \exp\bigg(-\frac{1}{2}f^T K^{-1}f\bigg),
$$
where $f = (f(X_1),\dots,m(X_n))$. Note that the prior favors those $f$ such that $f^T K^{-1} f$ is small. If $\lambda$ is an eigenvalue corresponding to the eigenfunction $f$, i.e., $Kf = \lambda f$, then $\lambda^{-1} = f^T K^{-1}f$, meaning small $f^T K^{-1}f$ implies large eigenvalues, which correspond to smooth functions. GP regression is self-regularizing in this way. 

Now, we're given a new test point $X_*$. Doing some math and using some properties of the Gaussian pdf, one can show that, conditional on $X_1,\dots,X_n$, $Y_1,\dots,Y_n$ and $X_*$, $f(X_*)$ is distributed as $N(\mu_*, \sigma^2_*)$, where 
$$
\mu_* = \bs{k}_*^T(\bs{K}_n + \sigma^2 \bs{I})^{-1} \bs{y}, \quad \sigma_*^2 = K(X_*, X_*) - \bs{k}_*^T(K + \sigma^2 \bs{I})^{-1} \bs{y}, 
$$
where $\bs{k}_* = (K(X_1,X_*), \dots, K(X_n, X_*))$, $\bs{K}_n$ is the covariance defined by the kernel K on the training data, and $\sigma^2$ is the noise inherent to the model, i.e., we assume that $Y_i = f(X_i) + \eps$ where $\eps$ has variance $\sigma^2$. Our prediction $f(X_*)$ is taken to be $\mu_*$, but writing down the predictive distribution lets us quantify [[uncertainty quantification|uncertainty]]. 

# Reading 
A lot has been written about GP regression, as you can imagine. Some useful references are 
- [An intuitive tutorial to GP regression](https://arxiv.org/pdf/2009.10862v5) 
- [Gaussian processes for Machine Learning](https://gaussianprocess.org/gpml/), the e-book. 
