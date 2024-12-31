---
created: 2024-07-09
lastmod: 2024-12-24
---

We are estimating the symmetric statistic $S = S(X_1,\dots,X_k$) with mean $\theta = \E S$. Given data $X_1,\dots,X_n$, $n\geq k$, the u-statistic for $S$ is 
$$
 
U_n(S) = {n\choose k}^{-1} \sum_{1\leq i_1<\dots< i_k\leq n} S(X_{i_1},\dots,X_{i_k}).
$$
Unlike [[v-statistics]], u-statistics are unbiased (hence the "u"). They were introduced by Hoeffing in 1948. Notice that unlike v-statistics, we are summing only over all ordered permutations. 

The sample mean and sample variance are both examples of u-statistics. 

U-statistics admit various decompositions which help reason about their asymptotic behavior. Eg the Hayek projection and the Hoeffding decomposition. 

U-statistics are reverse [[submartingale|submartingales]], so we can form [[confidence sequences]] for them ([[confidence sequences for convex functionals]]). Using similar machinery we can develop [[PAC-Bayes]] bounds for them. 