
Most [[statistical inference]] assumes the data is somehow supplied to you (even in sequential settings, see [[sequential statistics]]). You are given data, and you are asked to estimate some parameter. 

But suppose we are in a [[supervised learning]] setting you get to choose which data points to label — how should you label in them in order to help your inference (eg obtain smaller [[confidence intervals]])? Zrnic and Candes introduce the framework of active statistical inference to answer this question. 

Suppose we have data $(X_i,Y_i)_{i=1}^N$, where $Y_i$ is unobserved and $X_i$ is observed. We have a model $f$ which estimates $Y_i$ from $X_i$. The goal is to estimate $\theta^*$, the solution to an [[M-estimation]] problem: 
$$\theta^* = \argmin_\theta \E[\ell_\theta(X,Y)],$$
where $\ell_\theta$ is assumed to be convex. This handles [[mean estimation]], [[linear regression]] coefficients, and [[quantile estimation]].  We have a budget of $B$ observations that we're allowed to sample (in expectation). 

# Intuition 

Consider mean estimation, $\theta^* = \E[Y]$ (so $\ell_\theta(X,Y) = (\theta - Y)^2$).  Let $\pi(X_i)$ be the probability of sampling $X_i$. Consider the [[AIPW estimator]]: 
$$\wh{\theta} = \frac{1}{N} \sum_{i=1}^N \left( f(X_i) + (Y_i - f(X_i))\frac{\xi_i}{\pi(X_i)}\right),$$
which is unbiased. The variance is 
$$ \Var(\wh{\theta}) = \frac{1}{N} \left(\Var(Y) + \E\bigg[(Y - f(X))^2 \bigg(\frac{1}{\pi(X)}-1\bigg)\bigg]\right).$$
If $Y\approx f(X)$, or $\pi(X) \approx 1$, then $\Var(\wh{\theta})$ is much smaller than the variance of just $B$ randomly selected points, which is $\frac{1}{B} \Var(Y)$.   So, ideally, we want to choose $\pi(X)$ such that if the model is bad, then $\pi(X) \approx 1$.  

# Choosing $\pi$ 

Zrnic and Candes choose $\pi$ as a function of the model uncertainty. 

**Regression**: We train a model $u$ to predict $u(X) = |Y - f(X)|$.  This should be trained on a dataset different from that which $f$ was trained on. 

**Classification**: Here we assume that $f(x) = \argmax_{i\in[k]}p_i(x)$ where $\sum_i p_i(x)=1$. Then we set 
$$u(x) = \frac{K}{K-1}(1 - \max_{i}p_i(x)).$$
If the classifier is ultimately uncertain, then $p_i(x) = 1/K$ for all $i$ so $u(x)=1$. 
In practice, helps to mix $u$ with a uniform so that it doesn't blow up the variance. 
Once $u$ is determined, we might consider sampling strategies of the form: 
$$\pi_\eta(x) = \eta u(x),$$ where $\eta$ is some hyperparameter mean to ensure that we respect the budget $B$. They suggest choosing $\eta = \wh{\eta}$ where 
$$\wh{\eta} = \sup \left\{\eta \in \cH : \eta\sum_{i=1}^n u(X_i)\leq B\right\},$$is a _data-driven_ selected parameter. The actual sampling is done by then sampling $\xi_i \sim \Ber(\pi_\eta(X_i))$ (i.e., whether $X_i$ is sampled independently of other observations). Note that this means we only meet the budget in expectation: 
$$\E_S\sum_{i=1}^N \xi_i = \sum_{i=1}^N \E[\wh{\eta}\xi_i] = \sum_{i=1}^N \wh{\eta}u(X_i) \leq B,$$
where the expectation is over the sampling only. 


# Batch setting 

We design a sampling algorithm $\pi$ which samples $x_i$ with probability $\pi(x_i)$. That is, we draw $\xi_i \sim \Ber(\pi(x_i))$ and if $\xi_i=1$ we sample $x_i$, otherwise we don't. Note this implies that all observations are sampled independently from one another. $\pi$ is scaled such that $\E[\sum_i \xi_i]\leq B$ to ensure that the expected number of labeled observations does not exceed the budget. 

