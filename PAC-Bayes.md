# Master theorem 

Let $M_t(\theta)$ be a nonnegative [[supermartingale]] with initial value 1 for all $\theta\in\Theta$. Let $\nu$ be a data-free prior. Then, 
$$\Pr(\forall t, \forall\rho\in\Mspace{\Theta}: \E_\rho \log M_t(\theta) \leq \kl(\rho\|\nu) + \log(1/\delta))\geq 1-\delta.$$
This is the [[time-uniform]] version of the master theorem, but we can also state a master fixed-time version. This reads: Let $N(\theta)$ be nonnegative have expected value at most 1 (it is an [[e-value]]) for all $\theta\in\Theta$. Then 
$$\Pr(\forall\rho\in\Mspace{\Theta}: \E_\rho \log N(\theta) \leq \kl(\rho\|\nu) + \log(1/\delta))\geq 1-\delta.$$