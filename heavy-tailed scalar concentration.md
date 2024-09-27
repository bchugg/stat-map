---
created: 2024-08-29
lastmod: 2024-09-27
---

Unlike light-tailed settings, the sample mean is not well-behaved in heavy-tailed settings. Since heavy-tailed distributions may not have finite MGFs, the [[Chernoff method]] is not applicable. [Catoni gives an example](https://arxiv.org/abs/1009.2048) demonstrating the bound achieved via Markov's inequality ([[basic inequalities]]), i.e., 
$$
\Pr\left(|\overline{X}_n - \mu|) \geq \frac{\sigma}{\sqrt{ n\delta}}\right) \leq \delta,
$$
is essentially tight (where we receive observations $X_1,\dots,X_n$ and $\overline{X}_n$ is the sample mean). Ideally we want estimators with sub-Gaussian like behavior, i.e., 
$$
\Pr\left(|\widehat{\mu} - \mu| \gtrsim \sigma \sqrt{\frac{\log(1/\delta)}{n}}\right) \leq \delta.
$$
This is an exponential improvement in the dependence on $1/\delta$.
## Median-of-means (MoM)
The idea is simple: Split the data into $k$ buckets, and compute the sample mean $\widehat{\mu}_i$ of each bucket. With probability at least $3/4$ by Chebyshev, $\wh{\mu}_i$ is not too far from the true mean. So for the median to be far from the mean, many (at least half) independent Bernoulli events with probability 3/4 must fail to occur. 

If we choose $k = \lceil 8\log(1/\delta)\rceil$ then the median-of-means estimator $\wh{\mu}$ satisfies 
$$
\Pr\left(|\wh{\mu} - \mu| \geq \sigma \sqrt{\frac{32\log(1/\delta)}{n}}\right)\leq \delta.
$$
The MoM estimator can also be extended to situations where the distribution has no variance. If $\E|X - \mu|^{1+\eps} \leq v$, then 
$$
\Pr\left(|\wh{\mu} - \mu| \geq (12v)^{\frac{1}{1+\eps}} \left(\frac{8\log(1/\delta)}{n}\right)^{\frac{\eps}{1+\eps}}\right)\leq \delta.
$$
This was originally [proved by Bubeck, Cesa-Bianchi, and Lugosi](https://arxiv.org/abs/1209.1727) in the content of heavy-tailed bandits. I have a post with the proofs [here](https://benchugg.com/research_notes/median-of-means-univariate/). 

You can [[time-uniform|sequentialize]] the MoM estimator using the [[martingale concentration#Dubins-Savage inequality]]. I have a post about that [here](https://benchugg.com/research_notes/sequential-median-of-means/). 

## Catoni-Giulini M-estimator

