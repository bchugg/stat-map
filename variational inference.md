---
created: 2024-07-20
lastmod: 2025-03-12
---

A general approach to [[the problem of approximate inference in deep learning]] in [[Bayesian statistics]] It's faster, though typically less accurate, than [[MCMC]]. 

VI solves this via an optimization problem. We estimate $p(z|x)$ with 
$$
q^*(z) = \argmin_{q(z) \in\calQ } \kl(q(z)\| p(z|x)),
$$
where $\calQ$ is some tractable set of densities over $z$.  Of course, this objective is also intractable since it depends on $p(x)$, which is what is difficult to compute in the first place. Instead we define 
$$
\ell(q) := \E_{q(z)} \log p(z,x) - \E_{q(z)} \log q(z),
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
\log p(x) = \kl(q(z)\| p(z|x)) + \ell(q) \geq \ell(q),
$$
so $\ell(q)$ is a lower bound for the log-evidence. 

The ELBO can also be derived from the [[KL divergence#Donsker-Varadhan variational formula]]. Write 
$$
\log p(x) = \log \int p(x|z)p(z) \d z = \log \int \exp(h(z)) p(z) \d z,
$$
where $h(z) = \log p(x|z)$. The variational formula gives that, for all $q$, 
$$
\begin{align}
\log \int \exp h(z) p(z) \d z &\geq \int h(z) q(z) \d z - \kl(q(z)\|p(z)) \\
&= \int \log p(x|z) q(z) dz - \int \log (q(z)/p(z)) q(z) \d z \\ 
&= \int \log\left(\frac{p(x,z)}{q(z)}\right) q(z) \d z = \ell(q). 
\end{align}
$$





