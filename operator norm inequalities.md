---
created: 2024-08-29
lastmod: 2024-11-16
---

A summary of bounds on the operator norm of random operators. 

## Martingale-Bernstein inequality 
If we have a matrix martingale, i.e., $\E[Z_t |\calF_{t-1}] = Z_{t-1}$ for some filtration $(\calF_t)$ then the following [[martingale concentration]] inequality holds: 

![[martingale concentration#Variance bound — matrix version.|martingale concentration:Variance bound — matrix version.]]

## Dimension-free Bernstein inequality 
This is [given by Minsker](https://sminsker.wordpress.com/wp-content/uploads/2013/03/bernstein-inequality_preprint.pdf). If $X_1,\dots,X_n$ are independent and self-adjoint with $\E X_i=0$, $\|X_i\|\leq U$  and $\sigma^2 \geq \|\sum_i \E X_i^2\|$, then 
$$
\Pr(\left\| \sum_i X_i\|>t\right) \leq \frac{2\Tr(\sum_i \E X_i^2)}{\sigma^2}\exp(-f(t)) g(t),
$$
where 
$$
f(t) = \frac{t^2/2}{\sigma^2 + t/3}, \quad g(t) = 1 + \frac{6}{t^2\log^2(1 + t/\sigma^2)}.
$$
Note that $g(t)$ is decreasing. 