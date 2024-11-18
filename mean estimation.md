---
lastmod: 2024-11-17
created: 2024-11-17
---

Possibly the most common problem in statistics: How do we estimate the mean of a distribution given samples? 

## Light-tailed settings 
A common approach is to invert [[concentration inequalities]] for the sample mean, see eg [[bounded scalar concentration]] and [[light-tailed, unbounded scalar concentration]]. In light-tailed settings, concentration is often synonymous with studying mean estimation, since the sample mean is a good estimator of the mean, and we are usually interested in concentration about the mean. 

A separate approach is one based on [[hypothesis testing]] and [[game-theoretic statistics]]. See [[estimating means by betting]]. These are tighter than CIs based on Hoeffding and Bernstein inequalities. They are not in closed-form however, and require computational methods to estimate. 

## Heavy-tailed settings 
The sample mean fails to be a good estimator in heavy-tailed settings (see [Catoni's 2012 paper](http://www.numdam.org/item/10.1214/11-AIHP454.pdf)) so one uses other estimators. For specific discussions of mean estimation in heavy-tailed settings, see [[scalar heavy-tailed mean estimation]] and [[multivariate heavy-tailed mean estimation]]. 