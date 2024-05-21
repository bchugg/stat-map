

Let $X_1, X_2, \dots, X_n$ be independent random vectors in $\Re^d$ with mean $\mu$ such that $\norm{X_i}\leq c_i$ almost surely. Assume the norm $\norm{\cdot}$ is the $\ell_2$ norm. What sort of concentration inequalities exist for $S_n - \mu$, where $S_n = \frac{1}{n}\sum_{i\leq n}X_i$?

Remarkably, there exists a dimension-free Bernstein bound in this case. The method for generating the bound is quite unique as well. In particular, it works directly with the norm $\norm{S_n}$. This is different than several other established techniques (such as covering arguments and variational arguments) which attempt to simultaneously bound $S_n$ in each direction. 

First we form a martingale out of $S_n$. In particular, we consider its Doob decomposition: 
$$Z_t = \E[\norm{S_n}|\calF_{t}] - \E[\norm{S_n}].$$
By total expectation it's easy to see that  $\E[Z_t|\calF_{t-1}] = Z_{t-1}$, so $(Z_t)_{t\geq 0}$ is a martingale. Next we claim that it is a martingale with bounded increments. Set 
$$D_t = Z_t - Z_{t-1}.$$
We want to bound $|D_t|$. First, notice that 
$$\E[\norm{S_n - X_t}|\calF_{t}] - \E[\norm{S_n - X_{t}}|\calF_{t-1}] = 0,$$
since the only terms that remain in $S_n - X_t$ are either measurable with respect to both $\calF_t$ and $\calF_{t-1}$ or remain random. Therefore, 
$$
\begin{align}
|D_t| &= \left\vert \E[\norm{S_n}|\calF_t] - \E[\norm{S_n}|\calF_{t-1}]\right\vert \\
&=  \left\vert\E[\norm{S_n} - \norm{S_n - X_t}|\calF_t] - \E[\norm{S_n} - \norm{S_n - X_{t-1}}|\calF_{t-1}] \right\vert \\ 
&\leq \left\vert\E[\norm{S_n} - \norm{S_n - X_t}|\calF_t] \right\vert +  \left\vert\E[\norm{S_n} - \norm{S_n - X_{t}}|\calF_{t-1}] \right\vert \\ 
&= \left\vert\E[\norm{S_n} - \norm{S_n - X_t}|\calF_t] - \E[\norm{S_n} - \norm{S_n - X_{t}}|\calF_{t-1}] \right\vert \\ 
&\leq \E[\left\vert\norm{S_n} - \norm{S_n - X_t}\right\vert |\calF_t]  +  \E[\left\vert\norm{S_n} - \norm{S_n - X_{t}}\right\vert |\calF_{t-1}] \\ 
&\leq \E[\norm{X_t}|\calF_t] + \E[\norm{X_t}|\calF_{t-1}] \\ 
&= \norm{X_t} + \E[\norm{X_t}|\calF_{t-1}].
\end{align}
$$
Here, the first inequality is via the triangle inequality, the second by Jensen's inequality, and the third by the reverse triangle inequality. Using our assumption on the bounded of $X_t$, we have 
$$|D_t| \leq 2c_t.$$
What if we applied Azuma's inequality to this martingale? We have $Z_0=0$, so it gives 
$$\Pr(Z_n \geq \eps)\leq \exp\left(\frac{-\eps^2}{2\sum_{t\leq n}c_t^2 }\right).$$
Noting that $\E\norm{S_n}\leq \sqrt{\E\norm{S_n}^2} = \sqrt{\sum_{i\leq n}\E\norm{X_i}^2}$ and putting $V_n = \sum_{i\leq n} \E\norm{X_i}^2,$ we can rewrite the above bound as 
$$\Pr(\norm{S_n}\geq \sqrt{V_n} + \eps )\leq \exp\left(\frac{-\eps^2}{2\sum_{t\leq n}c_t^2 }\right).$$
In other words, with probability at least $1-\delta$, we have 
$$\norm{S_n} \leq \sqrt{V_n} + \sqrt{2\log(1/\delta)\sum_{i\leq n}c_i^2}.$$
Can we strengthen this bound? It turns out that we can. In fact, we can replace the term $\sum_{i\leq n}c_i^2$ with the term $V_n$ (or any upper bound thereof). Is this better than the current bound? Yes.
Notice that since $\norm{X_t}\leq c_t$ we have the trivial bound $\E\norm{X_t}^2 \leq c_t^2$. Therefore, if we have more information about the second moments of $X_t$, say they are upper bounded by $\sigma_t^2$, then we may assume that $\sigma_t^2\leq c_t^2$. 

To make this replacement, we need to modify the Azuma-Hoeffding inequality. 

# A martingale-variance inequality 

Suppose the increments of a martingale $(Z_t)$ are bounded and, in addition, 
$$\E [|Z_t - Z_{t-1}|^2|\calF_{t-1}]\leq \sigma_t^2.$$
Let $V_n = \sum_{i\leq n}\sigma_i^2$. Then we can modify Azuma's bound above to read: 
$$\Pr(Z_n \geq Z_0 + \eps) \leq \exp\left(\frac{-\eps^2}{4V}\right),$$
as long as $\eps \leq 2V/\max_i c_i$.  

To see this, start with the basic Chernoff method. For any $\lambda>0$, 
$$
\begin{align}
\Pr(Z_n \geq Z_0 + \eps ) &= \Pr(e^{\lambda Z_n} \geq e^{\lambda (Z_0 + \eps)}) \leq e^{-\lambda (Z_0 + \eps)}\E[e^{\lambda Z_n}].
\end{align}
$$
Then, write 
$$
\begin{align}
\E[e^{\lambda Z_n}] &= \E[\E[e^{\lambda (Z_{n-1} + D_n)}|\calF_{n-1}]] \\ 
& = \E[e^{\lambda Z_{n-1}} \E[e^{\lambda D_n}|\calF_{n-1}]]. 
\end{align}
$$
Recall that for $|x|\leq 1$ we have the inequality $e^x \leq 1 + x + x^2$. Therefore, if $|\lambda D_n| \leq 1$ we have 
$$
\begin{align}
\E[e^{\lambda D_n}|\calF_{n-1}] &\leq \E[1 + \lambda D_n + \lambda^2D_n^2 |\calF_{n-1}] \\
&= 1 + \lambda^2\E[D_n^2|\calF_{n-1}] \\
&\leq \exp(\lambda^2 \E[D_n^2|\calF_{n-1}]) \\ 
&\leq \exp(\lambda^2 \sigma_n^2),
\end{align}$$
where we've used that $1 + x \leq e^x$ and that $\E[D_n|\calF_{n-1}]=0$. Hence, 
$$\E[e^{\lambda Z_n}] \leq e^{\lambda^2 \sigma_n^2}\E[e^{\lambda Z_{n-1}}] \leq \dots \leq e^{\lambda Z_0}\prod_{i=1}^n e^{\lambda^2\sigma_i^2} = e^{\lambda Z_0 + \lambda^2V_n}.$$
Note the expectation has disappeared from $e^{\lambda Z_0}$ because $Z_0$ is assumed to be known. 
Putting this all together gives 
$$\Pr(Z_n \geq Z_0 + \eps) \leq e^{\lambda^2 V_n - \lambda\eps}.$$
Optimizing the value of $\lambda$ on the right hand side gives 
$$\lambda = \frac{\eps}{2V}.$$
Recall that we require that $\max_n \lambda |D_n|\leq 1$. This holds if $\eps \leq 2V / \max_t c_t$ since $|D_t|\leq c_t$ by assumption. This gives us the result. 

# The resulting Bernstein bound 







