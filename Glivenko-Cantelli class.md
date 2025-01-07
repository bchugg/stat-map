---
lastmod: 2025-01-07
created: 2024-09-24
---

In [[empirical process theory]], a Glivenko-Cantelli class $\calF$ whose associated empirical process satisfies an [[laws of large numbers|LLN]]. That is, if 
$$
\Delta_n(\calF) \to 0, \quad \text{for }\quad \Delta_n(\calF) = \sup_{f\in\calF}\left|\frac{1}{n}\sum_{i\leq n}f(X_i) - \E f(X)\right|,
$$
where the converge is either in probability or almost surely. Under various regularity conditions, $\calF$ is a GC class iff it is a [[Vapnik-Chervonenkis theory|VC class]] (meaning it has finite VC dimension). 

The most famous of example of a GC class is the class of indicator functions $\calF=\{f(x) = \ind(-\infty, x): x\in\Re\}$. This gives that the uniform convergence of the cdf (see [[cdf concentration]]). 

If $\calF$ is sufficiently rich it can fail to be a GC class. Suppose that $X_1,\dots,X_n\sim P$ where $P$ is a continuous distribution over $[0,1]$ and let $\calF$ be the indicators $\ind_A(\cdot)$ for all _finite_ subsets $A$ of $[0,1]$. Then $\E f(X)$ = $\E \ind_A(X) = P(A)=0$ for all such $A$ by continuity of $P$. Meanwhile, for the set $A = \{X_1,\dots,X_\}$ we have $\ind_A(X_i) = 0$ for all $i$, so $\Delta_n((\calF) = 1$. Hence $\calF$ is not GC. 