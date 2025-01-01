---
lastmod: 2024-12-31
created: 2024-12-31
---

Given scalar observations $Y_1,\dots,Y_n$, the conformal p-value of a new observation $Y$ is
$$
Q(Y) = \frac{1 + \sum_{i\leq n} \ind\{ Y_i \leq Y\}}{n+1}.
$$
If $(Y_1,\dots,Y_n,Y)$ is [[exchangeable distribution|exchangeable]], then $Q(Y)$ is equally distributed among $\frac{1}{n+1},\dots,\frac{n}{n+1}$. (This assumes that $Y_i \neq Y_j$ almost surely. If this doesn't hold then add random uniform noise to each observation.) 

Many procedures are based on this p-value, including [[conformal prediction]] and [[permutation test|permutation testing]]. It has also been used for [selection by prediction](https://arxiv.org/pdf/2210.01408), [testing for outliers](https://arxiv.org/abs/2104.08279), and [conditional testing](https://openreview.net/pdf?id=Ip6UwB35uT). An [[e-value]] and [[e-process]] were proposed which sequentialize the conformal p-value, see [[permutation testing by betting]]. 
