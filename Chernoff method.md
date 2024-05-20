The Chernoff method applies Markov's inequality to the nonnegative random variable $e^{\lambda X}$, and then chooses $\lambda$ to optimize the bound. This often results in tighter bounds and [[concentration inequalities]] than working with the random variable directly. 

In particular, for a random variable $X$, Markov's inequality gives that 
$$\Pr(X\geq t) = \Pr(e^{\lambda X}\geq e^{\lambda t}) \leq e^{-\lambda t}\E[e^{\lambda X}].$$
This holds for all $\lambda>0$, so we obtain the bound 
$$\Pr(X\geq t)\leq \inf_{\lambda >0}e^{-\lambda t}\E[e^{\lambda X}] = \inf_{\lambda >0} e^{-\lambda t}M_X(\lambda),$$
where $M_X$ is the [[MGF]] of $X$. If we place distributional assumptions on $X$ (eg bounded, [[sub-Gaussian distributions|sub-Gaussianity]]), then we can solve for the optimal value of $\lambda$. 