---
created: 2023-03-02
lastmod: 2025-03-12
---

For probability measures $\rho,\nu$ on a measurable space $(\Omega,\calF)$, the KL-divergence is 
$$
\kl(\rho\|\nu) = \E_\rho \left[\log\left(\frac{\d\rho}{\d\nu}(X)\right)\right] = \int \log\left(\frac{\d\rho}{\d\nu}(x)\right)\rho(\d x),
$$
if $\rho\ll \nu$ and $\infty$ otherwise. The KL-divergence is an [[f-divergence]] resulting from $f(x) = x\log x$. 

## Donsker-Varadhan variational formula 
Let $h:\Theta\to\Re$ be measurable and $\nu$ be a distribution over $\Theta$, then 
$$
\log \E_\nu \exp h(\theta) = \sup_{\rho} \left\{ \E_\rho h(\theta) - \kl(\rho\|\nu)\right\}.
$$
This strengthens the general variational inequality for f-divergences. This is a crucial ingredient in [[PAC-Bayes]] bounds, which are typically stated in terms of the KL-divergence. This formula also underlies the [[variational approach to concentration]]. The supremum is achieved by $\d\rho \propto \exp (h(\theta)) \d\mu$, which is the Gibbs measure. 