#sufficiency #estimators #decision-theory

We observe data drawn from some $P_\theta$ for some $\theta\in\Theta$.  Let $\ell:\Theta\to\Re$ be any convex loss on estimates of $\theta$ (see [[statistical decision theory]]). The Rao-Blackwell theorem states that the expected loss of an estimator $\wh{\theta}$ can never be made worse by conditioning on a [[sufficient statistic]] $T$. That is, if we consider $\widetilde{\theta} = \E[\wh{\theta}|T]$, then 
$$
\E \ell(\wh{\theta}) \geq \E\ell(\widetilde{\theta}).
$$
Sufficiency is only used in order to define the estimator $\widetilde{\theta}$ in order to make sure it's actually independent from $\theta$ (otherwise the theorem is useless). 

The estimator $\widetilde{\theta}$ is often called the Rao-Blackwellization of $\wh{\theta}$. The theorem is usually applied with the [[squared error]]. 