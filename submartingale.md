---
lastmod: 2024-12-21
created: 2024-12-21
---

A stochastic process $(S_t)$ is a submartingale with respect to a filtration $(\calF_t)$ if
$$
\E[S_t|\calF_{t-1}] \geq S_{t-1},\quad \forall t.
$$
If $\geq$ is swapped with $\leq$ then we have a [[supermartingale]]. 

Submartingales obey Doob's maximal inequality, which states that 
$$
\Pr\left(\max_{1\leq i\leq n}X_i \geq t\right)\leq \frac{\E \max(X_n,0)}{t}.
$$
Reverse-time submartingales also a

Nonnegative reverse submartingales also obey the time-reverse [[Ville's inequality]]. A reverse submartingale is a submartingale adapted to a reverse filtration. A reverse filtration $(\calF_t)$ is a sequence of σ-algebras such that $\calF_t\supset \calF_{t+1}$. That is, a reverse filtration represents decreasing information with time. 

An example of a reverse martingale is the empirical mean $\sum_i X_i/t$ adapted to the canonical reverse filtration $\calR_t = \sigma(Zt , Z_{t+1},\dots)$. When thinking about reverse martingales, it's easiest to think about time flowing backwards, i.e., information being revealed first at time $t$, then at time $t-1, t-2$, and so on. hus, reverse submartingales are increasing in expectation in reversetime and, if one were to plot the expected values such a process would resemble a supermartingale in forward time. 

Like supermartingales, submartingales obey versions of the optional stopping theorem and the martingale convergence theorem. 