---
created: 2024-09-05
lastmod: 2025-01-09
---

Pinelis (see his [1992](https://link.springer.com/content/pdf/10.1007/978-1-4612-0367-4_9?pdf=chapter+toc) and [1994](https://www.jstor.org/stable/2244912) papers) is responsible for both a Hoeffding and Bernstein bound in smooth and separable [[Banach space|Banach spaces]]. At the core of his proof is the construction of a [[supermartingale]] (see [[Pinelis approach to concentration]]) his results can therefore be made [[time-uniform]] by applying [[Ville's inequality]] instead of Markov's inequality (though they're usually stated as [[fixed-time]] bounds). 

## Chebyshev 
The sample mean doesn't necessarily concentrate in Banach spaces (see discussion in [[Banach space]]). One needs a smoothness assumption. But once such an assumption is added, we can get the following behavior of the sample mean. This result is from [Mean Estimation in Banach Spaces Under Infinite Variance and Martingale Dependence](https://arxiv.org/abs/2411.11271). 

Let $(X_n)_{n \geq 1}$ be random variables in a $(2,\beta)$-smooth Banach space which have conditional mean $\mu$ and conditional $p$-th moment, $p>1$, bounded by $v$ (i.e., $\E [\|X_n- \mu\|^p|\calF_{n-1}]\le v$). Then, for any $\delta \in (0, 1)$ and $n \geq 1$, we have
$$
\Pr\left(\|\wh{\mu}_n - \mu\| \leq \frac{2 \beta v}{n^{(p - 1)/p}}\right) \geq 1 - \delta,
$$
or equivalently, 
$$
\Pr(\|\wh{\mu}_n - \mu\| \geq t) \leq \frac{v2^p\beta^p}{n^{p-1}t^p}.
$$
where $\wh{\mu}_n := n^{-1}\sum_{m =1}^n X_m$ denotes the usual sample mean. So we see that $\beta$ pops up in the bound. 

## Marcinkiewicz–Zygmund inequality
The proof of Chebyshev's inequality above actually relies on a [Marcinkiewicz–Zygmund-style](https://en.wikipedia.org/wiki/Marcinkiewicz%E2%80%93Zygmund_inequality) inequality in smooth Banach spaces. Let $(X_n)_{n \geq 1}$ be random variables in a $(2,\beta)$-smooth Banach space such that $\E_{n - 1} X_n = 0$ and $\E\|X_n \|^p < \infty$ for all $n \geq 0$ and some $p \in (1, 2]$. Then, letting $(S_n)_{n \geq 0}$ be $S_n := X_1 + \cdots + X_n$, we have
$$
\E\|S_n\|^p \leq 2^p\beta^p\E\left[\left(\sum_{m = 1}^n \|X_m\|^2\right)^{p/2}\right] \leq  2^p \beta^p \sum_{m=1}^n \E\|X_m\|^p.
$$
## Hoeffding 
Consider a $(2,D)$-smooth separable Banach space with norm $\|\cdot\|$. Let $X_1,X_2,\dots$ have conditional mean $0$ with $\norm{X_t}\leq B$. Then: 
$$
\Pr\left(\norm{\sum_{i\leq n}X_i}\geq u\right) \leq 2\exp\left(-\frac{u^2}{2nD^2B^2}\right).
$$
Note the similarity to the usual Hoeffding bound ([[bounded scalar concentration]]) but with the extra factor of $D$. This is because [[Hilbert space|Hilbert spaces]] are $(2,1)$-smooth Banach spaces. 

## Bernstein 
Consider a $(2,D)$-smooth separable Banach space with norm $\|\cdot\|$. Let $X_1,X_2,\dots$ have conditional mean $0$ with $\norm{X_t}\leq B$. Then 
$$
\Pr\left(\norm{\sum_{i\leq n}X_i}\geq u\right) \leq 2\exp\left(-\frac{u^2/2}{D^2\norm{\sum_{i\leq n} \E_{i-1}\norm{X_i - \mu}^2}_\infty+ uB/3} \right).
$$
Like for Bernstein's/Bennett's inequality in the scalar setting ([[bounded scalar concentration#Bennett's inequality]]), if the random variables are iid then $\E_{i-1}\norm{X_i - \mu}^2$ is simply the variance. 

## Empirical-Bernstein 
See discussion on the work of Martinez-Taboada and Ramdas in [[empirical Bernstein bounds]]: 
![[empirical Bernstein bounds#Random vectors]]

## Heavy-tailed concentration
In 2015, [Minsker proposed](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=adb542bb749073d80af52f2038ad6980e3874337) the geometric median-of-means for Banach spaces. This is a general method for [[ensemble learning#Boosting|boosting]] weak (polynomial rate) estimators into an estimator with exponential rate. The idea is similar to the Lugosi-Mendelson median-of-means (see [[multivariate heavy-tailed mean estimation]]), but the weak estimators are aggregated using the geometric median. This can be computed in polynomial time (in $\Re^d$) using [Weisfeld's algorithm](https://github.com/scoutant/l1-median), since the objective is convex. This estimator was proposed simultaneously by [Hsu and Sabato](https://proceedings.mlr.press/v32/hsu14.pdf). 

In 2022, [Yun and Park extended](https://arxiv.org/abs/2211.17155) geometric median-of-means to Polish spaces, which include separable Banach spaces. They seem to get the same rates as Minsker, which are not quite sub-Gaussian in $\Re^d$. 

[Whitehouse et al. (2024)](https://arxiv.org/abs/2411.11271) propose extending Catoni and Giulini's truncation-based estimator ([[truncation-based estimators]]) to Banach spaces. This estimator can handle infinite variance. 