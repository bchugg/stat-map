---
lastmod: 2025-07-22
created: 2025-07-22
---

Subset of [[statistical decision theory]]. We have a loss function $L:\Theta\times\calA\to\Re_{\geq 0}$ where $\Theta$ is some parameter space (each $\theta$ corresponds to some distribution $P_\theta$) and $\calA$ is an action set (often $\calA = \Theta$). We have a prior $\pi$ over $\Theta$, as one does in [[Bayesian statistics]]. 

The _Bayes risk_ of a rule $\delta = \delta(X)$ which takes an action given data is 
$$
B(\delta) = E_{\theta\sim \pi} \E_{X\sim P_\theta}L(\theta, \delta(X)).
$$
We call $\delta^*$ a _Bayes estimator_ if it minimizes the Bayes risk, i.e., $B(\delta^*) = \inf_\delta B(\delta)$. 

Another view on optimality and the Bayes estimator is via the posterior expected loss. Given data $X$, take the action which minimizes expected loss under the posterior: 
$$
\delta_\pi(X) = \argmin_{a\in\calA} \int L(\theta, a) \pi(\theta|X)\d\theta.
$$
Then $\delta_\pi$ is the Bayes estimator. This is a huge result in Bayesian decision theory, and can be traced back to Wald, Blackwell, and Lehmann and Casella. Sometimes this is called the "Bayes rule theorem." (eg see [here](https://people.bath.ac.uk/masss/APTS/2022-23/LectureNotes/cha-DT.html)). 