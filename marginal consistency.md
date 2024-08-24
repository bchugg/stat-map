The idea behind marginal consistency in [[uncertainty quantification]] is to ensure that a model is consistent on average across the entire population. This comes in two flavors: Mean consistency, and quantile consistency. 

Note that **marginal guarantees are quite weak.**  Ideally one would have guarantees conditional on a specific input $x$, but here we're reasoning about averages over the entire population. 

Here we assume a batch setting, i.e., we have data $(X_1,Y_1),\dots,(X_n,Y_n)\sim P^n$ and we observe it all at once. There is also [[online marginal estimation]].  

We assume that the labels are bounded in $[0,1]$. 

# Mean consistency 

Ideally, we want to find a model which captures the conditional label $y|x$ for each $x$. That is, assume we have observations and labels drawn from some distribution $P$, $(X_1,Y_1),\dots,(X_n,Y_n)\sim P^n$, we want a model $f$ such that $$f(x) \approx \E_{Y\sim P(x)} [Y],$$
where $P(x)$ is the distribution over $y$ if given feature $x$.  A simpler task is the goal of a model which captures not the conditional mean, but the unconditional mean. 

To measure the error of an actual model we introduce the notion of _marginal mean consistency_, where we say $f$ is $\alpha$-marginally mean consistent if 
$$
\left|\E_{X\sim P_X}[f(X)] - \E_P [Y]\right|\leq \alpha.
$$

If you don't have a marginally-mean consistent model, then you can simply shift all model predictions by $\Delta = \E[Y] - \E[f(X)]$ in order to make it mean consistent. Doing so also makes the model more accurate with respect to the [[squared error]] (i.e., the Brier score). 

This ignores the problem that we don't know $\Delta$, but it can be estimated with a finite sample and Hoeffding style arguments (see [[concentration inequalities]]) can be used to show that if we do this shift on the empirical distribution, $\alpha$ is small over the true distribution with high probability. 

# Quantile consistency 

Here we ask that the model matches the target quantile of a distribution. We hope that for a target quantile $q$, $\Pr[y\leq f(x)]\approx q$. To measure error, we can introduce a similar notion as above. Say that a model $f$ has $\alpha$-marginal quantile consistency wrt $q$ if 
$$\left| \Pr_{(X,Y)\sim P}[Y\leq f(X)] -1\right|\leq \alpha.$$Just as the Brier score is relevant for mean consistency, the [[pinball loss]] is relevant for quantile consistency. 

If a model is not marginally quantile consistent (i.e,, $\alpha\neq 0$) we can again shift it so that it is, and this will actually improve the model in terms of the pinball loss. So there is a big parallel between mean consistency and quantile consistency in this way. (To do this we need to make certain smoothness assumptions on the CDF). Similar comments on finite-sample guarantees apply here. 



# References 
- Chapter 2 in Aaron Roth's [textbook](https://www.cis.upenn.edu/~aaroth/uncertainty-notes.pdf)