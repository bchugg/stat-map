
The method of moments is a generalization of Chebyshev's inequality ([[basic inequalities#Chebyshev's inequality]]). Notice that by Markov's inequality, we have 
$$\Pr(|X - \mu| \geq \lambda) = \Pr( | X - \mu|^k \geq \lambda^k ) \leq \frac{\E[|X-\mu|^k]}{\lambda^k}.$$
Since this holds for all $k$, we can minimize the right hand side over all $k$, i.e., 
$$\Pr( |X - \mu| \geq \lambda) \leq \inf_{k\in\mathbb{N}} \frac{\E|X-\mu|^k}{\lambda^k}.$$
This is somewhat reminiscent of the [[Chernoff method]]. In fact, the method of moments for concentration can be shown to be tighter than the Chernoff method, in the sense that 
$$\inf_{k\in\mathbb{N}} \frac{\E|X-\mu|^k}{\lambda^k} \leq \inf_{t> 0} \frac{\E\exp(t(X-\mu))}{\exp(t\lambda)},$$
for all $\lambda$ if $X\geq 0$ and its [[MGF]] exists.  However the Chernoff method is analytically much more tractable, hence more popular. It's difficult to find the $k$ which minimizes the left hand side. 
