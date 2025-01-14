---
created: 2024-08-29
lastmod: 2025-01-14
---

# Bounded distributions

## Bernstein bounds 
**Bounds in $\Re^d$**:  Let $X_1, \dots, X_n\in\Re^d$ obey $\norm{X_t}\leq c_t$ and $\E[\norm{X_t}^2]\leq v_t^2$. Let $V_n = \sum_{i\leq n}v_i^2$. Using the martingale-variance inequality [[martingale concentration#Variance bound|martingale concentration:Variance bound]], we obtain 
$$
\Pr( \norm{S_n} \geq \sqrt{V_n} + \eps) \geq \exp\left(\frac{-\eps^2}{4V_n}\right),
$$
for $\eps \leq V / \max_t c_t$. A bound of this form was first given by David Gross [here](https://arxiv.org/pdf/0910.1879). 

Note that a weaker form of this bound can be obtained by appealing to the Azuma-Hoeffding inequality ([[martingale concentration#Azuma-Hoeffding inequality|martingale concentration:Azuma-Hoeffding inequality]]). The difference is equivalent to the difference between the Hoeffding bound and the Bernstein/Bennett bound in the scalar case (see [[bounded scalar concentration]]).   

**Bounds in more general spaces**: There are dimension-free Bernstein bounds that hold in [[Banach space|Banach spaces]]: see [[concentration in Banach spaces]]. There are also dimension-free _empirical_ Bernstein bounds, see [[empirical Bernstein bounds]]. 

# Sub-Gaussian distributions 
See [[sub-Gaussian distributions]] distributions for definitions in multivariate settings. 

**Sub-Gaussian coordinates**: If $X_1,\dots,X_n$ are independent and sub-Gaussian with $\E X_i^2=1$, then the norm $\| X \| = \| (X_1,\dots,X_n)\|$ is concentrated around $\sqrt{n}$. In particular, for some $c>0$, 
$$
\Pr( |\| X\|_2 - \sqrt{n}| \geq u) \leq 2\exp(-cu^2 / K^4),
$$
where $K = \max_i \| X_i\|_{\psi_2}$ is the maximum sub-Gaussian [[Orlicz norm]]. 

**Sub-Gaussian random vectors**. [Hsu et al (2012)](https://web.archive.org/web/20160413235708id_/http://ecp.ejpecp.org/article/viewFile/2079/2154) give state-of-the-art sub-Gaussian concentration. They show that for a fixed matrix $A$, if $X$ is $I$-sub-Gaussian with mean 0, then with probability $1-\delta$, 
$$
\| AX\|^2 \leq \Tr(\Sigma) + 2\|\Sigma\|u + 2\sqrt{\Tr(\Sigma^2)u},
$$
where $u = \log(1/\delta)$. This can be translated into a sub-Gaussian as follows: If $X$ is $I$-subGaussian, then $AX$ is $A^t A$-subGaussian. Therefore, the above gives a bound for $\Sigma$-subGaussian $X$ where $\Sigma$ can be decomposed as $\Sigma = A^t A$. For $n$ such vectors, we get the bound 
$$
\|\ov{X}_n\|^2 \leq \frac{\Tr(\Sigma) + 2\|\Sigma\|u + 2\sqrt{\Tr(\Sigma^2)u}}{n}.
$$
There is also a [[time-uniform]] bound that allows for [[martingale dependence]] which is nearly as tight, but not quite. See [this paper](https://arxiv.org/abs/2311.08168) for details. For $X_1,X_2,\dots$ where $X_i$ is conditionally $\Sigma$-subGaussian (and still mean 0) we have 
$$
\norm{\frac{\sum_{i\leq t} \lambda_i X_i}{\sum_{i\leq t}\lambda_i}} \leq \frac{\sum_{i\leq t}\psi_N(\lambda_i)(\norm{\Sigma} + \beta^{-1}\Tr(\Sigma)) +   \beta/2 + \log(1/\alpha)}{\sum_{i\leq t}\lambda_i},
$$
where $(\lambda_i)$ is a predictable sequence. When instantiated with the optimal $\lambda_i$ and $\beta$ we get the rate 
$$
\widetilde{O}\left(\sqrt{\Tr(\Sigma) + \norm{\Sigma}\log(1/\alpha)}\sqrt{\frac{\log t}{t}}\right).
$$
This can be made into a bound with optimal iterated logarithm dependence ([[laws of the iterated logarithm]]) using stitching ([[stitching for LIL rates]]). At a fixed time $n$, the optimal choice of $\beta$ and $\lambda$ give the bound 
$$
\|\ov{X}_n\|^2 \leq \frac{\Tr(\Sigma) + 2\|\Sigma\|u + 2\sqrt{2\|\Sigma\|\Tr(\Sigma)u}}{n},
$$
which we can see is worse than Hsu et al's bound above, since $\|\Sigma\|\Tr(\Sigma)\geq \Tr(\Sigma^2)$ (but not by the leading factor, so the asymptotics are the same). This bound is proved with the [[variational approach to concentration]]. 

# Sub-$\psi$ distributions 

# Other conditions 

**Log-concave distributions.** This comes from [this paper](https://arxiv.org/abs/2311.08168) and is proved with the [[variational approach to concentration]]. Let $(X_t)_{t\geq 1}$ be conditionally [[log-concave distribution|log-concave]], meaning that for all $t\geq 1$,
$$
    \norm{\la\theta, X_t - \E[X_t|\calF_{t-1}]\ra}_{\psi_1} \leq C\sqrt{\la \theta, \Sigma\theta\ra},
$$
for all $\theta\in\Re^d$, some $C>0$ and PSD $\Sigma$. Let $f_\alpha(u) = \sqrt{\Tr(\Sigma)u} + u\sqrt{\norm{\Sigma}}$. Then with probability $1-\alpha$, for all $t\geq 1$, 
$$ 
\norm{\frac{\sum_{i\leq t}\lambda_i X_i}{\sum_{i\leq t}\lambda_i} - \mu} \leq \frac{2C f_\alpha(1) \sum_{i\leq t}\lambda_i^2 + 4Cf_\alpha(\log(2/\alpha))}{\sum_{i\leq t}
    \lambda_i},
$$
where $(\lambda_t)$ is any predictable sequence taking values in $(0,1)$. For a fixed-time $n$, taking $\lambda = \sqrt{\frac{2f_\alpha(\log(2/\alpha))}{nf_\alpha(1)}}$ gives a width bounded by $8C \sqrt{\log(1/\alpha)\Tr(\Sigma)} / \sqrt{n}$. In the sequential setting, taking $\lambda_t =\sqrt{\frac{2f_\alpha(\log(2/\alpha))}{t \log(t+1)f_\alpha(1)}}$ gives a width of 
$$
\widetilde{O}\left(\sqrt{\frac{\Tr(\Sigma) \log(1/\alpha) \log(t)}{t}}\right).
$$
Stitching can be used to get LIL rates ([[stitching for LIL rates]]). 



