---
created: 2024-08-29
lastmod: 2024-09-02
---

We are interested in solving the following regularized [[nonparametric regression]] problem under the squared loss: 
$$
\arg\min_m R(m) = \sum_i (Y_i - m(X_i))^2  +\lambda ||m||_K^2,
$$
where $K$ is a [[Mercer kernel]]. This is optimization over a [[RKHS]]. The [[representer theorem]] tells us that the the minimizer $\wh{m}$ has the form 
$$
\wh{m}(x) = \sum_i \alpha_i K(x_i,x),
$$
so the problem reduces to find the optimal $\alpha = (\alpha_1,\dots,\alpha_n).$ Thus we can write $R = ||\bs{Y} - \bs{K} \alpha||_2^2 + \lambda \alpha^T \bs{K}\alpha,$ where $\bs{K}_{i,j} = K(x_i,x_j)$.  Taking the gradient w.r.t. to $\alpha$ and keeping in mind that $K$ is invertible and symmetric, the minimizer is 
$$
\wh{\alpha} = (\bs{K} + \lambda I)^{-1}\bs{Y}.
$$
So $\wh{m}(x) = \sum_j \wh{\alpha_j} K(x_j,x)$, so 
$$
\wh{m}(x) = k_x^T (\bs{K} + \lambda I)^{-1}\bs{Y},
$$
where $k_x = (K(x_1,x),\dots,K(x_n,x))$. This demonstrates that RKHS regression is a member of the class of [[linear smoothers]]. 



