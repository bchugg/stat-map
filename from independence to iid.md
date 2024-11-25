---
lastmod: 2024-11-19
created: 2024-11-10
---

Given $n$ independent random variables, a natural question is "how far" these are from iid random variables. In 1998, [Montgomery-Smith and Pruss gave](https://arxiv.org/abs/math/9811124) the following general result, which allows the [[concentration inequalities|concentration]] of independent observations to be upper bounded by iid observations, with only a constant factor loss. 

The result is as follows:  There exists a constant $c>0$ such that if $X_1,\dots,X_n$ are independent random variables in some [[Banach space]], then for all $\lambda>0$, 
$$
\Pr(\|S_n\| \geq\lambda) \leq c \Pr\left(\|\sum_i Y_i\| \geq \lambda/c\right).
$$
where $S_n = \sum_i X_i$ and $Y_1,\dots,Y_n$ are iid such that 
$$
\Pr(Y_i \in A) = \frac{1}{n}\sum_i \Pr(X_i \in A),
$$
for all Borel sets $A$. Therefore, if one is only worried about the asymptotics of concentration, independence is equivalent to iid. 

## Maximal inequalities
There's a similar result but for [[maximal inequalities]]. If $Y_1,\dots,Y_n$ are arbitrary random variables and $X_1,\dots,X_n$ are independent with $X_ i \equald Y_i$ for all $i$, then 
$$
\Pr(\max_{1\leq i\leq n} X_i >u ) \leq \frac{e}{e-1}\Pr(\max_{1\leq i\leq n} Y_i > u).
$$
This is fairly straightforward to prove with a union bound and some elementary inequalities on $1-x$. 
