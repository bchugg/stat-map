



Perhaps the most basic desiderate in UQ is marginal consistency (see [[marginal estimation]] and [[online marginal estimation]]). Here we want roughly that the average prediction matches the average outcome. This is a pretty weak guarantee. 

Two ways of strengthening marginal consistency is to focus on [[calibration]] or [[multi-group consistency]], which are guarantees where we condition on something. In the calibration case we condition on the model output (eg for mean calibration we want $v\approx \E[y|f(x)=v]$). In the multi-group setting we condition on group membership (eg we want $\E[y|g(x)=1] \approx \E[f(x)|g(x)=1])$ for all groups $g$). 

We can combine calibration and multi-group consistency in [[multi-group calibration]] which, in the mean estimation setting, asks that $v\approx \E[y|f(x) = v, g(x)=1]$ for all $v$ and $g$. 

UQ can occur in both the batch setting and the sequential setting. 

# Batch setting 



# Sequential setting 

Every time $t$,  
- the adversary chooses a pair $(x_t,y_t)$ (perhaps from a distribution, perhaps not)
- We see $x_t$ only and produce a prediction $p_t$ 
- $y_t$ is revealed to us 

Ideally we want to develop algorithms for the sequential setting which constrain the adversary's behavior as little as possible. 

Of course, the sequential setting is strictly harder than the batch setting, in the sense that if we have a good sequential algorithm then we can just run it in the batch setting and obtain the same guarantee. 


# References 
- [Textbook](https://www.cis.upenn.edu/~aaroth/uncertainty-notes.pdf) by Aaron Roth 