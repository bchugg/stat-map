---
lastmod: 2024-12-31
created: 2024-12-31
---

For a nonnegative [[submartingale]] $(X_t)$, Doob's maximal inequality states that, for all $n\geq 1$ and $t>0$,  
$$
\Pr\left(\max_{1\leq i\leq n}X_i \geq t\right)\leq \frac{\E X_n}{t}.
$$
Like [[Ville's inequality]] for [[supermartingale|supermartingales]], this enables some concentration inequalities to be given for submartingales. But unlike Ville's inequality, the time-horizon is finite (eg the inequality is not truly [[time-uniform]]), and the bound is based on $\E X_n$ not $\E X_0$. 