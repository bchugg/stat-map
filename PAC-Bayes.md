---
created: 2024-08-29
lastmod: 2025-01-07
---

PAC-Bayes bounds were originally crafted as a method to prove guarantees in [[learning theory]] that didn't suffer from the same difficulties as [[PAC learning]]. However, they've become useful for proving more general [[concentration inequalities]], especially in multivariate settings. They are the cornerstone of the [[variational approach to concentration]]. 

Traditional PAC bounds are usually proven via [[uniform convergence bounds]], which result in bounds that depend on various notions of complexity such as the [[Vapnik-Chervonenkis theory|VC dimension]] of the class of learners. For sufficiently rich classes (such as neural nets) however, these complexities can be massive (or infinite), resulting in vacuous bounds. 

The PAC-Bayes approach is to discard the idea of a worst case analysis (which is the idea of uniform convergence), and instead take a [[Bayesian statistics|Bayesian]] perspective. We place a prior over the class of functions $\calF$ that we are trying to learn and develop a bound which depends not on the complexity of $\calF$, but instead some [[distributional distance|divergence]] (often the [[KL divergence]]) between our prior and any "posterior" over $\calF$. 

For instance, one of the earliest and most famous PAC-Bayes bounds comes from [Catoni in 2003](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=5446ba5ee753f3e5db962e8766695a1216e26193) (that guy did a lot of stuff). It says that for all $\lambda>0$ and priors $\nu$ over $\calF$, 
$$
\Pr\left(\forall \rho\in \calM(\calF): \E_{f\sim \rho} [R_n(f) - \wh{R}_n(f)] \geq \frac{\lambda}{8n} + \frac{\kl(\rho\|\nu) + \log(1/\delta)}{\lambda}\right) \leq \delta,
$$
where $\calM(\calF)$ is the set of distributions over $\calF$, $R_n(f) = \E [\ell(f, X)]$ is the risk, $\wh{R}_n(f) = \frac{1}{n}\sum_i \ell(f,X_i)$ is the empirical risk, and $\ell$ is some loss function (see [[statistical decision theory]]). So now instead of arguing about worst case loss, we're arguing about average loss. The bound is uniform over the distributions $\rho$, meaning it holds simultaneously for all of them. But if we pick $\rho$ that looks nothing like $\nu$, then $\kl(\rho\|\nu)$ will blow up. 

What good is a bound on $\E_\rho R_n(f)$ you may ask? Aren't we after a bound on $R_n(\wh{f})$ for some particular $\wh{f}$? Well yes, and sometimes this poses a problem. But sometimes it doesn't. Sometimes $\wh{f}$ is a randomized predictor, in which you really care about $\E \wh{f}$ anyway. But if not, then you need to perturb $\wh{f}$ a bit to induce a distribution over it (eg place Gaussians over the weights in a neural net). This sounds crazy but actually led to [non-vacuous bounds for neural nets](https://arxiv.org/pdf/1703.11008), which PAC bounds have not been able to do. 

So are they useful? As always, depends what you're trying to do. 

You can give a very general PAC-Bayes bound that is removed from learning theory altogether, but recovers known learning theory bounds. We gave this bound in a [2023 paper](https://arxiv.org/pdf/2302.03421). I'll call it the "master theorem" because I'm trying to add more gravitas to my life. 

## Master theorem 
Let $M_t(\theta)$ be a nonnegative [[supermartingale]] with initial value 1 for all $\theta\in\Theta$. Let $\nu$ be a data-free prior. Then, 
$$
\Pr(\forall t, \forall\rho\in\Mspace{\Theta}: \E_\rho \log M_t(\theta) \leq \kl(\rho\|\nu) + \log(1/\delta))\geq 1-\delta.
$$
This is the [[time-uniform]] version of the master theorem, but we can also state a master fixed-time version. This reads: Let $N(\theta)$ be nonnegative have expected value at most 1 (it is an [[e-value]]) for all $\theta\in\Theta$. Then 
$$
\Pr(\forall\rho\in\Mspace{\Theta}: \E_\rho \log N(\theta) \leq \kl(\rho\|\nu) + \log(1/\delta))\geq 1-\delta.
$$
## Refs 
- [User friendly introduction to PAC-Bayes bounds](https://arxiv.org/pdf/2110.11216), by Alquier. Extremely nice and simple overview. 
- [Primer on PAC-Bayesian learning](https://arxiv.org/abs/1901.05353) slightly more technical and general intro, by Guedj. 