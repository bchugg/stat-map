---
lastmod: 2024-12-31
created: 2024-09-26
---

Let $X_1,X_2,\dots$ be random variables taking values in a $\beta$-smooth [[Banach space]] $(\calX, \|\cdot\|)$ with conditional mean $\mu$, i.e., $\E[X_t | X_1,\dots,X_{t-1}] = \mu$, and satisfying $\| X_t - \mu\|\leq B$ almost surely. We want to develop [[concentration inequalities]] for $S_t = \sum_{i\leq t} \| X_i - \mu\|$. 

Pinelis' approach to concentration (explored in his [1994](https://arxiv.org/abs/2401.07365) and [1992](https://link.springer.com/content/pdf/10.1007/978-1-4612-0367-4_9?pdf=chapter+toc) papers) involves studying the process $\cosh(\lambda \| S_t\| )$. In particular, he shows that the process defined by 
$$
M_t = G_t \cosh(\lambda \|S_t\|),
$$
is a nonnegative [[supermartingale]], where 
$$
G_t = \exp\left\{- \frac{\beta^2}{B^2}\left\|\sum_{i\leq t} \| X_t - \mu\|^2\right\|_\infty \sum_{k\geq 2} \frac{(\lambda B)^2}{k!}\right\}.
$$
Applying [[basic inequalities#Markov's inequality]] to $M_n$ for a fixed $n$ and optimizing $\lambda$ gives either the gives the equivalent of [[bounded scalar concentration#Hoeffding's bound]] and [[bounded scalar concentration#Bernstein bound 1]] for bounded Banach space-valued observations; see [[concentration in Banach spaces]] for the statements. Applying [[Ville's inequality]] instead of Markov's inequality gives [[time-uniform]] versions of these inequalities. 

