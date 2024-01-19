
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

Gamble space ($\Omega, )

$$\overline{\E}[X] = \inf\{\alpha\in\Re: \exists Z \in Z \text{s.t.} \alpha + Z\geq X\}$$
$ = \inf_z \sup_\omega X(\omega) - Z(\omega)$. 






