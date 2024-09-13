---
created: 2024-08-29
lastmod: 2024-09-02
---
In [[hypothesis testing]], for a given $\alpha$, a uniformly most powerful (UMP) test is a test whose type-I error is bounded by $\alpha$ and, among all other tests with type-I error bounded by $\alpha$, has the most power. 

More formally, suppose we are testing $H_0$ vs $H_1$. Consider the family of all tests $\psi$ such that $\sup_{P\in H_0}P(\psi(X) = 1)\leq \alpha$. We say a test $\phi$ is UMP if for all other tests $\psi$, we have 
$$
P (\phi(X) = 1) \geq P(\psi(X)=1)\quad\text{for all}\quad P\in H_1.
$$
The [[Neyman-Pearson lemma]] states that the [[likelihood-ratio test]] is UMP for testing simple hypothesis (i.e. simple null vs simple alternative). The [[Karlin-Rubin theorem]] extends this to composite vs composite but under a [[monotone likelihood ratio]] assumption. 

UMP tests don't always exist. 