---
created: 2024-08-29
lastmod: 2025-01-11
---

[[density estimation|Density estimation]] in a parametric class of models. That, is we observe $X_1,\dots,X_n\sim P_\theta$ for some $\theta\in \Theta$, where $\Theta$ is finite dimensional. We want to [[statistical inference|infer]] $\theta$; either with a point estimate or a distribution. There are various approaches. 

The most common and straightforward is obviously the [[MLE]]; find the parameters $\theta$ that maximize the likelihood or log-likelihood. This is a [[frequentist statistics|frequentist approach]]. One can also use regularized MLE, in which we add some penalty to avoid overfitting. 

Another frequentist approach is the [[method of moments for estimation]]. This is simpler to compute than the MLE, but typically less efficient. But it's seen success in estimating mixtures of Gaussians, eg 
- [Optimal estimation of Gaussian mixtures via denoised method of moments](https://projecteuclid.org/journals/annals-of-statistics/volume-48/issue-4/Optimal-estimation-of-Gaussian-mixtures-via-denoised-method-of-moments/10.1214/19-AOS1873.full), by Wu and Yang. 

A final frequentist approach is [[deep density estimation]]. Many might consider this a solution to [[nonparametric density estimation]] but I think that's wrong; we choose the parameters of the network first, which gives rise to possible functions $f_\theta$, $\theta\in\Theta$ where $\theta$ represents a particular set of weights in the given architecture. The set of all weight configurations $\Theta$ is parametric (it's big, but not infinite).  

There is also a natural [[Bayesian statistics|Bayesian approach]], which is to place a prior $\pi$ over $\Theta$, and then compute the posterior $p(\theta|X)$. If we want a point estimate $\wh{\theta}$, we can compute it as some function of the posterior. Eg it's natural to take the expected value: $\wh{\theta} = \int \theta p(\theta|x)\d \theta$. As usual, the Bayesian approach allows for very natural [[uncertainty quantification]], since we have a distribution over the parameter space. 

Unlike [[nonparametric density estimation]], we must specify the parametric family of densities to use, which is of course challenging. Once we have an answer, we might consider running a [[goodness-of-fit test]] to see how well our model actually fits the data, or whether we need to consider a different class of functions. 

