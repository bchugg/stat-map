---
lastmod: 2025-01-04
created: 2025-01-04
---

A (strict) formulation of the [[optimal transport]] problem. It's always taught with dirt piles; why deviate from tradition. 

Consider dirt piles at locations $D_1,\dots,D_n$ and holes at locations $H_1,\dots,H_m$. Suppose pile $D_i$ has $\alpha_i$ units of dirt and hole $H_j$ can hold $\beta_j$ units of dirt.  It costs $c(i,j)\geq 0$ to transport a unit of dirt from $D_i$ to $H_j$. Our question is: Which dirt pile do we send to which hole in order to minimize the overall cost? 

More formally, we want a transportation plan $T:[n]\to[m]$ which maps piles to holes, telling us where to send the $i$-th dirt pile. Each pile can only be sent to one hole, and at the end of the process, each hole should be full. That is, for each $j$, we should have $\sum_i \alpha_i \delta_{T(i)=j}=\beta_j$. 

We are thus looking to solve the following problem: 
$$
\min_T \bigg\{ \sum_i\alpha_i c(i,T(i))\bigg| \sum_i \alpha_i \delta_{T(i)=j}= \beta_j,\forall j\in[m] \bigg\}.
$$
This is the Monge formulation in the discrete case. 

To see what this has to do with probability, suppose that $D_1,\dots,D_n$ and $H_1,\dots,H_m$ represent two discrete distributions, with mass $\alpha_i$ at $D_i$ and mass $\beta_j$ at $H_j$. That is, $\alpha_1,\dots,\alpha_n$ and $\beta_1,\dots,\beta_m$ constitute two discrete probability measures $\alpha=\Pr_\alpha$ and $\beta=\Pr_\beta$. $T$ is a map between these two measures that obeys 
$$
\beta_j = \Pr_\beta(j) = \Pr_\alpha(T^{-1}(j)) = \Pr_\alpha(\{i: T(i)=j\}).
$$
That is, the pushforward measure $\alpha_*(T)$ must be equivalent to the distribution $\beta$. With this perspective in mind, we can also notice that $\sum_i \alpha_i c(i,T(i))$ is simply the expected value of $c(X,t(X))$ when $X\sim\alpha$.  This motivates the extension of the discrete Monge formulation to the continuous case: 
$$
\inf_T \bigg\{ \E_{X\sim \alpha} c(X,T(X)) \;\bigg |\; \alpha_*(T) =\beta\bigg\}.
$$
This is the (continuous) Monge formulation, and a map $T$ solving the above problem is sometimes called a _Monge_ map (or a transportation plan). There's an obvious problem with this formulation, however: What if there is no mapping between piles and holes such that each hole will be filled by each pile. That is, what if there is no map $T$ such that $\alpha_*(T)=\beta$. In fact, this is a very restrictive requirement in many applications. This is what motivates the Kantorovich relaxation and [[optimal transport costs]].  
