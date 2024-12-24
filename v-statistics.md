---
created: 2024-07-09
lastmod: 2024-12-23
---

Suppose we are estimating the symmetric statistic $S = S(X_1,\dots,X_k)$ where $\E S = \theta$.  Given data $X_1,\dots,X_n$ the plug-in estimator 
$$
V_n(S) = \frac{1}{n^k} \sum_\beta S(X_\beta),
$$
is the v-statistic for $S$, where $\beta$ is a permutation $X_{i_1}, \dots,X_{i_k}$. V-statistics are named after von-Mises, having been [introduced by him in 1947](https://projecteuclid.org/journals/annals-of-mathematical-statistics/volume-18/issue-3/On-the-Asymptotic-Distribution-of-Differentiable-Statistical-Functions/10.1214/aoms/1177730385.full). They are not unbiased. Indeed even for $k=2$ we have 
$$
V_n(S) = \frac{1}{n^2}\sum_{i\neq j} S(X_i,X_j) + \frac{1}{n^2}\sum_i S(X_i,X_i),
$$
so $\E V_n(S) = \frac{n-1}{n} \theta + \frac{1}{n} \E S(X,X)$. As $n\to\infty$ this approaches $\theta$ but is biased for any finite $n$, unlike [[u-statistics]]. 