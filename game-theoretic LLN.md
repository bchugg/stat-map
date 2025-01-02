---
created: 2024-08-29
lastmod: 2025-01-01
---

A [[laws of large numbers|law of large numbers]] stated in terms of [[game-theoretic probability]]. Consider the following setup: 

- Bob has some initial capital, $C_0 = 1$. 
- For $t=1,2,\dots$
	- Bob makes a bet $M_t\in\Re$
	- The world reveals a value $x_t\in [0,1]$. 
- Bob updates his capital as $C_t = C_{t-1} + M_t(1/2 - x_t)$. 

The game stops if Bob goes broke (i.e.,$C_t<0$). The game-theoretic LLN states that Bob has a strategy which ensures that either
$$
\lim_{t\to\infty}\frac{1}{t}\sum_{i\leq t} x_i = 1/2, \tag{1}
$$
or he becomes infinitely wealthy, $\liminf_{t\to\infty}C_t = \infty$. There's nothing special about the constant 1/2 here. It could be replaced with any value between 0 and 1 and we'd simply change how Bob updates his capital. 

A [[Bayesian statistics|Bayesian interpretation]] would be that Bob has a belief that the average value of the observations $x_t$ is 1/2 and is betting accordingly. Or you don't have to get Bayesian at all, and you can instead say that Bob is able force the world to act in a certain way if the world wants to prohibit him from getting infinitely wealthy.

Notice that there no probabilistic assumptions in the statement of the game-theoretic LLN. There are no distributions, no probability measures, no sigma algebras, nothing. It makes a deterministic statement about _every_ sequence of numbers $(x_t)$, namely that there exists a betting strategy such that either (1) will happen, or Bob will become infinitely wealthy. 

Remarkably, the game-theoretic LLN recovers the measure-theoretic SLLN (under the assumption of boundedness, which were assuming here). I have a blog post about this [here](https://benchugg.com/research_notes/game_theoretic_lln/). 

