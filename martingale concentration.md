---
created: 2024-08-29
lastmod: 2025-03-13
---

Let $(S_t)$ be a martingale wrt to the filtration $(\calF_t)$. Assume $(S_t)$ is scalar-valued unless otherwise indicated. Here we investigate [[concentration inequalities]] for $(S_t)$. 

Note that martingale concentration inequalities generalize concentration inequalities for independent random variables (eg [[bounded scalar concentration]]), since we may take $S_t = \sum_{i\leq t} (X_i - \mu)$, in which the following bounds translate into bounds on $\sum_{i\leq t}X_i$. 

While we state concrete, mostly [[fixed-time]] results here, we note that many of the following bounds were made [[time-uniform]] (and often tightened) using [[sub-psi process|sub-psi processes]].  

See also [[matrix martingale inequalities]]. 

## Azuma-Hoeffding inequality 
Assume that $|X_t - X_{t-1}|\leq c_t$ for all $t$, i.e., the martingale has bounded increments. Then, for all $n$, 
$$
\Pr(|X_n - X_0| \geq \eps) \leq 2\exp\left(\frac{-\eps^2}{2\sum_{t=1}^n c_t^2}\right).
$$
The natural one-sided versions of this inequality also exist. Note that $n$ is fixed in advance here (i.e., it is [[fixed-time]] result). 

## Dubins-Savage inequality 
This is often considered [[basic inequalities#Chebyshev's inequality]] for martingales. If $(X_t)$ has conditional means $\mu_t$, i.e., $\E[X_t | \calF_{t-1}] = \mu_t$ and conditional variances $V_t = \Var(X_t | \calF_{t-1})$ then for any $a,b>0$, 
$$
\Pr\left(\exists t\geq 1: \sum_{i\leq t}(X_i - \mu_i) \geq a + b\sum_{i\leq t}V_i\right) \leq \frac{1}{ab+1}.
$$
This is a [[time-uniform]] result. This result can also be generalized to infinite variance. If $v_t(p) = \E[|X_t - \mu_t|^p|\calF_{t-1}]$ for $1<p\leq 2$, then 
$$
\Pr\left(\exists t\geq 1: \sum_{i\leq t}(X_i - \mu_i) \geq a + b\sum_{i\leq t} v_i(p)\right) \leq \frac{1}{(c_p ab^{\frac{1}{p-1}}+1)^{p-1}},
$$
where $c_p$ is a constant dependent on $c$. This was proven by [Kahn in 2009](https://link.springer.com/article/10.1007/s10959-008-0206-2). 

## Variance bound 
If the martingale has bounded increments and the _variance_ of the increments are also bounded, i.e., 
$$
\E [|X_t - X_{t-1}|^2|\calF_{t-1}]\leq v_t^2,
$$
then we can modify Azuma's bound to read 
$$
\Pr(|X_n - X_0|\geq \eps) \leq 2 \exp\left(\frac{-\eps^2}{4V}\right),
$$
where $V = \sum_i v_i^2$, as long as $\eps \leq 2V/\max_i c_i$.  Why is this better than Azuma's inequality? Since the increments are bounded by $c_t$, a trivial bound on $\E[|X_t - X_{t-1}|^2|\calF_{t-1}]$ is $c_t^2$. Thus we may assume that $v_t^2\leq c_t^2$, which means the right hand side of the bound is tighter. 

This was first proved by DA Grable in [A Large Deviation Inequality for Functions of Independent, Multi-way Choices](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=3b7858b4475d8027cf49c8afbaac34b4229731fb). A modern proof is given by Dubhasi and Panconesi in their textbook, [Concentration of Measure for the Analysis of Randomized Algorithms](http://wwwusers.di.uniroma1.it/~ale/Corsi/AlgoPro/monograph.pdf), Chapter 8. 

## Bentkus-style inequality 
Let $(X_i$) be a supermartingale adapted to $(\calF_i)$. If $a_i\leq X_i\leq b_i$, then 
$$
\Pr(S_n \geq u) \leq \inf_{\alpha\geq 1}\inf_t \frac{\E(S_n - t)^\alpha_+}{(u-t)^\alpha_+}.
$$
Similarly to [[bounded scalar concentration#Bentkus' inequality]] for scalar random variables, this improves over the [[Chernoff method]]. We can further bound this as 
$$
\begin{align}
\inf_{\alpha\geq 1}\inf_t \frac{\E(S_n - t)^\alpha_+}{(u-t)^\alpha_+} \leq \inf_{\alpha\geq 1}\inf_t \frac{\E(\sum_i G_i - t)^\alpha_+}{(u-t)^\alpha_+} \leq \inf_t \frac{\E(\sum_i G_i - t)_+}{(u-t)_+}. 
\end{align}
$$
where $G_i \in \{a_i,b_i\}$ and $\E G_i = 0$. The right hand side can be computed explicitly, or approximated, in some circumstances. See [here](https://link.springer.com/article/10.1007/s10986-006-0011-5). 
## Bentkus-style inequality for variance
In addition to the boundedness condition above, suppose we also have $\Var(X_i)\leq \sigma_i^2$. Then we can write 
$$
\Pr(S_n \geq u) \leq \inf_{\alpha\geq 2}\inf_t \frac{\E(S_n - t)^\alpha_+}{(u-t)^\alpha_+}.
$$
As above, we can bound the right hand side with a worst case distribution. In particular, this time we have $G_i \in \{-\sigma_i^2/b_i, b_i\}$ and $\E G_i = 0$.

# Reading
- [Concentration of Measure for the Analysis of Randomized Algorithms](http://wwwusers.di.uniroma1.it/~ale/Corsi/AlgoPro/monograph.pdf) by Dubhashi and Panconesi. 