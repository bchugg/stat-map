A Banach space is a complete normed vector space. That is, it's a vector space equipped with a norm $\norm{\cdot}$ which induces a distance function in the obvious way. Every Cauchy sequence converges to some point in the space. 

We often assume the space is _separable_. #todo what is separable?

For lots of statistical analysis in Banach spaces we place a smoothness assumption on the space. Without such a smoothness assumption, roughly speaking, values that are close to each other in the space may behave so differently that [[statistical inference]] becomes impossible. 

Formally, a Banach space $(B,\norm{\cdot})$ is $\beta$-smooth if the squared norm $\norm{\cdot}^2$ is $\beta$-smooth with respect to $\norm{\cdot}$, where we say that a function $f:B\to\Re$ is $\beta$-smooth with respect to $\norm{\cdot}$ if for any $x,y\in B$, 
$$

f(y) \leq f(x) + D_x f(x)(y-x) + \frac{\beta}{2}\norm{y-x}^2,

$$
where $D_x f(x)(y-x)$ is the Gateaux derivative of $f$ at $x$ in the direction $y-x$.  

