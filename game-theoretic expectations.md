
In [[game-theoretic probability]], the amount you'd be willing to sell a contract (variable) for is the _replication cost_. Let $(\Omega, \cZ)$ be a gamble space. Formally, we define the replication cost as  
$$\inf\{\alpha\in\Re: \exists Z\in\cZ\text{~ s.t ~} Z+\alpha \geq X\}.$$
That is, $\forall\omega, Z(\omega) + \alpha \geq X(\omega)$. The intuition is that the replication cost is the minimum amount of money you'd be willing to sell $X$ for. You'd to sell $X$ at $\alpha$ such that $Z(\omega) + \alpha \geq X(\omega)$  since, if I do, there exists some gamble that I can make that guarantees that I'll make money (or at least won't lose money). (Notice that the gambler is assumed to be entirely risk averse in this definition. There is no notion of expected reward, and you'd only be willing to sell if you're guaranteed to not incur a loss.) 

Game-theoretic upper expectation of $X$ is defined as the same thing, written $\overline{\E}^g[X]$ (where the $g$ stands for game-theoretic). This is also equal to 
$$\inf_Z \sup_\omega X(\omega) - Z(\omega).$$
One can think of this as a two-player [[zero sum game]] between you and reality. Reality is trying to maximize, you're trying to minimize, and you move first. The result, $\overline{\E}^g[X]$ is how much you have to pay reality. 

Why is this called upper expectation? Under some conditions on $\cZ$ , $$\overline{\E}[X] = \sup_{\mu\in\Delta(\cZ)}\E^\mu[X].$$where $\Delta(\cZ)$ is the set of distributions $\mu$ on $\Omega$ such that $\E^\mu(Z)\leq 0$ for all $Z\in\cZ$, i.e., the set of gambles where you're not expected to make money. 

The lower expected value is 
$$\underline{\E}^g[X] = \sup\{\beta\in\Re: \exists Z\in\cZ \quad Z + X\geq \beta\}.$$
This is the highest price at which you are willing to buy $X$. If I buy at $\beta$, then I'm guaranteed to make money since I earn $X(\omega) + Z(\omega)$. This can be shown to be $-\overline{\E}^g[-X]$, or 
$$\un{|E}^g[X] = \sup_Z \inf_\omega X(\omega) + Z(\omega).$$

We can use the expectations to define [[game-theoretic probabilities]].


