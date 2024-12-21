---
created: 2024-07-20
lastmod: 2024-12-20
---

A general approach to [[the problem of approximate inference in deep learning]] in [[Bayesian statistics]] It's faster, though typically less accurate, than [[MCMC]]. 

VI solves this via an optimization problem. We estimate $p(z|x)$ with 
$$
q^*(z) = \argmin_{q(z) \in\calQ } \kl(q(z)\| p(z|x)),
$$
where $\calQ$ is some tractable set of densities over $z$.  Of course, this objective is also intractable since it depends on $p(x)$, which is what is difficult to compute in the first place. Instead we define 
$$
\ell(q) := \E \log p(z,x) - \E \log q(z),
$$
and write 
$$
\begin{align}
\kl(q(z)\|p(z | x)) &= \E[\log q(z)] − \E[\log p(z, x)] + \log p(x) \\ 
&= \log p(x) - \ell(q).
\end{align}
$$
So, minimizing the KL divergence is equivalent to maximizing $\ell$ up to a constant which doesn't depend on $z$. The objective $\ell$ is called the "evidence lower bound", or ELBO. This name comes from the fact that 
$$
\log p(x) = \kl(q(z)\| p(z|x)) + \ell(q) \geq \ell(q),$$
so $\ell(q)$ is a lower bound for the log-evidence. 




