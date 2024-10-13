---
created: 2024-08-29
lastmod: 2024-09-02
---

Chaining is a generic method of generating [[maximal inequalities]] on the suprema of random processes. 

Suppose we have a collection of random variables indexed by some set  which we assume is a centered (zero-mean) [[sub-Gaussian process]] in the sense that 
$$
\Pr(|X_\theta - X_\phi| \geq \eps) \leq 2\exp\left(-\frac{\eps^2}{2\rho^2(\theta, \phi)}\right),
$$
for some metric $\rho$. The ultimate goal is to bound $\E\sup_{\theta }X_\theta$ but this is done via bounding
$$
\Pr(\sup_\theta X_\theta \geq \eps).
$$
If $X_\theta$ is mean-zero, then $\E\sup_\theta X_\theta = \E\sup _\theta (X_\theta - X_{\theta_0 })$ for any $\theta_0$ so we often focus on the quantity $X_\theta - X_{\theta_0}$.

# Overview 

The idea is to decompose $X_\theta - X_{\theta_0}$ as 
$$
X_\theta - X_{\theta_0} = \sum_{n\geq 1} (X_{\pi_n(\theta)} - X_{\pi_{n-1}(\theta)}),
$$
where $\pi_0(\theta) = \theta_0$ and $\pi_N(\theta) = \theta$ for all large enough $N$ (so that the sum is really a finite sum). This is the "chain". Here $\pi_n$ is a map from $\Theta \to \Theta_n$ where 
$$
\{\theta_0\} = \Theta_0 \subset \Theta_1\subset \dots \subset \Theta_N = \Theta.
$$
So $\theta_n(\theta)\subset \Theta_n$ is the approximation of $\theta$ within $\Theta_n$. We enforce that $\Theta_n$ is finite, so that union bound type arguments will apply. In particular we set $|\Theta_n| = 2^{2^n}$, which looks ridiculous I know, but we will want exponential growth in log-space. We let $\pi_n(\theta)$ be the closest point to $\theta$ in $\Theta_n$, so that
$$
\rho(\theta, \pi_n(\theta)) = \inf_{\phi\in\Theta_n} \rho(\theta, \phi).
$$
The intuition is the following:
- Bound $\Pr(|X_{\pi_n(\theta)} - X_{\pi_{n-1}(\theta)}\geq \eps)$ using that $X_\theta$ is a sub-Gaussian process. 
- Union bound over all elements of $\Theta_n \times \Theta_{n-1}$ (both are finite). 
- Union bound over all $n\leq N$ (again finite). 
- Use the chaining decomposition above to provide a bound on $X_\theta - X_{\theta_0}$. 

Chapter 2.2 in Talagrand's book below provides the details. We end up with a bound of the form: 
$$
\Pr(\sup_{\theta}|X_\theta - X_{\theta_0}|\geq t S) \leq 2\sum_{n\leq N} 2^{2^{n+1}} \exp(-t^2 2^{n-1}) \lesssim \exp(-t^2/2),
$$
where 
$$
S = \sup_{\theta\in\Theta} \sum_{n\leq N} 2^{n/2} \rho(\pi_n(\theta),\pi_{n-1}(\theta)) \lesssim \sup_{\theta\in\Theta}\sum_{0\leq n\leq N} 2^{n/2} \rho(\theta, \Theta_n) = A,
$$
where we've used the triangle inequality $\rho(\pi_n(\theta), \pi_{n-1}(\theta)) \leq \rho(\pi_n(\theta), \theta) + \rho(\theta, \pi_{n-1}(\theta))$. 
This gives $\E \sup_\theta X_\theta \lesssim A$. 

There are two main ways of dealing with $A$. One is [[generic chaining]], and one is [[Dudley chaining]]. The latter is looser than the former, but sometimes easier to compute. 

# References 
- _Upper and lower bounds for stochastic processes_, Talagrand. 