Procedure to achieve [[FDR control]]. Each hypothesis $H_i$ has a realized p-value $p_i$. If we reject all hypotheses with the smallest $k^*$ p-values, where $$

k^* = \max\bigg\{k: \frac{Kp_{(k)}}{k}\leq \alpha\bigg\}.

$$Then $$

\E[F_D/|D|] \leq \frac{\ell_K K_0}{K}\alpha,

$$where $K_0$ is the number of true null hypothesis and $\ell_K = \sum_k 1/k$. If the p-values satisfy [[PRDS]], then we can get rid of the $\ell_K$: $\E[F_D/|D|]\leq \alpha K_0/K$. 


