A fundamental result when testing composite nulls in the setting of [[game-theoretic hypothesis testing]]. 

Given any composite null $\calP$ against any point null $Q$, there exists a unique [[e-value]] (i.e., e-variable) $X^*$ such that $$
\E_Q [X/X^*]\leq 1,\quad \text{for all e-variables }X\text{ for }\calP.
$$This always exists. Note that $X^*$ is an e-variable under $\calP$, not under $Q$.  Some consequences of this definition: 

**Log-optimality**

The numeraire is the log-optimal e-value under $Q$: $\E_Q [\log(X/X^*)]\leq 0$. This means it is in some sense the best e-value when testing against the alternative $Q$, as its log-wealth grows the fastest (see [[maximizing log-wealth]] and [[growth rate conditions in sequential testing]]).

**Reverse Information Project (RIPr)**

Define the (sub)-measure $P^*$ by $d P^* / dQ = 1/X^*$ for numeraire $X^*$. $P^*$ satisfies $$
\E_Q [\log X^*] = \sup_{X\in \calE} \E_Q[\log X] = \inf_{P\in \calP^{\circ\circ}} H(Q \| P) = H(Q \| P^*),
$$i.e., it is the [[reverse information projection (RIPr)]]. Here $\calE$ is the set of e-variables for $\calP$. So the first equality says that again that $X^*$ is log-optimal among all e-variables. $\calP^{\circ\circ}$ is the _bipolar_ of $\calP$, which is the set of measures $R$ such that $\E_R[X]\leq 1$ for all $X\in\calE$. $\calP^{\circ\circ}$ is the _effective null hypothesis_, i.e., all distributions where the e-values for $\calP$ will also be e-values, so in some sense we won't be able to tell $\calP$ and $\calP^{\circ\circ}$ apart. The final inequality says that $P^*$ achieves the minimum relative entropy wrt $Q$, which is also the optimal growth rate.  
