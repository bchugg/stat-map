We can recover many of the classical concentration inequalities of measure-theoretic probabilities in game-theoretic form (see [[game-theoretic probability]]).  

Fix a gamble space $(\Omega, \cZ)$ ([[game-theoretic probability#Gamble spaces, prices, and probabilities]]).  

# Markov's inequality 

Let $X:\Omega\to[0,\infty)$ and $\alpha>0$. If the gamble space is arbitrage-free and positive-linear, then  
$$\ov{\Pr}(X\geq \alpha) \leq \frac{\ov{\E}[X]}{\alpha}.$$
The proof even mimics the proof of the usual Markov's inequality [[Concentration Inequalities#Markov's inequality]].  Notice that $X/(\alpha \ov{\E}[X])\geq \ind(X\geq \alpha\ov{\E}[X])$ by case analysis. So 
$$\ov{\Pr}(X\geq \alpha \ov{\E}[X]) = \ov{\E}\ind(X\geq \alpha \ov{\E}X) \leq \ov{\E}\left[\frac{X}{\alpha \ov{\E}[X]}\right] = \frac{1}{\alpha \ov{\E}[X]} \ov{\E}[X] = \frac{1}{\alpha},$$
where we've used the monotonicity and scaling properties of [[game-theoretic expectations]]. 

# Chebyshev's inequality

The usual Chebyshev's inequality [[Concentration Inequalities#Chebyshev's inequality]] bounds the concentration of a random variable in terms of its means variance. Since there's no natural notion of mean or variance in GTP, we need to introduce it explicitly. 

Let $(\Omega, \cZ)$ be positive-linear. Suppose there exist $\mu,\sigma$ such that $\ov{\E}(X-\mu)^2 \leq \sigma^2$.  Then 
$$\ov{\Pr}(|X-\mu|\geq \alpha\sigma)\leq \frac{1}{\alpha^2}.$$ 



