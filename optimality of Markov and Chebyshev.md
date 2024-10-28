---
lastmod: 2024-10-27
created: 2024-10-21
---

Is [[basic inequalities#Markov's inequality]] optimal? In a somewhat trivial sense, no. Suppose $X\geq 0$ has mean $\mu$. Consider $t = \mu/2$. By Markov, $\Pr( X\geq t) \leq \mu / t = 2$, which is trivial. Since probabilities, are bounded by 1 we can always write 
$$
\Pr( X\geq t) \leq \min\{\mu/t, 1\}.
$$
We can also arrive at this conclusion in a slightly more interesting way. For any nonrandom $v\geq 0$, write $\Pr(X\geq t) = \Pr( X + v\geq t + v) \leq (\mu + v)/ (t + v)$. Therefore, 
$$
\Pr(X\geq t)\leq \inf_{v\geq 0} \frac{\mu + v}{t + v}.
$$
Optimizing over $v$ gives $\min\{u/t, 1\}$ on the right hand side. 

## Achieving Markov 
The [[optimization perspective on Markov's inequality]] demonstrates (though it can of course be proved more directly) that the distributions which attain Markov's inequality take two values. More precisely, if $X\geq 0$ and $\Pr(X \geq a) = \mu/a$ then $X$ takes the value 0 and $a$. Consequently, the equality can hold only for a single threshold. That is, no distribution can attain $\Pr( X\geq t) = \mu / t$ for all $t>0$. 

Another way to state the optimality is that, for $t\geq 1$,  
$$
\sup_{X\geq 0: \E X=1} \Pr(X\geq t) = \frac{1}{t}.
$$
This has consequences for [[concentration inequalities]]. In particular, if $X_1$ and $X_2$ are iid and each take two values, then $X_1 + X_2$ can take three values. Therefore, _Markov's inequality cannot be tight for more than one random variable_. 

## Achieving Chebyshev
Since $\Pr( | X - \mu|^t \geq t^2) = \Pr(|X - \mu|\geq t)$ for $t>0$, Chebyshev's inequality is obtained if Markov is attained by $|X - \mu|$. This implies that random variables $X$ attaining equality in Chebyshev's inequality can take 3 values:  $| X - \mu| = 0$, and $| X - \mu| =a$ for some $a$. That is, $X =\mu$, $X = a + \mu$, and $X = -a + \mu$. 

As above, if $X_1, X_2$ are iid and each take two values, then $X_1 + X_2$ can take three values. This implies that Chebyshev _might_ be tight for sums of two variables. But if $X_3$ is a third iid rv, then $X_1 + X_2 + X_3$ can take four values, meaning that _Chebyshev's inequality cannot be tight for more than two random variables_. This was first proved by Ghosh and Meedenin 1977: [On the non-attainability of Chebyshev bounds](https://www.tandfonline.com/doi/pdf/10.1080/00031305.1977.10479191). 