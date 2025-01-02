---
lastmod: 2025-01-01
created: 2025-01-01
---

A _scoring rule_ is a function used to evaluate forecasts. Let $\calX$ be an outcome space of interest, and $\Delta(\calX)$ the set of distributions over $\calX$. The goal of a forecaster is to produce some $P\in \Delta(\calX)$ which is "good", in some sense. 

To measure whether $P$ is good, we introduce a scoring rule $S: \Delta(\calX) \times \calX \to \Re$, which takes in the forecaster's distribution $P$ and an outcome $x\in\calX$ and says how good $P$ was. Usually $S$ is taken to be "positively oriented," meaning larger values of $S$ imply better forecasts. 

Given $S$, the _expected score_ between $P,Q\in\Delta(\calX)$ is 
$$
S(P\|Q) := \E_{x\sim Q} S(P,x).
$$
A scoring rule $S$ is  _proper_ if for all $Q\in\Delta(\calX)$, 
$$
Q \in \argmax_{P\in\Delta(\calX)} S(P\|Q).
$$
In words: Suppose you as the forecaster knew that the "true" distribution was $Q$. If $S$ is a proper scoring rule, it means that you can play $Q$ to maximize your score. This is so intuitive it's almost painful. 

Examples of proper scoring rules for binary forecasts are (note that $P=p\in [0,1]$ in this case): 
- Brier score: $S(p,x) = 1 - (p - x)^2$ 
- Spherical score: $S(p,x) = \frac{py + (1-p)(1-x)}{\sqrt{p^2 + (1-p)^2}}$
- Logarithmic score: $S(p,x) = x\log(p) + (1-x) \log(1-p)$
- 0-1 score: $S(p,x) = x\ind\{p\geq 0.5\} + (1-x)ind\{p\leq 0.5\}$. 