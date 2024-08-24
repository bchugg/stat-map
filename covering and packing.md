Intuitively, covering and packing numbers are precisely what you think they are. 

> [!note] (Definition: $\delta$-cover and covering number)
 > Let $(X,\rho)$ be a [[metric space]].  A $\delta$-cover of $X$ wrt to $\rho$ is a subset $\{x_1,\dots,x_n\}\subset X$ such that for any $x\in X$ there exists some $x_i$ such that $\rho(x,x_i)\leq \delta.$ The cardinality of the smallest $\delta$-cover of $X$ wrt $\rho$ is called the $\delta$-covering number, often denoted $N(\delta; X,\rho)$. 
 > 

> [!note] (Definition: $\delta$-packing and packing number)
 > Let $(X,\rho)$ be a metric space.  A $\delta$-packing of $X$ wrt to $\rho$ is a subset $\{x_1,\dots,x_n\}\subset X$ such that $\rho(x_i,x_j)\geq \delta$ for all distinct $i,j$.  The cardinality of the largest $\delta$-packing of $X$ wrt $\rho$ is called the $\delta$-packing number, often denoted $M(\delta; X,\rho)$. 
 > 

Covering numbers and packing numbers are related as follows: 
$$
M(2\delta; X,\rho) \leq N(\delta; X,\rho)\leq M(\delta; X,\rho).
$$
The [[metric entropy]] of $(X,\rho)$ is $\log N(\delta; X,\rho)$. 

# Examples 
- Unit cube $[-1,1]^d$ with $\ell_1$ distance has $N(\delta)\leq (1 + 1/\delta)^d$. 
- Euclidean ball with $\ell_2$ norm has $\delta^{-d} \leq N(\delta) \leq ( 1 + 2/\delta)^d\leq (3/\delta)^d$.  