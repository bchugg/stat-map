---
created: 2024-09-03
lastmod: 2024-09-03
---

Asymptotic hypothesis test for testing a simple null against a composite alternative: $H_0 : \theta = \theta_0$ vs $H_1: \theta\neq \theta_0$. The test is based on any estimator of $\theta_0$ that, under the null, obeys a [[central limit theorems|CLT]] of the form 
$$
T(\wh{\theta}) = \frac{\wh{\theta} - \theta_0}{\sqrt{\Var(\wh{\theta})}} \to N(0,1),
$$
(We can also replace the denominator with any consistent estimator of $\sqrt{\Var(\wh{\theta})}$ ). Thus, we treat the statistic $T(\wh{\theta})$ as a normal under the null and reject if $|T(\wh{\theta})| \geq z_{\alpha/2}$.  