---
lastmod: 2025-01-07
created: 2025-01-05
---

"Probability approximately correct" [[learning theory]] was introduced by Leslie Valiant in 1984 ([A theory of the learnable](https://dl.acm.org/doi/pdf/10.1145/1968.1972)). While Valiant and early results in PAC learning were mostly focused on simple and finite model classes, the theory extends to more general settings. 

Let $\calF$ be a class of functions from a covariate space $\calX$ to some label space $\calY\subset \Re$. We witness from data drawn from a distribution $P$ over $\calX$ and chosen some $\wh{f}\in\calF$ as our model (perhaps via [[empirical risk minimization]], or perhaps some other way). The question is, how well does $\wh{f}$ generalize? 

To answer this question, Valiant proposed that we look for bounds of the form: For all $\delta\in(0,1)$, there exists some $\eps>0$ such that 
$$
\Pr(|R_n(\wh{f}) - R(f)| > \eps) \leq \delta.
$$
Thus, the algorithm is _probably_ (with high probability, $1-\delta$), approximately (off by at most $\eps$) correct (true risk matches empirical risk). 

PAC bounds are often proved using [[uniform convergence bounds]] (though not always, see eg[here](https://arxiv.org/pdf/2304.09167)). This results in bounds that depend on the complexity of $\calF$ in some way, such as [[Vapnik-Chervonenkis theory|VC dimension]] or [[covering and packing]] numbers. 

An alternative way to think about generalization bounds are [[PAC-Bayes]] bounds. 