---
lastmod: 2025-01-05
created: 2025-01-05
---

The study of proving performance guarantees for learning algorithms, usually in a [[supervised learning]] setting (also in [[self-supervised learning]], but this is a stupid category). 

We have a class $\calF$, a set of functions $f:\calX\to \calY$ which map the feature space $\calX$ to a label space $\calY$, which we'll assume is some subset of $\Re$. Our algorithm sees training data and chooses a function $\wh{f}\in\calF$. There is some target function $f^*$ which is the "best" or "true" map between $\calX$ and $\calY$. If $f^*\in\calF$ we say it is _realizable_. Ideally we learn $\wh{f}$ which is not far from, or equal to, $f^*$. 

Since $\wh{f}$ is data-dependent, typical analysis techniques which might lead to [[laws of large numbers]] or [[central limit theorems]] fail, because independence does not hold (even if the training data are independent). Two strategies to deal this, and thus two brands of learning theory, are: 
- [[PAC learning]], the application [[empirical process theory]] to $\calF$, where we often use [[Vapnik-Chervonenkis theory]] to bound the error. This is a worst case analysis, because we take the supremum over all $f\in\calF$. 
- [[PAC-Bayes]] analysis, which is a [[Bayesian statistics|Bayesian]] approach to PAC learning. We put a prior over $\calF$ and then bound the performance in terms of a "posterior". If the prior was well-chosen, these bounds can be significantly tighter than PAC bounds. 