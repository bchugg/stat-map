---
created: 2024-08-29
lastmod: 2024-09-02
---

In [[nonparametric regression]], a linear smoother is an estimate $\hat{m}(x)$ of $m(x) = \E[Y|X=x]$ such that 
$$
\wh{m}(x) = \sum_{i=1}^n \ell_i(x)Y_i = \ell(x)^T Y,
$$
for some functions $\ell_1(x),\dots,\ell_n(x)$. This is a very broad class of estimators. Indeed, [[partitions and trees]], [[kernel regression]], [[local polynomial regression]], and [[RKHS regression]] are all examples of linear smoothers. 

The fact that all of these methods are "linear", in the above sense, suggests the question of whether there are "non-linear" smoothers. The answer is yes, but they are less well-studied. See [[wavelets]]. 