---
lastmod: 2024-10-07
created: 2024-10-07
---

An approach to [[heavy-tailed scalar concentration]] and [[multivariate heavy-tailed concentration]]. 

The overall idea is straightforward: Split the data into $k$ buckets and compute the sample mean $\widehat{\mu}_i$ of each bucket. Then the overall estimator is 
$$
\wh{\mu} = \text{Median}(\wh{\mu}_1,\dots,\wh{\mu}_k).
$$
There are several questions to answer to implement this in practice. First, how to choose $k$? Second (especially relevant in multivariate settings), how do we define the median?  

## Scalar case
With probability at least $3/4$ by Chebyshev, $\wh{\mu}_i$ is not too far from the true mean. So for the median to be far from the mean, many (at least half) independent Bernoulli events with probability 3/4 must fail to occur. 

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

## Finite-dimensional vector case
Defining the median in $\Re^d$ is slightly trickier. 

One option is the geometric median, which is studied by Minsker (see below). This achieves rate $\sqrt{\Tr(\Sigma)\log(1/\delta)/n}$, which is not quite sub-Gaussian. 

[Lugosi and Mendelson define a specialized version of the median](https://www.econ.upf.edu/~lugosi/mean.pdf) and get sub-Gaussian rates. [Blog post here](https://benchugg.com/research_notes/median-of-means-multivariate/). [Hopkins made this computationally tractable](https://arxiv.org/pdf/1809.07425) in 2020. 

Unlike the scalar setting, MoM in $\Re^d$ has not been extended to settings where the variance doesn't exist. 

## Infinite-dimensional case 
MoM with the geometric median was studied in [[Banach space|Banach spaces]] by Minsker and in Polish spaces by Yun and Park:  
![[concentration in Banach spaces#Heavy-tailed concentration]]