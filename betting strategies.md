---
created: 2024-08-29
lastmod: 2024-12-20
---

In [[game-theoretic statistics]] we have some wealth process $\calK_t = \prod_{i\leq t}S_i$ where the "payoffs" $S_i$ are [[e-value|e-values]] depending on some predictable "bet" $\lambda_i$. The e-values might be of exponential form (see [[exponential inequalities]]) or of the form $1 + \lambda_i G_i$ (eg [[estimating means by betting]]). 

We want $\calK_t$ to increase if some null is not true. If a particular alternative is known, we might consider designing the $S_i$ according to some [[growth rate conditions in sequential testing]], if they can be solved exactly. If not, or if a particular alternative is not known, we need to do something else. Here we gather various strategies. 

## GRAPA and aGRAPA 
Idea behind GRAPA is to [[maximizing log-wealth|maximize log-wealth]]. If we don't know a particular alternative, we can ask, at any time $t$, what would have maximized the log-wealth in hindsight? GRAPA and aGRAPA are approximations to this answer (which does not have a closed-form solution). 

## LBOW 
Here we aim to maximize a specific lower bound on the wealth, similar to the ELBO in [[variational inference]]. A lower bound on the wealth is usually derived using some [[exponential inequalities]]. 

## ONS 
We may also borrow techniques from the online learning literature, such as [[Online Newton step]].