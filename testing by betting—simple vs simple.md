#hypothesis-testing #testing-by-betting #sequential-statistics #likelihood-ratio

Here we explore [[game-theoretic hypothesis testing]] for simple nulls vs simple alternatives.  Suppose we observe random variables $X_1, X_2,\dots$ and are testing 
$$H_0: (X_t) \sim P \quad H_1: (X_t)\sim Q,$$
for two distributions $P$ and $Q$. We want to design a payoff function $S_t$ such that 
$$\E_P[S_t(X_t)|\cF_{t-1}]=1.$$
Assuming densities of $P$ and $Q$ are well-defined (otherwise we can use Radon-Nikodym derivatives), note that this implies 
$$1 = \E_P [S_t(X_t)|\cF_{t-1}] = \int S_t(x)p(x|\cF_{t-1})dx,$$
so $S_t(x) p(x|\cF_{t-1})$ is a density, call it $r(x|\cF_{t-1})$. Hence $S_t(x) = r(x|\cF_{t-1}) / p(x|\cF_{t-1})$. So in order to maximize log wealth (see the principle of [[maximizing log-wealth]]), we want $r$ such that 
$$\E\left[\log\left(\frac{r(x)}{p(x)}\right)|\cF_{t-1}\right] \geq \E\left[\log\left(\frac{u(x)}{p(x)}\right)|\cF_{t-1}\right],$$
for all distributions $u$. It turns out that by Gibbs' inequality, the optimal distribution to pick is simply $Q$. Therefore, our bet is the likelihood ratio 
$$S_t(X_t) = \frac{q(X_t|\cF_{t-1})}{p(X_t|\cF_{t-1})}.$$
The corresponding wealth process $K_t = \prod_{i\leq t}S_i(X_i) = q(X_1^t) / p(X_1^t)$ therefore recovers the classical [[likelihood-ratio test]] (and is a sequentialized version of it). 

Note that this shows that the GRO (growth rate optimal) [[e-value]] for simple vs simple hypothesis testing is the likelihood ratio. 
