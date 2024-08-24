Most [[p-value|p-values]] hold only at fixed times. That is, a p-value $P_n$ based on $n$ observations has the guarantee 
$$
\text{for all data-independent times }n, \quad \Pr_0(P_n \leq\alpha)\leq \alpha.
$$
An [[anytime-valid]] p-value holds at all stopping times: $$\text{for all stopping times }\tau, \quad \Pr_0(P_\tau \leq \alpha),\alpha.$$Such p-values enable [[safe, anytime-valid inference (SAVI)]]. Anytime-valid p-values are to p-values what [[e-process|e-processes]] are to [[e-value|e-values]]. 

Here $\Pr_0$ is understood to be the probability under the null. Of course, it can also be replaced with the supremum over a class of null distributions, the case in composite hypothesis testing. 