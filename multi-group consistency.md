Multi-group consistency is [[marginal consistency]] but it holds simultaneously across possibly intersecting groups. (In fact, the notion of marginal-consistency is only interesting if the groups are intersecting; otherwise you can just port over the techniques from marginal consistency and apply them separately to each group). 

We operationalize a group $g$ as a function $g(x)=\{0,1\}$, indicator whether or not an observations with features $x$ belongs to the group. Let $\mu(g) = \Pr[g(x)=1]$ be the fraction of those in group $g$ in the population.  

A more challenging notion than multi-group consistency is [[multi-group calibration]]. 

# Mean consistency 

Like in [[marginal consistency#Mean consistency|marginal consistency:Mean consistency]], we want that $f(x) \approx$ y, but we want this guarantee conditional on belonging to each group. Formally, say that a model $f$ is $\alpha$-approximate group conditional mean consistent if for every group $g$, 
$$
\left(\E[f(x) | g(x)=1] - \E[y|g(x)=1]\right)^2 \leq \frac{\alpha}{\mu(g)}.
$$
Note that we re-weight the RHS by $\mu(g)$. Intuitively, if $\mu(g)$ is extremely small, it seems unfair to ask a model to be as consistent on that group. 

Similar to the marginal mean consistency case, there is a simple patching function which renders a function that is not group mean consistent into one that is. (To be perfectly consistent requires distributional access, but one can of course get finite sample guarantees using concentration arguments.)

While this patching procedure is usually presented as a sequential algorithm, there is also a one-shot algorithm which transforms the problem in to a simple optimization problem (ditto for quantile consistency below). 
# Quantile consistency 

A model is $\alpha$-approximate group conditional quantile consistency if 
$$
\left(\Pr[y\leq f(x) | g(x) = 1] - q\right)^2 \leq \frac{\alpha}{\mu(g)}.
$$
A similar patching algorithm applies here. Note that this patching algorithms again rely on showing that a specific loss is decreasing (either [[squared error]] or [[pinball loss]]) every time we modify the function. This is a very common analysis tool for these kinds of algorithms. 


# References 
- Chapter 4, Aaron Roth's [book](https://www.cis.upenn.edu/~aaroth/uncertainty-notes.pdf). 