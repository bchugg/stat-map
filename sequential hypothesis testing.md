---
created: 2024-08-29
lastmod: 2025-09-29
---

We observe data $X_1,X_2,\dots$ drawn from some distribution $R$, and want to test the hypotheses 
$$
H_0: (X_t) \sim P\in \calP \quad \text{vs}\quad H_1: (X_t)\sim Q\in \calQ,
$$
for some families of distributions $\calP$ and $\calQ$. 

There are different kinds of hypothesis tests we can consider in this setting. One is a "power-one" test, which is a test that continues to accept the null until there is sufficient evidence to reject it. This is characterized by a sequence of maps $(\phi_t)_{t\geq 1}$ where $\phi_t(X_1,\dots,X_t)\in\{0,1\}$ maps the first $t$ observations to an accept/reject decision. Once the test rejects we stop sampling. Philosophically, this is more aligned with Fisher's perspective ([[Fisher's paradigm]]) since we start by accepting the null and at each time step we're asking if we've accrued enough evidence to reject it. 

We can also consider sequential tests which can refrain from making any decision: At time $t$ they choose to either continue sampling data, or to accept/reject the null. See eg the [[sequential probability ratio test]]. This is perhaps more aligned with the [[Neyman-Pearson paradigm]], where we're trying to make a choice between two alternatives. 

Let $\tau$ be the time at which the test rejects the null (we may have $\tau=\infty$ if it never rejects). For some pre-specified $\alpha$, we want that type-I error is bounded by $\alpha$: 
$$
\sup_{P\in\calP}P(\tau < \infty)\leq \alpha,
$$
and that the test eventually rejects under the alternative: 
$$
\inf_{Q\in\calQ}Q(\tau <\infty) = 1.
$$
A general approach to sequential hypothesis testing is [[game-theoretic hypothesis testing]]. 

## Reading 
- [Stopping times of power-one sequential tests: Tight lower and upper bounds](https://arxiv.org/pdf/2504.19952) by Agrawal and Ramdas. 
- Waudby-Smith and others study log-optimality ([[maximizing log-wealth]]) in a general class of [[e-process]]. In particular they show that a process with sublinear regret is almost surely log-optimal. See https://arxiv.org/pdf/2504.02818 
- This [1994 paper](https://projecteuclid.org/journals/annals-of-statistics/volume-22/issue-1/A-Topological-Criterion-for-Hypothesis-Testing/10.1214/aos/1176325360.full) by Dembo and Peres considers a slightly different error metric than usual: they want a sequential test which makes only finitely many errors almost surely. What's the relationship between this and power? Doesn't seem entirely clear. 