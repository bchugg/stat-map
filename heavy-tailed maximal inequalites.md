---
lastmod: 2025-01-16
created: 2024-11-18
---

# Finite Variance
If $X_1,\dots,X_n$ are iid with $\E X^2\leq K$, then 
$$
\E \max_{1\leq i\leq n}|X_i| \leq B\sqrt{n}.
$$
There is also a partial converse: If $\E X^2 = \infty$, then 
$$
\E \max_{1\leq i\leq n} |X_i| \geq K n^{\frac{1}{2+\eps}},\quad \text{for all }\eps>0.
$$
I don't know where this result originally comes from, but it's not too hard to prove. 
## Kolmogorov's inequality 
If $X_1,\dots,X_n$ are independent and mean-zero, then 
$$
\Pr(\max_{1\leq k\leq n}|S_k|\geq u) \leq \frac{1}{u^2}\sum_{k\leq n} \E X_k^2,
$$
where $S_k = \sum_{i\leq k}X_i$. 