Let $\ell_{\theta,i} = \ell_\theta(X_i,Y_i)$ be the estimate of the loss on example $i$, and $\ell_{\theta,i}^f = \ell_\theta(X_i,f(X_i))$ be the loss of the model on example $i$. An unbiased estimator of $L(\theta) = \E[\ell_\theta(X,Y)]$  is 
$$L^\pi(\theta) = \frac{1}{n}\left(\sum_{i=1}^n \ell_\theta(X_i,f(X_i)) + (\ell_\theta(X_i,Y_i) - \ell_\theta(X_i,f(X_i)))\frac{\xi_i}{\pi(X_i)}\right).$$
Note that this is just the [[AIPW estimator]]. If $\pi$ is just the uniform rule and doesn't prioritize some observations over others, this recovers the [[prediction-powered inference]] estimator. 

The resulting confidence interval comes from a [[central limit theorem]], from which a [[Wald interval]] is constructed. The CLT mainly follows from the usual CLT for [[M-estimation]], but needs to correct for the fact that $\wh{\eta}$ is not independent of the data. 

We need the following assumptions: Let $\theta^{\eta} = \argmin_\theta L^{\pi_\eta}(\theta)$.
- There exists some $\eta^*\in \cH$ such that $\wh{\eta}\to \eta^*$ in probability,
- $\theta^{\eta^*} \to  \theta^*$ in probability (i.e., consistency of the M-estimator)
- the loss is "smooth enough" (differentiable, locally Lipschitz) 
- Hessian $H_{\theta} = \nabla^2 L(\theta) = \nabla^2 \E[\ell_\theta(X,Y)]$ is positive definite.  
 Then, 
$$\sqrt{n}(\wh{\theta}^{\wh{\eta}} - \theta^*) \xrightarrow{d} N(0,\Sigma_*),$$
where $\Sigma_* = H_{\theta^*}^{-1} \Var(\nabla \ell_\theta^f + (\nabla \ell_\theta + \nabla \ell_\theta^f )\frac{\xi^{\eta^*}}{\pi_{\eta^*}(X)})H_{\theta^*}^{-1}$. From here we can form a Wald CI for any consistent estimator of $\Sigma_*$. 

The last three assumptions are the usual assumptions for CLTs in M-estimation. The first assumption is required to ensure the data-driven choice of $\wh{\eta}$ does not affect the result. Basically one writes 

$$\sqrt{n}(\wh{\theta}^{\wh{\eta}} - \theta^*) = \sqrt{n}(\wh{\theta}^{\wh{\eta}} - \wh{\theta}^{\wh{\eta}^*}) + \sqrt{n}(\wh{\theta}^{\wh{\eta}^*} - \theta^*).$$
We use the CLT for M-estimators on the second term, and argue that the second term goes to 0.  


# Sequential setting 

Can iteratively update the model and the sampling rule. 
At step $t$: Observe $X_t$, collect its label with probability $\pi_t(X_t)$ where $\pi_t$ is based on the uncertainty of model $f_t$. 
Need $\pi_t,f_t\in\cF_{t-1}$ where $\cF_t = \sigma(X_1,Y_1\xi_1,\xi_1,\dots,X_2,Y_2\xi_2,\xi_t)$. 

The estimator is now $\wh{\theta} = \argmin_\theta L_\pi(\theta)$ where $L^\pi(\theta) = \sum_{i=1}^n \Delta_t$ and $$\Delta_t = \ell_\theta^{f_t} + (\ell_\theta - \ell_\theta^{f_t})\frac{\xi_t}{\pi_t(X_t)}.$$If the increments satisfy a Lindeberg condition, then a [[martingale CLT]] applies, and we can get another CLT and resulting asymptotic CI.  




# References 
- [Active statistical inference](https://arxiv.org/pdf/2403.03208.pdf) by Zrnic and Candes. 
- [Efficient adaptive experimental design for ATE estimation](https://arxiv.org/pdf/2002.05308.pdf) Very similar ideas, but with more focus on estimation as opposed to choosing the sampling strategy. 