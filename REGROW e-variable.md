Stands for "Relative Growth optimality in the worst case." This is one idea of how to extent the [[GRO e-variable]] to composite alternatives. Like GRO, it was coined by [Grunwald, De Heide, and Koolen](https://arxiv.org/abs/1906.07801) (2023). In practice, it's considered less often than the [[GROW e-variable]]. 

Consider a composite alternative; a class of distributions $\calQ$. REGROW finds the test [[supermartingale]] $(M_t)$ to maximize 
$$

\inf_{Q\in \calQ} \E_Q[\log M_\tau - \log M_\tau^Q],

$$
where $M_\tau^Q$ is the GRO process under a particular $Q\in\calQ$. 

In [[game-theoretic hypothesis testing]] (ad [[hypothesis testing]] more generally) and $\calQ$ is an exponential family being tested against a point null $P$, then the [[test-martingale]] obtained from [[Jeffreys prior]] is REGROW. 
