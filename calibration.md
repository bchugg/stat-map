---
created: 2024-08-29
lastmod: 2024-12-31
---

Given a distribution $P$ over feature-label pairs $(X,Y)$, the goal of _mean_ calibration is to produce a model $f$ such that 
$$
v \approx \E[Y|f(x)=v],
$$
and the goal of quantile calibration is to produce a model such that 
$$
q \approx \Pr[y\leq v|f(x)=v].
$$
The most interesting setting for calibration is [[online calibration]]. 

## Patching
Most research into calibration is not trying to generate a new model $f$ which is calibrated, but instead supposes we are given an uncalibrated model $f$ and asks whether we can we "fix" it to make it more calibrated? Yes, yes we can.  

We have a target average calibration error (see below) $K_2$ of $\alpha$. Let 
$$
v' =\argmax_v \Pr(f(x) =v) \left( v - \E_P [y|f(x)=v]\right).
$$
Then we simply set $\wh{f}(x) = v'$ if $f(x)=v$ and $\wh{f}(x) = f(x)$ otherwise. Repeating this procedure leads to a model with $\leq \alpha$ calibration error. Moreover, it also reduces [[squared error]]. You can show that this runs for $T\leq m/\alpha$ iterations where $m = |\range(f)|$. 

There's also a _one-shot_ algorithm that accomplishes this goal. If $c(v) = \E[y|f(x) = v]$, then simply let $\wh{f}(x) = c(f(x))$. Then $\wh{f}$ has $K_2=0$. 

Obviously, these assume access to the true distribution. One can approximate the means with the empirical distribution and then obtain bounds on the calibration error using standard [[concentration inequalities]]. 

Similar arguments apply if we're interested in quantile calibration. There's also a one-shot version. 

## Calibration error
How do we actually measure calibration error? Following Roth, define the average calibration error of a predictor $f$ with finite range $R(f)$ on distribution $D$ to be 
$$
K_1(f,D) := \sum_{v\in R(f)} \Pr_{x,y\sim D}[f(x) = v]\left| v - \E_{D}[y | f(x) = v]\right|.
$$
 This is similar to $\ell_1$ loss. We can also write something that's similar to [[squared error]]: 
$$
K_2(f,D) := \sum_{v\in R(f)} \Pr_{x,y\sim D}[f(x) = v]\left( v - \E_{D}[y | f(x) = v]\right)^2.
$$
Or we could naturally write something similar to $\ell_\infty$ by taking the maximum. Note that we are weighting each error term by the model predictions. So if our error is small, it's small according to our own model's lights, i.e., our own expected value. 

Similar error notions exist for quantile calibration. Here we have eg 
$$
Q_1(f,D) = \sum_{v\in R(f)} \Pr_{x,y\sim D}[f(x) = v]\left| q - \Pr_{D}[y\leq v | f(x) = v]\right|.
$$
We can also write down $Q_2$, $Q_\infty$, etc. 




