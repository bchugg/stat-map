---
created: 2024-08-29
lastmod: 2025-01-11
---

Suppose we want to do [[parametric density estimation]] but our parametric class is a set of complicated functions $\{f_\theta:\theta\in\Theta\}$ which may not be proper probability distributions. For instance, think of deep neural networks. 

One approach is to normalize $f_\theta$ as 
$$
p_\theta(x) := \frac{\exp(f_\theta(x))}{\int_\calX \exp f_\theta(x)dx}.
$$
The log-likelihood is then
$$
\log \calL(\theta) = \sum_i f_{\theta}(X_i) - n \log \int_\calX \exp f_\theta(x)dx.
$$
In order to maximize this, we must solve (or approximate) the integral $\log \int_\calX \exp f_\theta$,which is highly non-trivial for complex function families.  This is [[the problem of approximate inference in deep learning]], which can be solved by, eg [[variational inference]]. 

Energy-based models have a similar idea, but they define the probability distribution as $p_\theta(x) \propto \exp(-f_\theta(x))$. This also requires computing the normalizing constant as above. These are called energy based because $f_\theta$ is a neural net that represents the "energy," borrowing from statistical physics where lower energy is synonymous with higher probability. 

There are other approaches, such as normalizing flows, autoregressive models, and GANs. 