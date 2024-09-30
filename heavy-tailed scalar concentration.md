---
created: 2024-08-29
lastmod: 2024-09-29
---

Unlike light-tailed settings, the sample mean is not well-behaved in heavy-tailed settings. Since heavy-tailed distributions may not have finite MGFs, the [[Chernoff method]] is not applicable. [Catoni gives an example](https://arxiv.org/abs/1009.2048) demonstrating the bound achieved via Markov's inequality ([[basic inequalities]]), i.e., 
$$
\Pr\left(|\overline{X}_n - \mu|) \geq \frac{\sigma}{\sqrt{ n\delta}}\right) \leq \delta,
$$
is essentially tight (where we receive observations $X_1,\dots,X_n$ and $\overline{X}_n$ is the sample mean). The issue is that outliers can have devastating effects on the sample mean, and heavy-tailed distributions can have many extreme observations. See [this discussion by Lugosi and Mendelson](https://arxiv.org/pdf/1907.11391) for more details, or [Sub-Gaussian mean estimators](https://econ.upf.edu/~lugosi/subgaussian.pdf) by Devroye et al. 

Ideally we want estimators with sub-Gaussian like behavior, i.e., 
$$
\Pr\left(|\widehat{\mu} - \mu| \gtrsim \sigma \sqrt{\frac{\log(1/\delta)}{n}}\right) \leq \delta.
$$
This is an exponential improvement in the dependence on $1/\delta$. These are called sub-Gaussian estimators. 
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

## Trimmed mean estimator 
Since the empirical mean is ruined by outliers, a natural idea is to remove some fraction of the points and then compute the empirical mean on the remaining points. These are known as trimmed mean estimators. 

Oliveira and Orenstein prove that if you remove $\gamma n$ of the largest and smallest points for $\gamma = \Theta(\log(1/\delta)/n)$, then the trimmed mean is sub-Gaussian. See [here](https://arxiv.org/pdf/1907.11391) for a discussion. 

A related idea is proposed by [Lee and Valiant](https://arxiv.org/pdf/2011.08384) who don't remove entire points but instead weighted fractions of each observations: 
> At the highest level: in order to return a $\delta$-robust estimate of the mean, our estimator “throws out the $\frac{1}{1}\log(1/\delta)$ most extreme points in the samples”, and returns the mean of what remains. More specifically, outliers are thrown out in a weighted manner, where we throw out a fraction of each data point, with the fraction proportional to the square of its distance from a median-of-means initial guess for the mean, where the fraction is capped at 1, and the proportionality constant is chosen so that the total weight thrown out equals exactly $\frac{1}{3}\log(1/\delta)$. 

Their estimator achieves a bound of $\sigma ( 1 + o(1)) \sqrt{2\log(1/\delta)/n}$. 

## Catoni-Giulini M-estimator
