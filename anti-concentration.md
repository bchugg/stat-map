---
lastmod: 2024-11-10
created: 2024-11-09
---

Anti-concentration results are exactly what they sound like. If [[concentration inequalities]] study how random variables concentrate around particular values, anti-concentration inequalities are lower bounds on how much they concentrate around these values. Anti-concentration shows up when proving [[central limit theorems]]. 

Stated another way, concentration inequalities want to provide an upper bound on the quantity $\Pr(|X - \E X|>\eps)$, whereas anti-concentration wants to provide upper bounds on $L_\eps(X) = \sup_v \Pr(| X - v|\leq \eps)$, thus showing that the concentration around $X$ for any $v$ is limited. $L_\eps(X)$ is often called "Levy's concentration function". 

## Carbery-Wright 
Let $X$ be [[log-concave distribution|log-concave]] and $f$ a polynomial of degree $d$. In 2001, [Carbery and Wright proved](https://intlpress.com/site/pub/files/_fulltext/journals/mrl/2001/0008/0003/MRL-2001-0008-0003-a001.pdf) that 
$$
\sup_v \Pr(|f(X) - v|<\eps) \lesssim \left(\frac{\eps}{\sqrt{\E f(X)^2}}\right)^{1/d}.
$$
Note this covers the case of sums of normally distributed random variables, which is the typical application. See [here](https://math.mit.edu/~danmiku/slides/poly-ac.pdf) for a modern statement and explanation of Carbery-Wright. 

Glazer and Mikulincer [showed](https://arxiv.org/pdf/2108.04268) how to get dimension-free bounds on the variance of polynomials, which can then be used in combination with Carbery-Wright to upper bound the right hand side above in terms of $\eps$ and $d$ only.    

## Esseen's inequality 
Suppose $X$ has [[characteristic function]] $\varphi$, then 
$$
L_\eps(X) \leq \eps \int_{-2\pi/\eps}^{2\pi/\eps} |\varphi(\lambda)|\d \lambda.
$$
So if $|\varphi(\lambda)|\leq |\lambda|^{-\alpha}$, then $L_\eps(X) \leq \eps^\alpha$. 

## Levy-style anti-concentration  
If $X_1,\dots,X_n$ are independent and symmetric random variables in a [[Banach space]] and $S_n = \sum_i X_i$, then for all $u>0$ 
$$
\Pr(\|S_n\| >u) \geq \frac{1}{2}\Pr(\| \sum_i X_i \ind\{\|X_i\| \leq b\}>u).
$$
and
$$
\Pr(\|S_n \|>u)\geq \frac{1}{2} \Pr(\max_i\|X_i\|>u).
$$
