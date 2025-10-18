---
created: 2024-08-29
lastmod: 2025-10-18
---

Suppose we have a stochastic process $(S_t)$ evolving in some space. What techniques are available for bounding $\norm{S_t}$? If $S_t\in\Re$, then we usually argue about $S_t$ and $- S_t$ and take a union bound to get a bound on $|S_t|$ (see eg [[bounded scalar concentration]] and [[light-tailed, unbounded scalar concentration]]). However, in higher-dimensional spaces (in $\Re^d$, $d\geq 2$, say) a union bound doesn't suffice: there are infinitely many directions one has to worry about. 

There are several techniques for dealing with this problem. 

## Working directly with the norm 
There are roughly two approaches that I'm aware of: The Doob decomposition approach and the Pinelis approach. 

The idea for the first is to form a Doob martingale from the increments of the process and then apply well-known martingale bounds.  Set
$$
Z_t = \E[\norm{S_n} | \calF_t] - \|S_n\|.
$$
So $(Z_t)$ is a martingale with $Z_0=0$. Let $D_t = Z_t - Z_{t-1}$, be the increments of the process. Various [[martingale concentration]] bounds are stated as conditions on the increments of the process. For instance:
- If $S_t$ is bounded for each $t$, then we can use the Azuma-Hoeffding inequality ([[martingale concentration#Azuma-Hoeffding inequality|martingale concentration:Azuma-Hoeffding inequality]]) 
- If a bound on the variance of $D_t$ is known, then we can use the equivalent of a Bernstein inequality ([[martingale concentration#Variance bound|martingale concentration:Variance bound]], often called a Freedman inequality. 
This approach is taken by eg David Gross [here](https://arxiv.org/pdf/0910.1879) to get vector Bernstein inequalities. 

The [[Pinelis approach to concentration]] is another method which works directly with the norm. We might also label this the Yurinskii approach, since he does something similar in an earlier [1976 paper](https://pdf.sciencedirectassets.com/272481/1-s2.0-S0047259X00X01108/1-s2.0-0047259X76900014/main.pdf?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLWVhc3QtMSJIMEYCIQDMnxBaGTCR4OWoWmFsgCvkvMfrLMrpwqrtbuCoR57U%2BQIhAM6iU3kD7BC30MOeDFDqavyh28KhVO1dwCcAGeLkkxGoKrwFCMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQBRoMMDU5MDAzNTQ2ODY1IgyewY8wvdTH%2FvdjXnEqkAWOTzGzBn8jk3A%2FqFioFWQr4V1NLqRfGtm3iI0IbBqkeo8DgijnXbmGzCf1Fe%2Fd4XZRTk6bHfWe%2BkFefP3rdnLAdQK2Y7xSql7E5%2FMAhvc7jUZqiyusFHaI33yFH2E2cJamDuJilXqpCNfoFwSZuZQ9ARjp%2F897XYnr6YPU0lYglDA34nud03q6tYhiVsYbxSslh3Od6VMLPZtk%2B9Or2tAxj2wdgDg9t7bhR2%2BQgzd62Uh6ivcCj%2BxAa2w88UlW2EOAlUiAJyv83bWkSBGNTfr%2FDoIaZyegkjrzkwrAtyBx73AO7sjYOIiBbZ8neGiOEU0wNtN8U9Atxi%2F9JzV3eKry56IYvhST5uWYKnjp%2BFUjnHZFjZ3RqXfFemXwCJHtFFH1pTaHFOkxXS%2F1JBSX8m%2FrzLiVyUamYeMHtPFP7ogNS19DOjrmE7ZfYR%2BRTXrp0WNQtsF7aWWdDSuJlOuVmoI1bvJNnuXdNEhnE%2FQOJrtFCy3UjZBElYYoNR00JkyNkUgIK4HEKtB8beonEFi2tMElDxOAmmjKRs%2Byv57kx%2FAP6IZHHodD9l9eySoAKdWA0bkGS%2BdJ5fga5JbvVi%2FsFbql4GBcxxekMbTjjq9PIQDLymE3AJhaX0ZSfnVMuSdRUu5%2FKjpcstNGN03CXZIY1Oqjud0AC2JHU0mUcA1QyfBBguzQxS2czO3maAnrg3P1Lifw4MFBo8mkbHX25ACQ1amCVKz%2Bz%2BOaVNpkVQhluNZbCb%2BkCtr702MezBn01L66qElA%2FNXcS%2Funk1sFH2%2FXFoNbk3JyhnWTbWG%2FDitCLODNrwuDbTHEFBEB95WmJRhHlN5vuv4WZcW6sWabgyA7hBsiHP%2Fg9dJ5ANVOSOemYfaXXTCC5c7HBjqwAWOz9cQNGbVhx%2FCjMbCmZM8zakCEdiL2QUiqRQZH%2BTbnlIXqj3MLyblGuRisbBzIxmH3Y0Gi81elZ8Qi7G4F0itKcpS8XRmpex%2By8CB9yf9OThZKtSTGdqPDUy4ntBHFdsjSoIMoeVvmLBrqvTCOCbZdpyY2WpRW3g4Kd4hkhxpANAQ5e4lbZEt30Ue4xhIGgglaDwiPNbAQU0a8biS4hssj38E0n8WGnyvBV9Z2H2Ur&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20251018T162821Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIAQ3PHCVTYVHOGOPBQ%2F20251018%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=495a338cc41234b9611f82c2ab888dd029f9e65fb99bb08fe553a7e3f00544ec&hash=fe9b17459131a5e22ba61ff0a5083eecfc377bcac92e581712a207375ea67193&host=68042c943591013ac2b2430a89b270f6af2c76d8dfd086a07176afe7c76c2c61&pii=0047259X76900014&tid=spdf-5d66f654-1ef4-4787-b135-8cb9574a460c&sid=4e1148c82f52564dd02b1cf458cbf731e088gxrqa&type=client&tsoh=d3d3LnNjaWVuY2VkaXJlY3QuY29t&rh=d3d3LnNjaWVuY2VkaXJlY3QuY29t&ua=0d015c56555f595d5a&rr=99096888cf8e7bf4&cc=ca).   

For [[multivariate light-tailed concentration]] of [[sub-Gaussian distributions]], the technique of Hsu et al is another example of working directly with the norm. Their technique seems specific to sub-Gaussian distributions however; it doesn't seem to constitute a general approach. 

## Covering arguments 
See [[concentration via covering]] for an overview. The idea is decompose $\|S_t\|$ into $\sup_\theta \la \theta, S_t\ra$ where the supremum is over the unit ball, cover the the unit ball with an finite net, bound $\la \theta, S_t\ra$ for each $\theta$ in this finite set, and then take a union bound. You suffer the covering number ([[covering and packing]]) of the underlying space in the bound. 

This means covering arguments lead to dimension-dependent bounds because covering numbers will depend geometrically on the underlying space.  Obviously, you also have to be able to calculate the covering number. 

## Chaining 
This also works by decomposing $\|S_t\| = \sup_\theta \la \theta, S_t\ra$. See [[chaining]] for a more detailed overview. Chaining provides high probability guarantees of the form 
$$
\Pr\left(\sup_{\theta\in\dsphere} \la \theta, S_n\ra \geq tS\right)\lesssim \exp(-t^2),
$$
where
$$
 S = \sup_{\theta\in\dsphere} \sum_{n\leq N}2^{n/2} \rho(\theta, \Theta_n),
$$
and $\Theta_0\subset\Theta_1\subset\dots\subset\Theta_N$ are a selected sequence of sets which slowly "approximate" $\Theta=\dsphere$. The difference between [[generic chaining]] and [[Dudley chaining]] is how they choose to handle $S$. The latter typically bounds it using covering numbers and [[metric entropy]].  

## The variational approach 
See [[variational approach to concentration]]. The idea is to use [[PAC-Bayes]] inequalities which are high probability guarantees over all probabilities measures into a simultaneous guarantee over all directions. 

In some scenarios they allow you to escape-dimension dependence (eg for sub-Gaussian random vectors) which neither chaining nor covering arguments allow you to do. 

# Reading 
- [Variational approach to concentration](https://benchugg.com/research_notes/variational_approach_to_concentration/) 
- [Confidence estimation via sequential likelihood mixing](https://arxiv.org/pdf/2502.14689) by Kirschner et al. Gives several strategies including the [[variational approach to concentration]] and also relates it to [[variational inference]]. 