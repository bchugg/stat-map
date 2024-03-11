
Most [[statistical inference]] assumes the data is somehow supplied to you (even in sequential settings, see [[sequential statistics]]). You are given data, and you are asked to estimate some parameter. 

But suppose we are in a [[supervised learning]] setting you get to choose which data points to label — how should you label in them in order to help your inference (eg obtain smaller [[confidence intervals]])? Zrnic and Candes introduce the framework of active statistical inference to answer this question. 

Suppose we have data $(X_i,Y_i)_{i=1}^N$, where $Y_i$ is unobserved and $X_i$ is observed. We have a model $f$ which estimates $Y_i$ from $X_i$. The goal is to estimate $\theta^*$, the solution to an [[M-estimation]] problem: 
$$\theta^* = \argmin_\theta \E[\ell_\theta(X,Y)],$$
where $\ell_\theta$ is assumed to be convex. This handles [[mean estimation]], [[linear Regression]] coefficients, and [[quantile estimation]].  We have a budget of $B$ observations that we're allowed to sample (in expectation). 

# Batch setting 

We design a sampling algorithm $\pi$ which samples $x_i$ with probability $\pi(x_i)$. That is, we draw $\xi_i \sim \Ber(\pi(x_i))$ and if $\xi_i=1$ we sample $x_i$, otherwise we don't. Note this implies that all observations are sampled independently from one another. $\pi$ is scaled such that $\E[\sum_i \xi_i]\leq B$ to ensure that the expected number of labeled observations does not exceed the budget. 

Let $\ell_{\theta,i} = \ell_\theta(X_i,Y_i)$ be the estimate of the loss on example $i$, and $\ell_{\theta,i}^f = \ell_\theta(X_i,f(X_i))$ be the loss of the model on example $i$. An unbiased estimator of $L(\theta) = \E[\ell_\theta(X,Y)]$  is 
$$L^\pi(\theta) = \frac{1}{n}\left(\sum_{i=1}^n f(X_i) + (Y_i - f(X_i))\frac{\xi_i}{\pi(X_i)}\right).$$
Note that this is just the [[AIPW estimator]]. If $\pi$ is just the uniform rule and doesn't prioritize some observations over others, this recovers the [[prediction-powered inference]] estimator. 



# References 
- [Active statistical inference](https://arxiv.org/pdf/2403.03208.pdf) by Zrnic and Candes. 