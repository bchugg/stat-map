#uncertainty-quantification #calibration 

Multi-group calibration (aka multicalibration) seeks to combine [[calibration]] with [[multi-group consistency]]. That is, in the mean case we're looking for a model $f$ such that 
$$
\E[y| g(x) = 1, f(x) =v] \approx v,
$$
and in the quantile case 
$$
\Pr(y\leq f(x) | g(x) = 1, f(x) =v) \approx q.
$$
Here we're assuming that $f$ has a finite range. 

# Mean calibration 

A common metric here is based on the [[average calibration error]], but modified for the group-consistency setting. Define 
$$K_2 = K_2(f, g, P) = \sum_{v\in \range(f)} \Pr(f(x) = v|g(x)=1)(v - \E[y|f(x) = v, g(x)=1])^2.$$ We can also define $K_1, K_\infty$ etc analogously. $f$ is $\alpha$-approximately multicalibrated if for all groups $g$, 
$$
K_2 \leq \frac{\alpha}{\mu(g)}.
$$
Again, as in the case of [[multi-group consistency]], we weight the metric by $\mu(g)$. Note that this definition of multicalibration is wrt a specific family of groups. 

As discussed at a high level in [[uncertainty quantification#Modifying black-box functions|uncertainty quantification:Modifying black-box functions]] and seen in [[marginal consistency]] and [[multi-group calibration]], we can develop algorithms to fix black-box predictors $f$ to make them (approximately) multicalibrated.
 

#open-question
Open question: Is there a one-shot version of the multicalibrate algorithm, like there is for [[multi-group consistency]]?  

