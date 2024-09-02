---
created: 2024-09-02
lastmod: 2024-09-02
---
A broad class of [[distributional distance|distributional distances]]. For a convex function $f$ with $f(1)=0$ and two probability measures $\rho,\nu$ defined on a measurable space $(\Omega,\calF)$, set 
$$
D_f(\rho\|\nu) = \E_\nu \left[f\left(\frac{\d\rho}{\d\nu}(X)\right)\right] = \int f\left(\frac{\d\rho}{\d\nu}(x)\right ) \nu(\d x).
$$
Common examples are: 
- [[total variation distance]] 
- [[KL divergence]]
- [[Hellinger distance]]
- [[chi-squared divergence]]

#todo variational inequality 