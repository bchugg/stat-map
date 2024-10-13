---
created: 2024-08-29
lastmod: 2024-09-02
---

#hypothesis-testing #testing-by-betting 

Specific protocols of [[game-theoretic probability]] can be used to test hypotheses. This yields a fundamental tool in [[game-theoretic statistics]]. 

Suppose we receive data $X_1,X_2,\dots\sim P$ and we are testing the hypotheses: 
$$
H_0: P\in \bs{P} \text{~ vs ~} H_1: P\in \bs{Q}.
$$
This is a general framework which encapsulates both point nulls (eg $\theta^* = 0$) and composite nulls (eg $\theta^* \in S$ for some set $S$). $\bs{P}$ and $\bs{Q}$ can be infinite sets of distributions, singletons, finite sets, etc. 

The game proceeds as follows. 
Skeptic begins with wealth $\calK_0=1$. 
For $t=1,\dots,T$: 
- Skeptic proposes a payoff function $S_t: \calX \to [0,\infty]$ such that
$$
\E_{X\sim P}[S_t(X)|\calF_{t-1}]\leq 1 \quad \forall P\in\bs{P}. 
$$
 - Reality reveals an observation $X_t$. 
- Skeptic updates her wealth as $\calK_t = \calK_{t-1} S_t(X_t).$ 

As usual in [[game-theoretic statistics]], this implies that $\calK_t = \prod_{i=1}^t S_i(X_i)$ is an [[e-process]] for $\bs{P}$. Under the null, the skeptic's wealth is therefore not expected to grow. Indeed, by [[Ville's inequality]], 
$$
P(\forall t\geq 1: \calK_t \geq 1/\alpha) \leq \alpha \quad \forall P\in\bs{P}.
$$
Therefore, if we reject the null when the $\calK_t$ exceeds $1/\alpha$, we have only an $\alpha$ probability of making an error, i.e., our type I error uniformly over time is bounded by $\alpha$. In other words, this is a level-$\alpha$ sequential test. 

While this is framed as one-sample testing, we can also consider [[testing by betting—two-sample testing]]. 

# Payoff functions 

Clearly, it is important to find good payoff functions. This constitutes a large area of study. 
While $S_t$ is designed to be a supermartingale under the null, we want it to grow as large as possible as quickly as possible under the alternative so that the null is rejected quickly. 

Typically when designing betting strategies, we follow the approach of [[maximizing log-wealth]], i.e., we want $\log(\calK_t)$ to grow fast under the alternative.  Though see [[growth rate conditions in sequential testing]] for a more general overview. 

The payoff is _admissible_ if $S_t' \geq S_t$ a.s. under $P$ implies that $S_t' = S_t$. If $S_t$ is admissible, then $\E_P[S_t(X)|\calF_{t-1}]=1$ (as opposed to an inequality). This means the wealth process is a martingale (as opposed to a supermartingale). (This is easy to check: Set $S_t' = S_t / \E_P[S_t|\calF_{t-1}]$, which satisfies $\E[S_t'|\calF_{t-1}]=1$). 

So how do we actually choose $S_t$? This choice depends on the problem at hand, whether it's simple null vs simple alternative ([[testing by betting—simple vs simple]]), simple null vs composite alternative ([[testing by betting—simple vs composite]]), or composite null vs composite alternative ([[testing by betting—composite vs composite]], in which case we use [[universal inference]] or the [[reverse information projection (RIPr)]]. 





