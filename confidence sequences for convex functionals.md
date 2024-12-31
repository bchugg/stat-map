---
lastmod: 2024-12-30
created: 2024-12-24
---

We can create [[confidence sequences]] for some convex functionals by using [[Ville's inequality]] for reverse [[submartingale|submartingales]]. 

If $\varphi$ is convex, then $(Z_t)$ where $Z_t = \varphi(t^{-1}\sum_{i\leq t} X_i)$ is a submartingale by the "leave-one-out" property if $(X_i)$ is [[exchangeable distribution|exchangeable]]. 

This property was leveraged to give sequential concentration for convex [[distributional distance|divergences]], [[u-statistics]], and [[v-statistics]] (see [Martingale methods for sequential estimation of convex functionals and divergences](https://arxiv.org/pdf/2103.09267)) and was also used to provide sequential [[PAC-Bayes]] bounds (see [A unified recipe for (time-uniform) PAC-Bayes bounds](https://arxiv.org/pdf/2302.03421)). 

We note in general that concentration based on reverse submartingales will usually be weaker, in some sense, than those based on forward [[supermartingale|supermartingales]]. This is because reverse submartingales often can't handle predictable plug-ins (see [[confidence sequences via predictable plug-ins]]), and must instead rely on stitching (see [[stitching for LIL rates]]. Eg if $Z_t$ is as above, we might form the process $\exp\{\lambda Z_t - \psi(\lambda)V_t\}$, which is reminiscent of a [[sub-psi process]] for submartingales. But since $Z_t$ is not linear, this cannot be broken into a product, and a different $\lambda$ cannot be chosen at each timestep. So instead we must either mix over $\lambda$ (see [[confidence sequences via conjugate mixtures]]) or employ stitching to be able to allow $\lambda$ to be a function of time. 