---
created: 2024-08-30
lastmod: 2024-11-10
---

For a random variable $X$ taking values in some normed space $(\calX, \|\cdot\|)$, concentration is the search for decreasing functions $f(u)$ such that 
$$
P(\|X - Z \| \geq u)\leq f(u),
$$
where $Z\in\calX$ is some point of interest (often $Z = \E X$).  This page is a high-level pointer to more specific concentration inequalities in various settings. For specific results, see: 

- [[bounded scalar concentration]]
- [[light-tailed, unbounded scalar concentration]]
- [[heavy-tailed concentration]]
- [[martingale concentration]]
- [[multivariate concentration]]
- [[cdf concentration]]
- [[concentration in Banach spaces]]
- [[matrix inequalities]]
- [[concentration of functions]]

For notes related to techniques to achieve concentration, see:
- [[techniques for multivariate concentration]]
- [[exponential inequalities]], which typically underlie the proofs of many concentration inequalities, and
- [[basic inequalities]], which contains the building blocks for many concentration results (eg Markov's inequality and the [[Chernoff method]]).

A few other things: 
- [[anti-concentration|Anti-concentration]] inequalities, which are exactly what they sound like. 
- A 1998 result of Montgomery-Smith and Pruss which allows one to go [[from independence to iid]] in general [[Banach space|Banach spaces]]. 
- In light-tailed settings, concentration is often synonymous with studying mean estimation, since the sample mean is a good estimator of the mean, and we are usually interested in concentration about the mean. However, the sample mean fails to be a good estimator in heavy-tailed settings, so one uses other estimators. For specific discussions of mean estimation in heavy-tailed settings, see [[scalar heavy-tailed mean estimation]] and [[multivariate heavy-tailed mean estimation]]. 