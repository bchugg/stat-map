---
created: 2024-08-29
lastmod: 2025-03-13
---

The [[Neyman-Pearson paradigm]] is formulated in terms of Type I and Type II errors. Suppose we are testing the null $H_0$ vs the alternative $H_1$ (see [[hypothesis testing]]). In particular, we focus on constructing hypothesis tests $\phi$ such that 
$$
\Pr_{H_0}(\phi(X^n)=1)\leq \alpha,
$$
for some pre-specified $\alpha$. Here $X^n = (X_1, \dots, X_n)$ are the observations. (Note the pre-specification is important; see [[issues with p-values]]. This motivates [[post-hoc hypothesis testing]]). Subject to this constraint we want to maximize the _power_ of the test, i.e., 
$$
\beta = \Pr_{H_1}(\phi(X^n)=1).
$$
Wald was the first (I think) to formulate NP in terms of decision-theory. Introduce a loss function $\ell$ with two parameters, $\ell(a,b)$, where $a\in\{0,1\}$ represents the null and alternative hypothesis, and $b\in\{0,1\}$ represents the action (accept or reject). Presumably one has $\ell(0,0) = \ell(1,1)=0$.  

We restate the type-I error guarantee as a _Type-I risk_ guarantee:
$$
\E_{H_0} [\ell(0,\phi(X^n))]\leq 1.
$$
Note that $\E_{H_0}[\ell(0,\phi(X^n))] = \Pr_{H_0}(\phi(X^n)=1) \ell(0,1)$ so in order to recapture the type-I error guarantee, we can take $\ell(0,1) = 1/\alpha$, in which case 
$$
\E_{H_0}\ell(0,\phi(X^n)) \leq 1 \Leftrightarrow \Pr_{H_0}(\phi(X^n)=1)\leq \alpha.
$$
To recover the notion of power, introduce type-II risk, which is $\E_{H_1}[\ell(1,\phi(X^n))].$ Write 
$$
\E_{H_1}[\ell(1,\phi(X^n))] = (1-\beta)\ell(0,1),
$$
which relates type-II risk to power. We want to minimize type-II risk.

Using losses allows us to generalize the NP paradigm beyond binary decisions (accept/reject) and to consider more general decision spaces. Eg we can consider $\ell(a,b)$ for $b\in \mathcal{B}$.  This enables [[post-hoc hypothesis testing]], as Grunwald studies. 

# Reading 
- [Contributions to the theory of statistical estimation and testing hypotheses](http://www.stat.yale.edu/~hz68/619/Wald-1939.pdf), Wald 1936. 
- [Beyond Neyman-Pearson](https://arxiv.org/pdf/2205.00901), Grunwald 2024. 