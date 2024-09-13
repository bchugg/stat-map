---
created: 2024-08-29
lastmod: 2024-09-02
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

## Proof
I'm going to prove it only because I find the proofs in most textbooks exceedingly painful. 

First consider testing $H_0: \theta =\theta_0$ vs $H_1:\theta = \theta_1$ for $\theta_1>\theta_0$. From the NP lemma we know that the UMP test has the form 
$$
\psi(X) = \begin{cases}
1,& p_{\theta_1}(X) > k p_{\theta_0}(X),\\
\gamma,& p_{\theta_1}(X)=kp_{\theta_0}(X),\\
0,&p_{\theta_1}(X)<kp_{\theta_0}(X).
\end{cases}
$$
for some $k$ and $\gamma$ such that $P_{\theta_0}(\phi(X) = 1)=\alpha$.  
Since $P_\theta$ has MLR in $T$, there exists some monotonically increasing function $g$ such that, for all $\theta 