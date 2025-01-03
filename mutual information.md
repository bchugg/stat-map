---
lastmod: 2025-01-03
created: 2025-01-02
---

The [[KL divergence]] between the joint and the marginals. For joint distribution $P_{X\times Y}$ with marginals $P_X$ and $P_Y$, the mutual information is $I(X;Y) = \kl(P_{X,Y}\| P_X \otimes P_Y)$. 

The mutual information is a measure of dependence between $X$ and $Y$: If you know one, how much do you know about the other? (The MI is symmetric). $I(X;Y) = 0$ iff $X$ and $Y$ are independent. 