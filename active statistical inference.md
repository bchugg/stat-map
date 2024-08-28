
Most [[statistical inference]] assumes the data is somehow supplied to you (even in sequential settings; see [[sequential statistics]]). You are given data, and you are asked to estimate some parameter. 

But suppose we are in a [[supervised learning]] setting and you get to choose which data points to label. How should you label in them in order to help your inference (eg obtain smaller [[confidence intervals]])? Zrnic and Candes [introduce the framework](https://arxiv.org/abs/2403.03208) of active statistical inference to answer this question. 

Suppose we have data $(X_i,Y_i)_{i=1}^N$, where $Y_i$ is unobserved and $X_i$ is observed. We have a model $f$ which estimates $Y_i$ from $X_i$. The goal is to estimate $\theta^*$, the solution to an [[M-estimation]] problem: 
$$
\theta^* = \argmin_\theta \E[\ell_\theta(X,Y)],
$$
where $\ell_\theta$ is assumed to be convex. This handles [[mean estimation]], [[linear regression]] coefficients, and [[quantile estimation]].  We have a budget of $B$ observations that we're allowed to sample (in expectation). 

> [!Remark]
> That the budget holds only in expectation seems like a drawback of this model. Would that actually be the case in practice? Probably you would instead have some absolutely upper limit on the budget. 


# Intuition 

Consider mean estimation, $\theta^* = \E[Y]$ (so $\ell_\theta(X,Y) = (\theta - Y)^2$).  Let $\pi(X_i)$ be the probability of sampling $X_i$. Consider the [[doubly robust estimator]]: 
$$
\wh{\theta} = \frac{1}{N} \sum_{i=1}^N \left( f(X_i) + (Y_i - f(X_i))\frac{\xi_i}{\pi(X_i)}\right),
$$
which is unbiased. The variance is 
$$
\Var(\wh{\theta}) = \frac{1}{N} \left(\Var(Y) + \E\bigg[(Y - f(X))^2 \bigg(\frac{1}{\pi(X)}-1\bigg)\bigg]\right).
$$
If $Y\approx f(X)$, or $\pi(X) \approx 1$, then $\Var(\wh{\theta})$ is much smaller than the variance of just $B$ randomly selected points, which is $\frac{1}{B} \Var(Y)$.   So, ideally, we want to choose $\pi(X)$ such that if the model is bad, then $\pi(X) \approx 1$.  

# Choosing $\pi$ 

Zrnic and Candes choose $\pi$ as a function of the model uncertainty. It's hard to give rigorous guarantees here — the methods are mainly heuristics. 

**Regression**: We train a model $u$ to predict $u(X) = |Y - f(X)|$.  This should be trained on a dataset different from that which $f$ was trained on. 

**Classification**: Here we assume that $f(x) = \argmax_{i\in[k]}p_i(x)$ where $\sum_i p_i(x)=1$. Then we set 
$$
u(x) = \frac{K}{K-1}(1 - \max_{i}p_i(x)).
$$
If the classifier is maximally uncertain, then $p_i(x) = 1/K$ for all $i$ so $u(x)=1$. 
In practice, helps to mix $u$ with a uniform so that it doesn't blow up the variance. 
Once $u$ is determined, we might consider sampling strategies of the form: 
$\pi_\eta(x) = \eta u(x),$ where $\eta$ is some hyperparameter mean to ensure that we respect the budget $B$. They suggest choosing $\eta = \wh{\eta}$ where $\wh{\eta} = \sup \left\{\eta \in \calH : \eta\sum_{i=1}^n u(X_i)\leq B\right\},$ is a _data-driven_ selected parameter. The actual sampling is done by then sampling $\xi_i \sim \Ber(\pi_\eta(X_i))$ (i.e., whether $X_i$ is sampled independently of other observations). Note that this means we only meet the budget in expectation: 
$$
\E_S\sum_{i=1}^N \xi_i = \sum_{i=1}^N \E[\wh{\eta}\xi_i] = \sum_{i=1}^N \wh{\eta}u(X_i) \leq B,
$$
where the expectation is over the sampling only. 

# General setting 

We design a sampling algorithm $\pi$ which samples $x_i$ with probability $\pi(x_i)$. That is, we draw $\xi_i \sim \Ber(\pi(x_i))$ and if $\xi_i=1$ we sample $x_i$, otherwise we don't. This implies that all observations are sampled independently from one another. $\pi$ is scaled such that $\E[\sum_i \xi_i]\leq B$ to ensure that the expected number of labeled observations does not exceed the budget. 

Let $\ell_{\theta,i} = \ell_\theta(X_i,Y_i)$ be the estimate of the loss on example $i$, and $\ell_{\theta,i}^f = \ell_\theta(X_i,f(X_i))$ be the loss of the model on example $i$. An unbiased estimator of $L(\theta) = \E[\ell_\theta(X,Y)]$  is 
$$
L^\pi(\theta) = \frac{1}{n}\left(\sum_{i=1}^n \ell_\theta(X_i,f(X_i)) + (\ell_\theta(X_i,Y_i) - \ell_\theta(X_i,f(X_i)))\frac{\xi_i}{\pi(X_i)}\right).
$$
Note that this is just the [[doubly robust estimator]]. If $\pi$ is just the uniform rule and doesn't prioritize some observations over others, this recovers the [[prediction-powered inference]] estimator. 

The resulting confidence interval for our estimate $\wh{\theta}^{\wh{\eta}}$ comes from a [[central limit theorems|CLT]], from which a [[Wald interval]] is constructed. The CLT mainly follows from the usual CLT for [[M-estimation]], but needs to correct for the fact that $\wh{\eta}$ is not independent of the data. This is done by assuming that $\wh{\eta} \to \eta^*$ in probability for some fixed $\eta^*$. 

They also study a sequential setting, where the model and sampling rule can be iteratively updated. Then they apply a [[martingale CLT]] to get a CI for the estimate. 

# References 
- [Active statistical inference](https://arxiv.org/pdf/2403.03208.pdf) by Zrnic and Candes. 
- [Efficient adaptive experimental design for ATE estimation](https://arxiv.org/pdf/2002.05308.pdf) Very similar ideas, but with more focus on estimation as opposed to choosing the sampling strategy. 