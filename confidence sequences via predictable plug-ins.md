---
lastmod: 2025-01-03
created: 2024-10-08
---

Suppose we have a [[sub-psi process]] or, more generally, a multiplicative [[e-process]] of the form $M_t = \prod_{i\leq t} f_i(\lambda, X_i)$ where $(X_i)$ is some process and $\lambda$ is a scalar. 

How does one choose $\lambda$? You might integrate over it (see [[confidence sequences via conjugate mixtures]]), or you might choose it differently at each timestep. That is, the process becomes $M_t = \prod_{i\leq t} f_i(\lambda_i,X_i)$ where $\lambda_i$ can be predictable. This is called the method of predictable plug-ins. 

If we're building a [[confidence sequences|confidence sequence]] from $M_t$ (eg perhaps $f_i$ has the form $f_i(\lambda, X) = \exp\{ \lambda (X- \E X) - \psi(\lambda)\}$), or see [[estimating means by betting]]), then choosing a different $\lambda$ every time step allows the width of the sequence to shrink to zero over time, whereas this will not be the case for constant $\lambda$. 

Using predictable plug-ins is practically very convenient, but (usually) won't lead to optimal rates [[laws of the iterated logarithm]] rates. For that, one needs [[stitching for LIL rates]]. 

