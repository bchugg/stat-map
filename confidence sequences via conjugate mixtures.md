---
lastmod: 2024-10-07
created: 2024-10-07
---

Suppose you are trying to generate a [[confidence sequences|confidence sequence]] for a parameter $\mu$. Suppose you can write down a [[supermartingale]] of the form $M_t = \exp\{ \lambda S_t(\mu) - \psi(\lambda) V_t\}$ for $\mu$ (eg, a [[sub-psi process]]), where $(S_t(\mu))$ is some process which is a function of $\mu$. $(S_t)$ is often the martingale $S_t(\mu) = \sum_{i\leq t}(X_i - \mu)$.  

One option is to use a predictable sequence of $(\lambda_t)$, employing a different $\lambda_t$ at each time step. 

# Refs 
- [Conjugate mixtures](https://www.stat.cmu.edu/~aramdas/martingales18/L18-conjugate.pdf), Lecture notes by Aaditya Ramdas. 