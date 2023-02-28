Let $X_1,\dots,X_n\sim P$. The goal is to determine the density of $P$, call it $p$, while making as few assumptions about $p$ as possible (i.e., we don't assume that $P$ comes from some parametric family; see [[parametric versus nonparametric statistics]]).  

An obvious solution is to simply take the empirical distribution, in which case our estimator is 
$$\widehat{p}(x) = \frac{1}{n}\sum_i \ind(x = X_i).$$
But this solution obviously overfits the given data and has very few nice properties (continuity, smoothness, etc). 

A solution to nonparametric density estimation also provides a solution to [[nonparametric regression]] as follows. Suppose $\wh{p}$ is an estimate of the distribution $(X_1,Y_1), \dots, (X_n,Y_n)\sim P$. Then, for $m(x) = \E[Y|X=x)$, we can generate an estimate of $m$ with 
$$\wh{m}(x) = \int y \wh{p}(y|x)dx = \int y \wh{p}(x,y)/\wh{p}(x) dy,$$
where $\wh{p}(x) = \int \wh{p}(x,y)dy$. 


Common methods: 
- [[kernel density estimation]]