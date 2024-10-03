---
created: 2024-08-29
lastmod: 2024-09-02
---

A perspective on statistics which views the parameters of the statistical model as random. This is in distinction to [[frequentist statistics]] which views them as fixed but unknown. 

As an example, consider testing the bias of a coin. The frequentist assumes the bias is some value $p\in[0,1]$, flips the coin a bunch, and perhaps forms a [[confidence intervals|confidence interval]] for $p$. The Bayesian places a distribution $\pi$ over $p$ (eg a uniform), flips the coin, and then updates their prior via Bayes' theorem. Since their resulting inference will always depend on the prior, this leads to them to results such as [[credible intervals]], the Bayesian equivalent of confidence intervals. 
 
 Bayesian methods, both parametric ([[Bayesian parametrics]]) and nonparametric ([[Bayesian nonparametrics]]) put a prior $\pi$ over the model, and then compute a posterior based on given data and the prior. The posterior can then be used in downstream statistical tasks. 

The [[Bayesian interpretation of probability]] is the view of probability which is usually used to justify Bayesian statistical methods. This need not be the case, however. One can equally well make the case for Bayesian statistics via the [[instrumentalist theory of probability]]. 
 


