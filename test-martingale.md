---
created: 2024-08-29
lastmod: 2024-09-02
---
A test martingale for a distribution $P$ is a nonnegative $P$-martingale with initial value 1. That is, it is a stochastic process $(M_t)_{t\geq 1}$ with $M_t\geq 0$ for all $t$, $M_1 = 1$ and 
$$
\E_P[M_t|\calF_{t-1}] \leq M_{t-1},
$$
where $(\calF_t)$ is the filtration to which $(M_t)$ is adapted.

Test martingales are common tools in [[game-theoretic probability]] and [[game-theoretic statistics]] where they represent fair bets under $P$. Often one generalizes the discussion of test martingales to [[e-process]], as they are bounded above by test martingales and thus also obey [[Ville's inequality]].  Both e-processes and test-martingales thus immediately yield [[sequential hypothesis testing]] for the null $H_0: P = P_0$: we reject when the process exceeds $1/\alpha$. This constitutes a level-$\alpha$ sequential test. 

Note that while test-martingales and e-processes are useful for defining sequential tests, they can also be considered bonafide measures of evidence on their own. Eg the larger a $P$-test-martingale grows over time, the more evidence this is against $P$. Thus they can be used not only for the [[Neyman-Pearson paradigm]] but also satisfy [[Fisher's paradigm]]. 

Often we are interested in statistical problems involving sets of distributions, e.g., [[testing by betting—composite vs composite|testing composite nulls]]. For such problems, it's useful to have a family of martingales. A test martingale _family_ for a set of distributions $\calP$ is a family of test martingales $(M^P)_{P\in \calP}$. 

Another useful classification: $M_t$ is a $P$-martingale iff 
$$

M_t / M_{t-1} = ( 1 + \phi(X_t)),

$$
where $\phi$ is a bounded odd-function. 

Interestingly, sometimes test-martingales will appear in reduced filtrations and not in the original filtration. See [[coarsened filtrations can increase power]] and [[testing exchangeability]]. 



