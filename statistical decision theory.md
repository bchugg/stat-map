---
created: 2024-08-31
lastmod: 2025-07-22
---

You're doing some [[statistical inference]] on a Friday night, as one does. You compute some estimate $\wh{\theta}$ of the true parameter $\theta$. But how do you know if it's any good? 

You could look at whether it's consistent, or whether it's unbiased, or whether $\wh{\theta} - \theta$, obeys a [[central limit theorems|CLT]] around the true parameter. But who's to say? The point of statistical decision theory is to provide a formal framework for answering this question. 

One begins with a loss function $L:\Theta\times\Theta\to \Re_{\geq 0}$ which measures how good the estimator is. (eg $L(\theta,\phi) = (\theta - \phi)^2$ is the ol' classic [[squared error]]. There's also $\ell_1$ error, $L_p$ loss, zero-one loss, etc.)
The risk of an estimator $\wh{\theta}(X)$ the expected loss, i.e., 
$$
R(\theta,\wh{\theta}) = \E_{X\sim P_\theta} R(\theta, \wh{\theta}(X)). 
$$
Note that $\theta$ is fixed; the expectation is with respect to the randomness of the data. 

It's tempting to compare various estimators, $\wh{\theta}_1$, $\wh{\theta}_2$ by comparing their risks. The one with the lower risk wins, right? But $\wh{\theta}_1$ might have lower risk than $\wh{\theta}_2$ on some parameters $\theta$ and higher risk on others (in fact, this is almost certainly the case for any reasonable estimators). In that case how do we say which one is better? 

The two most common strategies are to consider the maximum risk and the Bayesian risk. 
- The maximum risk considers the worst case over all parameters $\theta$, $M(\wh{\theta}) = \sup_\theta R(\theta,\wh{\theta})$. The estimator minimizing the maximum risk is the minimax estimator. A huge swath of modern statistics is taken up with the question of determining minimax rates and finding minimax estimators. 
- The Bayesian risk puts a prior $\pi$ over $\Theta$ and then considers the Bayes risk: $B(\wh{\theta}) = \int R(\theta, \wh{\theta}) \pi(\theta) \d\theta$. There's lots more to say here, see [[Bayesian decision theory]]. 







