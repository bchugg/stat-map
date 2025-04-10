---
created: 2024-08-29
lastmod: 2024-09-02
---

False discovery rate control in [[multiple testing]]. We have hypothesis $H_1,\dots,H_K$. The true nulls are $N\subset[K]$. If $D\subset[K]$ are indices of discoveries (i.e., rejections) by some testing procedure, the number of false discoveries is $F_D = |D\cap N|$. The false discovery rate is $F_D/|D|$, which we want to be low. Since it's a random variable, we want to control $\E[F_D/|D|]$. 

This criteria was introduced by Benjamini and Hochberg in the most widely cited paper in statistics. They introduced a procedure for achieving FDR control in the same paper: the [[BH procedure]]. The [[e-BH procedure]] is a similar procedure but using [[e-value|e-values]] instead of [[p-value|p-values]], and can handle arbitrary dependence. 
