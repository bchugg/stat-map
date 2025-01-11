---
created: 2024-08-29
lastmod: 2025-01-11
---

Given samples $X_1,\dots,X_n\sim P$ we want to estimate the density of $P$. We can consider both [[parametric density estimation]] and [[nonparametric density estimation]], the latter of course being easier but sensitive to model misspecification. 

Density estimation is obviously a very common task. Once you have an estimate of the distribution, you can calculate regression functions, perform anomaly and outlier detection (just look at whether a new observation has a small probability) and [[hypothesis testing]] (in particular [[two-sample testing]], in which we can estimate the densities of the two samples  compute the [[distributional distance|divergence]] between them). 