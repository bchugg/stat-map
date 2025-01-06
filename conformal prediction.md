---
created: 2024-08-29
lastmod: 2025-01-06
---


Conformal prediction is a popular and practical tool in [[uncertainty quantification]]. We're in a [[supervised learning]] setting and have a black-box model $f$. Given a new observation $X$, we want to develop a [[confidence intervals|confidence set]] for its label $Y$. 

It turns out we can do this simply by having access to predictions $f(X_1), f(X_2), \dots, f(X_n)$ and outcomes $Y_1, Y_2, \dots, Y_n$. We need only make the assumption that the data $X_1, \dots, X_n$ are [[exchangeable distribution|exchangeable]], nothing else. 

There are several flavors of conformal prediction, split conformal being the easiest both conceptually and in terms of implementation. 

## Split conformal prediction
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

