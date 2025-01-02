---
lastmod: 2025-01-01
created: 2024-10-13
---

Just as we can [[testing forecasters by betting|test forecasters]], we can also compare two different forecasters who are making predictions over time. The setup follows that of [[game-theoretic hypothesis testing]]. 

Let $S:\Delta(\calX)\times [0,1] \to \Re$ be a [[proper scoring rule]]. Suppose forecaster 1 makes forecasts $p_t\in \Delta(\calX)$ at time $t$, and forecaster 2 makes forecasts $q_t \in \Delta(\calX)$ at time $t$. Define 
$$
\wh{\Delta}_t = \frac{1}{t}\sum_{i\leq t} (S(p_i,o_i) - S(q_i,o_i)),
$$
which is the empirical difference between the forecasters performance, where $o_i$ is the outcome of the $i$-th forecast. We want to quantity the difference between $\wh{\Delta}_t$ and $\Delta_t$, the true expected difference between the forecasters: 
$$
\Delta_t = \frac{1}{t}\sum_{i\leq t} \E_{o_i \sim D_i} [ S(p_i,o_i) - S(q_i,o_i)|\calF_{i-1}],
$$
where $(\calF_t)$ is the filtration capturing what's happened so far. Depending on the behavior of $S$ (eg if it's bounded, light-tailed etc) we can develop [[confidence sequences]] for the difference $|\wh{\Delta}_t - \Delta_t|$ or perform [[sequential hypothesis testing]] to determine if $\Delta_t \equiv 0$ (say). Depending on the behavior of $S$, we can form [[sub-psi process]] for $t(\Delta_t - \wh{\Delta}_t)$, which lets apply much of the machinery of [[safe, anytime-valid inference (SAVI)]] to this problem. 

## Refs 
- [Comparing sequential forecasters](https://arxiv.org/pdf/2110.00115), Choe and Ramdas. 