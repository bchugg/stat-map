---
created: 2024-08-29
lastmod: 2024-10-01
---

Bayes factors can be considered as a Bayesian ([[Bayesian statistics]]) analogue of the [[likelihood-ratio test]]. They are often used in [[hypothesis testing]] and [[model selection]]. Along with [[p-value|p-values]] and [[e-value|e-values]], they are considered measures of [[evidence against the null]]. 

For parameters $\theta_1, \theta_2$ (perhaps representing different hypotheses or models) and given data $X$, the Bayes factor is 
$$
B := \frac{\Pr_{\theta_1}(X)}{\Pr_{\theta_2}(X)} = \frac{\Pr(\theta_1|X)\Pr(\theta_1)}{\Pr(\theta_2 | X)\Pr(\theta_2)},
$$
where the second equality follows from Bayes' theorem if we place prior $\Pr(\theta)$ over the parameter space. Thus, it is really the second equality where Bayesianism enters the picture—the first equality is simply a likelihood ratio and need not be Bayesian at all. 

Jeffreys (a Bayesian) gave a table summarizing how much evidence is provided by different values of $B$. So did Kass and Raftery in 1995. This is pretty silly, as it depends on the application and what actions we're considering on the basis of $B$. 


