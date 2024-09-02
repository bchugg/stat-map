---
created: 2024-08-29
lastmod: 2024-09-02
---
Given a sample $X_1,\dots,X_n\sim F$, we want to estimate the cdf $F_X(a) = \Pr(X\leq a)$. 

The most common approach in [[frequentist statistics]] is to simply use the empirical cdf: 
$$

\wh{F}_n(x) = \frac{1}{n}\sum_i \ind(X_i\leq x).

$$
Glivenko and Cantelli showed that this estimator obeys the uniform convergence guarantee: 
$$

\sup_x |\wh{F}_n(x) - F(x)| \xrightarrow{P}0.

$$
In fact, we can get almost sure convergence as well. 

The most common approach in [[Bayesian statistics]] is to use the [[Dirichlet process]] prior. 
