#hypothesis-testing #sequential-statistics #plug-in-method #mixture-method 

In [[game-theoretic hypothesis testing]], suppose we are testing a simple null vs a composite alternative. We receive samples $(X_t)$ are testing 
$$
H_0: (X_t) \sim P, \quad H_1 : (X_t) \sim Q \in \Theta_1.
$$In the simple vs simple case, [[testing by betting—simple vs simple]], the optimal payoff function turned out to simply be the likelihood-ratio of $Q$ and $P$. But now there is no single $Q$, the likelihood-ratio isn't well-defined. What do we do? 

Since the observations are revealed sequentially (we can simulate this in a batch setting), it's natural to try and "learn" some appropriate $Q\in \Theta_1$ that has good power (you could look at this as trying to learn the true distribution $Q^*\in\Theta_1$ using the data thus far). 

There are two general methods. 

# Plug-in method 

Since the methods are inherently sequential and the payoff function $S_t$ (see [[game-theoretic hypothesis testing#Payoff functions|game-theoretic hypothesis testing:Payoff functions]]) need only be $\calF_{t-1}$-measurable, we can employ the likelihood ratio test but change which $Q\in\Theta_1$ is used every time. That is, if $(X_t)\sim Q^*$, we can try and learn $Q^*$ over time. 

In particular, we can consider a payoff function $S_t = q_t(X_t|\calF_{t-1}) / p(X_t|\calF_{t-1})$. $Q_t$ can be chosen baed on $X_1,\dots,X_{t-1}$. Regardless of how it's chosen $S_t$ will remain a [[test-martingale]] for $P$. 
(We are assuming densities are well-defined, otherwise we resort to Radon-Nikodym derivatives.)

While it may be tempting to use [[MLE]]  to choose $Q_t$, this is advised against when the data are discrete, otherwise it may assign 0 probability to an outcome that may in fact occur, and we will go broke. 

# The mixture method

Instead of choosing a particular $Q\in\Theta_1$ to use at each timestep, we mix over all such distributions by placing a distribution over $\Theta_1$. That is, we take 
$$
S_t(X_t) = \int_{q\in \Theta_1} q(X_t|\calF_{t-1}) \rho_t(dq) \bigg / p(X_t|\calF_{t-1}),
$$where $\rho_t$ is the mixing distribution, and it may depend on $\calF_{t-1}$. Since averages of distributions remain distributions, the numerator remains a distribution and $S_t$ remains a [[test-martingale]]. But note there is no guarantee that the numerator remains a distribution in $\Theta_1$ (unless $\Theta_1$ happens to be [[fork-convex]]) . 
