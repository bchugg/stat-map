---
created: 2024-05-27
lastmod: 2024-09-29
---

As in [[heavy-tailed scalar concentration]], the sample mean $\overline{X}_n$ is too easily influenced by outliers and does have good concentration properties. Also as in the scalar setting, the polynomial rate (in terms of the confidence level, $\delta$) given by Chebyshev's inequality is the best one can hope for when working with the sample mean. (See the discussion in [Hopkins](https://arxiv.org/pdf/1809.07425) or by [Catoni, section 6](http://www.numdam.org/item/10.1214/11-AIHP454.pdf)). 

What can we hope for in the multivariate setting? In $\Re^d$, the empirical mean of the Gaussian behaves as 
$$
\Pr\left(\wh{\mu} - \mu|\geq O\left(\sqrt{\frac{\Tr(\Sigma)}{n}} + \sqrt{\frac{\|\Sigma\| \log(1/\delta)}{n}}\right)\right)\leq \delta.
$$
This is called sub-Gaussian performance of an estimator, and is what we're trying to achieve even in heavy-tailed settings.  See the recent [survey by Lugosi and Mendelson](https://arxiv.org/pdf/1906.04280) for more.  

# Median-of-means (MoM)
In $\Re^d$, a gold-standard sub-Gaussian estimator—just as in the scalar case—is the MoM estimator.  The idea is the same as in the scalar case: Bucket the observations, take the sample mean in each bucket, then take the median of the sample means. 

Defining the median is slightly trickier though. [Lugosi and Mendelson define a specialized version of the median](https://www.econ.upf.edu/~lugosi/mean.pdf) and get sub-Gaussian rates. [Blog post here](https://benchugg.com/research_notes/median-of-means-multivariate/). [Hopkins made this computationally tractable](https://arxiv.org/pdf/1809.07425) in 2020. 

MoM (though with the geometric median not with the Lugosi-Mendelson median) was studied in [[Banach space|Banach spaces]] by Minsker and in Polish spaces by Yun and Park:  
![[concentration in Banach spaces#Heavy-tailed concentration]]

Unlike the scalar setting ([[heavy-tailed scalar concentration#Median-of-means (MoM)|univariate MoM]]) MoM has not been extended to settings where the variance doesn't exist. 

# Truncation-based estimators 
In 2018, [Catoni and Giulini proposed](https://arxiv.org/pdf/1802.04308) a simple estimator in $\Re^d$: Simply truncate the observations and take the empirical mean of the result. In particular, they consider 
$$
\wh{\mu} = \frac{1}{n} \sum_{i\leq n} \alpha(X_i)X_i,
$$
where 
$$
\alpha(X) := \frac{\min\{\lambda\norm{X}, 1\}}{\lambda\norm{X}} = \min\{1, (\lambda \norm{X})^{-1}\},
$$
for some $\lambda>0$. This has a rate of $O(\sqrt{v^2\log(1/\delta)/n})$ where $\E\norm{X - \mu}^2\leq v^2$. The rate is therefore not quite sub-Gaussian, but close. See the [discussion by Lugosi and Mendelson](https://arxiv.org/pdf/1906.04280) (Section 3.3) for a clear exposition about the precise rates of the Catoni-Giulini estimator. [We gave a sequential version of this estimator](https://arxiv.org/abs/2311.08168). 

# Catoni's M-estimator 
