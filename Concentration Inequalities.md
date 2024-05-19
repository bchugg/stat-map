
Here we focus on concentration of scalar random variables. See [[multivariate concentration]] for the more general setting. See also [[matrix inequalities]]. 

Here we work in measure-theoretic probability spaces, but see also [[game-theoretic concentration inequalities]]. 

Here we state some very basic tools used in concentration, but mostly this is a high-level pointer to more specific concentration bounds. In particular, see
[[light-tailed scalar concentration]]
[[heavy-tailed scalar concentration]] 



# Basic tools 

Here are some basic tools (used mostly as pointers) in the scalar setting. 

## Markov's inequality 

For a nonnegative random variable $X$ and parameter $a>0$, Markov's inequality states that 
$$\Pr(X\geq a)\leq \E[X]/a.$$
  The proof is easy: 
  $$\E X = \int_0^\infty x dP \geq \int_a^\infty xdP \geq a\int_a^\infty dP = a\Pr(X\geq a).$$
Markov's inequality is tight in the sense that there are distributions for which the inequality holds with equality. But it is not very interesting in the sense that it doesn't provide interesting concentration behavior. However, it's a cornerstone in more sophisticated concentration techniques. 

There is also a game-theoretic version: [[game-theoretic concentration inequalities#Markov's inequality]]. [[Ville's inequality]] is a time-uniform extension of Markov's inequality for nonnegative supermartingales (or reverse submartingales, as the case may be). 

There is also a randomized Markov's inequality [[randomized inequalities#Markov]] which uses [[external randomization]]. 

An intuition explanation of Markov's inequality is the [[optimization perspective on Markov's inequality]]. 
## Chebyshev's inequality 

Chebyshev's inequality is simply Markov's inequality applied to $(X-\mu)^2$. For $a>0$, 
$$\Pr(|X-\mu| \geq a) = \Pr(|X-\mu|^2 \geq a^2) \leq \frac{\Var(X)}{a^2}.$$
Chebyshev's inequality gives the first flavor of concentration. If $X_1, X_2, \dots, X_n$ are iid with mean $\mu$, then Chebyshev gives 
$$\Pr(|\ov{X}_n - \mu|\geq a) \leq \frac{\Var(\ov{X_n})}{a^2} = \frac{\Var(X)}{na^2},$$
where $\ov{X}_n = n^{-1}\sum_i X_i$. Making the RHS equal to $\delta$ gives with probability $1-\delta$, $|\ov{X}_n-\mu| \leq \sqrt{\Var(X) / (\delta n)}.$ The _rate_ of concentration here is actually not too bad, it scales with $\sqrt{n}$ which is what we expect in many scenarios. However, the dependence on $1/\sqrt{\delta}$ is not great. We'd rather have $\log(1/\delta)$. The Chernoff method gives us this sort of dependence, so we turn to that next. 
## Chernoff method 

The alck 

