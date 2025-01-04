---
created: 2024-08-29
lastmod: 2025-01-04
---

#todo 
# Bounded distributions

## Bernstein bounds 
**Bounds in $\Re^d$**:  Let $X_1, \dots, X_n\in\Re^d$ obey $\norm{X_t}\leq c_t$ and $\E[\norm{X_t}^2]\leq v_t^2$. Let $V_n = \sum_{i\leq n}v_i^2$. Using the martingale-variance inequality [[martingale concentration#Variance bound|martingale concentration:Variance bound]], we obtain 
$$
\Pr( \norm{S_n} \geq \sqrt{V_n} + \eps) \geq \exp\left(\frac{-\eps^2}{4V_n}\right),
$$
for $\eps \leq V / \max_t c_t$. A bound of this form was first given by David Gross [here](https://arxiv.org/pdf/0910.1879). 

Note that a weaker form of this bound can be obtained by appealing to the Azuma-Hoeffding inequality ([[martingale concentration#Azuma-Hoeffding inequality|martingale concentration:Azuma-Hoeffding inequality]]). The difference is equivalent to the difference between the Hoeffding bound and the Bernstein/Bennett bound in the scalar case (see [[bounded scalar concentration]]).   

**Bounds in more general spaces**: There are dimension-free Bernstein bounds that hold in [[Banach space|Banach spaces]]: see [[concentration in Banach spaces]]. There are also dimension-free _empirical_ Bernstein bounds, see [[empirical Bernstein bounds]]. 

# Sub-Gaussian distributions 

**Sub-Gaussian coordinates**: If $X_1,\dots,X_n$ are independent and sub-Gaussian with $\E X_i^2=1$, then the norm $\| X \| = \| (X_1,\dots,X_n)\|$ is concentrated around $\sqrt{n}$. In particular, for some $c>0$, 
$$
\Pr( |\| X\|_2 - \sqrt{n}| \geq u) \leq 2\exp(-cu^2 / K^4),
$$
where $K = \max_i \| X_i\|_{\psi_2}$ is the maximum sub-Gaussian [[Orlicz norm]]. 

**Sub-Gaussian random vectors** 

