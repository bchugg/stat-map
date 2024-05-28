
A list of exponential inequalities. These can be used to give [[concentration inequalities]] and also immediately yield [[e-value|e-values]]. They can also be used to construct  [[supermartingale|supermartingales]] and [[sub-psi process|sub-psi processes]]. 

Throughout, let $X$ be a random variable with mean $\mu$. Set $\overline{X} = X-\mu$.

| Name                   | Condition                                       | Bound                                                                                                                                                    |
| ---------------------- | ----------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Hoeffding              | $X\in [a,b]$                                    | $\forall \lambda\in\Re, \quad \E\exp\{\lambda \Xbar - \frac{\lambda^2}{8}(b-a)^2\}\leq 1$                                                                |
| Bernstein              | $\vert\Xbar\vert\leq c$                         | $\forall\lambda\in\Re\quad \E\exp\{\lambda \Xbar - \lambda^2\sigma^2\left(\frac{e^{\lambda c} - 1 - \lambda c}{(\lambda c)^2}\right)\}\leq 1$            |
| Self-bounding          | MGF exists                                      | $\forall \lambda\in\Re\quad \E \exp\{\lambda X - \log \E \exp(\lambda X)\}= 1$                                                                           |
| Bennett                | $\vert X \vert \leq H$ $\E[X^2]\leq v^2<\infty$ | $\forall\lambda\in (0,\frac{1}{v})\quad \E\exp\{-\lambda\Xbar - \frac{\mu^2}{H^2}(e^{\lambda H} - \lambda H -1)\}\leq 1$                                 |
| One-sided Bernstein I  | $X \leq H$ and $\E[X^2]<\infty$                 | $\forall \vert\lambda \vert\leq \frac{1}{2H}\quad \E\exp\{\lambda \Xbar - (e-2)\lambda^2\Var(X)\}\leq 1$                                                 |
| One-sided Bernstein II | $X\geq 0$ and $\E[X^2]<\infty$                  | $\forall \lambda>0 \quad \E\exp\{-\lambda\Xbar - \lambda^2\E[X^2]/2\}\leq 1$                                                                             |
| Delyon                 | $\E[X^2] < \infty$                              | $\forall \lambda\in \Re\quad \E[\exp\{\lambda\Xbar - \frac{\lambda^2}{6}(\Xbar^2 - 2\E[\Xbar^2])\}]\leq 1$                                               |
| Fan                    | $X\geq -1$, $\E[X]\leq 0$                       | $\forall \lambda\in[0,1)\quad \E\exp\{\lambda X + X^2(\log(1 - \lambda) + \lambda)\}\leq 1$                                                              |
| de la Pena             | $X-\mu$ is symmetric                            | $\forall\lambda\in\Re \quad \E\exp\{\lambda (X-\mu) - \frac{\lambda^2}{2}(X - \mu)^2\}\leq 1$                                                            |
| Catoni                 | $\E[\vert X\vert^p]<\infty, p>1$                | $\forall\lambda>0\quad \E\exp\{\phi_p(\lambda X) - \frac{\lambda^p}{p}\E[\vert X\vert^p]\} \leq 1$ where $\phi_p(x) \leq \log(1 + x + \vert x\vert^p/p)$ |
