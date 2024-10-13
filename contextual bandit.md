---
created: 2024-08-29
lastmod: 2024-09-02
---

#todo 

A slightly more general setting that the [[multiarmed bandit]]. As in that problem we have a set of actions $\calA$. The reward of each action now depends on an additional context vector, $s$. The formal setup is as follows. 

For $t=1,\dots,T$: 
- We are presented with a context vector $s$ 
- We select an action $a$ according to our policy $\pi_t$ (which can depend on $s$ and the history until the current moment)
- We see reward $r_t\sim R(a,s)$. 

Our goal is to minimize regret: 
$$
\E[Reg(T)] = \sum_{t=1}^T \bigg(\max_a [\E_S R(a,S)] - r_t\bigg).
$$
# Known results 