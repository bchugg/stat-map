---
lastmod: 2026-05-26
created: 2024-10-24
---

The [[Neyman-Pearson lemma]] says that the likelihood ratio test is the [[uniformly most powerful test]] at a given sample size. But the likelihood ratio is a nonnegative [[supermartingale]], hence an [[e-process]], so it provides type-I error control at all times, and is a [[sequential hypothesis testing|sequential test]]. How does it perform as such? 

Let $(X_t)$ be a stream of data and let $L_t = \prod_{i\leq t} q(X_1) / p(X_1)$ be the likelihood ratio at time $t$ for a simple alternative $Q$ with density $q$ against a simple null $P$ with density $p$. Suppose you have desired type-I error of $\alpha$ (false positives) and desired type-II error of $\beta$ (false negatives). Then there exist thresholds $t_1(\alpha,\beta)$ and $t_2(\alpha,\beta)$ such that if you reject the null when $L_t\geq t_1(\alpha,\beta)$ and reject the alternative when $L_t \geq t_2(\alpha,\beta)$ such that the test is optimal. Here optimality means that, among all tests with the same (or lower) type-I and type-II error rates, the SPRT requires the fewest number of samples in expectation. 

Wald introduced this test in the 1930s, and it was proved optimal by [Wald and Wolfowitz in 1948](https://projecteuclid.org/journals/annals-of-mathematical-statistics/volume-19/issue-3/Optimum-Character-of-the-Sequential-Probability-Ratio-Test/10.1214/aoms/1177730197.full). 

Unfortunately, $t_1$ and $t_2$ are often impossible to solve for, so approximations are necessary. One usually sets $t_1 = (1 - \beta)/\alpha$ and $t_2 = \beta / (1-\alpha)$. Note that if we set $\beta=0$, meaning we want a power 1 test (rejects the null with probability 1 in the limit under the alternative), then we recover the threshold $\log(1/\alpha)$ for rejecting the null, which is what one would usually obtain for sequential testing with [[Ville's inequality]]. 

# Reading 
- [Optimum Character of the Sequential Probability Ratio Test](https://projecteuclid.org/journals/annals-of-mathematical-statistics/volume-19/issue-3/Optimum-Character-of-the-Sequential-Probability-Ratio-Test/10.1214/aoms/1177730197.full). 
- Improving approximate SPRT: https://arxiv.org/pdf/2410.16076.  When the distributions are discrete, the thresholds $t_1(\alpha)$ and $t_2(\beta)$ may not be precisely attainable, in which case the test will be overly conservative.  