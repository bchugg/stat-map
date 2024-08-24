Suppose we have the wealth process of a gambler, $\calK_t = \prod_{i\leq t} S_t$. Such a process is common in, e.g., [[game-theoretic statistics]] and [[information theory]]. 

We are often interested in making the wealth grow over time (eg in [[game-theoretic hypothesis testing]]). A natural question is what sort of criteria should we use to measure the growth? 

Often one chooses bets in order to maximize the _log-wealth_, i.e., the expected value $\E[\log S_t]$. 

There are several reasons one might choose to do this: 
- In 1956, Kelly [pointed out that](https://www.princeton.edu/~wbialek/rome/refs/kelly_56.pdf) logarithmic returns add, hence the SLLN applies which makes it easier to reason about the behavior of the log-wealth over time. 
- 