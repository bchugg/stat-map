
Generic chaining is a method for proving [[maximal inequalities]]. It was invented by [Michel Talagrand](https://michel.talagrand.net/), whose beard I hope to be able to mimic some day. 

We are in the setting that was described in [[chaining]]. We are trying to obtain a maximal inequality for the [[sub-Gaussian process]] $(X_\theta)$, $\theta\in\Theta$. Chaining gave a bound of the form 
$$
\E\sup_\theta X_\theta \leq \sup_{\theta\in\Theta}\sum_{0\leq n\leq N} 2^{n/2}\rho(\theta, \Theta_n),
$$
where $\Theta_0\subset\Theta_1\subset\dots\subset \Theta_N=\Theta$ is a chain of sets approximating $\Theta$, where $|\Theta_n|\leq 2^{2^n}$.  
[[Dudley chaining]] moves the supremum inside the sum and then states the bound in terms of [[entropy number|entropy numbers]]. In generic chaining we leave the supremum outside the sum. 


