---
created: 2024-08-29
lastmod: 2024-10-24
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
- GTP statements are usually made with no reference to distributions, randomness, measures, etc. They are therefore typically much easier to understand than MTP statements. 
- GTP is inherently sequential. 

[[game-theoretic statistics]] is the application of game-theoretic probability to statistical procedures, such as [[hypothesis testing]].  

Since game-theoretic probability introduces a fundamentally different foundation for probability theory, it has a new set of definitions, concepts etc. These include gamble spaces, prices, game-theoretic expectations, and game-theoretic concentration inequalities. Many of these foundations are still under development and the connections to measure-theoretic probability are still being investigated. 


