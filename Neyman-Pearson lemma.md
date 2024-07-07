States that the [[likelihood-ratio test]] is the [[uniformly most powerful test]] among all level-$\alpha$ tests when testing simple nulls against simple alternatives. The NP lemma is generalized by the [[Karlin-Rubin theorem]]. 

Suppose we are testing $H_0:\theta = \theta_0$ vs $H_1: \theta = \theta_1$. Consider the likelihood ratio test, which says to reject if $L(\theta_1)/L(\theta_0)\geq k$ where $k$ is chosen so that 
$$\Pr_{H_0}(L(\theta_1) / L(\theta_0) \geq k)=\alpha.$$
The proof is easy so let's do it. Let $\phi$ denote the likelihood ratio test and $\psi$ denote any other level $\alpha$ test. Consider the integral $$\int(\phi(x) - \psi(x))(L(\theta_1) - kL(\theta_0)) \d x.$$We claim this integral is lower bounded by zero. If $\phi(x) = \psi(x)$ then this is immediate. If $\psi(x) =1$ then $L(\theta_1) \geq kL(\theta_0)$ by definition, so the product of both terms in the integral is nonnegative. Likewise, if $\psi(x)=0$ then both terms are non-positive. The claim follows. 

This gives that $$
\begin{align}\int(\phi(x) - \psi(x)) L(\theta_1)\d x &\geq k\int(\phi(x) - \psi(x))L(\theta_0)\d x \\ 
&=k\E_{H_0}[\phi(X) - \psi(X)]  \\
&= k (\Pr_{H_0}(\phi(X) = 1) - \Pr_{H_0}(\psi(X)=1))  \\ 
&\geq k\alpha - k\alpha =0, 
\end{align}
$$since $\phi$ is size $\alpha$ and $\psi$ is level $\alpha$, by assumption. Therefore, 
$$\Pr_{H_1}(\phi(X) = 1) - \Pr_{H_1}(\psi(X)=1)\geq 0,$$
which is the desired result. 