---
created: 2024-09-05
lastmod: 2024-10-07
---

Pinelis is responsible for both a Hoeffding and Bernstein bound in smooth and separable [[Banach space|Banach spaces]]. At the core of his proof is the construction of a [[supermartingale]]; his results can therefore be made [[time-uniform]] by applying [[Ville's inequality]] instead of Markov's inequality (though they're usually stated as [[fixed-time]] bounds). 
## Hoeffding 
Consider a $(2,D)$-smooth separable Banach space with norm $\norm{\cdot}$. Let $X_1,X_2,\dots$ have conditional mean $0$ with $\norm{X_t}\leq B$. Then: 
$$
\Pr\left(\norm{\sum_{i\leq n}X_i}\geq u\right) \leq 2\exp\left(-\frac{u^2}{2nD^2B^2}\right).
$$
Note the similarity to the usual Hoeffding bound ([[bounded scalar concentration]]) but with the extra factor of $D$. This is because [[Hilbert space|Hilbert spaces]] are $(2,1)$-smooth Banach spaces. 

## Bernstein 
Consider a $(2,D)$-smooth separable Banach space with norm $\norm{\cdot}$. Let $X_1,X_2,\dots$ have conditional mean $0$ with $\norm{X_t}\leq B$. Then 
$$
\Pr\left(\norm{\sum_{i\leq n}X_i}\geq u\right) \leq 2\exp\left(-\frac{u^2/2}{D^2\norm{\sum_{i\leq n} \E_{i-1}\norm{X_i - \mu}^2}_\infty+ uB/3} \right).
$$
Like for Bernstein's/Bennett's inequality in the scalar setting ([[bounded scalar concentration#Bennett's inequality]]), if the random variables are iid then $\E_{i-1}\norm{X_i - \mu}^2$ is simply the variance. 

## Empirical-Bernstein 
See discussion on the work of Martinez-Taboada and Ramdas in [[empirical Bernstein bounds]]: 
![[empirical Bernstein bounds#Random vectors]]

## Heavy-tailed concentration
In 2015, [Minsker proposed](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=adb542bb749073d80af52f2038ad6980e3874337) the geometric median-of-means for Banach spaces. This is a general method for [[ensemble learning#Boosting|boosting]] weak (polynomial rate) estimators into an estimator with exponential rate. The idea is similar to the Lugosi-Mendelson median-of-means (see [[multivariate heavy-tailed concentration]]), but the weak estimators are aggregated using the geometric median. This can be computed in polynomial time (in $\Re^d$) using [Weisfeld's algorithm](https://github.com/scoutant/l1-median), since the objective is convex. This estimator was proposed simultaneously by [Hsu and Sabato](https://proceedings.mlr.press/v32/hsu14.pdf). 

In 2022, [Yun and Park extended](https://arxiv.org/abs/2211.17155) geometric median-of-means to Polish spaces, which include separable Banach spaces. They seem to get the same rates as Minsker, which are not quite sub-Gaussian in $\Re^d$. 
