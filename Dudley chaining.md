---
created: 2024-08-29
lastmod: 2024-11-15
---

We are in the setting that was described in [[chaining]]. We are trying to obtain a maximal inequality for the [[sub-Gaussian process]] $(X_\theta)$, $\theta\in\Theta$. Chaining gave a bound of the form 
$$
\E\sup_\theta X_\theta \leq \sup_{\theta\in\Theta}\sum_{0\leq n\leq N} 2^{n/2}\rho(\theta, \Theta_n),
$$
where $\Theta_0\subset\Theta_1\subset\dots\subset \Theta_N=\Theta$ is a chain of sets approximating $\Theta$, where $|\Theta_n|\leq 2^{2^n}$.  The idea behind Dudley chaining is to move the supremum inside the sum. That is, we upper bound the right hand side as
$$
\sup_{\theta\in\Theta}\sum_{0\leq n\leq N} 2^{n/2}\rho(\theta, \Theta_n)\leq \sum_{0\leq n\leq N} 2^{n/2}\sup_{\theta\in\Theta}\rho(\theta, \Theta_n).
$$ 
We can then take the infimum over all sets $\Theta_n$ of size $2^{2^n}$, which leads to [[Dudley's entropy bound]] stated in terms of [[entropy number|entropy numbers]], which are
$$
e_n(\Theta) = \inf_{\Theta_n} \sup_{\theta} \rho(\theta, \Theta_n).
$$
This method is provably loose for bounds on the [[Gaussian complexity]]. [[generic chaining|Generic chaining]] is tighter but can be harder to compute at times. The idea behind generic chaining is to not move the supremum inside the sum.
