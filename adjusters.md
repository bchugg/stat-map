---
lastmod: 2026-05-26
created: 2026-05-25
---
In [[game-theoretic statistics]] we often have an [[e-process]] $(E_t)$ that we're using to collect [[evidence against the null]]. We might want to ensure that this process never decreases. But most e-processes are not nondecreasing. And while it's tempting to just consider the running maximum of an e-process,  $E_t^* = \max_{s\leq t} E_s$ the result is not an e-process. In fact, the running maximum can have expectation tending to infinity under the null; see [Appendix D in this paper](https://arxiv.org/pdf/2402.09698) for an example. 

_Adjusters_ solve this problem. They take the running maximum $(E_t^*)$ and shift it so that the result is an e-process. Formally, an adjuster $A$ is a function $A:[1,\infty]\to [0,\infty]$ such that 
$$ 
\int_1^\infty \frac{A(y)}{y^2}\d y\leq 1.
$$
They relate to e-processes as follows: For any test [[supermartingale]] $(X_t)$ (meaning a supermartingale with initial value 1) there exists a test supermartingale $(Y_t)$ such that $A(X_t^*)\leq Y_t$ almost surely, where $X_t^* = \max_{0\leq s\leq t} X_s$. This together with the optional stopping theorem imply that $A(X_t^*)$ is an e-process. Using results which upper bound e-processes in terms of supermartingales, the same conclusion holds if take $(X_t)$ to be an e-process. 

Adjusters originated [here](https://arxiv.org/pdf/1108.4113), [here](https://arxiv.org/pdf/1005.1811), and [here](https://arxiv.org/pdf/0912.4269). Examples are $A(y) = \kappa y^{1-\kappa}$ for any $\kappa\in(0,1)$, $A(y) = \sqrt{y} -1$, 
$$A(y) = \int_0^1 \kappa y^{1-\kappa} \d y = \frac{y-1 - \log(y)}{\log^2(y)},$$
with $A(y) = 1/2$, or 
$$ A(y) = \frac{y^2\log 2}{(1 + y)\log^2(1 + y)}.$$
See [here](https://arxiv.org/pdf/2402.09698) for credit for all of these, and an overview. 

One way to think about the definition of an adjuster is as follows. Suppose we define the function $h(w) = A(e^w)/e^w$. By a change of variables, write 
$$ 1 \geq \int_1^\infty \frac{A(y)}{y^2}\d y = \int_0^\infty h(t) \d t.$$
Now, $A(y) = yh(\log y)$, so the adjuster can be seen as adjusting $y$ downwards by a multiplicative factor of $h(\log y)$. And this function $h$ must act like a density on the log scale of $y$. Different adjusters will spread out this mass differently. Moreover, _admissible_ adjusters are precisely those such that $\int_1^\infty A(y)/y^2 \d y =1$, implying that $\int h(t) \d t = 1$. So as long as the adjuster spreads all its mass out, it is admissible. 
# Reading 
- [Test martingales, Bayes factors, and p-values](https://arxiv.org/pdf/0912.4269) 
- [Combining evidence across filtrations](https://arxiv.org/pdf/2402.09698)