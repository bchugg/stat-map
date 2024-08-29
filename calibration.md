Given a distribution $P$ over feature-label pairs $(X,Y)$, the goal of _mean_ calibration is to produce a model $f$ such that 
$$

v \approx \E[Y|f(x)=v],

$$
and the goal of quantile calibration is to produce a model such that 
$$

q \approx \Pr[y\leq v|f(x)=v].

$$

The most interesting setting for calibration is [[online calibration]]. 
# Patching

Most research into calibration is not trying to generate a new model $f$ which is calibrated, but instead supposes we are given an uncalibrated model $f$ and asks whether we can we "fix" it to make it more calibrated? Yes, yes we can.  

We have a target [[average calibration error]] $K_2$ of $\alpha$. Let 
$$
v' =\argmax_v \Pr(f(x) =v) \left( v - \E_P [y|f(x)=v]\right).
$$Then we simply set $\wh{f}(x) = v'$ if $f(x)=v$ and $\wh{f}(x) = f(x)$ otherwise. Repeating this procedure leads to a model with $\leq \alpha$ calibration error. Moreover, it also reduces [[squared error]]. You can show that this runs for $T\leq m/\alpha$ iterations where $m = |\range(f)|$. 

There's also a _one-shot_ algorithm that accomplishes this goal. If $c(v) = \E[y|f(x) = v]$, then simply let $\wh{f}(x) = c(f(x))$. Then $\wh{f}$ has $K_2=0$. 

Obviously, these assume access to the true distribution. One can approximate the means with the empirical distribution and then obtain bounds on the calibration error using standard [[concentration inequalities]]. 

Similar arguments apply if we're interested in quantile calibration. There's also a one-shot version. 




