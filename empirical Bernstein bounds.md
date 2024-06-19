A *Bernstein* bound is a kind of [[concentration inequalities|concentration inequality]] that takes advantage of the variance of the distribution. 

They are usually part of a progression of bounds for random variables with bounded range. See [[from boundedness to variance adaptivity]]. 

_Empirical-Bernstein bounds_ replace knowledge of the variance with data-driven estimates of the variance. This is useful since we often don't know what the variance is. Ideally, such bounds can be shown to converge in the limit to a bound with width depending on the true variance —  i.e., they scale asymptotically with the true variance. 

Some examples: 

# Scalar-random variables 

# Random vectors 

We prove the following dimension-dependent empirical Bernstein bound in the paper [Time-uniform confidence spheres for means of random vectors](https://arxiv.org/abs/2311.08168). 

Let $X_1,X_2,\dots$ have conditional mean $\mu$ with $\norm{X_i} \leq 1/2$. Then, with probability $1-\alpha$, for all $t$: 
$$\norm{\frac{\sum_{i\leq t} \lambda_i X_i}{\sum_{i\leq t}\lambda_i} - \mu} \leq \frac{\sqrt{d}\sum_{i\leq t} \psi_E(\lambda_i)\norm{X_i- \widehat{\mu}_{i-1}}^2 + 2\sqrt{d} + \sqrt{d}\log(1/\alpha)}{\frac{2}{3} \sum_{i\leq t}\lambda_i}.$$

This is a [[time-uniform]] bound. Here $\widehat{\mu}_{i-1}$ is any predictable quantity, i.e., based on $X_1, X_2, \dots, X_{i-1}$. 
