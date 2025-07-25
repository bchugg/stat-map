---
created: 2024-08-29
lastmod: 2025-05-30
---

States that a variant of the [[likelihood-ratio test]] is the [[uniformly most powerful test]] among all level-$\alpha$ tests when testing simple nulls against simple alternatives. The NP lemma is generalized to [[monotone likelihood ratio]] families by the [[Karlin-Rubin theorem]]. 

Suppose we are testing $H_0:\theta = \theta_0$ vs $H_1: \theta = \theta_1$. Consider the likelihood ratio test, which says to reject if $L(X) = p_1(X)/p_0(X)\geq k$ where $k$ is chosen so that 
$$
\Pr_0(p_1(X) / p_0(X) \geq k)=\alpha.
$$
where $\Pr_0$/$\Pr_1$ are the distributions under the null/alternative and $p_0/p_1$ are their densities. The NP lemma states that this test is UMP.  

The NP test is often written as 
$$
\phi(X) = \begin{cases}
1,& L(X) > c,\\
\gamma,& L(X)=c,\\
0,&L(X)<c,
\end{cases}
$$
where $L$ is the likelihood ratio $p_{1}/p_{0}$ and $\gamma$ and $c$ are chosen that such that $\E_{P_0} [\phi(X)]=\alpha$. In the continuous case, $\gamma$ is unimportant since $L(X)=c$ has probability zero. But it matters in the discrete case ([[Neyman-Pearson lemma for discrete distributions]]) where it's used to ensure that the test has size exactly $\alpha$. 
## Proof 1
Let $\phi$ denote the likelihood ratio test and $\psi$ denote any other level $\alpha$ test. Consider the integral
$$
I = \int(\phi(x) - \psi(x))(p_1(x) - k p_0(x)) \d x.
$$
We claim this integral is lower bounded by zero. If $\phi(x) = \psi(x)$ then this is immediate. If $\phi(x) =1$ then $p_1(x) \geq kp_0(x)$ by definition, so the product of both terms in the integral is nonnegative. Likewise, if $\phi(x)=0$ then both terms are non-positive. The claim follows.

This gives that
$$
\begin{align}\int(\phi(x) - \psi(x)) p_1(x)\d x &\geq k\int(\phi(x) - \psi(x))p_0(x)\d x \\ 
&=k\E_{H_0}[\phi(X) - \psi(X)]  \\
&= k (\Pr_{H_0}(\phi(X) = 1) - \Pr_{H_0}(\psi(X)=1))  \\ 
&\geq k\alpha - k\alpha =0, 
\end{align}
$$
since $\phi$ is size $\alpha$ and $\psi$ is level $\alpha$, by assumption. Therefore,
$$
\Pr_{1}(\phi(X) = 1) - \Pr_{1}(\psi(X)=1)\geq 0,
$$
which is the desired result. Note this also implies uniqueness: If $\psi$ is also assumed to be UMP, then $\int (\phi(x) - \psi(x)) p_1(x) \d x = 0$ so $k \int (\phi(x) - \psi(x)) p_0(x) \d x = 0$ as well. Therefore, $I=0$ and since we showed the integrand is nonnegative above, this implies the integrand is 0. Therefore, 
$$
(\phi(x) - \psi(x)) (p_1(x) - kp_0(x)) =0,
$$
implying that $\psi(x) = \phi(x)$ whenever $p_1(x) \neq kp_0(x)$. Moreover, the set $\{ x: p_1(x)= kp_0(x)\}$ has positive measure, then we can show the randomization levels must be the same, otherwise one of the two tests would have less power than the other. 
## Proof 2 

Turn the problem into a constrained optimization problem using Lagrange multipliers. We want to maximize $\int \phi(x)p_1(x)\d x$ subject to the constraint that $\int \phi(x)p_0(x)\d x \leq \alpha$. So we want to maximize 
$$
\begin{align}\calL(\phi, \lambda) &= \int \phi(x) p_1(x)\d x - \lambda\left(\int \phi(x)p_0(x) -\alpha\right) \\ 
&= \int \phi(x) (p_1(x) - \lambda p_0(x))\d x - \lambda \alpha.
\end{align}
$$
For a given $\lambda$, the test $\phi$ which maximizes this clearly is 1 when $p_1(x)\geq \lambda p_0(x)$ and 0 otherwise. And what is $\lambda$? Given our choice of $\phi$ we have
$$
\int \phi(x) p_0(x) = \int_{p_1(x)\geq \lambda p_0(x)} p_0(x) \d x = \Pr_0 (p_1(x)/p_0(x)\geq \lambda).
$$
If we want this to equal $\alpha$ clearly we take $\lambda = k$.
