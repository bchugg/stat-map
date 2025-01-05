---
lastmod: 2025-01-05
created: 2024-09-24
---

Let $X_1,\dots,X_n$ be random samples with values in some space $\calX$. Let $\calF$ be a set of functions $f:\calX\to\Re$. Let 
$$
\alpha_n(f) = \frac{1}{n}\sum_{i\leq n}f(X_i) - \E f(X).
$$
The empirical process associated with $\calF$ is 
$$
\Delta_n(\calF) = \sup_{f\in \calF} \left|\alpha_n(f)\right|.
$$
(Though sometimes $\alpha_n(f)$ itself is referred to as the empirical process.)

Empirical process theory is concerned with statements about the limiting behavior of $\sup_f \alpha_n(f)$ and $\Delta_n(\calF)$, whether in probability, almost surely, or in distribution. That is, we are searching uniform [[laws of large numbers]] or uniform [[central limit theorems]]. _Uniform_ refers to uniformity over $\calF$, which is what makes empirical process theory more challenging than simply analyzing sums of iid random variables. 

If $\Delta_n(\calF)\to 0$ in probability (or almost surely), we call $\calF$ a [[Glivenko-Cantelli class]]. If $\sqrt{n}\alpha_n$ obeys a CLT (in the space of processes indexed by $\calF$), we say it is a [[Donsker class]]. 

A common way to control $\Delta_n(\calF)$ is via [[covering and packing]] numbers for the class $\calF$. The relationship between covering and shattering numbers is then exploited by [[Vapnik-Chervonenkis theory]] to give bounds based on the VC-dimension. 

Applications of empirical process theory are wide ranging. It pops up in [[M-estimation]] (eg proving properties of the [[MLE]]), [[hypothesis testing]] (eg analyzing [[goodness-of-fit test|goodness-of-fit tests]]), analyzing [[bootstrapping]], [[learning theory]] (especially via [[Vapnik-Chervonenkis theory]]), [[nonparametric density estimation]] and [[nonparametric regression]], and [[causal inference]]. 

