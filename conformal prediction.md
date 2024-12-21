---
created: 2024-08-29
lastmod: 2024-10-13
---


Conformal prediction is a popular and practical tool in [[uncertainty quantification]]. We're in a [[supervised learning]] setting and have a black-box model $f$. Given a new observation $X$, we want to develop a [[confidence intervals|confidence set]] for its label $Y$. 

It turns out we can do this simply by having access to predictions $f(X_1), f(X_2), \dots, f(X_n)$ and outcomes $Y_1, Y_2, \dots, Y_n$. We need only make the assumption that the data $X_1, \dots, X_n$ are [[exchangeable distribution|exchangeable]], nothing else. 

There are several flavors of conformal prediction, split conformal being the easiest both conceptually and in terms of implementation. 

# Split conformal prediction

Introduce an arbitrary _score function_ $s$ which maps observation-label pairs to a positive number. We should think of $s$ as quantifying a heuristic notion of uncertainty, but it can be anything. If $f$ is a regressor then a popular choice is $s(X, Y) = |f(X) - Y|$. For classification we might take $s(X,Y) = 1 - f_Y(X)$ if $f_Y(X)$ is the probability that $f$ assigns to $X$ being in class $Y$. 

Our algorithm is as follows: Compute the $\lceil (1-\delta)(n+1)/n\rceil$ quantile of $s(X_1, Y_1), \dots, s(X_n, Y_n)$. Call this $q$. Then our confidence set for a new observation $X$ is
$$
C(X) = \{y: s(X,y)\leq q\}.
$$
and it obeys $$
1-\delta\leq \Pr_{(X,Y), (X_i,Y_i)_1^n}(Y\in C(X))\leq 1-\delta + 1/n,
$$
where we note that the probability is over both the new test point and the training data.

The intuition is very straightforward: we're just letting the holdout set $s(X_1,Y_1),\dots,s(X_n,Y_n)$ tell us what the most extreme values of $s(X,Y)$ are empirically. If we had access to the full distribution $s(X,Y)$, then we could compute the precise $1-\delta$ quantile $q$ and our set $C(X)$ would be an exact $1-\delta$ CI. The extra factor of $(n+1)/n$ is a finite sample correction. 

