---
lastmod: 2024-10-27
created: 2024-10-27
---

Consider the function 
$$
h_\alpha(u) = \begin{cases}
\ind\{u\geq 0\}, & \alpha = 0, \\
(1 + u/\alpha)^\alpha_+, & \alpha\in(0,\infty), \\
e^\alpha, & \alpha = \infty,
\end{cases}
$$
which is nondecreasing in $\alpha$ and $u$ (and continuous in $\alpha$ for $u\geq 0$).  Therefore, for any random variable $X$,  
$$
\Pr(X\geq t) = \E\ind\{\lambda ( X - t)\geq 0\} \leq \E\left(1 + \frac{\lambda(X -t)}{\alpha}\right)_+^\alpha\leq \E e^{\lambda (X - t)}.
$$
Thus, we see that the [[Chernoff method]] corresponds to the case $\alpha =0$ and [[basic inequalities#Markov's inequality]] corresponds to $\alpha = 0$. Considering other values of $\alpha$ can thus get us tighter inequalities than the Chernoff bound. Of course, for values of $\alpha$ in $(0,\infty)$ the bound is much less nicer to work with, especially for sums of random variables. 

While the Chernoff method requires that all moments exist (at least in some neighborhood), this method does not require that. Similarly to [[concentration via convex optimization]], because this method is tighter than Chernoff, if we really need tight concentration in practice we should try it.  