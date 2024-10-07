---
created: 2024-09-01
lastmod: 2024-10-07
---

Functions which capture "distances" between probability distributions. They may not be metrics in the formal sense ([[metric space]]) (eg perhaps they're not symmetric as in the [[KL divergence]]). 

Examples: 
- [[KL divergence]]
- [[Wasserstein distance]]
- [[KS distance]]
- [[total variation distance]]
- [[Hellinger distance]]
- [[chi-squared divergence]]
- [[f-divergence]] (encapsulates several of the above)
- [[Fisher information distance]]

# Some definitions

Different authors have different notation: Some write distances as functions of the distributions themselves, eg $\rho(P_1,P_2)$, and some write them as functions of random variables, $\rho(X_1,X_2)$. 

A metric $\rho$ is _regular_ if $\rho(X + Z, Y + Z)\leq \rho(X,Y)$ for any $Z$ independent of $X$ and $Y$. This captures the notion that blurring observations by independent noise makes them harder to distinguish, i.e., decreases the distance between them. 

Regularity is equivalent to _sub-additivity_: 
$$
\rho(X_1 + X_2, Y_1+ Y_2)\leq \rho(X_1,Y_1) + \rho(X_2,Y_2),\quad \text{for } X_1\perp X_2, Y_1\perp Y_2.
$$
A metric is _homogeneous of order_ $s$ if 
$$
\rho(cX,cY) = |c|^s \rho(X,Y)\quad \text{for all }c\in\Re.
$$
_[[ideal metrics|Ideal metrics]] of order_ $s$ are simultaneously regular and homogeneous of order $s$. These come up in the study of [[central limit theorems]] (see [[quantitative CLT template with ideal metrics]]). 