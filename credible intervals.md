The [[Bayesian statistics|Bayesian]] analogue of [[confidence intervals]]. A $(1-\alpha)$-credible interval is a region $C_\alpha$ to which the posterior assigns mass at least $1-\alpha$: 
$$

\int_{C_\alpha}\pi(\theta|X_1,\dots,X_n) d\theta \geq 1-\alpha.

$$
It's an interesting question to ask how "good" a credible interval is. After all, Bayesian statistics does not cash out it's value in terms of the long run performance of its methods. So in some sense, any credible interval is as good as any other - you have your prior, I have mine, and we compute our credible intervals. End of story. 

# Posterior contraction

Of course, in practice, even Bayesians want some sort of frequentist type guarantee for their methods. If we adopt a frequentist perspective ([[frequentist statistics]]) and assume that there's a true and fixed parameter $\theta^*$, we can define the ball $$
B_\eps = \{\theta: \norm{\theta - \theta^*}\leq \eps\},
$$for some appropriate norm. Then define $$
T(X^n) = \int_{B_\eps} \pi(\theta|X^n)\d\theta,
$$as the mass of $B_\eps$ under the posterior. We can then analyze $T(X^n)$ as a function of the data, i.e., we can treat it as a frequentist type object and analyze it's size. If the posterior converges to $\theta^*$, then $T(X^n)\to 1$. The rate of convergence is analyzed in terms of $\eps_n$. In particular, the rate of convergence is $\eps_n$ if $T(X^n)\to 1$ as $\eps_n\to0$. 

As a rule of thumb, in finite-dimensional parametric models, if the prior has positive mass on $\theta$, then the posterior is consistent and typically converges at rate $O(n^{-1/2})$. The [[Bernstein von-Mises theorem]] says that the under certain conditions on the prior, the posterior converges to a normal distribution centered at the [[MLE]] estimate of $\theta^*$. Outside the realm of applicability of the BvM theorem, however, there is no guarantee about the posterior. The posterior can converge to zero coverage in the [[Gaussian sequence model]] for instance.

# References 
- Larry Wasserman's excellent 705 lecture notes. #todo 