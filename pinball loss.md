The typical loss used when attempting to estimate quantiles. For a target quantile $q$, the loss is 
$$
L_q(\tau, y) = \begin{cases}
(y-\tau)q, & y>\tau,\\
(\tau - y)(1-q), & y\leq \tau.
\end{cases}
$$
Here $\tau$ should be interpreted as your guess for the $q$-th quantile, and $y$ is the observed value. In the case where $q=1/2$ we have 
$$

L_{1/2}(\tau, y) = \frac{1}{2}|\tau - y|,

$$
which is just the $\ell_1$ loss, the minimizer of which the median. 

Suppose $q=0.9$. Then if $y>\tau$ we are "surprised" in some sense, since this should not happen very often. So the loss takes on a higher value (proportional to $q$). But if $y\leq \tau$ we are less surprised, so the loss is small. The minimizer of the loss can be shown to be exactly the $q$ quantile. 
