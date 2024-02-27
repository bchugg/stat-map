Intuitively, a stopping time is simply a random variable that determines when to stop a random process. Naturally, the decision to stop the process should be based on only information until that time, not any future information. 

Mathematically, a stopping time $\tau$ is a random variable on a probability space $(\Omega,\cF,P)$ with filtration $\{cF_t\}$ such that for all $t$, the event is $\{t\leq t\}$ is $\cF_{t}$ measurable. Eg suppose you have a stochastic process $(X_t)$ and $\cF_t = \sigma(X_1,\dots,X_t)$. Then the decision to stop the process at time $t$ should be based only on $X_1,\dots,X_t$, not on $X_j$ for any $j>t$. 

