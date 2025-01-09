---
lastmod: 2025-01-09
created: 2025-01-09
---

In 2018, [Catoni and Giulini proposed](https://arxiv.org/pdf/1802.04308) a simple estimator in $\Re^d$: Simply truncate the observations and take the empirical mean of the result. In particular, they consider 
$$
\wh{\mu} = \frac{1}{n} \sum_{i\leq n} \alpha(X_i)X_i,
$$
where 
$$
\alpha(X) := \frac{\min\{\lambda\norm{X}, 1\}}{\lambda\norm{X}} = \min\{1, (\lambda \norm{X})^{-1}\},
$$
for some $\lambda>0$. Estimators of this type are also called thresholding estimators. The Catoni-Giulini estimator. 

This has a rate of $O(\sqrt{v^2\log(1/\delta)/n})$ where $\E\norm{X-\mu}^2\leq v^2$. The rate is therefore not quite sub-Gaussian, but close. See the [discussion by Lugosi and Mendelson](https://arxiv.org/pdf/1906.04280) (Section 3.3) for a clear exposition about the precise rates of the Catoni-Giulini estimator. [We gave a sequential version of this estimator](https://arxiv.org/abs/2311.08168). The guarantees for the original Catoni-Giulini estimator rely on proofs using [[PAC-Bayes]]. [Blog post on this estimator is here](https://benchugg.com/research_notes/catoni_giulini/). See [[variational approach to concentration]] for a generalization of this proof technique to other estimators. 

As presented, the Catoni-Giulini truncation estimator requires a bound on the raw second moment $\E\norm{X}^2$. This is less desirable than a _central_ moment assumption, i.e., a bound on $\E\norm{X - \mu}^2$, since the latter is immune to translations of the data.  As noted by Lugosi and Mendelson, this translation invariance can be overcome by sample splitting: use some logarithmic number of points to construct a naive estimate $m$ of the mean, and then center the Catoni-Giulini estimator around $m$. 

This estimator was extended to [[Banach space|Banach spaces]] (see also [[concentration in Banach spaces]]) by [Whitehouse et al](https://arxiv.org/abs/2411.11271). They (we) also show that the estimator handles martingale dependence and is [[time-uniform]], and also can handle a central moment assumption (instead of the raw moment), and also handles infinite variance (requires only a central $p$-th moment for $p>1$). Interestingly, they don't use a [[PAC-Bayes]] analysis, but instead employ the [[Pinelis approach to concentration]]. 
