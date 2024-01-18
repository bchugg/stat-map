Hypothesis tests can be inverted to create [[confidence intervals]] and, conversely, confidence intervals can be used to derive hypothesis tests. 

The intuition is straightforward: A hypothesis test of a point null tests whether a parameter $\theta^*$ is equal to a particular value $\theta_0$. If we gather all $\theta_0$ such that the null is not rejected, then this is a confidence interval. Likewise, if we have a CI $C$, we can simply reject the null $H_0: \theta^*=\theta_0$ if $\theta_0\notin C$.

This duality also holds for [[confidence sequences]], see eg my notes [here](https://benchugg.com/research_notes/sequential_testing_duality/). 

