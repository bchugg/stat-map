An e-variable with respect to a set of distributions $\calP$ is a nonnegative random variable $E$ such that $$
\E_P[E]\leq 1,\quad \forall P\in\calP.
$$It is a measure of [[evidence against the null]], somewhat analogous to [[p-value|p-values]] but defined in terms of expectations instead of probabilities. They are immune to lots of the [[issues with p-values]]. The realized value of $E$ is called an e-variable (akin to p-variables), though we often simply refer to the e-variable as an e-value. 

E-values are intimately tied to [[hypothesis testing]]. If we are testing the null $P\in\calP$, a large e-value can be used to reject the null at level $\alpha$ since, by Markov's inequality ([[basic inequalities#Markov's inequality|basic inequalities:Markov's inequality]]), $\Pr(E\geq 1/\alpha)\leq \alpha$. Thus, designing e-values which will be large under the alternative is a fruitful strategy in hypothesis testing. This is the focus of [[game-theoretic hypothesis testing]]. 
(See also [[growth rate conditions in sequential testing]], which investigates how to design e-values and e-processes, and [[testing by betting—simple vs simple]], [[testing by betting—simple vs composite]], [[testing by betting—composite vs composite]] to see e-values in practice). 

E-values have a natural interpretation in terms of [[game-theoretic probability]] (which leads to their applicability in hypothesis testing). 

E-values also have a sequential analogue, useful in [[sequential statistics]] and [[sequential hypothesis testing]], called an [[e-process]]. An e-process is simply a stochastic process which is an e-value at each stopping time (which thus provides a level-$\alpha$ test at each stopping time, again by Markov's inequality). 

The [[numeraire e-variable]] is a special (and in some sense, optimal) e-value when testing composite alternatives. 

# Properties 

The inverse of an e-value is a [[p-value]]: $\Pr(1/E \leq \alpha) = \Pr(E\geq 1/\alpha)\leq \alpha$. They tend to be more conservative than classical p-values, however (this is the price to pay for avoiding some of the issues with p-values). 

E-values solve the [[optional continuation]] problem, in the sense that the product of conditionally independent e-values remains an e-value. This is because such a product forms a [[test-martingale]]. 






# References 
- [Safe testing](https://arxiv.org/abs/1906.07801) by Grunwald, De Heide, and Koolen 
- [The numeraire e-variable](https://arxiv.org/pdf/2402.18810.pdf), by Larsson, Ramdas, and Ruf. 