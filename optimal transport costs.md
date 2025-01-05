---
lastmod: 2025-01-04
created: 2025-01-04
---

Let $\Gamma(\rho,\nu)$ be the set of joint probability distributions over a space $\calX\times\calX$ whose martingales are $\rho$ and $\nu$. Given a (nonnegative) cost function $c:\calX \times\calX \to \Re_{\geq 0}$, the optimal transport cost between $\rho$ and $\nu$ is 
$$
L_c(\rho,\nu) = \inf_{\pi \in \Gamma(\rho,\nu)} \E_{(X,Y)\sim \pi) c(X,Y)} = \inf_{\pi \in \Gamma(\rho,\nu)} \int c(x,y) \d\pi (x,y).
$$
If we take $c = d^p$ where $d$ is a metric, we recover the [[Wasserstein distance]]. We call this an optimal transport cost because it's a formulation of the [[optimal transport]] problem. The optimization problem can be seen as a relaxation of [[Monge formulation]], often called the Kantorovich formulation (see below). 

Optimal transport costs are convex [[distributional distance|divergences]]. We can thus build [[confidence sequences]] for them using [[confidence sequences for convex functionals]]. 

## The Kantorovich Dual 
$L_c$ admits the following dual representation, known as the Kantorovich dual: 
$$
L_c(\rho,\nu) \leq  \sup_{(f,g)\in \calM_c} \big\{\E_P[f] + \E_Q[g]\big\},
$$
where $\calM_c$ is the set of pairs of functions $f,g$ such that $f(x) + g(y)\leq c(x,y)$ for all $x,y\in\calX$ (almost surely). If $c$ is lower semi-continuous then we have equality above. This might be considered the equivalent of the variational representation of e.g., [[f-divergence|f-divergences]]. 

## Motivation: The Kantorovich Relaxation 
We can recover optimal transport costs by relaxing the [[Monge formulation]], which does not always admit a solution. To remedy this, we might allow ourselves to transport dirt from one pile to multiples holes. Let $\pi(i,j)$ denote the amount of dirt transported from pile $i$ to hole $j$. Then we are looking to minimize the total transportation cost $\sum_{i,j} \pi(i,j) c(i,j)$ such that the total amount of dirt transported from pile $i$ is $\alpha_i$, and the total amount of dirt transported to hole $j$ is $\beta_j$.  That is, we are looking to solve 
$$
 \min_\pi \sum_{i,j}\pi(i,j)c(i,j) \quad \text{s.t.} \quad \sum_j \pi(i,j) = \alpha(i),\quad \sum_i \pi(i,j) = \beta(j).
$$
Again, looking at $\alpha$ and $\beta$ as discrete probability distribution, we are searching for a map between $\alpha$ and $\beta$ which minimizes total transportation cost who _marginal_ distributions are $\alpha$ and $\beta$. This suggests the continuous version of the above optimization problem: 
$$
L_c(\alpha,\beta) = \inf_{\pi\in \Gamma(\alpha,\beta)} \big\{\E_{(X,Y)\sim \pi} \;[c(X,Y)]\big\},
$$
where 
$$
\Gamma(\alpha,\beta) = \bigg\{\pi \in \mathcal{P}(\calX \times \calX): \int \pi(x,y)dy = \alpha(x),\quad \int\pi(x,y)dx = \beta(y).\bigg\},
$$
is the set of joint distributions on $\calX\times\calX$ whose marginals are $\alpha$ and $\beta$. This is known as the Kantorovich relaxation.  
