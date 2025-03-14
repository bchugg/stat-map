---
created: 2024-08-29
lastmod: 2025-03-14
---


Conformal prediction is a popular and practical tool in [[uncertainty quantification]]. We're in a [[supervised learning]] setting and have a black-box model $f$. Given a new observation $X$, we want to develop a [[confidence intervals|confidence set]] for its label $Y$. 

It turns out we can do this simply by having access to predictions $f(X_1), f(X_2), \dots, f(X_n)$ and outcomes $Y_1, Y_2, \dots, Y_n$. We need only make the assumption that the data $X_1, \dots, X_n$ are [[exchangeable distribution|exchangeable]], nothing else. There are several flavors of conformal prediction, split conformal being the easiest both conceptually and in terms of implementation. 

## Split conformal 
Introduce an arbitrary _score function_ $s$ which maps observation-label pairs to a positive number. We should think of $s$ as quantifying a heuristic notion of uncertainty, but it can be anything. If $f$ is a regressor then a popular choice is $s(X, Y) = |f(X) - Y|$. For classification we might take $s(X,Y) = 1 - f_Y(X)$ if $f_Y(X)$ is the probability that $f$ assigns to $X$ being in class $Y$. 

Suppose we have some validation data $(X_i,Y_i)$, $1\leq i\leq n$ and we compute the scores $s_i = S(X_i,Y_i)$.  Given a new covariate $X_{n+1}$, our uncertainty set is based on the [[conformal p-value]]
$$
Q_n(X,y) = \frac{1 + \sum_{i\leq n} \ind\{ s(X_i,Y_i) \geq s(X_{n+1},y)\}}{n+1}.
$$
Let $Y_{n+1}$ be the true label for $X_{n+1}$. If $(X_i,Y_i)$, $1\leq i\leq n+1$ are [[exchangeable distribution|exchangeable]], then $Q_n(X_{n+1}, Y_{n+1})$ is a [[p-value]]. Therefore, given $\alpha\in(0,1)$, our confidence set is 
$$
C_n(X_{n+1}) = \{ y\in \calY: Q_n(X_n,y) > \alpha\},
$$
which by definition of a p-value, satisfies $\Pr(Y_{n+1} \notin C_n(X_{n+1})) = \Pr(Q_ n(X_{n+1},Y_{n+1}) \leq \alpha) \leq \alpha$. 
Intuitively, if $y\neq Y_{n+1}$ then $s(X_{n+1}, y)$ should be large, making $Q_n(X_{n+1},y)$ small and ensuring that $y\notin C_n(X_{n+1})$. 

An alternative way to describe the same algorithm is as follows. Compute the $\lceil (1-\delta)(n+1)/n\rceil$ quantile of $s_1,\dots,s_n$. Call this $q$. Then our confidence set for a new observation $X$ is
$$
C_n(X_{n+1}) = \{y: s(X,y)\leq q\}.
$$
It can be shown to obey
$$
1-\delta\leq \Pr_{(X_{n+1},Y_{n+1}), (X_i,Y_i)_1^n}(Y_{n+1}\in C_n(X_{n+1}))\leq 1-\delta + 1/n,
$$
where we note that the probability is over both the new test point and the training data.

The intuition for the quantile version is very straightforward: we're just letting the holdout set $s(X_1,Y_1),\dots,s(X_n,Y_n)$ tell us what the most extreme values of $s(X,Y)$ are empirically. If we had access to the full distribution $s(X,Y)$, then we could compute the precise $1-\delta$ quantile $q$ and our set $C(X)$ would be an exact $1-\delta$ confidence interval. The extra factor of $(n+1)/n$ is a finite sample correction. 

# Extensions 
Conformal inference is a huge research now, and I don't stand the slightest chance of keeping up with all the developments. But here are a few: 

**Beyond Marginal guarantees.** The marginal guarantee given by split conformal is quite weak. One would ideally like to give coverage guarantees that are conditional on some properties of the new covariates $X$. Unfortunately, fully conditional coverage (i.e., conditional on $X$ itself) is too high a bar: [Lei and Wasserman showed that](https://www.stat.cmu.edu/~ryantibs/statml/lectures/Lei-Wasserman.pdf), absent any further assumptions, an algorithm that achieves conditional coverage will also be trivial. But there are notions of conditional coverage: 
- Mondrian conformal prediction studies conditional guarantees for disjoint subgroups. [Mondrian confidence machine](https://algolabs.com/wp-content/uploads/2023/04/mcm-1.pdf) by Vovk et al. 
- Conditional coverage guarantees for overlapping subgroups: [Conformal prediction with conditional guarantees](https://arxiv.org/pdf/2305.12616) by Gibbs et al. and [Batch multivalid conformal prediction](https://arxiv.org/pdf/2209.15145) by Jung et al. 
- [Kandinsky Conformal Prediction: Beyond Class- and Covariate-Conditional Coverage](https://arxiv.org/pdf/2502.17264) by Bairaktari et al. Here the group definitions are allowed to depend on both the covariates and the labels, which is a departure from the conditional guarantees above. The guarantees also hold for fractional groups (i.e., membership in a group is not binary, it's probabilistic). 

**Beyond exchangeability**
- The conditional coverage methods of Gibbs et al. and Kandinsky conformal prediction allow guarantees to be given under distribution shift. 
- [Conformal Prediction Under Covariate Shift](https://proceedings.neurips.cc/paper/2019/file/8fb21ee7a2207526da55a679f0332de2-Paper.pdf) Tibsharani et al. 
- [Conformal prediction beyond exchangeability](Conformal prediction beyond exchangeability), Barber et al. 