---
created: 2024-08-29
lastmod: 2024-09-29
---

Here we list [[concentration inequalities]] for scalar-valued random variables under various light-tailed conditions (which typically means that the [[MGF]] exists in some neighborhood).  This is contrast to [[heavy-tailed scalar concentration]], where we assume only a few moments. 

For rvs $X_1,\dots,X_n$ let $\overline{X}_n = \frac{1}{n}\sum_ {i=1}^n X_i$. 

Many of these concentration inequalities are proven using corresponding [[exponential inequalities]]. There are also [[time-uniform]] versions of these inequalities which stem from the [[sub-psi process]] given by the corresponding exponential inequality. 

# Bounded random variables 

## Hoeffding bound 
Let $X_1, \dots, X_n$ be independent with $a_i\leq X_i\leq b_i$. Hoeffding showed that 
$$
\Pr( |\overline{X}_n - \mu|\geq \eps)\leq 2\exp\left(\frac{-\eps^2n^2}{\sum_{i=1}^n (b_i - a_i)}\right).
$$
The natural one sided versions also exist. This is generalized by McDiarmid's inequality ([[bounded difference inequalities]]). 

## Bennett's inequality 
Hoeffding's bound doesn't use any information beside boundedness of the observations. It therefore must (implicitly) assume a worse case bound on the variance. If we know a bound on the variance, we can do better. Both Bennett's inequality and Bernstein's inequality use such information to tighten the bound. 

Let $X_1,\dots,X_n$ be independent with finite variance and one-sided boundedness, i.e., $X_i\leq B$ for some $B$. If $\sigma^2 = \sum_{i\leq n} \E[(X_i - \E X_i)^2]$ and $S = \sum_{k\leq n} (X_i- \E X_i)$ then 
$$
\Pr(S \geq \eps) \leq \exp\left(-\frac{\sigma^2}{B^2}h(B\eps/\sigma^2)\right),
$$
where $h(u) = ( 1 + u )\log(1 + u) - u$. If we assume that $|X_i|\leq B$ then we can get a bound on $|S|$. This trend of first presenting a result using only the boundedness of observations and then giving a variance-adaptive result is a common one, see [[from boundedness to variance adaptivity]]. 

If the $X_i$ have conditional mean $\mu$, then we can replace $\sigma^2$ with $\sum_{i\leq n} \E_{i-1}\norm{X_i - \E X_i}^2$ where $\E_{i-1}$ is the expectation conditional on the first $i-1$ observations. 

## Bernstein bound 1 
There are several bounds that go under the name "Bernstein bound". The most common is perhaps a relaxation of Bennett's bound and uses that 
$$
h(u) \geq \frac{u^2}{2(1 + u/3)},
$$
to show that 
$$
\Pr(S \geq \eps) \leq \exp\left(-\frac{\eps^2}{2(M + B\eps /3)}\right),
$$
where $M$ and $B$ are as above. Both Bennett's bound and Bernstein's bound are proven using the [[Chernoff method]]. 

There are two regimes in Bernstein's bound: A sub-Gaussian regime where the tail decays at a [[sub-Gaussian distributions|sub-Gaussian]] rate, and a sub-exponential regime where it decays at a [[sub-exponential distributions|sub-exponential rate]]. The former occurs when the contribution of $B\eps/3$ is small, so the tail decays as $\eps^2$. When $B\eps/3$ is large, the bound decays as $\eps$. 

## Empirical Bernstein bounds 
Empirical Bernstein bounds replace the oracle variance with an estimated variance. This is useful because the true variance is not always known. These bounds deserve their own page: [[empirical Bernstein bounds]]. 

# References 
- Concentration inequalities by Boucheron, Lugosi, and Massart. 