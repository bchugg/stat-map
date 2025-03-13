---
created: 2024-08-29
lastmod: 2025-03-13
---

Uncertainty quantification is a vague term. It might mean classical parameter estimation techniques in statistics (like generating [[confidence intervals]], for instance). But in modern ML it often means techniques to ensure that black box predictive models and behaving in desired ways. That's what I'll focus on here. 

Perhaps the most basic desiderate in UQ is marginal consistency (see [[marginal consistency]] and [[online marginal estimation]]). Here we want roughly that the average prediction matches the average outcome. This is a pretty weak guarantee. 

Two ways of strengthening marginal consistency is to focus on [[calibration]] or [[multi-group consistency]], which are guarantees where we condition on something. In the calibration case we condition on the model output (eg for mean calibration we want $v\approx \E[y|f(x)=v]$). In the multi-group setting we condition on group membership (eg we want $\E[y|g(x)=1] \approx \E[f(x)|g(x)=1])$ for all groups $g$). 

We can combine calibration and multi-group consistency in [[multi-group calibration]] which, in the mean estimation setting, asks that $v\approx \E[y|f(x) = v, g(x)=1]$ for all $v$ and $g$. 

# Modifying black-box functions 

Often we are interested in "patching" or altering an existing black-box model $f$ so that it it meets our goal (whether calibration, consistency, etc). This is often done iteratively: we pick the output that is maximizing our notion of error (eg the term that maximizes [[calibration#Calibration error]]) and then "fix it". Variants of this same idea occur in [[marginal consistency]], [[multi-group consistency]], and [[multi-group calibration]]. The proofs of these algorithms typically rely on demonstrating that every time the function is modified, some notion of error (eg [[squared error]] or [[pinball loss]]) decreases, meaning the algorithm must terminate. Bounding by how much it goes down gives you a bound on the number of iterations. 

For quantiles, we typically require that the cdf of the distribution be Lipschitz.  


## Sequential vs batch setting 
UQ can occur in both the batch setting and the sequential setting. The sequential setting is as follows: 

Every time $t$:  
- the adversary chooses a pair $(x_t,y_t)$ (perhaps from a distribution, perhaps not)
- We see $x_t$ only and produce a prediction $p_t$ 
- $y_t$ is revealed to us 

Ideally we want to develop algorithms for the sequential setting which constrain the adversary's behavior as little as possible. 

Of course, the sequential setting is strictly harder than the batch setting, in the sense that if we have a good sequential algorithm then we can just run it in the batch setting and obtain the same guarantee. 

# Reading
- [Textbook](https://www.cis.upenn.edu/~aaroth/uncertainty-notes.pdf) by Aaron Roth 