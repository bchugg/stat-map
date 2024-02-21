
Specific protocols of [[game-theoretic probability]] can be used to test hypotheses. This yields a fundamental tool in [[game-theoretic statistics]]. 

Suppose we receive data $X_1,X_2,\dots\sim P$ and we are testing the hypotheses: 
$$ H_0: P\in \bs{P} \text{~ vs ~} H_1: P\in \bs{Q}.$$
This is a general framework which encapsulates both point nulls (eg $\theta^* = 0$) and composite nulls (eg $\theta^* \in S$ for some set $S$). $\bs{P}$ and $\bs{Q}$ can be infinite sets of distributions, singletons, finite sets, etc. 

The game proceeds as follows. 
Skeptic begins with wealth $\cK_0=1$. 
For $t=1,\dots,T$: 
- Skeptic proposes a payoff function $S_t: \cX \to [0,\infty]$ such that $$\E_{X\sim P}[S_t(X)]\leq 1 \quad \forall P\in\bs{P}.$$
- Reality reveals an observation $X_t$. 
- Skeptic updates her wealth as $\cK_t = \cK_{t-1} S_t(X_t).$ 

As usual in [[game-theoretic statistics]], this implies that $\cK_t = \prod_{i=1}^t S_i(X_i)$ is a [[test-martingale]] for $\bs{P}$. Under the null, the skeptic's wealth is therefore not expected to grow. Indeed, by [[Ville's inequality]], 
$$ P(\forall t\geq 1: \cK_t \geq 1/\alpha) \leq \alpha \quad \forall P\in\bs{P}.$$
Therefore, if we reject the null when the $\cK_t$ exceeds $1/\alpha$, we have only an $\alpha$ probability of making an error, i.e., our type I error uniformly over time is bounded by $\alpha$. In other words, this is a level-$\alpha$ sequential test. 

But how do we actually choose $S_t$? We want to choose it such that, under the alternative $\bs{Q}$, the wealth grows as quickly as possible. 

## P



The precise choice will be based on the problem at hand. However, there are some general strategies. 

- For testing the point null $\theta^*  = \theta_0$, [Waudby-Smith and Ramdas (2023)](https://arxiv.org/abs/2010.09686) use $S_t = 1 + \lambda_t(X_t - \theta_0)$, where $\lambda_t$ is any predictable sequence of scalars that guarantee non-negativity of $S_t$. [[Online Newton Step]] is usually a good strategy for choosing $S_t$ and gives some nice theoretical guarantees on the convergence time. 
- For [[two-sample testing]], [Shekhar and Ramdas](https://arxiv.org/abs/2112.09162) use $S_t = 1 + \lambda_t(X_t - Y_t)$ (more generally $S_t =  1 + \lambda_t(k(X_t) - k(Y_t))$  if $X_t,Y_t$ are multivariate observations, and $k$ is some kernel. 




