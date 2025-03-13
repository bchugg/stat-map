---
created: 2024-08-29
lastmod: 2025-03-13
---

> [!note] Definition
> A measure $\mu$ is log-concave if for all measurable sets $A, B$ and all $\lambda\in[0,1]$, we have
> $$
> \mu(\lambda A + (1-\lambda)B) \geq \mu(A)^\lambda \mu(B)^{1-\lambda},
> $$
> if the set $\lambda A + (1-\lambda)B$ is measurable. 

Equivalently, if if a density $f$ can be written as $f(x) = \exp(\varphi(x))$ for some concave $\varphi$, then the distribution is log-concave.  

If $X$ is a log-concave distributed random vector, then we can state a bound on its $\psi_1$ [[Orlicz norm]], thus demonstrating that it is [[sub-exponential distributions|sub-exponential]]. In particular, Lemma 2.3 [here] (see also Equation (21) [here](https://arxiv.org/pdf/2108.08198)) demonstrate that 
$$
\norm{\la u,X-\E X\ra}_{\psi_1} \leq c\sqrt{\E\la u,X-\mu\ra^2} = c \sqrt{\la u,\Sigma u\ra},
$$
for some $c\geq 0$ and all unit vectors $u$ where $\Sigma = \Var(X)$. This demonstrates that all log-concave distributions are sub-exponential.  

Many common distributions are log-concave: 
- The normal distribution 
- Exponential distribution 
- Dirichlet distribution for parameters all at least 1 
- Laplace distribution 
- and others 

[[time-uniform|Time-uniform]] [[concentration inequalities]] for log-concave vectors are given in [[multivariate light-tailed concentration]]. 

# Reading 
- https://sites.stat.washington.edu/jaw/RESEARCH/TALKS/Toulouse1-Mar-p1-small.pdf

