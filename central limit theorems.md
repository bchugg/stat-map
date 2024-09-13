---
created: 2024-08-29
lastmod: 2024-09-02
---
CLTs concern the convergence in distribution of (some statistic of) data. They are foundational in [[statistical inference]] because they show that, for large enough sample sizes, we can treat data from an unknown or complicated distribution as though it comes from a nicer, well-behaved distribution (eg, a Gaussian). Under mild conditions (asymptotic negligibility) the set of limiting distributions are precisely the [[infinitely divisible distribution|infinitely divisible distributions]]. 

The first CLT ever proved was for binomial distributions by de Moivre in 1738. He showed that if $X_n\sim \text{Binomial}(n,p)$, then 
$$
\frac{X_n - np}{\sqrt{np(1-p)}} \to N(0,1).
$$
Of course, this has been significantly generalized by other CLTs. 

# Qualitative CLTs 

These are the "usual" CLTs—they state that some quantity converges in distribution to some limiting distribution. These are the results that are used in practice when constructing [[confidence intervals]] or doing [[hypothesis testing]] (eg the [[Wald test]] or the [[Wald interval]] are based on qualitative CLTs). 

Examples: 
- [[Lindeberg-Feller CLT]]
- [[Lindeberg-Levy CLT]]
- [[Lyapunov CLT]]

# Quantitative CLTs

Quantitative CLTs are often called [[Berry-Esseen bounds]]. They give explicit, non-asymptotic bounds on the deviation between distributions (eg between the sum of iid random variables and the normal). 

They are usually stated in terms of the [[KS distance]] between the distributions, though other metrics (usually ideal metrics; see [[distributional distance]]) can be used. 

- [[quantitative CLT template with ideal metrics]]
