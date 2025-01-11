---
created: 2024-08-29
lastmod: 2025-01-11
---

Possibly the simplest method for [[nonparametric density estimation]] after the empirical distribution. 

We split the space $\calX\subset \Re^d$ into $N$ equal sized bins, $B_1,\dots,B_N$. Note that the true density is 
$$
p(x) = \sum_i \Pr(x|x\in B_i)\Pr(x\in B_i).
$$
We estimate $\Pr(x\in B_i)$ by simply counting the fraction of training points $X_i$ which landed in bin $B_i$. We estimate $\Pr(x|x\in B_i$) by placing a uniform distribution over the bin $B_i$, i.e., we assume $\Pr(x|x\in B_i) \approx \frac{1}{vol(B_i)}\ind(x\in B_i)$.  Our estimator is therefore 
$$
\wh{p}(x) = \sum_{i=1}^N \frac{\wh{\theta}_j}{vol(B_i)}\ind(x\in B_i),
$$
where $\wh{\theta}_j = \frac{1}{n}\sum_{i=1}^n \ind(X_i\in B_j)$. Note that $N$ is the number of bins and $n$ is the number of training points. 

If $\calX=[0,1]^d$, then $vol(B_i) = h^d$ and $N=(1/h^d)$. Obviously, the choice of $h$ is important and affects performance. The minimax $L_2$ risk ([[statistical decision theory]]) of the histogram in a 1-[[Hölder space]] is bounded by 
$$
L^2 h^2d + O\left(\frac{1}{nh^d}\right),
$$
so minimizing over $h$ we get a risk of $O(n^{-2/(d+2)})$. This rate of $2/(d+2)$ is much slower than parametric models ([[parametric density estimation]]), which are usually on the order of $(d/ \sqrt{n})$, which is much better. In a $q$-Holder space the rate is $2q/(d + 2q)$. Histograms are not minimax optimal, unlike [[kernel density estimation]].

There are also high-probability guarantees. In particular, with probability $1-\delta$, 
$$
\| \wh{p}_h - p\|_\infty \leq O\left(\left(\frac{\log n}{n}\right)^{\frac{1}{2+d}}\right),
$$
where $p$ is the true density and $\wh{p}_h$ is the histogram with bin size $h = O( n^{-1/(2+d)})$. 

There have been efforts to choose the bin size adaptively. These estimators are sometimes called density trees. See: 
- [Density estimation trees](https://home.ipipan.waw.pl/j.mielniczuk/Density_estimation_trees.pdf) by Ram and Gray 
- [Density estimation via adaptive sequential partitition](https://arxiv.org/pdf/1404.1425) Li, Yang, and Wong. 
- [Density estimation via adaptive partitioning](https://arxiv.org/pdf/1401.2597), Liu and Wong. 


