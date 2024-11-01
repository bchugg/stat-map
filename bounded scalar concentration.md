---
created: 2024-08-29
lastmod: 2024-10-31
---

Here we list [[concentration inequalities]] for scalar-valued random variables that are bounded with probability 1 (sometimes only bounded on one side). This in contrast to [[light-tailed, unbounded scalar concentration]] which does not assume boundedness and [[heavy-tailed scalar concentration]], where we assume only a few moments. 

Many of these concentration inequalities are proven using corresponding [[exponential inequalities]]. There are also [[time-uniform]] versions of many of these inequalities which stem from the [[sub-psi process]] given by the corresponding exponential inequality. 

# Bounded random variables 

## Hoeffding's bound 
Let $X_1,\dots,X_n$ be independent and set $S_n = \sum_{i\leq n} (X_i - \E X_i)$. Suppose $a_i\leq X_i\leq b_i$. Hoeffding showed that, for any $t$,  
$$
\Pr\left( S_n\geq t\right)\leq \exp\left(\frac{-2t^2}{\sum_{i=1}^n (b_i - a_i)}\right).
$$
The natural two sided version also exists. This is proved with the [[Chernoff method]]. Hoeffding's bound is generalized by McDiarmid's inequality ([[bounded difference inequalities]]). 

Note that this is suboptimal. To see this, note that $\frac{1}{\sqrt{n}}\sum_i (X_i - \E X_i)$ is roughly $N(0,\sigma^2)$ by the [[Lindeberg-Levy CLT]], and $\Pr(N(0,1)\geq u) \asymp \frac{1}{u}e^{-u^2/2}$. So there is a missing factor of $1/t$ in the  bound. This is well-known and is called [the missing factor in Hoeffding's bound](http://www.numdam.org/item/AIHPB_1995__31_4_689_0.pdf). Hoeffding's bound can therefore be improved with a more careful analysis (see Talagrand's bound below). 

Hoeffding's bound is also suboptimal in a more straightforward way: If we take $t = cS_n$ for $c>1$, then $\Pr(S_n > t) = 0$ but the bound does not capture this behavior. 

## Bennett's inequality 
Hoeffding's bound doesn't use any information beside boundedness of the observations. It therefore must (implicitly) assume a worse case bound on the variance. If we know a bound on the variance, we can do better. Both Bennett's inequality and Bernstein's inequality use such information to tighten the bound. 

Let $X_1,\dots,X_n$ be independent with finite variance and one-sided boundedness, i.e., $X_i\leq B$ for some $B$. If $\sigma^2 = \sum_{i\leq n} \E[(X_i - \E X_i)^2]$ and $S_n = \sum_{k\leq n} (X_i- \E X_i)$ then 
$$
\Pr(S_n \geq t) \leq \exp\left(-\frac{\sigma^2}{B^2}h(Bt /\sigma^2)\right),
$$
where $h(u) = ( 1 + u )\log(1 + u) - u$. If we assume that $|X_i|\leq B$ then we can get a bound on $|S|$. This trend of first presenting a result using only the boundedness of observations and then giving a variance-adaptive result is a common one, see [[from boundedness to variance adaptivity]]. 

If the $X_i$ have conditional mean $\mu$, then we can replace $\sigma^2$ with $\sum_{i\leq n} \E_{i-1}\|X_i - \E X_i\|^2$ where $\E_{i-1}$ is the expectation conditional on the first $i-1$ observations. 

Like Hoeffding's bound, Bennett's inequality also does not recover the missing factor of $1/t$ that we expect from the central limit theorem. This is because it is also based on the [[Chernoff method]], but bounding the exponential function a little differently than does Hoeffding's bound to take advantage of the variance information. 

## Bernstein bound 1 
There are several bounds that go under the name "Bernstein bound". The most common is perhaps a relaxation of Bennett's bound and uses that 
$$
h(u) \geq \frac{u^2}{2(1 + u/3)},
$$
to show that 
$$
\Pr(S_n \geq t) \leq \exp\left(-\frac{t^2}{2(\sigma^2 + B t /3)}\right),
$$
where $M$ and $B$ are as above. We can of course obtain two-sided versions of Bennett's and Bernstein's bound if we assume two-sided boundedness ($|X_i|\leq B$), apply the bound twice and use a union bound. 

There are two regimes in Bernstein's bound: A sub-Gaussian regime where the tail decays at a [[sub-Gaussian distributions|sub-Gaussian]] rate, and a sub-exponential regime where it decays at a [[sub-exponential distributions|sub-exponential rate]]. The former occurs when the contribution of $B t/3$ is small relative to $\sigma^2$ so the tail decays as $t^2$. When $B t/3$ is large, the bound decays as $t$. Therefore, if we have good a priori knowledge of small variance, Bernstein's (and Bennett's) can be a big improvement over Hoeffding, scaling as $t^2/\sigma^2$ instead of $t^2/(nB^2)$.  

## Hoeffding's bound remastered 
It is somewhat of a shame that Hoeffding's name came to be associated with the first bound above, since this is much weaker than the following more general result that he proved in his [famous 1963 paper](https://www.jstor.org/stable/2282952), which recovers both Bennett's and Bernstein's bounds. 

If $X_1,\dots,X_n$ are iid with variance $\sigma^2$ and lying in $(\infty, c]$, then 
$$
\Pr(S_n \geq nt) \leq \exp\left(-n \kl\left(\frac{\sigma^2 + tc}{\sigma^2 + c^2} \bigg \| \frac{\sigma^2}{\sigma^2 + c^2}\right)\right), \quad t\leq c,
$$
where $\kl$ denotes the binary entropy function: $\kl(p\| q) = p\log\frac{p}{q} + (1-p)\log\frac{1-p}{1-q}$. If $p>1$ we interpret $\kl(p\|q)$ as infinity, meaning the bound cuts off at that point. Thus, this bound circumvents one of the drawbacks mentioned above. 

This is the sharpest bound using the [[Chernoff method]]. We can recover the first Hoeffding bound by assuming worst-case variance. 

## Bentkus' inequality 
#todo 

## Empirical Bernstein bounds 
Empirical Bernstein bounds replace the oracle variance with an estimated variance. This is useful because the true variance is not always known. These bounds deserve their own page: [[empirical Bernstein bounds]]. 

# References 
- Concentration inequalities by Boucheron, Lugosi, and Massart. 