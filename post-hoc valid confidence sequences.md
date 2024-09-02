We might extend the desiderata of [[post-hoc hypothesis testing]] to post-hoc confidence sequences. 

[[confidence sequences|Confidence sequences]] are the [[time-uniform]] equivalent to [[confidence intervals]]. But what if we want time-uniformity in addition to post-hoc validity, i.e., the ability to change $\alpha$ after the fact? 
As we did in [[post-hoc hypothesis testing]], formulating the notion of post-hoc validity requires discussing risk instead of error probabilities. We might say a family of confidence sequences $\{(C_t(\alpha))_{t\geq 1}:\alpha\in(0,1)\}$ for a parameter $\mu$ is post-hoc valid if  
$$
\sup_{P\in\calP_\mu} \E_P\left[\sup_{\alpha\in(0,1)}\frac{\ind(\mu\notin C_\tau(\alpha))}{\alpha}\right]\leq 1\quad \text{for all stopping times }\tau,
$$
where $\calP$ is the family of distributions (possibly a singleton) which have the relevant parameter $\mu$ (eg all distributions in some class with mean $\mu$).  Note we need a family of confidence sequences since the CS may be different for different $\alpha$. 

Post-hoc valid confidence can be built with e-processes: [[post-hoc confidence sequences via e-processes]]. 