
To motivate maximal inequalities, I'll quote from the opening of Michael Talagrand's excellent book [_Upper and Lower Bounds for Stochastic Processes_](https://link.springer.com/book/10.1007/978-3-642-54075-2): 

> What is the maximum level a certain river is likely to reach over the next 25 years? What is the likely magnitude of the strongest earthquake to occur during the life of a planned nuclear plant, or the speed of the strongest wind a suspension bridge will have to stand? The present book does not deal with such fundamental practical questions, but rather with some (arguably also fundamental) mathematics which have emerged from the consideration of these questions. All these situations can be modeled in the same manner. The value $X_t$ of the quantity of interest (be it water level or speed of wind) at time $t$ is a random variable. What can be said about the maximum value of $X_t$ over a certain range of $t$? In particular, how can we guarantee that, with probability close to one, this maximum will not exceed a given threshold?

Mathematically, maximal inequalities are concerned with suprema of a stochastic process $(X_\theta)_{\theta\in \Theta}$ where $\Theta$ is an index set in some space—often in $\Re^d$ be could be a [[Hilbert space]] or a [[Banach space]].  That is, we want to compute $$\E\sup_{\theta\in\Theta} X_\theta.$$Often $\Theta$ is equipped with a metric $d$ and we consider the [[metric space]] $(\Theta, d)$. $\Theta$ could be time (i.e., $\Re_{\geq0}$ or $\mathbb N$), but is usually not. 

Both [[Gaussian complexity]] and [[Rademacher complexity]] are defined as maximal inequalities. 

Maximal inequalities can be used to obtain [[concentration inequalities]]. If $(S_t)$ is some process, then $\norm{S_t} = \sup_{\theta} \la \theta, S_t\ra$, and maximal inequalities help bound the latter quantity. See [[techniques for multivariate concentration]]. 


# References 
- Wainwright's _High dimensional statistics: A nonasymptotic viewpoint_, Chapter 5. 
- Talagrand's [_Upper and Lower Bounds for Stochastic Processes_](https://link.springer.com/book/10.1007/978-3-642-54075-2), Chapter 2. 

