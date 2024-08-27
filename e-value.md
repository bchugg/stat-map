An e-variable with respect to a set of distributions $\calP$ is a nonnegative random variable $X$ such that $$\E_P[X]\leq 1,\quad \forall P\in\calP.$$It is a measure of [[evidence against the null]], somewhat analogous to [[p-value|p-values]] but defined in terms of expectations instead of probabilities. They are immune to lots of the [[issues with p-values]]. The realized value of $X$ is called an e-variable (akin to p-variables), though we often simply refer to the e-variable as an e-value. 

E-values are intimately tied to [[hypothesis testing]]. If we are testing the null $P\in\calP$, a large e-value can be used to reject the null at level $\alpha$ since, by Markov's inequality ([[basic inequalities]]). If we are testing the null $P\in\calP$, a large e-value can be used to reject the null at level $\alpha$ since, by Markov's inequality ([[basic inequalities#Markov's inequality|basic inequalities:Markov's inequality]]), $\Pr(X\geq 1/\alpha)\leq \alpha$. Thus, designing e-values which will be large under the alternative is a fruitful strategy in hypothesis testing. This is the focus of [[game-theoretic hypothesis testing]]. 

E-values also have a sequential analogue, useful in [[sequential statistics]] and [[sequential hypothesis testing]],  called an [[e-process]]. An e-process is simply a stochastic process which is an e-value at each stopping time. 

The [[numeraire e-variable]] is a special (and in some sense, optimal) e-value when testing composite alternatives. It generalizes the [[reverse information projection (RIPr)]]. 

# References 
- [Safe testing](https://arxiv.org/abs/1906.07801) by Grunwald, De Heide, and Koolen 
- [The numeraire e-variable](https://arxiv.org/pdf/2402.18810.pdf), by Larsson, Ramdas, and Ruf. 