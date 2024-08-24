
Consider a two-player, zero sum game. Player 1 (row player, say) plays a stategy $x$, and player 2 (column) players strategy $y$. A nash equilibrium is a pair of strategies $(x^*,y^*)$ such that, when player 2 plays $y^*$, player 1 has no incentive to deviate from $x^*$, and vice versa. Thus, conditional on the other player not changing strategies, each player will not change strategies. 

Suppose player 1 is trying to minimize the value of a loss $\ell$, and player 2 is trying to maximize the loss. Player 1 attempts to find the strategy: $$\argmin_x \max_y \ell(x,y),$$
since this is the best "worst case" scenario (worst case since it assumes that column can make the first move). This is the "minimax" strategy. Similarly, player 2 attempts to find the "maximin" strategy 
$$
\argmax_y \min_x \ell(x,y).
$$
In general, the value of these strategies is not equal, since 
$$
\min_x \max_y \ell(x,y) \geq \max_y \min_x \ell(x,y).
$$
Note that $x$ and $y$ here can be mixed (randomized) strategies, in which case we interpret $\ell(x,y)$ as the expected loss. 