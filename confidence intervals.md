---
created: 2024-08-29
lastmod: 2025-01-31
---

A $(1-\alpha)$-CI for a parameter $\theta$ based on observations $X_1, X_2,\dots,X_n$ is a set $C_n = C(X_1,\dots,X_n)$ such that
$$
 \Pr(\theta\notin C_n)\leq \alpha.
$$
This is a frequentist notion ([[frequentist statistics]]) as opposed to a Bayesian one ([[Bayesian statistics]]). The Bayesian equivalent of CIs are [[credible intervals]].

The interpretation of CIs is notoriously tricky. The correct interpretation is that if you repeat the experiment many times (where an experiment consists of drawing $n$ datapoints), then the parameter $\theta$ will be inside the interval about an $(1-\alpha)$-fraction of the time. The incorrect (but common) interpretation is that the parameter $\theta$ has a $(1-\alpha)$ chance of being inside a given interval. This isn't true: for each realization of $C_n$, the parameter is either covered by the interval or it's not. 

CIs are fundamental tools in uncertainty quantification. They can be obtained directly, or via inverting hypothesis tests (see [[hypothesis testing]] and [[duality between hypothesis tests and CIs]]). 

They also have some problems. If you repeatedly compute confidence intervals after receiving new data, your intervals will eventually contradict one another (with probability 1). That is, there will be at least two intervals with no overlap, $C_n \cap C_m =\emptyset$. This implies they are not _sequentially valid_, in the sense that they do not guarantee that $\theta$ is contained $C_n$ for all $n$ with probability $1-\alpha$. This issue is solved with [[confidence sequences]]. 

The name confidence intervals is a slight misnomer, in the sense that some methods will produce confidence _regions_ instead of intervals. That is, the confidence set will not always look like a convex set. And sometimes the parameter space is discrete (eg [[conformal prediction]]), so the resulting confidence set is certainly not an interval. 




