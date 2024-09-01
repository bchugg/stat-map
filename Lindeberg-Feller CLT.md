A [[central limit theorems|CLT]] for independent random variables with finite variances. 

Let $X_1,X_2,\dots$ be independent with $\E[X_i] = \mu_i$ and $\Var(X_i) = \sigma_i^2$. Let $s_n^2 = \sum_{i\leq n}\sigma_i^2$ and 
$$
L_n(\eps) = \frac{1}{s_n^2}\sum_{i\leq n} \E[|X_i - \mu_i^2|\ind(|X_i-\mu_i|>\eps s_n)].
$$
If $L_n(\eps)\to 0$ as $n\to\infty$ for all fixed $\eps>0$, then we have the following CLT: 
$$
\frac{1}{s_n}\sum_{i\leq n}(X_i-\mu_i)\xrightarrow{d}N(0,1).
$$
Note that this implies the "usual" CLT for iid random variables with finite variance $\sigma^2$, since in that case $L_n(\eps) = \E[|X-\mu|^2 \ind(|X - \mu|>\eps \sigma\sqrt{n})]/\sigma^2$ which certainly goes to 0 as $n\to\infty$. In that case we get the CLT
$$
\sqrt{n}\left(\frac{1}{n}\sum_{i\leq n}X_i - \mu\right) \to N(0,\sigma^2).
$$
The quantity $L_n(\eps)$ is called the Lindeberg function, and $L_n(\eps)\to 0$ is called the Lindeberg condition. 