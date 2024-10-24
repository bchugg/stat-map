---
lastmod: 2024-10-24
created: 2024-10-24
---

We are doing [[sequential hypothesis testing]] for a simple null $P$ vs simple alternative $Q$ with densities $p$ and $q$, respectively. We examine the likelihood ratio at time $t$, 
$$
\Lambda_t = \frac{\prod_{i\leq t}q(X_i)}{\prod_{i\leq t}p(X_i)}.
$$
We reject the null of $\Lambda_t \geq m_1$ and accepts the null if $\Lambda_t\leq m_0$, otherwise we keep sampling. let $\phi$ be the outcome of the procedure: $\phi=1$ if the null is rejected, $\phi=0$ if accepted. $m_1$ and $m_0$ are chosen such that the type-I error and type-II error satisfy
$$P(\phi = 1) = \alpha, \quad Q(\phi = 0)=\beta,$$
for some pre-specified $\alpha, \beta\in(0,1)$. Wald introduced the test in the 1930s and showed that its stopping time is almost surely finite. and Wald and Wolfowitz proved its optimality: If another test has lower type-I and type-II error then the expected stopping time is larger. 

Unfortunately, $m_0$ and $m_1$ are often impossible to solve for, so approximations are necessary. One usually sets $m_1 = (1 - \beta)/\alpha$ and $m_0 = \beta / (1-\alpha)$. But this loosens the guarantees. [Fischer and Ramdas show](https://arxiv.org/pdf/2410.16076) how to improve the SPRT when approximating $m_1$ and $m_0$. 
