---
created: 2024-08-29
lastmod: 2024-12-20
---

The Dirichlet process is a commonly used prior for the task of [[cdf estimation]] in [[Bayesian nonparametrics]]. It was invented by Thomas Ferguson in 1973. 

The Dirichlet process is a distribution over distributions. Specifically, for a base distribution $F_0$ and a concentration parameter $\alpha$, a DP prior generates random distributions $F\sim DP(\alpha,F_0)$. Intuitively, $\alpha$ controls how tightly the prior is around $F_0$, similarly to the variance of the normal distribution. 

### Sampling from the prior.  
We use the "stick breaking" procedure: First draw $\beta_k\sim \text{Beta}(1,\alpha), then set 
$$
\pi_k = \beta_k \prod_{i\leq k-1} (1-\beta_i),
$$
which satisfies $\sum_k \pi_k = 1$. Then draw $\theta_k \sim F_0$ independently, and finally set $F = \sum_{k=1}^\infty \pi_k \delta_{\theta_k}$. In practice we stop after some finite number $K$. 

### Sampling from the marginal 
As usual, can draw $F\sim DP(\alpha,F_0)$ (using stick breaking), and then draw $X_1,\dots,X_n$ from $F$ which is a draw from the marginal. 

An alternative method which doesn't involve two steps is called the "Chinese restaurant process". Here we draw $X_1\sim F_0$, and then 
$$
X_i | X_{1},\dots,X_{i-1} = \begin{cases}
X\sim F_{i-1},& \text{w.p. } \frac{i-1}{i+\alpha-1}\\
X\sim F_{0},& \text{w.p. } \frac{\alpha}{i+\alpha-1},
\end{cases}
$$
where $F_{i-1}$ is the empirical distribution on $X_1,\dots,X_{i-1}$. (So there will very likely be duplicates in the sample). It's called the Chinese restaurant process since we can imagine it as follows: the $i$-th customer walks into the restaurant, and sits at each table proportional to the number of people already at that table. With some probability he sits at a new table. 

### Sampling from the posterior 
Turns out that the posterior is also a Dirichlet distribution, namely if $X_1,\dots,X_n\sim F$ and $F$ has prior $DP(\alpha,F_0)$, then the posterior is $DP(\alpha + n, \overline{F}_n)$ where 
$$
\overline{F}_n = \frac{n}{n+\alpha}F_n + \frac{\alpha}{n + \alpha}F_0,
$$
where again $F_n$ is the empirical cdf on the $n$ points. 
