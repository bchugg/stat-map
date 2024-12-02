---
created: 2024-08-29
lastmod: 2024-12-02
---

Some basic probabilistic inequalities. Used mostly under the hood to build more sophisticated [[concentration inequalities]], but also useful in other scenarios. 

## Markov's inequality 
For a nonnegative random variable $X$ and parameter $a>0$, Markov's inequality states that 
$$
\Pr(X\geq a)\leq \frac{\E[X]}{a}.
$$
Clearly the condition that $X\geq 0$ is necessary: consider any random variable which has negative mean but some positive mass. 

The proof of Markov's is easy: 
$$
\E X = \int_0^\infty x dP \geq \int_a^\infty xdP \geq a\int_a^\infty dP = a\Pr(X\geq a).
$$
Markov's inequality is tight in the sense that there are distributions for which the inequality holds with equality. But it is not very interesting in the sense that it doesn't provide interesting concentration behavior. However, it's a cornerstone in more sophisticated concentration techniques, which often rely on applying Markov's inequality to the random variable 
$$
\exp\left(\lambda \sum_{i\leq n} X_i\right).
$$
(See the Chernoff method below, which is precisely this strategy.) 

You can strengthen Markov by writing 
$$
\Pr(X\geq a)\leq \frac{\E[X\ind\{X\geq t\}]}{a},
$$
for any (not necessarily nonnegative) random variable $X$. To prove this just apply expectations to the inequality $\ind\{x\geq t\} \leq \frac{x}{t}\ind\{x\geq t\}$ which holds for all $x$ and all $t\geq 0$. 

Some notes and pointers: 
- For achievability and optimality see [[optimality of Markov and Chebyshev]]. 
- Markov's inequality can also be derived using convex optimization arguments ([[concentration via convex optimization]]). 
- [[Ville's inequality]] is a time-uniform extension of Markov's inequality for nonnegative supermartingales (or reverse submartingales, as the case may be). Just as Markov's inequality is used as a foundation for concentration inequalities, Ville's inequality is used as a foundation for [[time-uniform]] concentration inequalities. 
- There is also a randomized Markov's inequality ([[randomized inequalities#Markov|randomized inequalities:Markov]]) which uses [[external randomization]].  
- An intuitive explanation of Markov's inequality is the [[optimization perspective on Markov's inequality]]. 

## Paley-Zygmund inequality 
A lower bound, with a similar flavor to Markov's inequality. If $X$ is non-negative, then for all $\theta\in(0,1)$, 
$$
\Pr(X\geq \theta \E X)\geq (1-\theta)^2 \frac{(\E X)^2}{\E X^2}.
$$
This is useful for proving lower bounds. Similarly to Markov's inequality, it is rarely applied to $X$ directly, but typically some transformation of $X$. 

## Chebyshev's inequality 
Chebyshev's inequality is simply Markov's inequality applied to $(X-\mu)^2$. For $a>0$, 
$$
\Pr(X-\mu\geq a)\leq \Pr(|X-\mu| \geq a) = \Pr(|X-\mu|^2 \geq a^2) \leq \frac{\Var(X)}{a^2}.
$$
Chebyshev's inequality gives the first flavor of concentration. If $X_1, X_2, \dots, X_n$ are iid with mean $\mu$, then Chebyshev gives 
$$
\Pr(|\ov{X}_n - \mu|\geq a) \leq \frac{\Var(\ov{X_n})}{a^2} = \frac{\Var(X)}{na^2},
$$
where $\ov{X}_n = n^{-1}\sum_i X_i$. Making the RHS equal to $\delta$ gives with probability $1-\delta$,
$$
|\ov{X}_n-\mu| \leq \sqrt{\Var(X) / (\delta n)}.
$$
The _rate_ of concentration here is actually not too bad, it scales with $\sqrt{n}$ which is what we expect in many scenarios. However, the dependence on $1/\sqrt{\delta}$ is not great. We'd rather have $\log(1/\delta)$, which is an exponential improvement over $1/\sqrt{\delta}$. The Chernoff method gives us this sort of dependence. 

Note that the strict iid assumption is not necessary for the above bounds. If we have $\Var(X_i)\leq v^2$ for all $i$ and $\Cov(X_i, X_j)\leq 0$ (uncorrelated or reverse-correlated) for all $i\neq j$, then $\Var(\ov{X}_n) \leq \sigma^2/n$ so the same discussion applies after swapping $\Var(\ov{X}_n)$ with $v^2$. See [[negative correlation can improve concentration]] for more. 

Notes: 
- Chebyshev's inequality is a specific instance of the [[method of moments for concentration]].
- The [[time-uniform]] extension of Chebyshev's inequality is the [[martingale concentration#Dubins-Savage inequality]]. 
- For achievability and optimality see [[optimality of Markov and Chebyshev]]. 

## Cantelli's inequality 
Cantelli's inequality is a one-sided improvement to Chebyshev's inequality. For any random variable $X$ with mean $\mu$ and variance $\sigma^2$, for any $t\geq 0$, write 
$$
\Pr(X -\mu\geq a) \leq \Pr( (X - \mu + t)^2 \geq (t + a)^2), 
$$
so by Chebyshev, 
$$
\Pr( X - \mu\geq a) \leq \inf_{t\geq 0} \frac{\sigma^2+t^2}{(t + a)^2}  = \frac{\sigma^2}{\sigma^2 + a^2}.
$$
which is Cantelli's inequality. This was proved using [[concentration via convex optimization]]. 

## Chernoff method 
The Chernoff method applies Markov's inequality to the nonnegative random variable $e^{\lambda X}$, and then chooses $\lambda$ to optimize the bound. More detail is given in [[Chernoff method]] (also called the Cramer-Chernoff method). 

