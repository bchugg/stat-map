---
lastmod: 2025-01-08
created: 2025-01-08
---

Method for [[heavy-tailed concentration]]. So far it has been applied only to [[scalar heavy-tailed mean estimation]], but one could imagine analyzing it in a multivariate setting as well. 

Since the empirical mean is ruined by outliers, a natural idea is to remove some fraction of the points and then compute the empirical mean on the remaining points. These are known as trimmed mean estimators. It's easy to define: Given a random sample $X_1,\dots,X_n$ and an integer $k<n/2$, define 
$$
\ov{X}_{n,k} = \frac{1}{n-2k}\sum_{i=k+1}^{n-k} X_{(i)},
$$
where $X_{(i)}$ are the order-statistics. 

Oliveira and Orenstein prove that if you remove $\gamma n$ of the largest and smallest points for $\gamma = \Theta(\log(1/\delta)/n)$, then the trimmed mean is sub-Gaussian. See [here](https://arxiv.org/pdf/1907.11391) for a discussion. 

[Oliveira et al (2025)](https://arxiv.org/pdf/2501.03694) perform a robust analysis of the trimmed mean, examining the tails of the estimator and showing they obey a [[central limit theorems|CLT]] under certain conditions. They also show the estimator is minimax-optimal up to constants under the [[adversarial contamination model]]. 

A related idea is proposed by [Lee and Valiant](https://arxiv.org/pdf/2011.08384) who don't remove entire points but instead weighted fractions of each observations: 
> At the highest level: in order to return a $\delta$-robust estimate of the mean, our estimator “throws out the $\frac{1}{3}\log(1/\delta)$ most extreme points in the samples”, and returns the mean of what remains. More specifically, outliers are thrown out in a weighted manner, where we throw out a fraction of each data point, with the fraction proportional to the square of its distance from a median-of-means initial guess for the mean, where the fraction is capped at 1, and the proportionality constant is chosen so that the total weight thrown out equals exactly $\frac{1}{3}\log(1/\delta)$. 

Their estimator achieves a bound of $\sigma ( 1 + o(1)) \sqrt{2\log(1/\delta)/n}$, where $\sigma^2$ is the variance of the observations.  


