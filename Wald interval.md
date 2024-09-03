---
created: 2024-08-29
lastmod: 2024-09-03
---
The Wald interval is a nonasymptotic [[confidence intervals|confidence interval]] for the mean based on the [[central limit theorems|CLT]]:
$$
C_n = \left\{\overline{X}_n \pm z_{1-\alpha/2}\wh{\sigma}_n/\sqrt{n} \right\},
$$
where $\wh{\sigma}_n$ is the empirical variance. Its cousin in [[hypothesis testing]] is the [[Wald test]]. 

An error-bound on the Wald interval can be written in terms of the [[KS distance]]: 
$$
\Pr(\mu \notin C_n) \leq \alpha + 2\rho_\ks(n^{1/2}(\wh{\mu}_n - \mu)\|N(0,1)).
$$
