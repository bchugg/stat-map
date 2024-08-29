A sub-exponential distribution has tails which decay at an exponential rate. This is a weaker condition than [[sub-Gaussian distributions|sub-Gaussianity]] (meaning that sub-Gaussian tails decay at a faster rate, $\propto t^2$ instead of $\propto t$) but is still considered a light-tailed condition as the [[MGF]] exists in some neighborhood. 

Sub-exponential conditions are also natural conditions to study because a variable $X$ is sub-Gaussian iff $X^2$ is sub-exponential. So sub-exponential distributions arise naturally when studied the square (or squared norm) of sub-Gaussian variables and processes. 

The most straightforward definition of a sub-exponential random variable $X$ with mean $\mu$ is: 
$$

\E[\exp(\lambda (X-\mu))] \leq \exp(\lambda^2\sigma^2/2),

$$
for all $\lambda\leq 1/c$ where $c\in [0,\infty)$. In this case we say $X$ is $(\sigma,c)$-sub-exponential. Note that $X$ is $\sigma$-sub-Gaussian if it is $(\sigma, 0)$-sub-exponential. 

There is also a natural [[anisotropic distribution|anisotropic]] version for a random vector $X$, namely: 
$$

\E\exp(\lambda\la \nu, X-\mu\ra) \leq \exp(\lambda^2\la \nu, \Sigma\nu\ra/2),

$$
for all $\nu\in\dsphere$ and some [[positive semi-definite]] matrix $\Sigma$. As in the case of [[sub-Gaussian distributions]], there is also the accompanying [[isotropic distributions|isotropic]] version, which we don't state. 

In the scalar setting, equivalent formulations are: 
- $\Pr(|X|\geq t)\leq 2e^{-Kt}$ for some $K$ 
- $\sqrt{|X|}$ is sub-Gaussian. 
- If $\norm{X}_{\psi_1}$ is finite, where $\psi_1$ is the sub-exponential [[Orlicz norm]]. 
