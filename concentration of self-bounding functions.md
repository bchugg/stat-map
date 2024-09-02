---
created: 2024-08-29
lastmod: 2024-09-02
---

Let $f:\calX^n\to\Re$ and $f_i :\calX^n\to\Re$ for $i=1,\dots,n$. We say $f$ is self-bounding (wrt to $(f_i)$) if 
$$

0\leq f(x) - f_i(x^{(i)})\leq 1,

$$
and
$$
\sum_{i=1}^n (f(x) - f_i(x^{(i)})) \leq f(x),
$$
where $x^{(i)}$ drops the $i$-th coordinate of $x$. Often we take
$$

f_i(x^{(i)}) = \inf_{x_i'} f(x^{(i)}, x_i').

$$
This definition has been weakened by others. See second ref below for details. 

# Results 

Let $X_1, \dots, X_n$ be independent, and set $X = (X_1,\dots,X_n).$ 

If $f$ is self-bounding then it is roughly a Poisson random variable, in the sense that 
$$

\log  \E[e^{\lambda(Z - \E Z)}] \leq (e^\lambda - \lambda - 1)\E Z,

$$
where $Z = f(X^n)$. Consequently, applying the [[Chernoff method]], one obtains that 
$$

\Pr(Z\geq \E Z + t)\leq \exp\left(\frac{-t^2}{2(\E Z + t/3)}\right).

$$
Also note that the first self-bounding property condition implies that $(f(X) - f_i(X^{(i)}))^2 \leq f(X) - f_i(X^{(i)})$. Therefore, the [[Efron-Stein inequality]] implies that 
$$

\Var(Z) \leq \sum_i \E[(f(X) - f_i(X^{(i)})^2] \leq \sum_i \E[f(X) - f_i(X^{(i)})] \leq \E[f(X)] = \E Z,

$$
where the final inequality follows from the second self-bounding property condition. 

This simply fact, that the variance is bounded by the expected value, has many applications. See Section 3.1 in first ref below. 

# References 
- Concentration inequalities by Boucheron, Lugosi, Massart, Chapter 3.1 and 3.3. 
- [Concentration of self-bounding functions](https://econ.upf.edu/~lugosi/boluma4.pdf) by Boucheron, Lugosi, Massart
 