---
created: 2024-08-29
lastmod: 2024-09-02
---
A *Bernstein* bound is a kind of [[conc inequalities|concentration inequality]] that takes advantage of the variance of the distribution. They are usually part of a progression of bounds for random variables with bounded range. See [[from boundedness to variance adaptivity]]. 

_Empirical-Bernstein bounds_ replace knowledge of the variance with data-driven estimates of the variance. This is useful since we often don't know what the variance is. Ideally, such bounds can be shown to converge in the limit to a bound with width depending on the true variance —  i.e., they scale asymptotically with the true variance. 

Some examples: 

# Scalar-random variables 

The first empirical Bernstein bound was given by [Maurer and Pontil in 2009](https://arxiv.org/pdf/0907.3740). A second, tighter bound, was given by [Waudby-Smith and Ramdas](https://arxiv.org/pdf/2010.09686) using the betting approach to concentration (see [[estimating means by betting]]). These are very reminiscent of Bennett's bound ([[light-tailed scalar concentration#Bennett's bound|estimating means by betting]]). These are very reminiscent of Bennett's bound ([[light-tailed scalar concentration:Bennett's bound]]), but has a data-driven variance term. 

Let $X_1, X_2, ,\dots, X_n$ be iid random variables in $[0,1]$. The Maurer and Pontil bound reads that with probability $1-\delta$,
$$
\bigg|\frac{1}{n}\sum_i X_i - \E X_1 \bigg|\leq \sqrt{\frac{2\wh{\sigma}_n\log(2/\delta)}{n}} + \frac{7\log(1/\delta)}{3(n-1)},

$$
where $\wh{\sigma}_n = \frac{1}{n(n-1)}\sum_{i<j} (X_i- X_j)^2$ is the sample variance. The width of the bound, $W_n$ (the RHS above), has the limiting behavior $\sqrt{n} W_n \to \sigma\sqrt{2\log(4/\alpha)}$.

For the same setting, the bound by Waudby-Smith and Ramdas gives that for any $\lambda_n>0$, with probability $1-\delta$,
$$
\bigg|\frac{1}{n}\sum_i X_i - \E X_1\bigg| \leq \frac{\log(1/\alpha) + \psi_E(\lambda_n)\sum_{i\leq n} v_i}{\lambda_nn},
$$
for $v_i - \wh{\mu}_{i-1}$ where $\wh{\mu}_{i-1}$ is _any_ function based on $X_1,\dots,X_{i-1}$ (though one should think of it as roughly $\frac{1}{i}\sum_{j\leq i}X_i$). For the appropriate choice of $\lambda_n$ the width scales as $\sqrt{n} W_n \to \sigma\sqrt{2\log(2/\alpha)}$, which is optimal and has the same asymptotic variance as the Hoeffding bound ([[light-tailed scalar concentration#Hoeffding bound|light-tailed scalar concentration:Hoeffding bound]]).

Finally, betting techniques can yield other empirical-Bernstein bounds depending on the choice of predictable plug-in. These do not have closed-form solutions, but are often tighter. See [[estimating means by betting]]. 
# Random vectors 

We prove the following dimension-dependent empirical Bernstein bound in the paper [Time-uniform confidence spheres for means of random vectors](https://arxiv.org/abs/2311.08168). This was proven using the [[variational approach to concentration]]. It's an example of a time-uniform confidence sphere (see [[time-uniform confidence spheres]]). 

Let $X_1,X_2,\dots$ have conditional mean $\mu$ with $\norm{X_i} \leq 1/2$. Then, with probability $1-\alpha$, for all $t$: 
$$

\norm{\frac{\sum_{i\leq t} \lambda_i X_i}{\sum_{i\leq t}\lambda_i} - \mu} \leq \frac{\sqrt{d}\sum_{i\leq t} \psi_E(\lambda_i)\norm{X_i- \widehat{\mu}_{i-1}}^2 + 2\sqrt{d} + \sqrt{d}\log(1/\alpha)}{\frac{2}{3} \sum_{i\leq t}\lambda_i}.

$$

This is a [[time-uniform]] bound. Here $\widehat{\mu}_{i-1}$ is any predictable quantity, i.e., based on $X_1, X_2, \dots, X_{i-1}$. This is an unsatisfying bound for several reasons. First is the annoying factor of 3/2 in front of the bound. This hardly seems like it will be optimal. The second more significant drawback is the reliance of the bound on the dimension of the ambient space. An open question is to develop a dimension-free Bernstein bound. 

# Random matrices 

Wang and Ramdas develop an empirical Bernstein bound for random matrices. #todo 
