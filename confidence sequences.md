
A confidence sequence can be thought of as a sequence of sequentially valid [[confidence intervals]]). Formally, $(C_t)_{t\geq 1}$ is a $(1-\alpha)$-CS for a parameter $\theta$ if 
$$ \Pr(\exists t\geq 1: \theta \notin C_t) \leq \alpha.$$ That is, a CS is a time-uniform confidence interval. It avoids the known problem with confidence intervals that, if they are computed at different times, they risk contradicting themselves (eg an interval computed at time $t_1$ might not overlap with one at time $t_2$. ) 

They are common tools in [[safe, anytime-valid inference (SAVI)]]. 

# References 

- [Time-uniform, nonparametric, nonasymptotic confidence sequences](https://arxiv.org/abs/1810.08240) 
- 