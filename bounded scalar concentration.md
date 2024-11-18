---
created: 2024-08-29
lastmod: 2024-11-17
---

Here we list [[concentration inequalities]] for scalar-valued random variables that are bounded with probability 1 (sometimes only bounded on one side). This in contrast to [[light-tailed, unbounded scalar concentration]] which does not assume boundedness and [[heavy-tailed concentration]], where we assume only a few moments. 

Many of these concentration inequalities are proven using corresponding [[exponential inequalities]]. There are also [[time-uniform]] versions of many of these inequalities which stem from the [[sub-psi process]] given by the corresponding exponential inequality. 

## Hoeffding's bound 
Let $X_1,\dots,X_n$ be independent and set $S_n = \sum_{i\leq n} (X_i - \E X_i)$. Suppose $a_i\leq X_i\leq b_i$. Hoeffding showed that, for any $t$,  
$$
\Pr\left( S_n\geq t\right)\leq \exp\left(\frac{-2t^2}{\sum_{i=1}^n (b_i - a_i)}\right).
$$
The natural two sided version also exists. This is proved with the [[Chernoff method]]. Hoeffding's bound is generalized by McDiarmid's inequality ([[bounded difference inequalities]]). 

Hoeffding's bound suboptimal in a somewhat cheap and straightforward way: If we take $t = cS_n$ for $c>1$, then $\Pr(S_n > t) = 0$ but the bound does not capture this behavior. However, it's also suboptimal in a more fundamental way, namely that there's a missing factor of $1/t$, which can be seen by appealing to [[central limit theorems]]. See [[the missing factor in Hoeffding's bounds]]. This factor is recovered by Talagrand's inequality and Bentkus' inequality below.

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

There are two regimes in Bernstein's bound: A sub-Gaussian regime where the tail decays at a [[sub-Gaussian distributions|sub-Gaussian]] rate, and a sub-exponential regime where it decays at a [[sub-exponential distributions|sub-exponential rate]]. The former occurs when the contribution of $B t/3$ is small relative to $\sigma^2$ so the tail decays as $t^2$. When $B t/3$ is large, the bound decays as $t$. Therefore, if we have good a priori knowledge of small variance, Bernstein's (and Bennett's) inequality can be a big improvement over Hoeffding, scaling as $t^2/\sigma^2$ instead of $t^2/(nB^2)$.  

This result was first presented by Bernstein in 1927. It was not until 1962 that this was [sharpened by Bennett](https://www.tandfonline.com/doi/abs/10.1080/01621459.1962.10482149), which resulted in Bennett's inequality above.  

## Hoeffding's bound remastered 
It is somewhat of a shame that Hoeffding's name came to be associated with the first bound above, since this is much weaker than the following more general result that he proved in his [famous 1963 paper](https://www.jstor.org/stable/2282952), which recovers both Bennett's and Bernstein's bounds. 

If $X_1,\dots,X_n$ are iid with variance $\sigma^2$ and lying in $(\infty, c]$, then 
$$
\Pr(S_n \geq t) \leq \exp\left(-n \kl\left(\frac{\sigma^2 + \frac{t}{n}c}{\sigma^2 + c^2} \bigg \| \frac{\sigma^2}{\sigma^2 + c^2}\right)\right), 
$$
where $\kl$ denotes the binary entropy function: $\kl(p\| q) = p\log\frac{p}{q} + (1-p)\log\frac{1-p}{1-q}$. If $p>1$ we interpret $\kl(p\|q)$ as infinity, meaning the bound cuts off at that point. Thus, this bound circumvents one of the drawbacks mentioned above. 

This is the sharpest bound using the [[Chernoff method]]. We can recover the first Hoeffding bound by assuming worst-case variance. 

## Talagrand's inequality 
Talagrand's inequality improves Hoeffding's inequality above by recovering the missing factor of $t$. If $X_1,\dots,X_n$ are iid with variance $\sigma^2$ and lying in $(\infty, c]$, then 
$$
\Pr(S_n \geq t) \leq \left(\theta\left(\frac{t}{\sigma}\right) + \frac{Bc}{\sigma}\right)\exp\left(-n \kl\left(\frac{\sigma^2 + \frac{t}{n}c}{\sigma^2 + c^2} \bigg \| \frac{\sigma^2}{\sigma^2 + c^2}\right)\right), \quad t\leq \frac{\sigma^2}{Bc},
$$
for some constant $B$, where 
$$
\theta(x) = \frac{1}{\sqrt{2\pi}} e^{x^2/2}\int_x^\infty e^{-u^2/2}\d u,
$$
which is of the order $\sigma/t$. Therefore, for $t\leq \sigma^2/(Bc)$, we have $Bc/\sigma<\sigma/t$. Hence the multiplier on the left hand side of the exponential is of the order $1/t$, which is clearly an improvement over Hoeffding's bound above. 

## Bentkus' inequality 
Bentkus' inequality is another way to recover the missing factor of $t$. The approach is significantly different from Talagrand's, and is based on [[interpolating between Markov and Chernoff]]. Instead of applying Markov's inequality to the exponential, we apply it to the function $h_\alpha(x) = ( 1 + x/\alpha)_+^\alpha$ for any $\alpha \geq 0$ and obtain, for $X_1,\dots,X_n$ independent with finite variance, 
$$
\Pr(S_n \geq t) \leq \inf_{x\leq t} \frac{\E (S_n - x)_+^\alpha}{(t - x)_+^\alpha}.
$$
The right hand side can be bounded by considering the worst case random variables. If $\Var(X_i) \leq \sigma_i^2$ and $X_i \leq c$, then defining $G_i$ with $\Pr(G_i = - \sigma_i^2/c) = c^2 / (\sigma_i^2 + c^2)$ and $\Pr ( G_i = c) = 1 - \Pr(G_i = \sigma_i^2/c)$, we obtain that 
$$
\Pr(S_n \geq t) \leq \inf_{x\leq t} \frac{\E (\sum_i G_i - x)_+^\alpha}{(t - x)_+^\alpha}.
$$
This is not a closed-form bound, but it can be computed. See eg [here](http://www.numdam.org/article/AIHPB_2014__50_1_15_0.pdf) and references therein. 


## Empirical Bernstein bounds 
Empirical Bernstein bounds replace the oracle variance with an estimated variance. This is useful because the true variance is not always known. These bounds deserve their own page: [[empirical Bernstein bounds]]. 

# References 
- Concentration inequalities by Boucheron, Lugosi, and Massart. 
- [On the Bennett-Hoeffding inequality](http://www.numdam.org/article/AIHPB_2014__50_1_15_0.pdf) by Pinelis. 
- [On Hoeffding's inequalities](https://arxiv.org/pdf/math/0410159) by Bentkus. 