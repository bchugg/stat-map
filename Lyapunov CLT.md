Like the [[Lindeberg-Feller CLT]], the Lyapunov [[central limit theorems|CLT]] is for independent observations without a common mean or variance. 

Let $X_1,X_2,\dots$ be independent with $\E[X_i] = \mu_i$ and $\Var(X_i) = \sigma_i^2$. If 
$$
\lim_n \frac{1}{s_n^3}\sum_{i\leq n}\E|X_i-\mu_i|^3 = 0,
$$
then 
$$
\frac{1}{s_n}\sum_{i\leq n}X_i-\mu_i \xrightarrow{d}N(0,1).
$$
The Lyapunov CLT replaces the Lindeberg condition with a Lyapunov condition, which is a condition of the third moments. It also recovers the usual CLT for iid random variables with finite variance. 

The Lyapunov result is weaker than the [[Lindeberg-Feller CLT]], as the Lyapunov condition implies the Lindeberg condition. 