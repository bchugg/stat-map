---
created: 2024-08-29
lastmod: 2024-09-02
---
Sufficient statistics attempt to capture precisely what is important about a distribution. It is statistic of the data which, informally, we should be able to use instead of the data itself to do our analysis. 

For a more concrete example of how knowing a sufficient statistic suffices in downstream analysis see [[sufficiency and the likelihood]]. 

> [!Definition]
> Formally, given a model $\{P_\theta\}$, we say $T$ is a sufficient statistic for $\theta$ if after conditioning on $T$, the distribution non longer depends on $\theta$: $p_\theta(x|T(X))$ is independent of $\theta$.  

An alternative definition is that the [[information processing inequality]] is an equality: $I(\theta;T(X)) = I(\theta;X)$. This is intuitive: knowing $T(X)$ tells you everything you need to know. 

Many statistics can be sufficient; for a stricter definition see [[minimal sufficiency]]. 

The [[Rao-Blackwell theorem]] says that an estimator can be improved by conditioning on a sufficient statistic. 

In the discrete case, we can view the sufficient statistic as partitioning the values of $p_\theta(x)$ into the values $p_\theta(x|t)$ for the possible values of the statistic $t$. If the elements of the resulting partition do not depend on $\theta$, then $T$ is a sufficient statistic. Eg: Draw $X_1,X_2,X_3\sim \Ber(\theta)$ and let $T = \sum X_i$. 

# Fisher-Neyman characterization

In general, though, we can appeal to the Neyman-Fisher characterization: 

**Thm:** $T$ is sufficient for $\theta$ iff the joint pdf of $X^n$ can be factored as $p_\theta(x^n) = h(x^n) g(T(x^n);\theta).$ That is, it can be factored into a product of a function of the data only (no parameter) and a function of $T$ and the parameter. 

# References 
- Larry Wasserman's notes on sufficient statistics in [_All of Statistics_](https://link.springer.com/book/10.1007/978-0-387-21736-9)
