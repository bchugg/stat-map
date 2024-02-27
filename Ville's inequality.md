Let $M=(M_t)$ be a $P$-supermartingale. Ville's inequality is a time-uniform version of Markov's inequality ([[Concentration Inequalities#Markov's inequality]]), stating that 
$$\Pr(\exists t\geq 1: M_t \geq x)\leq \frac{\E[M_1]}{x},$$
for all $x>0$. Note this bound is _uniform over all time_. If we take $x = 1/\alpha$, then this says that the probability that $M$ will _ever_ exceed $1/\alpha$ is at most $\E[M_1]/x$. 

Ville's inequality can also be written as 
$$\forall \tau: \Pr(M_\tau \geq x) \leq \frac{\E[M_1]}{x},$$
where $\tau$ represents a [[stopping-time]]. This is what enables statistical inference procedures based on Ville's inequality to be valid at arbitrary stopping times (which are data dependent). 


Ville's inequality also implies the classical result that a nonnegative supermartingale will reach infinity with probability 0. Let $(M_t)$ be a nonnegative supermartingale and define the event $A_k = \{\sup_t M_t \geq 2^k\}$. By Ville, $\Pr(A_k) \leq 2^{-k} \E[M_1]$. Since the events $(A_k)$ are monotonically decreasing, i.e., $A_{k+1} \subset A_k$ for all $k$, we have 
$$\Pr(\sup_t M_t = \infty) = \Pr(\cap_{k\geq 1}A_k) = \lim_k \Pr(A_k) = \lim_k 2^{-k} \E[M_1]=0.$$
Much of [[game-theoretic statistics]] relies on Ville's inequality, where we often construct some [[test-martingale]] or [[e-process]] under the null. Ville's implies that this process is unlikely to ever become large. Thus, if it does became large, this is [[evidence against the null]]. 