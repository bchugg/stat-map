---
lastmod: 2025-01-08
created: 2024-11-10
---

Unlike light-tailed settings ([[light-tailed, unbounded scalar concentration]] and [[bounded scalar concentration]]) the sample mean is not well-behaved in heavy-tailed settings. Since heavy-tailed distributions may not have finite MGFs, the [[Chernoff method]] is not applicable. [Catoni gives an example](https://arxiv.org/abs/1009.2048) demonstrating the bound achieved via Markov's inequality ([[basic inequalities]]), i.e., 
$$
\Pr\left(|\overline{X}_n - \mu|) \geq \frac{\sigma}{\sqrt{ n\delta}}\right) \leq \delta,
$$
is essentially tight (where we receive observations $X_1,\dots,X_n$ and $\overline{X}_n$ is the sample mean). The issue is that outliers can have devastating effects on the sample mean, and heavy-tailed distributions can have many extreme observations. See [this discussion by Lugosi and Mendelson](https://arxiv.org/pdf/1907.11391) for more details, or [Sub-Gaussian mean estimators](https://econ.upf.edu/~lugosi/subgaussian.pdf) by Devroye et al. 

Ideally we want estimators with sub-Gaussian like behavior, i.e., 
$$
\Pr\left(|\widehat{\mu} - \mu| \gtrsim \sigma \sqrt{\frac{\log(1/\delta)}{n}}\right) \leq \delta.
$$
This is an exponential improvement in the dependence on $1/\delta$. These are called sub-Gaussian estimators. 

There are several approaches to heavy-tailed mean estimation in scalar settings: 
- [[median-of-means]] 
- [[trimmed mean estimator]]
- [[Catoni-Giulini M-estimator]]
