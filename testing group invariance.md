---
created: 2024-08-29
lastmod: 2024-10-13
---

A particular setup in [[hypothesis testing]] which generalizes [[testing exchangeability|testing for exchangeability]], testing for sphericity (which can be used to test the Gaussian-error assumption in [[linear regression]]), [[permutation test|permutation testing]], and sign-flipping tests. 

We have some compact topological group $\calG$, which is a set of invertible transformations $G:\calX\to\calX$ which is closed under composition. We observe some data $X\in \calX$ drawn from distribution. 

We say $X$ is $\calG$-invariant if $X \equald GX$  for all $G\in\calG$. The null and alternative are: 
$$
H_0: X\text{ is group invariant}, \quad H_1: X\text{ is not group invariant}.
$$
In particular applications of interest, the group $\calG$ is usually huge (eg permutation tests), and it's infeasible to test each element $G\in\calG$. Typically a random subset of $\calG$ is chosen. 

- Lardy and Perez-Ortiz study [sequential tests of group invariance](https://arxiv.org/pdf/2401.15461).
- [Koning and Hemerik use a deterministic subgroup](https://arxiv.org/pdf/2202.00967) of $\calG$ instead of a random sample. 