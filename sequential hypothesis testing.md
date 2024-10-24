---
created: 2024-08-29
lastmod: 2024-10-24
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

