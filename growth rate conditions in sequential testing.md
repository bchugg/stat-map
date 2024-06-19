
In [[sequential hypothesis testing]] based on [[e-value|e-values]] (i.e., [[game-theoretic hypothesis testing]]), one wants to find e-values and [[e-process|e-processes]] which grow quickly under the alternative. "Quickly" is a non-technical condition, however. What exactly should be maximized? Various authors have used different conditions based on the particular problem at hand. 

## GRO 

"Growth rate optimality". Consider a simple alternative ([[testing by betting—simple vs simple]]). This says to find the e-value which maximizes $\E_Q [\log E_\tau]$ under the alternative $Q$. This is the same principle as [maximizing log-wealth].

This was coined by [Grunwald, De Heide, and Koolen](https://arxiv.org/abs/1906.07801) (2023). 

## REGROW 

"Relative Growth optimality in the worst case." Consider a composite alternative; a class of distributions $\calQ$. REGROW finds the test supermartingale $(M_t)$ to maximize 
$$\inf_{Q\in \calQ} \E_Q[\log M_\tau - \log M_\tau^O],$$
where $M_\tau^O$ is the GRO process. Also coined by Grunwald, De Heide, and Koolen. 

## GROW 

"Growth rate optimality in worst case."
Similar to above but we do not compare to the grow process. That is, we look for the process $(M_t)$ maximizing $$\inf_{Q\in\calQ} \E_Q \log M_\tau.$$Both REGROW and GROW should be considered as methods to extend the GRO condition to composite alternatives.  

