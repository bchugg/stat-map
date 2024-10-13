---
created: 2024-08-29
lastmod: 2024-09-02
---

> [!note] Definition
> Let $(\Theta,\rho)$ be a [[metric space]].  The entropy number of $\Theta$ with respect to $\rho$ is
> $$
> e_n(\Theta) \equiv e_n(\Theta, \rho) := \inf_{\Theta_n}\sup_{\theta \in\Theta} \rho(\theta, \Theta_n),
> $$
where the infimum is taken over all subset $\Theta_n$ of $\Theta$ subject to a cardinality constraint $N_n$ (usually $N_n=2^{2^n}$ in the case of [[Dudley chaining]]). 

Entropy numbers show up when proving [[maximal inequalities]] via [[chaining]]-type arguments. [[Dudley's entropy bound]] can be expressed in terms of entropy numbers. 

They are related to covering numbers ([[covering and packing]]) via the formula
$$
e_n(\Theta) = \inf\{\eps>0: N(\Theta, \rho, \eps)\leq N_n\}.
$$
That is, they are the minimum width $\eps$ required to cover $\Theta$ in balls of width $\eps$. Entropy numbers are equivalent to the [[metric entropy]] of $\Theta$ in the sense that
$$
\sum_{n\geq 0} 2^{n/2}e_n(\Theta) \asymp \int_0^\infty \sqrt{\log N(\Theta; \rho ,\eps)}\d\eps,
$$
which is what yields the equivalence between the two forms of [[Dudley's entropy bound]].


