

Ville's inequality also implies the classical result that a nonnegative supermartingale will reach infinity with probability 0. Let $(M_t)$ be a nonnegative supermartingale and define the event $A_k = \{\sup_t M_t \geq 2^k\}$. By Ville, $\Pr(A_k) \leq 2^{-k} \E[M_1]$. Since the events $(A_k)$ are monotonically decreasing, i.e., $A_{k+1} \subset A_k$ for all $k$, we have 
$$\Pr(\sup_t M_t = \infty) = \Pr(\cap_{k\geq 1}A_k) = \lim_k \Pr(A_k) = \lim_k 2^{-k} \E[M_1]=0.$$
