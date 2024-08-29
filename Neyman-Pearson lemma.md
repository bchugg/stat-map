States that the [[likelihood-ratio test]] is the [[uniformly most powerful test]] among all level-$\alpha$ tests when testing simple nulls against simple alternatives. The NP lemma is generalized by the [[Karlin-Rubin theorem]]. 

Suppose we are testing $H_0:\theta = \theta_0$ vs $H_1: \theta = \theta_1$. Consider the likelihood ratio test, which says to reject if $p_1(\theta_1)/p_0(\theta_0)\geq k$ where $k$ is chosen so that 
$$

\Pr_0(p_1(\theta_1) / p_0(\theta_0) \geq k)=\alpha.

$$
where $\Pr_0$/$\Pr_1$ are the distributions under the null/alternative and $p_0/p_1$ are their densities. The NP lemma states that this test is UMP.  
## Proof 1

Let $\phi$ denote the likelihood ratio test and $\psi$ denote any other level $\alpha$ test. Consider the integral
$$
\int(\phi(x) - \psi(x))(p_1(x) - k p_0(x)) \d x.
$$
We claim this integral is lower bounded by zero. If $\phi(x) = \psi(x)$ then this is immediate. If $\psi(x) =1$ then $p_1(x) \geq kp_0(x)$ by definition, so the product of both terms in the integral is nonnegative. Likewise, if $\psi(x)=0$ then both terms are non-positive. The claim follows.

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

\Pr_{H_1}(\phi(X) = 1) - \Pr_{H_1}(\psi(X)=1)\geq 0,

$$
which is the desired result. 

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
