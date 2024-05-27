An e-variable with respect to a set of distributions $\cP$ is a nonnegative random variable $X$ such that $$\E_P[X]\leq 1,\quad \forall P\in\cP.$$ It is a measure of [[evidence against the null]], somewhat analogous to [[p-values]] but defined in terms of expectations instead of probabilities. They are immune to lots of the [[issues with p-values]]. The realized value of $X$ is called an e-variable (akin to p-variables), though we often refers to e-variables as e-values and vice-versa. 

E-values are intimately tied to [[hypothesis testing]]. If we are testing the null $P\in\cP$, a large e-value can be used to reject the null at level $\alpha$ since, by Markov's inequality ([[basic inequalities#Markov's inequality]]), $\Pr(X\geq 1/\alpha)\leq \alpha$. Thus, designing e-values which will be large under the alternative is a fruitful strategy in hypothesis testing (see, e.g., [[universal inference]] which explicitly uses e-values). 

E-values also have a sequential analogue, useful in [[sequential statistics]] and [[sequential hypothesis testing]],  called an [[e-process]]. An e-process is simply a stochastic process which is an e-value at each stopping time. 

# Numeraire e-value 

Let $\cP$ be a set of distributions, and $Q$ a distribution. The numeraire e-variable is the unique e-variable $X^*$ such that $$\E_Q [X/X^*]\leq 1,\quad \text{for all e-variables }X\text{ for }\cP.$$ This always exists. Note that $X^*$ is an e-variable under $\cP$. 

Some consequences of this definition: 

**Log-optimality**: 

The numeraire is the log-optimal e-value under $Q$: $\E_Q [\log(X/X^*)]\leq 0$. This means it is in some sense the best e-value when testing against the alternative $Q$, as its log-wealth grows the fastest ([[maximizing log-wealth]]).

**Reverse Information Project (RIPr)**

Define the (sub)-measure $P^*$ by $d P^* / dQ = 1/X^*$ for numeraire $X^*$. $P^*$ satisfies $$\E_Q [\log X^*] = \sup_{X\in \cE} \E_Q[\log X] = \inf_{P\in \cP^{\circ\circ}} H(Q \| P) = H(Q \| P^*).$$
Here $\cE$ is the set of e-variables for $\cP$. So the first equality says that again that $X^*$ is log-optimal among all e-variables. $\cP^{\circ\circ}$ is the _bipolar_ of $\cP$, which is the set of measures $R$ such that $\E_R[X]\leq 1$ for all $X\in\cE$. $\cP^{\circ\circ}$ is the _effective null hypothesis_, i.e., all distributions where the e-values for $\cP$ will also be e-values, so in some sense we won't be able to tell $\cP$ and $\cP^{\circ\circ}$ apart. The final inequality says that $P^*$ achieves the minimum relative entropy wrt $Q$, which is also the optimal growth rate.  


# References 
- [The numeraire e-variable](https://arxiv.org/pdf/2402.18810.pdf)