---
lastmod: 2025-01-07
created: 2025-01-07
---

Extremely general, and well-subscribed to, framework for how to pick a good model in [[learning theory]]. Suppose we have some set of models $\calF$. Given training data, a natural way to choose a predictor $\wh{f}\in\calF$ is to minimize the empirical risk: 
$$
\hat{f} \in \argmin_{f\in\calF} \wh{R}_n(f), 
$$
where $\wh{R}_n(f)$ is the empirical risk (see [[statistical decision theory]]). 

You can prove bounds on the performance of ERM compared to the best classifier in $\calF$ via [[PAC learning]] or [[PAC-Bayes]] bounds, though the former is more common. Note that because $\wh{f}$ is data-driven, one apply usual [[concentration inequalities]] to argue about $|\wh{R}_n(f) - R(f)|$. One needs to use different machinery, such as eg [[uniform convergence bounds]]. 