---
created: 2024-08-29
lastmod: 2024-09-06
---

Some mathematical drawbacks of [[p-value|p-values]] that can lead to (possibly inadvertent) [[p-hacking]].  

Let $P_n$ be a p-value which is a calculated based on $n$ observations $X_1, \dots, X_n$. As a reminder, the usual p-value guarantee reads: 
$$
\forall n, \forall\alpha,\; \Pr_{H_0}(P_n \leq \alpha) \leq \alpha.
$$
The issues with p-values explored here are all consequences of the fact that $n$ (the sample size) and $\alpha$ (the significance level) are outside of the probability statement. Consequently, they should not depend on the data. This basic property has many consequences. 

> [!note] 
> In the case of $n$, the sample size, this issue is fixed with [[anytime-valid p-values]], but these must be specially constructed. Most p-values are not [[anytime-valid]], and these are the focus of this note.)

- First, $\alpha$ must be selected independently of the data. You cannot analyze your data and then choose $\alpha$. In particular, you cannot reject at level $\alpha=p$. This is fixed with [[post-hoc hypothesis testing]]. 
- P-values don't allow [[optional stopping]], i.e., stopping early based on your results. This is sometimes also called "peeking". 
- P-values don't allow [[optional continuation]], i.e., choosing to gather more data after analyzing your results. 

The final two issues above can be viewed as facets of a more general problem with p-values, which is the issue of counterfactual worlds. 

We keep emphasizing that the sample size needs to be fixed in advance. But the p-value requirement is stronger than this. It actually says that _the sample size needs to be same in all counterfactual worlds_. If it's not, it means that the sample size was actually data-dependent. In other words, no matter what happens in the experiment, the sample size cannot change. 

(Mathematically, it can help to view the sample size as a deterministic random variable. That is, if $N$ is the sample size, then for all outcomes $\omega\in\Omega$, we require that $N(\omega) = c$ for some $c$ if the p-value is valid.)

This is an incredibly frustrating property. For one, it is unverifiable: how do you know the sample size would not have changed in every possible world? Second, it makes it extremely easy to start doubting p-values. 

Imagine you have a grad student analyzing the drug trial data as it arrives, just to make sure your data collection software is working. Do you think there's any situation in which he would stop the experiment early? What if the results looked _really, really_ good? If so, then the sample size is not truly fixed, and your p-value is invalid. 

The issues of optional stopping and optional continuation are resolved with [[e-value|e-values]] and [[e-process|e-processes]]. 