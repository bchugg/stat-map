Given a distribution $P$ over feature-label pairs $(X,Y)$, the goal of calibration is to produce a model $f$ such that 
$$v \approx \E[Y|f(x)=v].$$

# Calibration via patching

Suppose we are given a model $f$. Can we 

