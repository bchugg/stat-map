Given some parameter space $\Theta\subset\Re^d$, consider $\{G_\theta: \theta\in\Theta\}$, where 
$$

G_\theta = \la w,\theta\ra, \quad w_i \sim N(0,1).

$$
This is called a canonical Gaussian process. The expected value of the supremum of this process (see [[maximal inequalities]]), 
$$

\calG(\Theta) = \E\sup_{\theta\in\Theta} G_\theta,

$$
is the Gaussian complexity of $\Theta$. Like [[metric entropy]], it's a measure of the size of $\Theta$. If we replace $w_i$ with Rademacher random variables, then we obtain the [[Rademacher complexity]]. 

The relationship to the Rademacher complexity is $\calR(\Theta) \leq \sqrt{\frac{\pi}{2}} \calG(\Theta)$. 