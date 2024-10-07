---
lastmod: 2024-10-07
created: 2024-10-07
---

An ideal metric $\rho$ of order $s$ is a [[distributional distance]] that is both regular and homogeneous of order $s$. That is, it satisfies $\rho(X + Z, Y + Z)\leq \rho(X,Y)$ for any $Z$ independent of $X$ and $Y$ and 
$$
\rho(cX,cY) = |c|^s \rho(X,Y)\quad \text{for all }c\in\Re.
$$
(See more in [[distributional distance#Some definitions|distributional distance - definitions]]). The [[KS distance]] is ideal of order 0, and the [[Wasserstein distance]] is ideal of order 1. 

To see how they can be useful for proving [[central limit theorems]], see [[quantitative CLT template with ideal metrics]]. 

Do ideal metrics of an arbitrary order $s\geq 0$ always exist? This question was answered affirmatively by VM Zolotarev in 1975. It is nicely described by Senatov in his book [Normal approximation: New Results, Methods, and Problems](https://books.google.com/books/about/Normal_Approximation.html?id=xmKi21fpX0sC). 

For any $s$, write $s = m + \alpha$ where $m\in\mathbb{Z}$ and $\alpha\in[0,1]$. Consider the set of functions $\calF_s$ which have Holder exponent $\alpha$, i.e.., 
$$
|f^{(m)}(x) - f^{(m)}(y)| \leq \norm{x - y}^\alpha.
$$
If we define the distance 
$$
\rho_s(P,Q) = \sup_{f\in\calF_s}\left\{\left|\int f(x)(P - Q)(dx)\right|\right\},
$$
then this is an ideal metric of order $s$. 

