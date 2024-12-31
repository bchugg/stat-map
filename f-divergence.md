---
created: 2024-09-02
lastmod: 2024-12-31
---

A broad class of [[distributional distance|distributional distances]]. For a convex function $f$ with $f(1)=0$ and two probability measures $\rho,\nu$ defined on a measurable space $(\Omega,\calF)$, set 
$$
D_f(\rho\|\nu) = \E_\nu \left[f\left(\frac{\d\rho}{\d\nu}(X)\right)\right] = \int_\Omega f\left(\frac{\d\rho}{\d\nu}(x)\right ) \nu(\d x).
$$
With different choices of $f$ we can obtain 
- [[total variation distance]] 
- [[KL divergence]]
- [[Hellinger distance]]
- [[chi-squared divergence]]

f-divergences are mostly a distinct class of divergence than [[integral probability metric|IPMs]], intersecting only that the TV distance. Taking 
$$
f(u) = \frac{u^\alpha - 1}{\alpha(\alpha-1)},
$$
results in the [[alpha-divergence]]. There is a lots of literature on [[fixed-time]] plug-in estimators for $f$-divergences. In the sequential setting, because $f$-divergences are convex by construction they can estimated using reverse [[submartingale|submartingales]]; see [[confidence sequences for convex functionals]]. 

$f$-divergences admit the following variational inequality: For all measurable $h:\Theta\to\Re$ and all distributions $\rho,\nu$ over $\Theta$,  
$$
D_f(\rho\|\nu) \geq \E_\rho h(\theta) - \E_\nu f^*(h(\theta)),
$$
where $f^*$ is the convex conjugate of $f$: $f^*(y) = \sup_{x\in\Re} \{ xy - f(x)\}$. Equality holds for any $h$ in the subdifferential $\partial f(\d\rho/\d\nu)$. For the [[KL divergence]], the [[KL divergence#Donsker-Varadhan variational formula]] strengthens this variational inequality. 