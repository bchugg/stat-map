---
lastmod: 2025-09-30
created: 2025-08-25
---

[[concentration inequalities|Concentration inequalities]] on Markov chains. The most general result comes from Fan, Jiang, Sun, and 2021, which gives the equivalent of [[bounded scalar concentration#Hoeffding's bound]] for Markov chains. 

Let $f_i : \calX \to [a_i,b_i]$. For a markov chain $\{X_i\}$ (could be continuous or discrete state space) taking values in $\calX$ with stationary distribution $\pi$ and spectral gap $1-\lambda>0$, they show that 
$$
\E_\pi\exp\left(t\left(\sum_{i\leq n}f_i(X_i) - \sum_{i\leq n} \pi(f_i)\right)\right) \leq \exp\left(\frac{1+\lambda}{1-\lambda} t^2\sum_{i\leq n} \frac{(b_i-a_i)^2}{8}\right).
$$
Here $\pi(f) = \int f \d\pi$. One can then apply Markov's inequality to get a concentration result.  

For iid observations, $\lambda=0$, so this recovers the usual Hoeffding lemma. This generalizes the discrete reversible setting studied by [Leon and Perron](https://www.stat.berkeley.edu/users/aldous/260-FMIE/Papers/leon.pdf). In general, the spectral gap tells us how fast the chain mixes and approaches the stationary distribution. For iid observations, the chain mixes immediately. As $\lambda\to 1$ it mixes slowly, and the quality of the bound degrades.  

# Reading 
- [Bernstein’s inequalities for general Markov chains](https://arxiv.org/pdf/1805.10721), Jiang, Sun, Fan, 2018. 
- [Hoeffding’s Inequality for General Markov Chains and Its Applications to Statistical Learning](https://jmlr.org/papers/volume22/19-479/19-479.pdf) by Fan, Jiang, Sun, 2021. 
- [Bernstein-type Inequalities for Markov Chains and Markov Processes: A Simple and Robust Proof](https://arxiv.org/pdf/2408.04930) by Huang and Li, 2024.  
- [Optimal Hoeffding Bounds for Discrete Reversible Markov Chains](https://www.stat.berkeley.edu/users/aldous/260-FMIE/Papers/leon.pdf)
- Some [[PAC-Bayes]] bounds on Markov chains: https://arxiv.org/pdf/2509.20985
