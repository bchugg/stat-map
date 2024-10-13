---
created: 2024-08-29
lastmod: 2024-09-02
---

A family of distributions $\{P_\theta:\theta\in\Theta\}$ form a $d$-dimensional exponential family if their densities have the form 
$$
p_\theta(x) = \exp\left\{\sum_{i\leq d} \eta_i(\theta)T_i(x) - A(\theta)\right\}h(x),
$$
for some functions $\eta_i$ and $A$ of the parameter space and function $h$ of the data. Typically we parameterize the family such that we may just write $\eta_i(\theta) = \theta_i$. 

The exponential family structure is preserved for iid samples: For $n$ samples, $A(\theta)$ becomes $n A(\theta)$, $h(x)$ becomes $\prod h(x_i)$ and $T_i(x)$ becomes $\sum_j T_i(x_j)$. 

Many distributions are exponential families; normals, binomials, Poisson, etc. See [wikipedia](https://en.wikipedia.org/wiki/Exponential_family) for more. 

The tuple $(T_1(x), \dots, T_d(x))$ is a [[sufficient statistic]]. $A(\theta)$ is the factor which ensures the density integrates to 1. It's called the log-partition function and can be written as 
$$
A(\theta) = \log \int \exp \left\{\sum_{i\leq d} \eta_i(\theta) T_i(x) \right\} h(x) \d x.
$$
$A(\theta)$ is also known as the cumulant function. It is a convex function of $\theta$. Its derivatives generate moments as follows: 
$$
\frac{\partial^2 A(\theta)}{\partial \theta_i\partial\theta_j} = \Cov(T_i(X), T_j(X)).
$$
