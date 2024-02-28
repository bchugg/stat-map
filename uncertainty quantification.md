
- [[marginal estimation]]
- [[online marginal estimation]]

Can be in batch or sequential setting. 

# Sequential setting 

Every time $t$,  
- the adversary chooses a pair $(x_t,y_t)$ (perhaps from a distribution, perhaps not)
- We see $x_t$ only and produce a prediction $p_t$ 
- $y_t$ is revealed to us 

Ideally we want to develop algorithms for the sequential setting which constrain the adversary's behavior as little as possible. 

Of course, the sequential setting is strictly harder than the batch setting, in the sense that if we have a good sequential algorithm then we can just run it in the batch setting and obtain the same guarantee. 


# References 
- [Textbook](https://www.cis.upenn.edu/~aaroth/uncertainty-notes.pdf) by Aaron Roth 