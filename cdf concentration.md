---
lastmod: 2025-01-06
created: 2024-09-24
---

What can we say about the concentration of the empirical CDF about the true CDF? 

## Scalar DKW inequality 
For real valued observations $X_1, \dots, X_n$ with $F_n (x) = \frac{1}{n}\sum_{i\leq n}\ind(X_i\leq x)$, the DKW (Dvoretzky-Kiefer-Wolfowitz) inequality states that 
$$
\Pr\left(\sup_{x\in\Re} |F_n(x) - F(x) > t\right) \leq 2\exp(-2nt^2).
$$
Note this statement is uniform in $x$ which, depending on your expectations, is kind of remarkable. The intuition is that if $F(x)$ sharply increases (it can't decrease, of course) at some $x$, then these are precisely the places where we expect to see many observations, so $F_n(x)$ won't be too far from $F(x)$. 

The original DKW inequality was an asymptotic statement: it bounded the probability as $\lesssim \exp(-2nt^2)$. In 1990, [Paul Massart proved that](https://www.jstor.org/stable/2244426) the constant on the right hand side was 2, and he proved that this was tight.  

## Multivariate DKW inequality 
In 2021, [Naaman gave](https://www.sciencedirect.com/science/article/pii/S016771522100050X) a multivariate extension of DKW. Namely, 
$$
\Pr\left(\sup_{x\in\Re^d} |F_n(x) - F(x) > t\right) \leq d(n+1)\exp(-2nt^2).
$$
For sufficiently large $n$, $n+1$ can be replaced by $2$ in which case the constant in front of the exponential is $2d$, which is optimal. Here the empirical CDF is as above, but $\ind(X_i\leq x$) is interpreted component-wise: to be true each component of $X_i$ must be at most $x_i$. 

In 1977, [Devroye gave a similar result](https://core.ac.uk/download/pdf/81205834.pdf) but with $2e^2(2n)^d$ replacing $d(n+1)$. 

Both the univariate and multivariate DKW inequalities hold under slightly weaker assumptions than the usual iid assumption.  

## Glivenko-Cantelli theorem 
Glivenko and Cantelli proved that, in the scalar case,  
$$
\sup_{x\in \Re} |F_n(x) - F(x) | = \norm{F_n - F}_\infty \xrightarrow{a.s.} 0.
$$
The DKW inequality implies almost sure convergence (via the Borel-Cantelli) lemma, so the Glivenko-Cantelli theorem is strictly weaker than the DKW inequality, which provides explicit rates of convergence. But the Glivenko-Cantelli theorem is part of a broader conversation about [[Glivenko-Cantelli class|Glivenko-Cantelli classes]] in [[empirical process theory]]. 

