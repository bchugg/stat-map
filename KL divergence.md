---
created: 2023-03-02
lastmod: 2024-09-02
---
For probability measures $\rho,\nu$ on a measurable space $(\Omega,\calF)$, the KL-divergence is 
$$
\kl(\rho\|\nu) = \E_\rho \left[\log\left(\frac{\d\rho}{\d\nu}(X)\right)\right] = \int \log\left(\frac{\d\rho}{\d\nu}(x)\right)\rho(\d x),
$$
if $\rho\ll \nu$ and $\infty$ otherwise. 