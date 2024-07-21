Let $X_1,\dots,X_n\sim P$. The goal of [[density estimation]] is to determine the density of $P$, call it $p$. Here we want to make as few assumptions about $p$ as possible (i.e., we don't assume that $P$ comes from some parametric family; see [[parametric versus nonparametric statistics]]). 

An obvious solution is to simply take the empirical distribution, in which case our estimator is 
$$\widehat{p}(x) = \frac{1}{n}\sum_i \ind(x = X_i).$$
But this solution obviously overfits the given data and has very few nice properties (continuity, smoothness, etc). 

Common methods to nonparametric density estimation include: 
- [[histograms]]
- [[kernel density estimation]]

A solution to nonparametric density estimation also provides a solution to [[nonparametric regression]] as follows. Suppose $\wh{p}$ is an estimate of the distribution $(X_1,Y_1), \dots, (X_n,Y_n)\sim P$. Then, for $m(x) = \E[Y|X=x]$, we can generate an estimate of $m$ with 
$$\wh{m}(x) = \int y \wh{p}(y|x)dx = \int y \wh{p}(x,y)/\wh{p}(x) dy.$$
We can estimate both of $\wh{p}(x,y)$ and $\wh{p}(x)$ with nonparametric density estimation. Then we can plug this into the empirical distribution of the $Y_1,\dots,Y_n$ to estimate the integral. 

## Evaluation 
Typically we're interested in $L_2$ loss, i.e., 
$$L(p,\wh{p}) = \int_x (\wh{p}(x) - p(x))^2 dx.$$
The risk is then the expectation over the training data: 
$$R(p,\wh{p}) = \E[L(p,\wh{p})].$$
As usual, the risk can be decomposed into a bias term and variance term. 

