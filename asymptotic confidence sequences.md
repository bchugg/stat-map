---
created: 2024-08-29
lastmod: 2025-01-05
---

Typically, [[confidence sequences]] are non-asymptotic objects. There's no "limit" in the statements as there is with, say, [[confidence intervals]] that are constructed via the [[central limit theorems|CLT]]. 

Non-asymptotic results are useful, but typically require stronger assumptions. Eg sub-$\psi$ tail bounds (see [[sub-psi process]]) or known bounded moments. But asymptotic results usually require weaker assumptions. Eg [[Wald interval]]'s based on the [[central limit theorems|CLT]] only requires finite variance. 

In fact, [Bahadur and Savage](https://projecteuclid.org/journals/annals-of-mathematical-statistics/volume-27/issue-4/The-Nonexistence-of-Certain-Statistical-Procedures-in-Nonparametric-Problems/10.1214/aoms/1177728077.full) show that if all you have is finite variance, and no known bound on this variance, then you cannot do non-asymptotic inference. 

This suggests the question of whether there exists some notion of _asymptotic_ confidence sequences, which require weaker assumptions to obtain coverage guarantees. Asymptotic confidence sequences were introduced by [Waudby-Smith et al.](https://arxiv.org/pdf/2103.06476) 

The intuition is as follows: We say a sequence of sets $(C_t^A)_{t\geq 1}$ is an asymptotic-CS if it approximates a non-asymptotic $(C_t^{NA})_{t\geq 1}$. In particular, the (right and left) boundary of $C_t^A$ should converge (almost-surely) to that of $C_t^{NA}$ as $t\to\infty$. The formal definition is: 

> [!Definition]
> A $(1-\alpha$)-asymptotic CS for a parameter $\mu$ is a sequence of intervals $([\theta_t - L_t, \theta_t + R_t])$ such that there exists a (nonasymptotic) CS for $\mu$ of the form $[\theta_t - L_t^*, \theta_t + R_t^*]$ such that $L_t/L_t^*\xrightarrow{a.s.} 1$ and $R_t/R_t^*\xrightarrow{a.s.} 1$. 

[Waudby-Smith et al.](https://arxiv.org/pdf/2103.06476) give:  
- an asymptotic CS for iid random variables with finite variance. The result resembles Robbins' original mixture ([[confidence sequences via conjugate mixtures]]) but, like the CLT, does not require an a priori bound on the variance, instead using the empirical variance. The result relies on [[strong approximations]]. 
- Asymptotic CSs which hold for changing means and variances under martingale dependence. These might be considered the time-uniform analogues of the [[Lindeberg-Feller CLT]] and the [[Lyapunov CLT]]. 

## Asymptotic coverage 

One would hope that the asymptotic CSs obey some notion of time-uniform coverage. But what exactly is that notion in the asymptotic setting? In the [[fixed-time]] setting, the correct notion of miscoverage is $\lim_{n} \Pr(\mu \in C_n)\geq 1-\alpha$. How to extend this to the [[time-uniform]] setting? 

> [!Definition]
> We say that a sequence of CSs $(C_t(m))_{t\geq m}$, $m\geq 1$ has $(1-\alpha$) time- uniform coverage if $\lim\inf_m \Pr(\forall t\geq m, \mu_t\in C_t(m)) \geq 1-\alpha$.  

Intuitively, this says that the time-uniform coverage starts later and later. 

As long as the variances can be estimated quickly enough (at polynomial rates), then the above examples have asymptotic coverage guarantees. 