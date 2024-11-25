---
lastmod: 2024-11-15
created: 2024-11-13
---

When constructing [[confidence sequences]] using either the [[confidence sequences via conjugate mixtures|method of mixtures]] or [[confidence sequences via predictable plug-ins|predictable plug-ins]], one often ends up with rates on the order of $\sqrt{\log(t)/t}$. While this is clearly shrinking to zero at $t\to\infty$, it's worth asking if it's shrinking to zero at an optimal rate. If the problem satisfies a LIL ([[laws of the iterated logarithm]]), then the optimal rate is $\sqrt{\log\log(t)/t}$. 

Obtaining bounds that shrink at this rate can be done via _stitching_ (see [time-uniform, nonparametric, nonasymptotic confidence sequences](https://arxiv.org/pdf/1810.08240)).  This involves deploying distinct bounds over different epochs, and then taking a union bound to ensure time-uniform coverage. Eg, one might consider the epochs $[2^j, 2^{j+1})$, and deploy an estimator $\wh{\mu}_t(j)$ with the guarantee 
$$
\Pr(\exists t\in [2^j, 2^{j+1}): | \wh{\mu}_t(j) - \theta^* | \geq B(t,j))\leq \delta_j,
$$
where $\theta^*$ is some parameter of interest. If $\sum_j \delta_j\leq \delta$, then we can get [[time-uniform]] coverage with probability $1-\delta$ for all $t\geq 1$ via a union bound. The goal is then to show that $B(t,j)$ shrinks at the desired logarithm rate. There are many examples of this, e.g. [here](https://arxiv.org/pdf/2010.09686), [here](https://arxiv.org/pdf/2311.08168), [here](https://arxiv.org/pdf/2202.01250), and [here](https://arxiv.org/abs/2302.03421). 

[Duchi and Haque](https://proceedings.mlr.press/v247/duchi24a/duchi24a.pdf) applied stitching to non-time-uniform estimator and still achieve iterated logarithm rates. In other words, they give a general reduction from fixed-time bounds to time-uniform bounds at the loss of only an iterated logarithm rate. In particular, they show that if for all $n\geq 1$, there exists a fixed-time estimator $\widehat{\theta}_n$ of $\theta^*$ such that 
$$
  \Pr(\| \widehat{\theta}_n - \mu\|\leq  F(\log(1/\delta), n))\geq 1-\delta,  
$$
for some function $F:\Re_{\geq 0}\times \mathbb{N}\to \Re_{\geq 0}$, then the estimator $\widetilde{\theta}_n = \widehat{\theta}_{g(n)}$ where $g(n) = \lfloor \log_2(n)\rfloor$ satisfies 
$$
  \Pr(\forall n\geq 1: \| \widetilde{\theta}_n - \mu\| \leq F(2\log\log(n) + \log(1/\delta) + 1/2, n/2))\geq 1-\delta.  
$$
That is, by updating the estimator only once every $2^k$ timesteps for $k\in\mathbb{N}$, we can transform any fixed-time estimator into a time-uniform estimator at an iterated logarithm cost. 

While an elegant theoretical construction, it is somewhat dissatisfying for practical purposes as we only update the estimator every $2^j$ timesteps. If data collection stops at some time $n$ for $2^j<n<2^{j+1}$, then we must discard observations (indeed, possibly as many as $n/2-1$ observations). This is unlike the examples above, which use time-uniform estimates within each epoch, which allow the estimator to be updated after observation is received. 