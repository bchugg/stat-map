---
created: 2024-08-29
lastmod: 2024-09-02
---

Intuitively, the Fisher information is the expected curvature around a parameter. The more curvature, the "easier" the parameter is to estimate. 

Formally, the Fisher information is the expected outer-product of the [[score function]], which is the gradient of the log-likelihood. If $s_n(\theta) = \nabla_\theta \ell_n(\theta)$ is the score based on $n$ observations, then the Fisher information is:
$$
I_n(\theta) := \E[s(\theta)s(\theta)^\top].
$$
Since $s(\theta)$ is a $d$-dimensional vector (if $\theta$ is d-dimensional), the Fisher information is a $d\times d$ matrix. For iid data, the Fisher information satisfies $I_n(\theta) = nI_1(\theta)$, which is extremely handy.

An equivalent way to define it is
$$
I_1(\theta) = -\E[\nabla^2_\theta\ell_1(\theta)],
$$
i.e. the second derivative of the negative log-likelihood.
