Anytime validity is a property of inferential tasks. In particular, we say that something is anytime-valid if its properties hold at all [[stopping-time|stopping times]], not just at some fixed-time determined a priori. (Note that by "time" we usually mean the number of observations). 

Anytime-validity has a close relationship to [[time-uniform|time uniformity]]. For probability statements, the two concepts are identical. Formally, for a set of events $\{A_t\}$ , 
$$
\Pr(\exists t: A_t) \leq \alpha \Leftrightarrow \Pr(A_\tau)\leq \alpha, \forall \tau,
$$
where $\tau$ is a stopping time. But they are not equivalent for statements concerning expected values. Suppose for instance that $\{E_t\}$ is a collection of random variables. Then the statement $\E[\sup_t E_t]\leq c$ implies that for all $\tau$, $\E[E_\tau]\leq c$ but not vice versa. The first statement is actually equivalent to the statement $\E[E_T]\leq c$ for all random times $c$ (not only for stopping times). 

The equivalence when discussing probability statements means that [[confidence sequences]] are objects that are both time-uniform and anytime-valid. But [[e-process|e-processes]], which are defined in terms of stopping times, are not necessarily time-uniform.  

# Refs 
- [Admissible anytime-valid sequential inference must rely on nonnegative martingales](https://arxiv.org/pdf/2009.03167) by Ramdas et al. 