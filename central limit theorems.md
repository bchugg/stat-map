CLTs concern the convergence in distribution of (some statistic of) data. They are foundational in [[statistical inference]] because they show that, for large enough sample sizes, we can treat data from an unknown or complicated distribution as though it comes from a nicer, well-behaved distribution (eg, a Gaussian). 

CLTs are asymptotic results. They are less exact than non-asymptotic results but typically require fewer assumptions. 

Examples: 
- [[Lindeberg-Feller CLT]]
- [[Lyapunov CLT]]

The first CLT ever proved was for binomial distributions by de Moivre. He showed that if $X_n\sim \text{Binomial}(n,p)$, then 
$$
\frac{X_n - np}{\sqrt{np(1-p)}} \to N(0,1).
$$
Of course, this has been significantly generalized by other CLTs. 