A test martingale for a distribution $P$ is a nonnegative $P$-martingale with initial value 1. That is, it is a stochastic process $(M_t)_{t\geq 1}$ with $M_t\geq 0$ for all $t$, $M_1 = 1$ and 
$$\E[M_t|\cF_{t-1}] \leq M_{t-1}.$$ where $(\cF_t)$ is the filtration to which $(M_t)$ is adapted. 

Test martingales are common tools in [[game-theoretic probability]] and [[game-theoretic statistics]] where they represent fair bets under $P$. Often one generalizes the discussion of test martingales to [[e-processes]], as they are bounded above by test martingales and thus also obey [[Ville's inequality]]. 

Often we are interested in statistical problems involving sets of distributions, e.g., composite nulls. A test martingale _family_ for a set of distributions $\bs{P}$ is a family of test martingales $(M^P)_{P\in \bs{P}}$. 

