---
lastmod: 2024-10-21
created: 2024-10-21
---
Stronger [[concentration inequalities]] can sometimes be given for random variables which are negatively correlated. 

The intuition is as follows: consider two random variables $X_1 = X$ and $X_2 = -X$. Then $\Cov(X_1,X_2) = - \sigma^2<0$ where $\sigma^2 = \Var(X_1)$.  Applying, say [[basic inequalities#Chebyshev's inequality]] gives 
$$
\Pr(| X_1 + X_2|\geq t) \leq \frac{\Var(X_1 + X_2)}{t^2} = \frac{\sigma^2}{t^2}.
$$
But this is quite weak since, of course, $X_1$ and $X_2$ are perfectly concentrated around 0. 

Negative correlation can be incorporated in the [[Chernoff method]] (see eg [here](https://homes.cs.washington.edu/~jrl/teaching/cse525sp19/notes/lecture5.pdf)). Garbe and Vondrak [study the concentration of Lipschitz functions of negatively correlated rvs](https://arxiv.org/pdf/1804.10084). 