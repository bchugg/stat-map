---
created: 2024-08-29
lastmod: 2024-09-02
---

Part of [[uncertainty quantification]] in which we have roughly the same goals as [[marginal consistency]] but we want to achieve our guarantees in a sequential setting (see [[uncertainty quantification#Sequential setting|uncertainty quantification]] in which we have roughly the same goals as [[marginal consistency]] but we want to achieve our guarantees in a sequential setting (see [[uncertainty quantification#Sequential vs batch setting:uncertainty quantification:sequential vs batch]] for the precise setup). 

In the online setting, we are interested in mean and quantile guarantees that have low regret. We say an algorithm has marginal mean consistency $\alpha$ if 
$$
\left |\frac{1}{T}\sum_{t=1}^T p_t - \frac{1}{T}\sum_{t=1}^T y_t\right|\leq \alpha,
$$
and marginal quantile consistency $\alpha$ if 
$$
\left| \frac{1}{T} \sum_{t=1}^T \ind[y_t\leq p_t]-q\right|\leq \alpha.
$$
Marginal estimation in the online setting is not terribly interesting, especially in the mean case. If we just pick $p_t = y_{t-1}$ and ignore $x_t$, then we achieve regret $1/T$ (if $y_t\in[0,1]$).  The adversary can be arbitrarily powerful here. 

In the quantile case, we could simply predict $p_t=1$ for $q$ fraction of the rounds, and $0$ for the remaining fraction. This easy algorithm should make us suspicious of marginal consistency. 

There's also a somewhat more interesting algorithm in the quantile case (though still not terribly interesting, and it still ignores the features). If we do an update similar to [[online gradient descent]], we can also achieve $1/T$ regret. In particular, we pick 
$$
p_{t+1} = p_t + \eta(q - \ind[y_t\leq p_t]).
$$
So if $y_t>p_t$ we increase $p_t$ slightly, and if $y_t\leq p_t$ we lower $p_t$ slightly. This has regret bound 
$$
\frac{1+\eta}{\eta T}.
$$
