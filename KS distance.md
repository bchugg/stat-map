The Kolmogorov-Smirnoff [[distributional distance]] between two distributions $P_X$ and $P_Y$ over the reals is 
$$
\rho_\ks(X,Y) = \sup_{z\in\Re} |P_X(X\leq z) - P_Y(Y\leq z)|.
$$
Note that $P_X$ and $P_Y$ need not have the same support for this definition to make sense. They could even be defined on different probability spaces. 

The KS distance is an ideal metric of order 0. It is useful for proving [[central limit theorems]] and provides an error bound on the [[Wald interval]]. 