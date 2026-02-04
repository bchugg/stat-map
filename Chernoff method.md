---
created: 2024-08-29
lastmod: 2026-01-26
---

The Chernoff method, also called the Cramer-Chernoff method, applies [[basic inequalities#Markov's inequality]] to the nonnegative random variable $e^{\lambda X}$, and then chooses $\lambda$ to optimize the bound. This often results in tighter bounds and [[concentration inequalities]] than working with the random variable directly. 

In particular, for a random variable $X$, Markov's inequality gives that 
$$
\Pr(X\geq t) = \Pr(e^{\lambda X}\geq e^{\lambda t}) \leq e^{-\lambda t}\E[e^{\lambda X}].
$$
This holds for all $\lambda>0$, so we obtain the bound 
$$
\Pr(X\geq t)\leq \inf_{\lambda >0}e^{-\lambda t}\E[e^{\lambda X}] = \inf_{\lambda >0} e^{-\lambda t}M_X(\lambda),
$$
where $M_X$ is the [[MGF]] of $X$. If we place distributional assumptions on $X$ (eg bounded, [[sub-Gaussian distributions|sub-Gaussianity]]), then we can solve for the optimal value of $\lambda$. If $X = \sum_{i\leq n} X_i$ is the sum of iid observations, then $\E[e^{\lambda X}] = \prod_i \E[e^{\lambda X_i}] = n \E[e^{\lambda X_1}]$. This makes the Chernoff particularly attractive under independence assumptions, even though it is not optimal (see below).  

The Chernoff method is often written in terms of the Cramer transform of $X$ (which is why it's often called the Cramer-Chernoff method), which is
$$
\psi_X^*(t) = \sup_{\lambda\geq 0} (\lambda t - \psi_X(\lambda)),\quad \text{where}\quad \psi_X(\lambda) = \log \E e^{\lambda Z}.
$$
This is also often called the Fenchel-Legendre transform. This gives, 
$$
\Pr(X\geq t) \leq \exp(-\psi_X^*(t)), 
$$
which leads us to studying and bounding the function $\psi_X^*(t)$. 

## Optimality 
The Chernoff method is very convenient hence widely deployed, but it's not optimal. We can see this in the case of [[bounded scalar concentration#Hoeffding's bound]], which is missing a factor of $1/t$ in the exponent from what we expect from the CLT. (See [The missing factor in Hoeffding's inequalities](http://www.numdam.org/item/AIHPB_1995__31_4_689_0.pdf) by Talagrand). 

More generally, the [[method of moments for concentration]] beats the Chernoff bound (when all moments exist), and the optimization approach to concentration ([[concentration via convex optimization]]) will give the tightest results if the convex program can be solved. See also [[interpolating between Markov and Chernoff]], which is tighter than the Chernoff method but also less computationally convenient. 

However, the Chernoff method is optimal is one sense. If $X_1,\dots,X_n$ are iid mean zero, $S_n = \sum_i X_i$, and for all $t\geq 0$,
$$
\Pr(S_n \geq nt) \leq Q^n(t),
$$
then 
$$
Q(t) \geq \inf_{\lambda \geq 0} \E[\exp(\lambda(X-t))].
$$
That is, if we have a bound which _uses the product structure of the observations_ (hence the power of $n$ on $Q(t)$), then the Chernoff method is optimal.  


