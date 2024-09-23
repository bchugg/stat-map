---
created: 2024-08-29
lastmod: 2024-09-02
---
Sub-$\psi$ processes were introduced by Howard et al. (2020) in [Time-uniform Chernoff bounds via nonnegative supermartingales](https://arxiv.org/pdf/1808.03204). The core insight was that many seemingly distinct concentration inequalities can be unified by noticing that they all stem, at their core, from nonnegative supermartingales. Sub-$\psi$ processes are a way to generalize the discussion and provide [[conc inequalities]] for large classes of distributions, while also making the bounds [[time-uniform]] at no loss (and sometimes a gain). 

Let $\psi:[0,\lambda_{\max})\to\Re_{\geq 0}$  be some function. In the scalar case, we say a pair of stochastic processes $(S_t), (V_t)$ are a sub-$\psi$ process if
$$
\exp\{\lambda S_t - \psi(\lambda)V_t \}\leq L_t^\lambda.
$$
where $L_t^\lambda$ is a [[supermartingale]]. That is, the process $\exp\{\lambda S_t - \psi(\lambda)V_t\}$ is upper bounded by a nonnegative supermartingale.

In $\Re^d$, we say $(S_t), (V_t)$ are sub-$\psi$ (where $S_t\in\Re^d$ and $V_t\in\Re^{d\times d})$ if for all $\nu\in\dsphere$,
$$
\exp\{\lambda \la \nu, S_t\ra - \psi(\lambda)\la \nu, V_t\nu\ra\}\leq L_t^{\lambda, \nu},
$$
where $L_t^{\lambda, \nu}$ is a nonnegative supermartingale.  The extension of sub-$\psi$ processes to $\Re^d$ was initially provided by [Whitehouse, Wu, and Ramdas](https://jwhitehouse11.github.io/arxiv_2023_selfnorm.pdf).

# Examples 



