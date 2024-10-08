---
created: 2024-08-29
lastmod: 2024-10-07
---

Let $X_1,\dots,X_n$ be independent random variables and let $f:\calX^n\to\Re$ obey $\E[f^2(X)]<\infty$ where $X = (X_1,\dots,X_n)$. The Efron-Stein inequality states that
$$
\Var(f(X)) \leq \sum_{i=1}^n \E[(f(X) - \E[f(X)|X^{(i)}])^2]=:v,
$$
The Efron-Stein inequality is a fundamental result for bounding the variance of functions of random variables. It implies various other results such as [[bounded difference inequalities]] (though sometimes not the strongest versions). 

We can write $v$ in several different ways. First we can write it as a function of $f$ acting on iid copies: 
$$
v = \frac{1}{2} \sum_{i=1}^n \E[(f(X) - f(\bs{X}_i'))^2],
$$
where $\bs{X}_i'=(X_1,\dots,X_{i-1}, X_i', X_{i+1}, \dots, X_n)$ and $X_i'$ is an iid copy of $X_i$.  Next we can write it as 
$$
v= \inf_{Z_1,\dots,Z_n}\sum_{i=1}\E[(f(X) - Z_i)^2],
$$
where $Z_i$ is $(X_1,\dots,X_{i-1}, X_{i+1}, \dots, X_n)$-measurable (i.e., the only randomness comes from $X_i$). 

Efron-Stein inequalities also exist for random matrices, see [here](https://www.tropp.caltech.edu/papers/PMT16-Efron-Stein-Inequalities.pdf). 

# References 
- [An Efron-Stein inequality for nonsymmetric statistics](http://www-stat.wharton.upenn.edu/~steele/Publications/PDF/AEifns.pdf) by Steele. 
- Concentration Inequalities by Boucheron, Lugosi, Massart, Chapter 3.1 
