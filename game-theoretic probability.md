---
created: 2024-08-29
lastmod: 2024-10-28
---

Game-theoretic probability (GTP) is a foundation for probability theory, distinct from the measure-theoretic foundations laid out by Kolmogorov in the 1920s. Whereas Kolmogorov conceptualized probability as a subset of measure theory, game-theoretic probability lays its foundations in game-theory.  

GTP makes statements by means of iterated games between various players, often consisting of reality, skeptic, and possibly several other players. The moves made by reality are the "observations," and skeptic is betting on the result of the moves. A GTP statement often has the following form: Either (i) the observations obey some property, or (ii) the skeptic can make infinite money. 

For concrete examples, see 
- [[game-theoretic LLN]] 
- [[game-theoretic hypothesis testing]]
- [[game-theoretic convergence of opinions]]

You can recover many other results of classical/modern probability theory using the game-theoretic framework. Examples not included in these notes include stochastic calculus, zero-one laws, pricing formulas in finance, and others. See the [probability and finance project](http://www.probabilityandfinance.com/articles/index.html) for more examples. 

Some key differences between GTP and measure-theoretic probability (MTP): 
- The definition of a probability measure comes first in MTP, and then expectations are defined as integrals with respects to measures. In GTP, the definition of expectations comes first, and then probabilities are defined afterwards. 
- GTP statements are usually made with no reference to distributions, randomness, measures, etc. They are therefore typically much easier to understand than MTP statements. The lack of randomness was a motivating factor of GTP. Instead of positing randomness from the start, GTP would rather view randomness as an emergent property of interactions between players. 
- GTP is inherently sequential. 

[[game-theoretic statistics|Game-theoretic statistics]] is the application of game-theoretic probability to statistical procedures, such as [[hypothesis testing]].  

Since game-theoretic probability introduces a fundamentally different foundation for probability theory, it has a new set of definitions, concepts etc. These include gamble spaces, prices, game-theoretic expectations, and game-theoretic concentration inequalities. Many of these foundations are still under development and the connections to measure-theoretic probability are still being investigated. 

## History 

Game-theoretic probability arguably dates back to Jean Ville, who studied betting using martingales. Glenn Shafer writes: 
> The project of using betting games as the starting point for mathematical probability dates back to Jean Ville, who used it in 1939 to generalize and criticize Richard von Mises’s earlier project of axiomatizing probability as a theory about frequencies. Ville’s idea was further developed by Per Martin Löf, Claus-Peter Schnorr, Phil Dawid, and others, including Vladimir Vovk and myself. But it is only now being deployed in mathematical statistics.
> - [How the game-theoretic foundation for probability resolves the Bayesian vs. frequentist standoff](https://www.probabilityandfinance.com/articles/56.pdf), 2020. 

There are now many papers (see eg [The Probability and Finance Project](https://www.probabilityandfinance.com/)) and two books, both by Shafer and Vovk. Many authors have started using game-theoretic ideas in their research, but still state the results in terms of measure-theoretic probability. See eg the [survey on game-theoretic statistics](https://arxiv.org/pdf/2210.01948) by Ramdas, Grunwald, Vovk, and Shafer. 