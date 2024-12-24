---
lastmod: 2024-12-24
created: 2024-12-24
---

Let $\calH$ be a [[RKHS]] with [[Mercer kernel]] $K$. The MMD (maximum mean discrepancy) is the [[integral probability metric]] over the unit ball $\{f\in \calH: \|f\|_\calH \leq 1\}$. 

If the data come in pairs $(X_t,Y_t)$, the MMD has the following plug-in estimator 
$$
\text{MMD}(P_t,Q_t) = \sqrt{\frac{1}{t^2}\sum_{i,j}(K(X_i,X_j) + K(Y_i,Y_j) - 2K(X_i,Y_j))},
$$
which is a second-order [[v-statistics|v-statistic]]. Because the MMD is a convex [[distributional distance]], we can develop [[confidence sequences via reverse submartingales]] for it. The Kernel MMD also plays a big role in [[two-sample testing]]. 
