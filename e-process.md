An e-process is the sequential analogue of the [[e-value]]. We say a stochastic process $(E_t)$ is an e-process if it is an e-value at every [[stopping-time]]:
$$
\text{for all stopping times }\tau,\quad \E[E_\tau]\leq 1, \quad E_\tau \geq 0.
$$
E-processes are a strict superset of supermartingales. For example, the [[universal inference]] e-process is not a supermartingale.

E-processes always have the form $N_t = \inf_P M_t^P$ where $M_t^P$ is a $P$-martingale for $P$. 

The game-theoretic interpretation ([[game-theoretic statistics]]) is to partition to null, play a game on each, and take your overall wealth to be the minimum in each game. They are one of the foundational tools in [[safe, anytime-valid inference (SAVI)]]. 