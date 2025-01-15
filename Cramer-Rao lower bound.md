---
lastmod: 2025-01-15
created: 2025-01-15
---

Suppose $X_1,\dots,X_n\sim P_\theta$ and let $\wh{\theta}=\wh{\theta}(X)$ be an unbiased estimator of $\theta$. Then 
$$
\Var(\wh{\theta}(X)) \geq \frac{1}{I_n(\theta)} = \frac{1}{nI_1(\theta)},
$$
where $I(\theta)$ is the [[Fisher information]]. Note this shows that the [[MLE]] is (asymptotically) optimal, since it achieves this lower bound and is (asymptotically) unbiased. 

The multivariate version of the bound is, as you might guess, 
$$
\Var(\wh{\theta}(X)) \succeq I_n^{-1}( \theta) = \frac{1}{n}I_1^{-1}(\theta).
$$
Estimators achieving the Cramer-Rao lower bound are living their best life, you might say. 