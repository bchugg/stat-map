---
created: 2024-08-31
lastmod: 2025-08-22
---

We observe data drawn from some $P_\theta$ for some $\theta\in\Theta$.  Let $\ell:\Theta\to\Re$ be any convex loss on estimates of $\theta$ (see [[statistical decision theory]]). The Rao-Blackwell theorem states that the expected loss of an estimator $\wh{\theta}$ can never be made worse by conditioning on a [[sufficient statistic]] $T$. That is, if we consider $\widetilde{\theta} = \E[\wh{\theta}|T]$, then 
$$
\E \ell(\wh{\theta}) \geq \E\ell(\widetilde{\theta}).
$$
Sufficiency is only used in order to define the estimator $\widetilde{\theta}$ in order to make sure it's actually independent from $\theta$ (otherwise the theorem is useless). 

The estimator $\widetilde{\theta}$ is often called the Rao-Blackwellization of $\wh{\theta}$. The theorem is usually applied with the [[squared error]]. 

There is also a Rao-Blackwell-like result for [[e-value|e-values]] and [[e-process|e-processes]] (see this [blog post](https://benchugg.com/research_notes/rao-blackwell-evalues/) or [this paper](https://arxiv.org/pdf/2508.00770)), which says that conditioning on a [[sufficient statistic]] will never decrease log-power under the alternative (or $f$-power for any concave $f$). In sequential settings this means that the growth rate of the process will never be worse ([[growth rate conditions in sequential testing]]). 

Relatedly, conditioning on a sufficient statistic was used by [Lee and Ren](https://arxiv.org/pdf/2404.17562) in the context of [[multiple testing]] to improve the [[e-BH procedure]]. 