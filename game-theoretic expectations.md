
In [[game-theoretic probability]], the amount you'd be willing to sell a contract (variable) for is the _replication cost_. Let $(\Omega, \calZ)$ be a gamble space. Formally, we define the replication cost as  
$$

\inf\{\alpha\in\Re: \exists Z\in\calZ\text{~ s.t ~} Z+\alpha \geq X\}.

$$
That is, $\forall\omega, Z(\omega) + \alpha \geq X(\omega)$. The intuition is that the replication cost is the minimum amount of money you'd be willing to sell $X$ for. You'd sell $X$ at $\alpha$ such that $Z(\omega) + \alpha \geq X(\omega)$  since, if I do, there exists some gamble that I can make that guarantees that I'll make money (or at least won't lose money). (Notice that the gambler is assumed to be entirely risk averse in this definition. There is no notion of expected reward, and you'd only be willing to sell if you're guaranteed to not incur a loss.) 

Game-theoretic upper expectation of $X$ is defined as the same thing, written $\overline{\E}^g[X]$ (where the $g$ stands for game-theoretic). This is also equal to 
$$

\inf_Z \sup_\omega X(\omega) - Z(\omega).

$$
One can think of this as a two-player [[zero sum game]] between you and reality. Reality is trying to maximize, you're trying to minimize, and you move first. The result, $\overline{\E}^g[X]$ is how much you have to pay reality. 

Why is this called upper expectation? Under some conditions on $\calZ$ ,
$$

\overline{\E}[X] = \sup_{\mu\in\Delta(\calZ)}\E^\mu[X].

$$
where $\Delta(\calZ)$ is the set of distributions $\mu$ on $\Omega$ such that $\E^\mu(Z)\leq 0$ for all $Z\in\calZ$, i.e., the set of gambles where you're not expected to make money.

The lower expected value is 
$$

\underline{\E}^g[X] = \sup\{\beta\in\Re: \exists Z\in\calZ \quad Z + X\geq \beta\}.

$$
This is the highest price at which you are willing to buy $X$. If I buy at $\beta$, then I'm guaranteed to make money since I earn $X(\omega) + Z(\omega)$. This can be shown to be $-\overline{\E}^g[-X]$, or 
$$

\un{\E}^g[X] = \sup_Z \inf_\omega X(\omega) + Z(\omega).

$$
We can use the expectations to define [[game-theoretic probabilities]].

# Properties 

Game-theoretic expectations obey many of the properties you want/would expect. In particular, 
- $\ov{\E}[X + c] = \ov{\E}[X] + c$ for any constant $c$, 
- $X\leq Y$ implies that $\ov{\E}[X] \leq \ov{\E}[Y]$
- If $(\Omega,\calZ)$ is arbitrage-free (see [[game-theoretic probability#Gamble spaces, prices, and probabilities|game-theoretic probability:Gamble spaces, prices, and probabilities]]]) then $\ov{\E}[0]\leq 0$. 
- If it is AF and contains the zero bet (i.e., $0(\omega)=0$ for all $\omega$) then $\ov{\E}[0]=0$. 
- If it is positive-linear, then $\ov{\E}[X+Y] \leq \ov{\E}[X] + \ov{\E}[Y]$, $\ov{\E}[cX] = c\ov{\E}[X]$ for all $c\geq 0$ and $\un{\E}[X]\leq \ov{\E}[X]$.  

We've omitted the superscript $g$ above for brevity. These properties [[game-theoretic concentration inequalities]]. 







