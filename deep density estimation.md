---
created: 2024-08-29
lastmod: 2024-12-20
---

Suppose we want to do [[parametric density estimation]] but our parametric class is a set of complicated functions $\{f_\theta:\theta\in\Theta\}$ which may not be proper probability distributions. For instance, think of deep neural networks. 

If $\{p_\theta\}$ is a well-behaved family of probability distributions (i.e., integrate to 1, non-negative) then a natural approach to density estimation is [[MLE]]. Thus, one approach is to normalize $f_\theta$ as 
$$
p_\theta(x) := \frac{\exp(f_\theta(x))}{\int_\calX \exp f_\theta(x)dx}.
$$
The log-likelihood is then
$$
\log \calL(\theta) = \sum_i f_{\theta}(X_i) - n \log \int_\calX \exp f_\theta(x)dx.
$$
In order to maximize this, we must solve (or approximate) the integral $\log \int_\calX \exp f_\theta$,which is highly non-trivial for complex function families.  This is [[the problem of approximate inference in deep learning]], which can be solved by, eg [[variational inference]]. 