---
created: 2024-09-07
lastmod: 2024-09-07
---
The general approach is as follows. Let $C_\eps$ be an $\epsilon$-cover of $\ball^{d-1}$ (see [[covering and packing]]). Then 
$$
\sup_{v\in \dball} \la v, S_n\ra \leq \sup_{v\in C_\eps}\la v,S_n\ra + \sup_{v\in \eps \dball} \la v,S_n\ra = \sup_{v\in C_\eps}\la v,S_n\ra + \eps \sup_{v\in \dball} \la v,S_n\ra,
$$
so
$$
\sup_{v\in \dball}\la v,S_n\ra \leq \frac{1}{1-\eps} \sup_{v\in C_\eps}\la v,S_n\ra.
$$
From here, $C_\eps$ is a finite set, so we can apply well-known [[maximal inequalities]] over finite sets. For instance, if $S_n=X$ is sub-Gaussian, then [[light-tailed maximal inequalities]] give 
$$
\E\sup_{v\in C_\eps} \la v,X\ra \leq \sqrt{2\Var(X) \log|C_\eps|} \leq \sqrt{2 \Var(X) d\log(3/\eps)},
$$
where we use an upper bound on the $\eps$-covering number of $\dball$. This gives 
$$
\E \norm{S_n}\leq \frac{1}{1-\eps} \sqrt{2\Var(X) \log|C_\eps|}.
$$
We can then optimize over $\eps$ to get a final bound. The sub-Gaussian case usually takes $\eps = 1/2$ (e.g., Theorem 1.19 in [high-dimensional statistics](https://arxiv.org/abs/2310.19244) by Rigollet and Hutter). We can also get a high-probability bound by noticing that 
$$
\Pr(\sup_{v\in \dball}\la v,S_n\ra\geq t) \leq \Pr\left(\frac{1}{1-\eps}\sup_{v\in C_\eps}\la v,S_n\ra\geq t\right),
$$
which can be bounded with a union bound and a tail bound and then maybe a Chernoff bound ([[Chernoff method]]) based on the properties of $S_n$.
