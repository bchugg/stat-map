---
created: 2024-08-29
lastmod: 2024-11-17
---

A summary of bounds on the operator norm of random operators. See also [[matrix martingale inequalities]], but I'm also linking these below because I'm a bit confused about how to organize matrix bounds if we're being honest. 

## Variance bound
![[matrix martingale inequalities#Variance bound]]

## Bennet-style bound
![[matrix martingale inequalities#Bennett-style bound]]

## Bernstein-style bound 
This replaces boundedness of the maximum eigenvalue with a moment condition. Let $X_1,\dots,X_n$ satisfy $\E X_i=0$ and $\E X_i^p \leq \frac{p!}{2} K^{p-2} \Sigma_i$ ([[Loewner order]]). If $\sigma^2 = \| \sum_i \Sigma_i\|$ then 
$$
\Pr(\lambda_{\max}(S_n) \geq u)\leq d\exp\left(-\frac{u^2}{2(\sigma^2 + Ku)}\right).
$$
This was proved by [Tropp in 2012](https://arxiv.org/abs/1004.4389). 
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