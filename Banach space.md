---
created: 2024-08-29
lastmod: 2024-10-20
---

A Banach space $(B,\|\cdot\|)$ is a complete normed vector space. That is, it's a vector space equipped with a norm $\|\cdot\|$ which induces a distance function in the obvious way. Completeness means every Cauchy sequence converges to some point in the space. 

A major obstacle to working in Banach spaces is that an inner product does not necessarily exist.  

In statistics, we usually assume the space is _separable_, meaning that it admits a countable dense subset. This makes sure that probability measures, Borel $\sigma$-algebras, and empirical means are well-defined. If a Banach space is not separable, then distributions on the space can behave in pathological ways. One can often circumvent the non-separability of a particular space with various tricks, but theorists often prefer to just assume separability to keep gross details at bay. 

We also often place a smoothness assumption on the space. Without such a smoothness assumption, roughly speaking, values that are close to each other in the space may behave so differently that [[statistical inference]] becomes impossible. 

A Banach space $(B,\|\cdot\|)$ is $(2,\beta)$ smooth if 
$$
\norm{x + y}^2 + \norm{x-y}^2 \leq 2\|x\|^2 + 2\beta^2\norm{y}^2,\quad \forall x,y\in B.
$$
An [equivalent condition](https://arxiv.org/pdf/1808.03204) is that the Banach space $(B,\norm{\cdot})$ is $\beta$-smooth, where we say the space is $\beta$-smooth if the squared norm $\norm{\cdot}^2$ is $\beta$-smooth with respect to $\norm{\cdot}$, where we say that a function $f:B\to\Re$ is $\beta$-smooth with respect to $\norm{\cdot}$ if for any $x,y\in B$, 
$$
f(y) \leq f(x) + D_x f(x)(y-x) + \frac{\beta}{2}\norm{y-x}^2,
$$
where $D_x f(x)(y-x)$ is the Gateaux derivative of $f$ at $x$ in the direction $y-x$.  

Smooth, separable Banach spaces include any separable [[Hilbert space]] $(\beta=1)$ and [[Lp norm|Lp spaces]] ($\beta \leq p\wedge 2$). 

For statistical results in Banach spaces see [[concentration in Banach spaces]] and [[CLTs in Banach spaces]]. 

# Types and co-types 
A Banach space has Type 2 if there exists some $T>0$ such that 
$$
\E_\eps\norm{\sum_{i\leq n}\eps_i x_i} \leq T \sqrt{\sum_{i\leq n}\norm{x_i}^2}.
$$
where $\eps_i$ are Rademacher. Hilbert spaces are Banach spaces of type 2 with $T=1$, which is easy to see if you write the norm in terms of the inner product.  