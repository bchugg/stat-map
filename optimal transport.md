---
created: 2023-03-02
lastmod: 2025-01-04
---

The general area of study which deals with how to move abstract "stuff" from one place to another in the most efficient way, where efficient is relative to some given cost function. This is usually framed in terms of [[distributional distance]]: Move mass from one distribution to another while minimizing cost. 

The problem requires introducing new classes of divergences, since typical divergences do not take advantage of the underlying geometry. Eg: consider the following density functions defined on the real line: $p_1(x) = \ind(x\in [0,1])$, $p_2(x) \in \ind(x\in [2,3])$ and $p_3(x) = \ind(x\in [1000,1001])$. Intuitively, it seems like $p_1$ is "closer" to $p_2$ than it is to $p_3$. Unfortunately, several common divergences do not capture this relationship. The [[total variation distance]] has $TV(P_1,P_2) = 1 = TV(P_1,P_3)$ (here $P_i$ is the measure associated having density $p_i$) and the [[KL divergence]]  is $+\infty$ between any two of these distributions, since each puts zero mass on places where the others place positive mass. 

The problem is that our intuition that $p_1$ and $p_2$ are closer than $p_2$ and $p_3$ comes from the underlying geometry of $\Re$. This motivates constructing [[optimal transport costs]] (a special case of which is the [[Wasserstein distance]]), which take advantage of the underlying geometry of the sample space. 

The [[Monge formulation]] is the strictest formulation of the optimal transport problem, giving rise to an optimization problem which may not have a solution. The Kantorovich formulation is a relaxation of Monge's formulation, resulting in [[optimal transport costs]]. 

