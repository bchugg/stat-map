
Prices, probabilities, and contracts 
$X$ is some contract, you have a personal buying and selling price. eg $X$ = "the bearer of this doc receives tomorrow's temp at 7am in dollars". 

Game between Ada, Charles, Mary 

They find a coin. Charles thinks it's fair. Ada thinks biased towards heads. Game: 
For $t=1,\dots,$ 
- Ada bets $\beta_t \in\Re$ 
- Ada receives $\beta_t y_t$ where $y_t =1$ if heads, $y_t=-1$ if tails.  

Suppose Ada bets a constant fraction of her wealth, $\alpha$. So $W_t = W_{t-1}(1+\alpha y_t)$. Total wealth is $W_t = \prod_{i\leq t} (1 + \alpha y_t)$. 

Mary enters game. "I'll pay you $3 now, if HHH comes in first three rounds, you pay me $16". This might completely change Ada's strategy. She can win a risk-free 1 dollar, by accepting, putting 1 dollar aside and then betting double or nothing. Same strategy if Mary gave her x>2 dollars at the beginning. So the "right price" for this contract is $2. 

It's risk free for Ada to accept the contract (she'll end with zero regardless, which is what she started with).

This leads to: The "right price" of $X is the smallest amount of money needed to replicate that contract with gambles. 

Gamble space ($\Omega, \cZ$) 

$$\overline{\E}[X] = \inf\{\alpha\in\Re: \exists Z \in Z \text{s.t.} \alpha + Z\geq X\}$$
= \inf_z \sup_\omega X(\omega) - Z(\omega)$. 





— - 

Gamble space $(\Omega, \cZ)$. Outcomes $\omega\in\Omega$. Gambles are functions $Z:\Omega\to\overline{\Re}$ (think of this as payoff as a result of gambling a certain way). 

Variables $X:\Omega\to\Re$ are the results of certain contracts. Think of $X$ as a contract. 

Replication cost of $X$ relative to $\cZ$ (set of gambles available to me) is defined as 
$$\inf\{\alpha\in\Re: \exists Z\in\cZ\quad Z+\alpha \geq X\}.$$
That is, $\forall\omega, Z(\omega) + \alpha \geq X(\omega)$. Intuition: minimum amount of money you'd be willing to sell $X$ for. 

I''d be willing to sell $X$ at $\alpha$ since, if I do, there exists some gamble that I can make that guarantees that I'll make money (or at least won't lose money). 

Game-theoretic upper expectation of $X$ is defined as the same thing, written $\overline{\E}^g[X]$ (where the $g$ stands for game-theoretic). This is also equal to 
$$\inf_Z \inf_\omega X(\omega) - Z(\omega).$$
Think of 2player zero sum game between you and reality. Reality is trying to maximize, you're trying to minimize. This is how much you have to pay reality. 

We will see the following fact: Under some conditions on $\cZ$ , $$\overline{\E}[X] = \sup_{\mu\in\Delta(\cZ)}\E^\mu[X].$$
where $\Delta(\cZ)$ is the set of distributions $\mu$ on $\Omega$   such that $\E^\mu(Z)\leq 0$ for all $Z\in\cZ$, i.e., the set of gambles where you're not expected to make money. 

The lower expected value is 
$$\underline{\E}[X] = \sup\{\beta\in\Re: \exists Z\in\cZ \quad Z + X\geq \beta\}.$$
THis is the highest price at which you are willing to buy $X$. If I buy at $\beta$, then I'm guaranteed to make money since I earn $X(\omega) + Z(\omega)$. This can be shown to be $-\overline{\E}[-X]$.  

Introduce three settings for the games: 

1. Nature is passive, probabilistic, and consistent with $\cZ$
2. Nature is probabilistic and cannot respond to gambler 
3. Nature is adversarial and responds to the gambler 

$$\sup_{\mu\in\Delta_0(\cZ)}\E^\mu X \leq \sup_{\mu\in\Delta(\Omega)} \inf_{Z} \E^\mu[X-Z]\leq \inf_Z \sup_\omega X(\omega) - Z(\omega).$$

$\Delta_0(\cZ)$ are distributions when the expected value of $Z$ is negative. First inequality follows from noticing that 
$$\sup_{\mu\in\Delta_0(\cZ)} \E^\mu[X]\leq \sup_{\mu\in\Delta_0(\cZ)} \E^\mu[X-Z].$$

The RHS is equal to $\inf_Z \sup_{\mu\in\Delta(\Omega)} X(\omega) - Z(\omega)$ because in a game, it's never strictly advantageous to play a probability distribution when you're responding to the opponent. From here the second inequality is clear since max min $\leq $ min max

 LHS is measure-theoretic upper expectation, RHS is game theoretic upper expectation. 

For lower expectations, we get the opposite chain of inequalities. 

We get: 
$$\underline{E}^g[X]\leq \underline{E}^{mg}[X]\leq \underline{E}^m[X]\leq \overline{E}^m[X]\leq \overline{E}^{gm}[X]\leq \overline{\E}^g[X].$$


We define probabilities using expectations: $\overline{P}(A) = \overline{E}^g[\ind_A]$ and $\underline{P}(A) = \underline{\E}^g[\ind_A]$. If they are equal we just write $P(A)$. 

Examples. 

$\Omega = \{-1,1\}$. $\cZ=\{Z_\beta : \omega \mapsto \beta\omega: \beta\in\Re\}$.  

$$\overline{P}[1] = \overline{\E}^g[\ind_1] = \inf_{\beta\in\Re}\sup_{-1,1} \ind(\omega=1) - \beta\omega = \inf_\beta \max(\beta, 1-\beta) = 1/2$$

Note that $X$ here is $\ind_1$, i.e., a payoff of 1 if it comes up 1. 
THis value is intuitive, because the gambles are somehow setup such that the payoffs are symmetric, so in some sense we think we're dealing with a fair coin. 


Can show that for general $X$, $\E^g[X] = (X(1) + X(2))/2$. 



