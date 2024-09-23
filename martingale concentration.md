---
created: 2024-08-29
lastmod: 2024-09-02
---

Let $(S_t)$ be a martingale wrt to the filtration $(\calF_t)$. Assume $(S_t)$ is scalar-valued unless otherwise indicated. Here we investigate [[concentration inequalities]] for $(S_t)$. 

Note that martingale concentration inequalities generalize concentration inequalities for independent random variables (eg [[light-tailed scalar concentration]]), since we may take $S_t = \sum_{i\leq t} (X_i - \mu)$, in which the following bounds translate into bounds on $\sum_{i\leq t}X_i$. 

While we state concrete, mostly [[fixed-time]] results here, we note that many of the following bounds were made [[time-uniform]] (and often tightened) using [[sub-psi process|sub-psi processes]].  


## Azuma-Hoeffding inequality 

Assume that $|X_t - X_{t-1}|\leq c_t$ for all $t$, i.e., the martingale has bounded increments. Then, for all $n$, 
$$

\Pr(|X_n - X_0| \geq \eps) \leq 2\exp\left(\frac{-\eps^2}{2\sum_{t=1}^n c_t^2}\right).

$$
The natural one-sided versions of this inequality also exist. Note that $n$ is fixed in advance here (i.e., it is [[fixed-time]] result). 

## Variance bound 

If the martingale has bounded increments and the _variance_ of the increments are also bounded, i.e., 
$$

\E [|X_t - X_{t-1}|^2|\calF_{t-1}]\leq v_t^2,

$$
then we can modify Azuma's bound to read 
$$

\Pr(|X_n - X_0|\geq \eps) \leq 2 \exp\left(\frac{-\eps^2}{4V}\right),

$$
where $V = \sum_i v_i^2$, as long as $\eps \leq 2V/\max_i c_i$.  Why is this better than Azuma's inequality? Since the increments are bounded by $c_t$, a trivial bound on $\E[|X_t - X_{t-1}|^2|\calF_{t-1}]$ is $c_t^2$. Thus we may assume that $v_t^2\leq c_t^2$, which means the right hand side of the bound is tighter. 

This was first proved by DA Grable in [A Large Deviation Inequality for Functions of Independent, Multi-way Choices](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=3b7858b4475d8027cf49c8afbaac34b4229731fb). A modern proof is given by Dubhasi and Panconesi in their textbook, [Concentration of Measure for the Analysis of Randomized Algorithms](http://wwwusers.di.uniroma1.it/~ale/Corsi/AlgoPro/monograph.pdf), Chapter 8. 

## Variance bound —  matrix version. 

Suppose $(Z_t)$ is a matrix-valued martingale ([[Hermitian matrix|Hermitian Matrices]]). Let $D_i = Z_i - Z_{i-1}$ and suppose 
$$

\norm{D_i}\leq c_i, \quad \norm{\E[D_i^2|\calF_{i-1}]}\leq \sigma_i^2.

$$
Then, for $V = \sum_{i\leq n} \sigma_i^2$, 
$$

\Pr(\norm{Z_n}> \eps)\leq 2d\exp\left(\frac{-\eps^2}{4V}\right),

$$
where each $Z_t$ is a $(d\times d)$-matrix. This was first proved by David Gross: [Recovering Low-Rank Matrices From Few Coefficients In Any Basis](https://www.math.ucdavis.edu/~strohmer/courses/270/lowrank_Gross.pdf). 


# References
- [Concentration of Measure for the Analysis of Randomized Algorithms](http://wwwusers.di.uniroma1.it/~ale/Corsi/AlgoPro/monograph.pdf) by Dubhashi and Panconesi. 
- [Recovering Low-Rank Matrices From Few Coefficients In Any Basis](https://www.math.ucdavis.edu/~strohmer/courses/270/lowrank_Gross.pdf), David Gross 

