---
created: 2024-08-29
lastmod: 2024-09-02
---

A powerful approach for estimating the mean of bounded random variables pioneered by Waudby-Smith and Ramdas and inspired by [[game-theoretic statistics]]. Their results are currently tightest known [[confidence intervals]] and [[confidence sequences]] for bounded observations with constant conditional means. In fact, betting-style CIs and CSs are [nearly-optimal](https://arxiv.org/pdf/2310.01547).

The idea is to leverage the [[duality between hypothesis tests and CIs]]. In particular, imagine: 
- Betting on whether each value $m\in[0,1]$ is the mean.
- For values $m$ that aren't the mean, we will make money (using the core ideas in [[game-theoretic hypothesis testing]]). 
- Our confidence set at any time is the set of $m$ such that we haven't made sufficient money while betting against them. 

We can generate Hoeffding-like ([[light-tailed scalar concentration#Hoeffding bound|light-tailed scalar concentration:Hoeffding bound]]) CSs and [[empirical Bernstein bounds]] in this way, but the most powerful results come from consider payoff functions of the form
$$
M_t(m) = \prod_{i=1}^t (1 + \lambda_i(X_i-m)),
$$
which is a martingale if $(\lambda_t)$ is a predictable sequence and a nonnegative [[test-martingale]] if $\lambda_i \in [-1/(1-m), 1/m]$. If our bets $\lambda_i$ are chosen well, then this will grow large when $m$ is not the true mean of the $X_i$. When $m=\mu$ is the mean, then by [[Ville's inequality]] $M_t(\mu)$ is unlikely to ever get large. Formally, a $(1-\alpha)$-CS is achieved by taking 
$$
C_t = \{m\in[0,1]: M_t(m)<1/\alpha\}.
$$
How should we actually choose our bets? See [[betting strategies]].
