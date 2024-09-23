---
created: 2024-08-29
lastmod: 2024-09-22
---
An e-process is the sequential analogue of the [[e-value]]. They are one of the foundational tools in [[safe, anytime-valid inference (SAVI)]]. 

We say a stochastic process $(E_t)$ is an e-process for $\calP$ if it is an e-value at every [[stopping-time]]:
$$
\text{for all stopping times }\tau,\quad \sup_{P\in\calP}\E_P[E_\tau]\leq 1, \quad E_\tau \geq 0.
$$
E-processes are a strict superset of supermartingales. For example, the [[universal inference]] e-process is not a supermartingale. However, e-processes can be equivalently defined in terms of [[test-martingale|test martingales]]: $(E_t)$ is an e-process if there exists a family of test martingale $(M_t^P)$, $P\in\calP$ such that 
$$
E_t \leq M_t^P, \quad \text{for all }P\in\calP \text{ and }t\geq 0.
$$
This representation implies that [[Ville's inequality]] applies to e-processes. (In fact, the generalization of Ville's inequality to compose distributions requires e-processes, see [Ruf et al. (2023)](https://arxiv.org/pdf/2203.04485)). It also implies that e-processes always have the form 
$$
E_t = \inf_P M_t^P.
$$
The game-theoretic interpretation ([[game-theoretic statistics]]) is to partition to null, play a game on each, and take your overall wealth to be the minimum in each game. 

Like e-values, e-processes are measures of [[evidence against the null]], but in sequential settings. 

