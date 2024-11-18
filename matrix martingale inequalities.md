---
lastmod: 2024-11-17
created: 2024-11-17
---

## Variance bound
Matrix version of [[martingale concentration#Variance bound]]. Suppose $X_1,\dots,X_n$ is a matrix-valued martingale of [[Hermitian matrix|Hermitian Matrices]] adapted to some filtration $\calF$, i.e., $\E[X_i |\calF_{i-1}] = X_{i-1}$. Let $D_i = X_i - X_{i-1}$ and suppose 
$$
\norm{D_i}\leq c_i, \quad \norm{\E[D_i^2|\calF_{i-1}]}\leq \sigma_i^2.
$$
Then, for $V_n = \sum_{i\leq n} \sigma_i^2$, 
$$
\Pr(\norm{X_n}> \eps)\leq 2d\exp\left(\frac{-\eps^2}{4V_n}\right),
$$
where each $X_t$ is a $(d\times d)$-matrix. This was first proved by David Gross: [Recovering Low-Rank Matrices From Few Coefficients In Any Basis](https://www.math.ucdavis.edu/~strohmer/courses/270/lowrank_Gross.pdf). 

## Bennett-style bound 
Let $X_1,X_2,\dots$ be a matrix valued martingale difference sequence ($\E[X_i |\calF_{i-1}] = 0$) adapted to $\calF$ with $\lambda_{\max}(X_i)\leq K$ for all $i$. Let $S_k = \sum_{i\leq k} X_i$ and $\Sigma_k = \sum_{i\leq k} \E[X_i^2|\calF_{i-1}]^2$. Then, 
$$
\Pr\left(\exists t\geq 0: \lambda_{\max}(S_t)\geq u\text{ and }\|\Sigma_t\|\leq \sigma^2\right)\leq d\exp\left\{-\frac{\sigma^2}{K^2}h\left(\frac{Ku}{\sigma^2}\right)\right\},
$$
where $h$ is as in [[bounded scalar concentration#Bennett's inequality]]. This was proved by [Tropp in 2011, Theorem 3.1](https://arxiv.org/abs/1101.3039). This a Freedman-style inequality. 


