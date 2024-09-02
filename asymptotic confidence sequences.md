---
created: 2024-08-29
lastmod: 2024-09-02
---
#todo 

Typically, [[confidence sequences]] are non-asymptotic objects. There's no "limit" in the statements as there is with, say, [[confidence intervals]] that are constructed via the [[central limit theorems|CLT]]. 

Non-asymptotic results are useful, but typically require stronger assumptions. Eg sub-$\psi$ tail bounds (see [[sub-psi process]]) or known bounded moments. But asymptotic results usually require weaker assumptions. Eg [[Wald interval]]'s based on the [[central limit theorems|CLT]] only requires finite variance. 

In fact, [Bahadur and Savage](https://projecteuclid.org/journals/annals-of-mathematical-statistics/volume-27/issue-4/The-Nonexistence-of-Certain-Statistical-Procedures-in-Nonparametric-Problems/10.1214/aoms/1177728077.full) show that if all you have is finite variance (without a known bound on this variance) then you cannot do non-asymptotic inference. 

This suggests the question of whether there exists some notion of _asymptotic_ confidence sequences, which require weaker assumptions to obtain coverage guarantees. Asymptotic confidence sequences were introduced by Waudby-Smith et al. 

# Definition

> [!Definition]
> A $(1-\alpha$)-asymptotic CS (asympCS) for a parameter $\mu$ is a sequence of sets $(C_t)$ obeying 
>$$
> \lim_{k\to\infty} \Pr(m\geq k: \mu \in C_m).
$$



