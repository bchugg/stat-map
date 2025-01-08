---
lastmod: 2025-01-07
created: 2025-01-05
---

The study of proving performance guarantees for learning algorithms, usually in a [[supervised learning]] setting (also in [[self-supervised learning]], but this is a stupid category). 

We have a class $\calF$, a set of functions $f:\calX\to \calY$ which map the feature space $\calX$ to a label space $\calY$, which we'll assume is some subset of $\Re$. Our algorithm sees training data (usually drawn iid from some distribution, but occasionally the distribution is more complicated) and chooses a function $\wh{f}\in\calF$ (via [[empirical risk minimization]], say). 

From here, there are several questions we might want to answer. 

The first is, naturally, how good is $\wh{f}$? That is, how well does $\hat{f}$ generalize to unseen data? <ore formally, how close is the empirical risk of $\wh{f}$ to the true risk (see [[statistical decision theory]])?  [[PAC learning|PAC bounds]] are the most common way to answer this question. This usually leads to bounds which depend on some notion of the complexity of the class $\calF$, such as [[Vapnik-Chervonenkis theory|VC dimension]] or [[Rademacher complexity]]. Another way to answer this question is via [[PAC-Bayes]] bounds, which is a [[Bayesian statistics|Bayesian]] take (sort of) on traditional PAC bounds. Here, the generalization gap is bounded in terms of some [[distributional distance|divergence]]. 

The second is, how close is $\wh{f}$ to the best function $f^* \in \calF$, the one that has the lowest risk. This question is usually answered by [[uniform convergence bounds]] in the following way. We want to bound $\alpha = R(\wh{f}) - R(f^*)$ where $R$ is the risk. Write 
$$
\alpha = \underbrace{R(\wh{f}) - R_n(\wh{f})}_{(i)} + \underbrace{R_n(\wh{f}) - R_n(f^*)}_{(ii)} + \underbrace{R_n(f^*) - R(f^*)}_{(iii)}.
$$
Term (ii) is $\leq 0$, since $\wh{f}$ is chosen to minimize empirical risk. Since $f^*$ is independent of the data, term (iii) can be handled via normal [[concentration inequalities]] (it's simply the deviation between the sum of random variables and their mean). Then for term (i) we turn to a uniform convergence bound, since $\wh{f}$ is highly data-dependent. 