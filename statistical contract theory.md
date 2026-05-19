---
lastmod: 2026-05-19
created: 2026-05-16
---
Most [[hypothesis testing]] (and [[statistical inference]] more generally) does not consider the incentives of the various parties involved. It focuses only on what the statistician does with the data once it's in hand. 

But in practice, statistical testing often involves multiple parties with different objectives. Who generated the data? Who benefits if a hypothesis is rejected? Who bears the cost of collecting evidence? Statistical contract theory studies these questions by treating inference as part of an incentive system, aiming to design _contracts_ which map statistical evidence into allocations (rewards, licenses, etc) while encouraging desirable behavior from the agents who generate the data.

This is usually formalized in terms of principal agent problems. We assume there is a principal who is offering access to some good and an agent who is vying for access. The principal designs the contract that the agent can opt into. The original statistical contract of this form is from Bates et al, who called this framework principal-agent hypothesis testing: 

- The principal publicly announces a cost $C>0$ and a menu of payout functions $\calF$. 
- If the agent opts in, they pay $C$ and select $f\in\calF$. 
- They generate data $X$ from their private distribution and are awarded payout $f(X)$. 

Agents are typically partitioned into null agents and non-null agents, and the principal wants to interact with non-null agents. To deter null agent entry, we want to design _incentive-compatible_ contracts: those with $\E_P[f(X)]\leq C$ for null distributions $P$. 

# Reading 
- [Principal agent hypothesis testing](https://arxiv.org/pdf/2205.06812)
- [Optimizing Social Utility in Sequential Experiments](https://arxiv.org/pdf/2605.06520)