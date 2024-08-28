The Dirichlet process is a commonly used prior for the task of [[cdf estimation]] in [[Bayesian nonparametrics]]. It was invented by Thomas Ferguson in 1973. 

It has two parameters, $\alpha$ and $F_0$ and is written $DP(\alpha,F_0)$. $F_0$ is a cdf and $\alpha$ a positive real value. Intuitively, $\alpha$ controls how tightly the prior is around $F_0$, similarly to the variance of the normal distribution. 

#todo clean this up.

### Sampling from the prior.  
We use the "stick breaking" procedure. 

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
Turns out that the posterior is also a Dirichlet distribution, namely if $X_1,\dots,X_n\sim F$ and $F$ has prior $Dir(\alpha,F_0)$, then the posterior is $Dir(\alpha + n, \overline{F}_n)$ where 
$$
\overline{F}_n = \frac{n}{n+\alpha}F_n + \frac{\alpha}{n + \alpha}F_0,
$$
where again $F_n$ is the empirical cdf on the $n$ points. 
