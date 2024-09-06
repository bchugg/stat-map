---
created: 2024-09-05
lastmod: 2024-09-05
---
A nonparametric solution to [[two-sample testing]]. Let $\{X_1,\dots,X_n\}$ and $\{Y_1,\dots,Y_m\}$ be the two sets of observations we obtain, and let $T(X^n, Y^n)$ be any test statistic. 

The idea is simple: We recompute $T$ on permutations of the data. Under the null, $X^n \equald Y^n$, so each of these will be distributed the same. The probability that the original statistic, $T(X^n, Y^n$), is an outlier is thus very low. We therefore reject if $T(X^n, Y^n)$ is in the $(1-\alpha)$ quantile of the permuted statistics $T_1,\dots,T_K$. If $K$ is large, 

How do we choose $K$? Ideally, we'd compute all permutations, so $K = (n+m)!$. But this is infeasible, so typically we random sample some permutations and run the test only on those. 


A reasonable objection is that we have to choose the number of permutations in advance. Can we get around this? Yes, there is an [[anytime-valid]] version using ideas from [[game-theoretic hypothesis testing]]: [[permutation testing by betting]]. 