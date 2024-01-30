
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

[[game-theoretic statistics]] is the application of game-theoretic probability to statistical procedures, such as hypothesis testing. 

# Gamble spaces, prices, and probabilities 

Like measure-theoretic probability, GTP introduces various notation and concepts to formalize the discussion. 

Let $\Omega$ be the _outcome_ space, i.e., the set of things that can happen. Elements $\omega\in\Omega$ are called _outcomes_ and subsets $A\subset \Omega$ are called _events_.   

A variable is a mapping $X:\Omega\to\overline{\Re}$,  where $\overline{\Re}$ is the extended reals. A useful way to think about variables is as contracts. Eg, $X$ might be the contract "if this coin lands heads then the bearer obtains $1". Here $\Omega=\{H,T\}$ and $X(H)=1$, $X(T)=0$. Then we can start asking questions such as: "How much are you willing to pay $X$ for?" 

A gamble is also a mapping $Z:\Omega\to\overline{R}$, but it's useful to differentiate gambles from variables. 
Think of the outcome $Z(\omega)$ is how much money is obtained when the outcome is $\omega$ when using gambling strategy $Z$. 

The set of all gambles under consideration is $\cZ$ and together $(\Omega,\cZ)$ form the _Gamble space_.  
Using the concept of a gamble space, we can define [[game-theoretic expectations]] which in turns defines [[game-theoretic probabilities]]. 