---
created: 2024-05-27
lastmod: 2025-01-09
---

As in [[heavy-tailed concentration]], the sample mean $\overline{X}_n$ is too easily influenced by outliers and does have good concentration properties. Also as in the scalar setting, the polynomial rate (in terms of the confidence level, $\delta$) given by Chebyshev's inequality is the best one can hope for when working with the sample mean. (See the discussion in [Hopkins](https://arxiv.org/pdf/1809.07425) or by [Catoni, section 6](http://www.numdam.org/item/10.1214/11-AIHP454.pdf)). 

What can we hope for in the multivariate setting? In $\Re^d$, the empirical mean of the Gaussian behaves as 
$$
\Pr\left(\wh{\mu} - \mu|\geq O\left(\sqrt{\frac{\Tr(\Sigma)}{n}} + \sqrt{\frac{\|\Sigma\| \log(1/\delta)}{n}}\right)\right)\leq \delta.
$$
This is called sub-Gaussian performance of an estimator, and is what we're trying to achieve even in heavy-tailed settings.  See the recent [survey by Lugosi and Mendelson](https://arxiv.org/pdf/1906.04280) for more. 

Approaches include: 
- [[median-of-means]] 
- [[truncation-based estimators|truncation-based estimators]]
- [[Catoni-Giulini M-estimator]]
