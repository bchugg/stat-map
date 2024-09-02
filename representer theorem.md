---
created: 2024-08-29
lastmod: 2024-09-02
---
We are in the setting of [[nonparametric regression]]. Suppose we have training data $(x_i,y_i)$ and a loss $\ell$. Consider empirical risk minimization where we add a regularization term based on a [[Mercer kernel]] $K$: 
$$

f^* = \arg\min_f \frac{1}{n}\sum_i \ell(y_i,f(x_i)) + \lambda ||f||_K^2.

$$
Then $f^*$ can be represented as $f^*(x) = \sum_i \alpha_i K(x_i,x)$ (where the $x_i$ are the training points) for some $\alpha_1,\dots,\alpha_n$. 

This is an amazing fact, and allows us to boil down the gigantic search space in nonparametric regression to a quadratic program that we can solve by hand —  see [[RKHS regression]]. 

This theorem is actually more general, and works for any loss $\ell$ which is a function of $(X_i,Y_i,f(X_i))$ and any monotone $g$, in which case $f^*$ minimizes
$$

\ell + g(||f||_K).

$$

