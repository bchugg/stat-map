
Here we explore [[game-theoretic hypothesis testing]] for simple nulls vs simple alternatives.  Suppose we observe random variables $X_1,X_2$ and are testing 
$$H_0: (X_t) \sim P \quad H_1: (X_t)\sim Q,$$
for two distributions $P$ and $Q$. We want to design a payoff function $S_t$ such that 
$$\E_P[S_t(X_t)|\cF_{t-1}]=1.$$
Assuming densities of $P$ and $Q$ are well-defined (ow we can use Radon-Nikodym derivatives), note that this implies 
$$1 = \E_P [S_t(X_t)|\cF_{t-1}] = \int S_t(x)p(x|\cF_{t-1})dx,$$
so $S_t(x) p(x|\cF_{t-1})$ is a density, call it $r(x)$. Hence $S_t(x) = r(x) / p(x|\cF_{t-1})$. 
