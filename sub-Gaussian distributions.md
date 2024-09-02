---
created: 2024-08-29
lastmod: 2024-09-02
---

Sub-Gaussian distributions are a large class of distributions used in a wide variety of applications. Intuitively, they behave "like or better than" Gaussian distributions, meaning their tails decay at the same rate or faster than Gaussian tails. Consequently, sub-Gaussian random variables are nice to work with. 

Some facts about this class: 
- Sub-Gaussian distributions are a nonparametric class. There is no common dominating measure: it contains both discrete and continuous random variables. 
- If told $X$ is $\sigma$-sub-Gaussian (see below), can't estimate $\sigma$ from data. (Similar to how one can't estimate the bounds for a bounded random variable). 
- There is no [[test-martingale]] for this class 
- They specify an [[e-value]]. 

# Scalar case

There are several equivalent ways to define them. The easiest way is to place a specific bound on the MGF. A real-valued random variable $X$ with mean $\mu$ is $\sigma$-sub-Gaussian if, for all $\lambda\in\Re$, 
$$

\E \exp(\lambda (X-\mu)) \leq \exp(\lambda^2\sigma^2/2).

$$
Equivalent definitions are: 
- The [[Orlicz norm]] $\norm{X}_{\psi_2} = \inf\{u>0 \ \E\exp(|X|^2/u^2)\leq 2\}$ is finite. 
- $X^2$ has as [[sub-exponential distributions|sub-exponential distribution]]. 
- $\Pr(|X|\geq t)\leq 2\exp(-t^2/K^2)$ for some $K$. (Note the $t^2$ which makes it have Gaussian-like behavior, whereas [[sub-exponential distributions]] are linear in $t$).

An [[e-value]] for $\sigma$-sub-Gaussian distributions is $\exp\{\lambda (X-\mu)- \lambda^2\sigma^2/2\}$ which follows immediately from the definition above. The product of such e-values naturally gives a nonnegative [[supermartingale]] which gives rise to [[confidence sequences]] for sub-Gaussian random variables.  

# Multivariate case 

If $X$ is a random vector, we say it is $\Sigma$-sub-Gaussian for some PSD $\Sigma$ if
$$
\E\exp(\lambda\la \nu, X-\mu\ra) \leq \exp\left(\frac{\lambda^2}{2}\la \nu, \Sigma\nu\ra\right),
$$
for all $\nu\in\dsphere$. In the isotropic case (see [[isotropic distributions]]), we have $\Sigma = \sigma^2 I$ for some $\sigma$, and the condition above becomes
$$

\E\exp(\lambda\la \nu, X-\mu\ra) \leq \exp\left(\frac{\lambda^2\sigma^2}{2}\right),

$$
which is perhaps the more common definition in the literature. But if we want to allow for anisotropy (see [[anisotropic distribution]]) then the first definition is preferred. 

Note that this definition extends easily to infinite dimensional spaces as long as they are endowed with an inner product. Eg, in an infinite-dimensional [[Hilbert space]], $\Sigma$ is interpreted as an operator $\Sigma:\calH \to \calH$, and we work with the dot product $\la \cdot, \cdot\ra_\calH$. 



# References 
- Nice expository note: https://www.stat.cmu.edu/~arinaldo/36788/subgaussians.pdf
