Possibly the simply method for [[nonparametric density estimation]] after the empirical distribution. 

We split the space $\cX\subset \Re^d$ into $N$ equal sized bins, $B_1,\dots,B_N$. Note that the true density is 
$$p(x) = \sum_i \Pr(x|x\in B_i)\Pr(x\in B_i).$$
We estimate $\Pr(x\in B_i)$ by simply counting the fraction of training points $X_i$ which landed in bin $B_i$. We estimate $\Pr(x|x\in B_i$) by placing a uniform distribution over the bin $B_i$, i.e., we assume $\Pr(x|x\in B_i) \approx \frac{1}{vol(B_i)}\ind(x\in B_i)$.  Our estimator is therefore 
$$\wh{p}(x) = \sum_{i=1}^N \frac{\wh{\theta}_j}{vol(B_i)}\ind(x\in B_i),$$
where $\wh{\theta}_j = \frac{1}{n}\sum_{i=1}^n \ind(X_i\in B_j)$. Note that $N$ is the number of bins and $n$ is the number of training points. 

If $\cX=[0,1]^d$, then $vol(B_i) = h^d$ and $N=(1/h^d)$. 
