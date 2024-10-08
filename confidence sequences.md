---
created: 2024-08-29
lastmod: 2024-10-07
---

A confidence sequence can be thought of as a sequence of sequentially valid [[confidence intervals]]). Formally, $(C_t)_{t\geq 1}$ is a $(1-\alpha)$-CS for a parameter $\theta$ if
$$
\Pr(\exists t\geq 1: \theta \notin C_t) \leq \alpha.
$$
That is, a CS is a [[time-uniform]] confidence interval. It avoids the known problem with confidence intervals that, if they are computed at different times, they risk contradicting themselves (eg an interval computed at time $t_1$ might not overlap with one at time $t_2$. )

Like [[confidence intervals]], confidence sequences have frequentist guarantees ([[frequentist statistics]]), not Bayesian ones. Whether there exist anytime-valid [[credible intervals]] (the Bayesian notion of confidence interval) is an interesting question. 

Equivalent definitions are: 
- $\Pr(\theta^* \in C_\tau)\geq 1-\alpha$ for any stopping time $\tau$ 
- $\Pr(\theta^*\in C_T)\geq 1-\alpha$ for all random times $T$. A random time could be a function of a stopping time, for instance (eg $\tau/2$). 

These are not obviously equivalent definitions. They have to be proved. For instance, the same properties do not hold with expected values. See lemmas 2 and 3 [here](https://arxiv.org/pdf/2009.03167.pdf) and the [[anytime-valid]] notes. 

Confidence sequences are common tools in [[safe, anytime-valid inference (SAVI)]]. 

Many confidence sequences are construct from applying [[Ville's inequality]] to [[supermartingale|supermartingales]] or [[test-martingale|test-martingales]]]. It is known how to construct non-trivial confidence sequences for a variety of problems. A few include: 
- bounded, non-parametric mean estimation in $\Re$ ([[estimating means by betting]]) and in $\Re^d$ ([CSs via universal gambling strategies](https://arxiv.org/pdf/2207.12382)), and in Banach spaces (via [[empirical Bernstein bounds]]). 
- Mean estimation under light-tailed [[sub-psi process|sub-psi conditions]]: See [Howard et al.](https://arxiv.org/abs/1810.08240) 2021.  
- Mean estimation for heavy-tailed scalar observations (see discussion in [[Catoni-Giulini M-estimator]]) with possibly infinite variance. 
- [Estimating Gaussian means with unknown variance](https://arxiv.org/pdf/2310.03722)
- [Light and heavy-tailed (finite variance) mean estimation](https://arxiv.org/abs/2311.08168) in $\Re^d$, using the [[variational approach to concentration]].  
- [[confidence sequences for quantiles]]

There is also an extension of confidence sequences to the asymptotic regime: [[asymptotic confidence sequences]]. 

# Refs 
- [Time-uniform, nonparametric, nonasymptotic confidence sequences](https://arxiv.org/abs/1810.08240) by Howard et al.