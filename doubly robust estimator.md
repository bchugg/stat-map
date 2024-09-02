---
created: 2024-08-29
lastmod: 2024-09-02
---

Suppose we are trying to estimate a parameter $\theta$ and we have estimates $Y_1,\dots,Y_n$ of $\theta$ drawn from a meta-population $Y_1,\dots,Y_N$. Suppose we also have a model $f$ which estimates $Y_i$ given some covariates $X_i$, and that the covariates $X_i$ have been sampled from some larger population with probability $\pi(X_i)$. Then the doubly robust estimator, also called the augmented IPW estimator, is 
$$

\wh{\theta} = \frac{1}{N} \sum_{i=1}^N \left( f(X_i) + (Y_i - f(X_i))\frac{\xi_i}{\pi(X_i)}\right),

$$
where $\xi_i$ indicates whether $X_i$ has been sampled. Here $N$ is the size of the entire population, and we've sampled some number $n<N$ of labels $Y_i$. For the rest, we estimate the true value $Y_i$ with $f(X_i)$. 

Since $\E[\xi_i] = \pi(X_i)$, this estimator is unbiased. It also tends to have lower variance. It's used in [[survey sampling]], [[reinforcement learning]], and [[causal inference]]. 


