---
created: 2024-09-05
lastmod: 2024-12-31
---

A method using [[game-theoretic statistics]] to get around the pre-specification of the number of random permutations to test in the monte carlo version of the [[permutation test]]. 

Consider the [[conformal p-value]], 
$$
Q(Y) = \frac{1 + \sum_{i\leq n} \ind\{ Y_i \leq Y\}}{n+1},
$$
for observations $Y_1,\dots,Y_n$ and $Y$. Under the null, $Q(Y)$ is a [[p-value]]. The idea is to bet on the binary outcomes $B_i = \ind\{Y_i \leq Y\}$. We setup bets $S_t:\{0,1\}\to (0,\infty)$ similarly to [[testing forecasters by betting]] such that $K_t = \prod_{i\leq t } S_i(B_i)$ is an [[e-process]] under the null. If $K_t$ becomes large it indicates that $Y$ is stochastically larger than $Y_1,\dots,Y_n$. 

[Fischer and Ramdas](https://arxiv.org/abs/2401.07365) derive the log-optimal bet $S_i$ (see [[maximizing log-wealth]]) and give approximations for it. 