---
lastmod: 2024-12-20
created: 2024-12-20
---

Suppose we have a latent variable model 
$$
p(x,z) = p(x|z)p(z),
$$
where $z$ are latent, and $x$ is the data. A core problem in [[Bayesian statistics]] is to compute the conditional distribution $p(z|x)$, i.e., to solve the problem: what are the hidden parameters given the data? 

Writing, 
$$
p(z|x) = \frac{p(x,z)}{p(x)} = p(x,z)\left(\int p(x,z)\d z\right)^{-1},
$$
we start to see the trouble. The integral on the rhs is usually intractable, since it involves integrating across all latent variables. So we typically approximate $p(z|x)$ in some way. This is the problem of approximate inference. Noet that $p(x)$ is usually called the "evidence". 

Common solutions to the problem include [[MCMC]] and [[variational inference]]. 
