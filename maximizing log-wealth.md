---
created: 2024-08-29
lastmod: 2024-09-02
---

Suppose we have the wealth process of a gambler, $\calK_t = \prod_{i\leq t} S_t$. Such a process is common in, e.g., [[game-theoretic statistics]], [[information theory]], and [[portfolio optimization]]. 

We are usually interested in making the wealth grow over time (eg in [[game-theoretic hypothesis testing]]). A natural question is what sort of criteria should we use to measure the growth? 

Often one chooses bets in order to maximize the _log-wealth_, i.e., the expected value $\E[\log\calK_t]$. This is also called [[Kelly betting]]. 

There are several reasons one might choose to do this: 
- In 1956, Kelly [pointed out that](https://www.princeton.edu/~wbialek/rome/refs/kelly_56.pdf) logarithmic returns add, hence the SLLN applies which makes it easier to reason about the behavior of the log-wealth over time. 
- In 1961, [Breiman showed that](http://stat.wharton.upenn.edu/~steele/Resources/FTSResources/KellyBreiman/Breiman61.pdf) in iid settings, maximizing the log-wealth leads to the reaching a desired threshold ($1/\alpha$ say, for [[hypothesis testing]] purposes) as fast as possible, without risking all of your wealth at any time (which can happen if one maximizes $\E[\calK_t]$ say). 