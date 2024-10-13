---
lastmod: 2024-10-08
created: 2024-10-07
---

Suppose you are trying to generate a [[confidence sequences|confidence sequence]] for a parameter $\mu$. Suppose you can write down a [[supermartingale]] of the form $M_t(\lambda) = \exp\{ \lambda S_t(\mu) - \psi(\lambda) V_t\}$ for $\mu$ (eg, a [[sub-psi process]] based on an [[exponential inequalities|exponential inequality]]), where $(S_t(\mu))$ is some process which is a function of $\mu$. $(S_t)$ is often the martingale $S_t(\mu) = \sum_{i\leq t}(X_i - \mu)$.  

One option is to use a predictable sequence $(\lambda_t)_{t\geq 1}$, employing a different $\lambda_t$ at each time step. See [[confidence sequences via predictable plug-ins]]. 

Another approach, that of conjugate mixtures, is to integrate over $\lambda$. Suppose $M_t(\lambda$) is a supermartingale for all $\lambda\in\Lambda$. Then 
$$
N_t := \int_\lambda M_t(\lambda) \rho(\d \lambda),
$$
is a supermartingale for any distribution $\rho$ over $\Lambda$ by Tonelli's theorem. (For intuition take $\rho$ to be a discrete distribution).  Applying [[Ville's inequality]] to $N_t$ then yields a (sometimes implicit) CS for $\mu$. 

Various distributions $\rho$ were studied by [Howard et al](https://arxiv.org/pdf/1810.08240), most of them giving implicit CSs. One nice exception is Robbins' Gaussian mixture. 

## Robbins' Gaussian mixture
If $X_1,X_2,\dots$ are $\sigma$-sub-Gaussian with conditional means $\mu_i = \E[X_i|X_1^{i-1}]$, then $M_t(\lambda) = \prod_{i\leq t}\exp\{\lambda (X_i - \mu_i) - \lambda^2\sigma^2/2\}$ is the standard sub-Gaussian supermartingale then taking $\rho$ to be Gaussian with mean 0 and variance $a^2$ gives the following bound: 
$$
\Pr\left(\exists t\geq 1: \left|\sum_{i\leq t} X_i - \mu_i\right|\geq \sigma\sqrt{\frac{2(ta^2 + 1)}{t^2a^2}\log\left(\frac{\sqrt{ta^2 + 1}}{\alpha}\right)}\right)\leq \alpha.
$$
Robbins noted this CS (in a slightly less general sense) in the 1970s. [This has been generalized to vector-valued random variables](https://arxiv.org/pdf/2311.08168). 

# Refs 
- [Conjugate mixtures](https://www.stat.cmu.edu/~aramdas/martingales18/L18-conjugate.pdf), Lecture notes by Aaditya Ramdas. 