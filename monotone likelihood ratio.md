> [!Definition]
> A family of densities parameterized by real values $\theta$, $\calP = \{P_\theta: \theta\in\Theta\subset\Re$} has monotone likelihood ratio in $T(X)$ (some statistic of the data) if for any $\theta_1<\theta_2$, the likelihood ratio $\d P_{\theta_2}(x) / \d P_{\theta_1}(x)$ is well-defined and is a monotonically increasing function of $T(x)$. 

This might some an obscure property, but many families of distributions have the monotone likelihood ratio property. For eg: 
- One parameter [[exponential families]]
- Exponential and double exponential distributions 
- Logistic distributions 
- Uniform distributions 
- Hypergeometric distributions 

The MLR property is important in [[hypothesis testing]]: The [[Karlin-Rubin theorem]] extends the [[Neyman-Pearson lemma]] to MLR families. This makes the NP lemma significantly more practical, as testing point nulls vs point composites is really done in practice. 