---
created: 2024-08-31
lastmod: 2024-09-02
---

Let $\{P_\theta\}$ be a statistical model and $T$ a [[sufficient statistic]] for $\theta$. By the Neyman-Fisher characterization (see [[sufficient statistic#Neyman-Fisher characterization|sufficient statistic: Neyman-Fisher characterization]]), we can write the likelihood as 
$$
\calL(\theta) = p(x^n;\theta) = h(x^n) g(T(x^n);\theta).
$$
We're interested in the likelihood as a function of $\theta$ (eg in [[MLE]]) so $\calL(\theta) = \propto g(T(x^n);\theta)$. Therefore, to do any analysis on the likelihood, it suffices to know a sufficient statistic of the data, as opposed to the data itself. 