---
created: 2024-08-29
lastmod: 2024-09-13
---
Extension of the [[Neyman-Pearson lemma]] to classes with [[monotone likelihood ratio]]. Here's the statement.

Suppose $\{P_\theta:\theta\in\Theta\subset\Re\}$ has MLR in the [[sufficient statistic]] $T$ and consider testing  $H_0: \theta \leq \theta_0$ vs $H_1: \theta>\theta_0$. Then the [[uniformly most powerful test]] has the form
$$
\phi(X) = \begin{cases}
1,& T(X) > c,\\
\gamma,& T(X)=c,\\
0,&T(X)<c,
\end{cases}
$$
where $\gamma$ and $c$ are chosen such that $\sup_{\theta\leq \theta_0}P_\theta(\phi(X) = 1)=\alpha$. The main takeaway is that the test is a threshold test based on the statistic $T$. 