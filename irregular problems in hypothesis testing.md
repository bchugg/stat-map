
The validity of many test statistics depends on various regularity conditions. For instance, Wilk's famous theorem states that -2 times the log-likelihood converges to a $\chi^2$ distribution, which provides a test statistic for simple nulls and simple alternatives. But what if these regularity conditions don't hold? Such problems are called irregular problems. 

There are methods to handle such irregular problems; [[universal inference]] is one such method. 

Some examples of irregular problems: 
- **Mixtures of Gaussians** Suppose we want to test whether the samples come from a mixture of $k_0$ or $k_1$ Gaussians with $k_0<k_1$. This is an irregular problem (even for $k_1 = k_0 +1$). 
- **Shape constraints** For instance, testing whether a given sample is from a [[log-concave distribution]]. 
- **Latent variables** Problems with latent variables, such as: 
	- testing if a [[hidden Markov model]] has $\leq k$ states
	- testing whether a factor model has $\leq k$ factors
	- [[conditional independence testing]]