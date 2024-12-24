---
created: 2024-01-18
lastmod: 2024-12-24
---

In [[hypothesis testing]], given a stream of paired observations $(X_t,Y_t)$, $t=1,2,\dots,n$, where $X_t \sim P_X$ and $Y_t\sim P_Y$, two-sample testing asks $H_0: P_X = P_Y$, $H_1: P_X\neq P_Y$. This can of course be asked in the [[sequential hypothesis testing|sequential setting]] or the batch setting. 

Approaches: 
- [[testing by betting—two-sample testing]] (sequential, nonparametric)
- Original [Kernel MMD test in the batch setting](https://jmlr.csail.mit.edu/papers/volume13/gretton12a/gretton12a.pdf) (nonparametric)
- Two-sample [[t-test]] or z-test (parametric)
- [General framework for two-sample testing](https://ieeexplore.ieee.org/abstract/document/8276312), but seems to be beat by testing by betting (sequential, nonparametric)
- One can build confidence sequences for the [[KS distance]] or the [[kernel MMD]] from [[confidence sequences via reverse submartingales]], and then use the [[duality between hypothesis tests and CIs]] to form hypothesis tests. This is more conservative than testing directly. 



