Given some parameter space $\Theta\subset\Re^d$, consider $\{R_\theta: \theta\in\Theta\}$, where $R_\theta = \la \xi,\theta\ra$ and $\xi_i$ is a Rademacher random variable (i.e., $\pm 1$ with equal probability). This process is called a Rademacher process. The expected value of the supremum of this process (see [[maximal inequalities]]), 
$$
\calR(\Theta) = \E\sup_{\theta\in\Theta} R_\theta,
$$
is the Gaussian complexity of $\Theta$. Like [[metric entropy]], it's a measure of the size of $\Theta$. If we replace $w_i$ with Rademacher random variables, then we obtain the [[Gaussian complexity]]. 

The relationship to the Gaussian complexity is $\calR(\Theta) \leq \sqrt{\frac{\pi}{2}} \calG(\Theta)$. 