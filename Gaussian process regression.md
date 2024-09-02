---
created: 2024-08-29
lastmod: 2024-09-02
---
A Bayesian (see [[Bayesian statistics]]) approach to [[nonparametric regression]]. 

We say a stochastic process $\{m(x): x\in \calX\}$ is a Gaussian process if, for any finite collection $x_1,\dots,x_n$, 
$$

(m(x_1),\dots,m(x_n)) \sim N(\mu,K),

$$
where $K_{i,j} = K(x_i,x_j)$ is a [[Mercer kernel]] and $\mu = (\mu(x_1),\dots,\mu(x_n))$. Typically we suppose that $\mu=0$ since we can always subtract the mean from the data. 

Gaussian process regression places a prior $\pi$ on the regression function $m(x) = \E[Y|X=x]$ which assumes that $m$ is a Gaussian process. Thus, assuming $\mu=0$, the prior has density 
$$

\pi(m) = \frac{|K|^{-1/2}}{(2\pi)^{n/2}} \exp\bigg(-\frac{1}{2}m^T K^{-1}m\bigg),

$$
where $m = (m(x_1),\dots,m(x_n))$. 

### Predictive Distribution
Suppose we have observed training data $(X_1,Y_1),\dots,(X_n,Y_n)$ and observe a new point $Y_{n+1} = m(X_{n+1}) + \eps_{n+1}$. 
We have
$$
(Y_1,\dots,Y_n) = (m(x_1),\dots,m(x_n)) + (\eps_1,\dots,\eps_n) \sim N(0, K + \sigma^2I),
$$
if $\eps_i \sim N(0,\sigma^2)$. Then $\Cov(Y_i,Y_{n+1}) = \Cov(m(x_i),m(x_{n+1})) = K(x_i,x_{n+1})$ and $\Var(Y_{n+1}) = K(x_{n+1}, x_{n+1})) + \sigma^2$, so 
$$
 (Y_1,\dots,Y_{n+1}) \sim N\bigg(0, \begin{pmatrix} K_n +\sigma^2 I & k \\
k^t & K(x_{n+1},x_{n+1}) + \sigma^2\end{pmatrix}\bigg).
$$

