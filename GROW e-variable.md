Stands for "Growth rate optimality in worst case."

Similar to [[REGROW e-variable]] in that it seeks to extend [[GRO e-variable]] to composite alternatives, but we do not compare to the GRO process. Instead, we simply look for the process $(M_t)$ maximizing $$\inf_{Q\in\calQ} \E_Q \log M_\tau.$$Both REGROW and GROW should be considered as methods to extend the GRO condition to composite alternatives.  

GROW can be found by minimizing [[KL divergence]] between the convex hull of null and alternative distributions. The likelihood ratio that achieves this minimum is an [[e-value]]. 

