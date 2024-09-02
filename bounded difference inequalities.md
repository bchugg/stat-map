---
created: 2024-08-29
lastmod: 2024-09-02
---

These are [[concentration inequalities]] that concern functions of random variables that obey a bounded differences condition. Intuitively this means that if you change one argument, the function value doesn't change too much. 

The most famous example of a bounded difference inequality is McDiarmid's inequality, which is the following. Suppose $f:\Re^n \to \Re$ obeys 
$$

\sup_{z_1,\dots,z_n,z_i'} |f(z_{-i}, z_i) - f(z_{-i},z_i')|\leq c_i,

$$
for all $i$. (Here $z_{-i}$ is the vector of arguments that omits $z_i$). Then 
$$
\Pr(|f(X^n) - \E[f(X^n)]|\geq \eps)\leq 2\exp\left(-\frac{2\eps^2}{\sum_{i=1}^n c_i^2}\right).
$$
Note this is a generalization of the [[light-tailed scalar concentration#Hoeffding bound|light-tailed scalar concentration:Hoeffding bound]]. It is recovered by taking $f(x^n) = \frac{1}{n}\sum_{i=1}^n x_i$. 

In fact, $f$ need not be a function with domain $\Re^n$. We can replace $\Re^n$ with $\calX^n$ for any space $\calX$. (See [Raginsky's lecture notes](https://maxim.ece.illinois.edu/teaching/fall13/notes/concentration.pdf) for the proof). This is useful if, for instance, we are interested in obtaining bounds on the norm of random vectors. If we take $\calX= \Re^n$ for instance, then $f$ could be $f = \norm{\sum_i X_i}$ and we can obtain deviation inequalities between $\norm{\sum_i X_i}$ and $\E \norm{\sum_i X_i}$.  