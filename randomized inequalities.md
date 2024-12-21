---
created: 2024-08-29
lastmod: 2024-12-21
---

Many [[basic inequalities]] are unimprovable ([[optimality of Markov and Chebyshev]]), in the sense that there are distributions which make them equalities. However, if you enlarge the probability space via [[external randomization]], then you can make some of these inequalities tighter. 

All of these examples come from the paper [Randomized and exchangeable improvements of Markov’s, Chebyshev’s and Chernoff’s inequalities](https://arxiv.org/pdf/2304.02611). 
## Markov 
For $X$ nonnegative, and $U\sim \unif(0,1)$ independent of $X$, 
$$
\Pr( X \geq Ut ) \leq \frac{\E[X]}{t},
$$
which strengthens Markov's inequality. We emphasize that $U$ must be independent of $X$.  There is also an additive version: For $t>0$ and $U\sim \unif(0,t)$, 
$$
\Pr( X \geq t - U) \leq \frac{ \E X}{t},
$$
which again strengthens Markov. 

## Chebyshev 
For $X_1,\dots,X_n$ iid and $U\sim\unif(0,1)$ independent of $X_i$, 
$$
\Pr\left(|\ov{X}_n - \E X|\geq k\sigma \sqrt{\frac{U}{n}}\right) \leq \frac{1}{k^2},
$$
which strengthens [[basic inequalities#Chebyshev's inequality]]. 

## Hoeffding 
For $X_1,\dots,X_n$ and $U\sim \unif(0,1)$ independent of $X_i$, we have 
$$
\Pr\left(|\ov{X}_n - \E X| \geq \sigma\sqrt{\frac{2\log(1/\alpha)}{n}} + \sigma\frac{\log U}{\sqrt{2n\log(1/\alpha)}}\right)\leq \alpha,
$$
which is stronger than [[bounded scalar concentration#Hoeffding's bound]] since $\log U <0$. The proof works by applying the [[Chernoff method]] to the randomized Markov inequality above. In the same, many of the other bounds in [[bounded scalar concentration]] can be randomized, including [[bounded scalar concentration#Bentkus' inequality]] and [[bounded scalar concentration#Hoeffding's bound remastered]]. 

## Ville 
There also exists a randomized version of [[Ville's inequality]], though it requires careful interpretation. For a nonnegative [[supermartingale]] with $(S_n)$ with $\E S_0\leq 1$, any stopping time $\tau$ and and $U\unif(0,1)$ drawn independently of $(S_n)$ and $\tau$, we have 
$$
\Pr( S_\tau \geq U/\alpha)\leq \alpha.
$$
In terms of [[sequential hypothesis testing]], this should be interpreted as using [[test-martingale|test martingales]] in the usual way. If one stops at time $\tau$ for any reason and has not yet rejected (the budget runs out, say), then one can do a final test and check if the wealth is greater than $U/\alpha$ instead of just $1/\alpha$. If so, then one can reject. However, one cannot do this and then continue the procedure—this has to be the final step. 





