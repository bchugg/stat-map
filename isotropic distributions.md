---
created: 2024-08-29
lastmod: 2024-11-18
---

Intuitively, an isotropic distribution is rotationally invariant. That is, it is the same in all directions when viewed from the origin. For instance, a normal $N(\mu,\sigma^2I)$ is isotropic, because the variance is the same in all directions. 

Mathematically, we say a distribution $P$ is isotropic if for all orthogonal matrices $Q$, 
$$
X = QX,
$$
in distribution, where $X\sim P$. The opposite of isotropy is an [[anisotropic distribution]]. 

A characterization of isotropy comes from [Vershynin, Lemma 3.2.3](https://www.math.uci.edu/~rvershyn/papers/HDP-book/HDP-book.html#): $X\in\Re^d$ is isotropic iff $\E\la X,z\ra^2 = \|z\|_2^2$ for all fixed $z\in\Re^d$. 


