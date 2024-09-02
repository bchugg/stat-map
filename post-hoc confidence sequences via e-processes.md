Let $\calP$ be some set of distributions, and $\calP_\theta\subset\calP$ be those distributions which share some parameter $\theta$: eg the set of distributions on $[0,1]$ with mean $\theta$. We receive observations from $P\in \calP_{\theta^*}$ for some $\theta^*$ and want to form a post-hoc CS (see [[post-hoc valid confidence sequences]]) for $\theta^*$. 

Let $(E_t^\theta)_{t\geq 1}$ be an [[e-process]] for $\calP_\theta$: 
$$
\sup_{P\in\calP_\theta} \E[E_\tau^\theta]\leq 1\quad\text{for all stopping times }\tau.
$$
For any $\alpha\in(0,1)$, let $C_t(\alpha) = \{\phi: E_t^\phi < 1/\alpha\}$. (This is precisely how we'd built a [[confidence intervals|CI]] or [[confidence sequences|CS]] with an e-process or an [[e-value]] at a fixed time $t$). Then, $\{(C_t(\alpha))_{t\geq 1}:\alpha\in(0,1)\}$ is immediately post-hoc valid: For any stopping time $\tau$, 
$$
\sup_{P\in\calP_{\theta^*}}\E_P \left[\sup_{\alpha\in(0,1)} \frac{\ind(\theta^*\notin C_\tau(\alpha))}{\alpha}\right] = \sup_{P\in\calP_{\theta^*}}\E_P \left[\sup_{\alpha\in(0,1)} \frac{\ind(E_\tau^{\theta^*}\geq 1/\alpha)}{\alpha}\right] \leq \sup_{P\in \calP_{\theta^*}} \E_P [E_\tau^{\theta^*}] \leq 1,
$$
where the second inequality follows from basic case analysis on the indicator. 

Note that e-processes accomplish this for free. We didn't have to add additional assumptions. Therefore procedures which are already working with e-processes (such as [[estimating means by betting]]) are immediately post-hoc valid in this sense.  