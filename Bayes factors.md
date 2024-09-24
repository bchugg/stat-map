---
created: 2024-08-29
lastmod: 2024-09-24
---

Bayes factors can be considered as a Bayesian ([[Bayesian statistics]]) analogue of the [[likelihood-ratio test]]. They are often used in [[hypothesis testing]] and [[model selection]]. Along with [[p-value|p-values]] and [[e-value|e-values]], they are considered measures of [[evidence against the null]]. 

For parameters $\theta_1, \theta_2$ (perhaps representing different hypotheses or models) and given data $X$, the Bayes factor is 
$$
B := \frac{\Pr_{\theta_1}(X)}{\Pr_{\theta_2}(X)} = \frac{\Pr(\theta_1|X)\Pr(\theta_1)}{\Pr(\theta_2 | X)\Pr(\theta_2)},
$$
where the second equality follows from Bayes' theorem if we place prior $\Pr(\theta)$ over the parameter space.


