---
created: 2024-08-29
lastmod: 2024-09-02
---

In traditional [[hypothesis testing]] we fix a significance level $\alpha\in(0,1)$ and look for tests $\phi$ which have type-I error bounded by $\alpha$: 
$$
\sup_{P\in\calP} P(\phi(X) = 1)\leq \alpha,
$$
where $\calP$ is the null. To do [[post-hoc hypothesis testing]], we want to be able to quantify over $\alpha$, so we rewrite this as _risk_: 
$$
\sup_{P\in\calP} \E_P\left[\frac{\phi(X)}{\alpha}\right]\leq 1.
$$
(We make a similar move when viewing hypothesis testing through the lens of decision-theory: [[Neyman-Pearson paradigm with losses]]). To allow $\alpha$ to be data-dependent, we add a supremum over $\alpha$ inside the expectation (it is implicitly outside the expectation in the previous display):  
$$
\sup_{P\in\calP} \E_P\left[\sup_{\alpha\in(0,1)}\frac{\phi(X)}{\alpha}\right]\leq 1.
$$
We call a rule $\phi$ which obeys the above inequality a post-hoc valid hypothesis test.  

Suppose the test is based on an [[e-value]], i.e., for a given $\alpha$, $\phi(x) = \ind(E(x) \geq \alpha)$  for some e-variable $E$ for $\calP$. Then $\phi(x)/\alpha \leq E(x)$ by case analysis on the numerator, so 
$$
\sup_P \E_P\left[\sup_\alpha \frac{\ind(E(X)\geq \alpha)}{\alpha}\right]\leq \sup_P\E_P[E(X)]\leq 1,
$$
meaning that tests based on thresholding e-values e-values enable post-hoc hypothesis testing. 

The other direction is true as well: If one has a post-hoc valid test that is based on some threshold $T$, i.e., $\phi(x) = \ind(T(x) \geq \alpha)$, then $T$ must be an e-value. You can see this by taking $\alpha = T$ in the definition of post-hoc validity.  

This was first pointed out in [False discovery rate control with e-values](https://arxiv.org/pdf/2009.02824) by Wang and Ramdas (2022) and in [Beyond Neyman-Pearson](https://arxiv.org/abs/2205.00901) by Grunwald (2022). 

