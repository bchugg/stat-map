---
created: 2024-08-29
lastmod: 2024-09-02
---
The proof of the [[Neyman-Pearson lemma]] relies on finding some threshold $\kappa$ such that 
$P(\Lambda(X) \geq \kappa) = \alpha$ where $\Lambda$ is the likelihood ratio. If $P$ is continuous, then this is possible. But what if the distribution is discrete? In that case, we use randomization. 

We still use a variant of the [[likelihood-ratio test]], but it has the following form: 
$$
\phi(x) = \begin{cases}
1, & \Lambda(x) > \kappa, \\
\gamma, & \Lambda(x) = \kappa, \\
0, &\Lambda(x) < \kappa,
\end{cases}
$$
for some threshold $\kappa$ and where $\gamma$ is chosen such that $\phi$ has type-I error exactly $\alpha$. Therefore, $\gamma$ solves $\E_Q[\phi(X)] = \sum_{x: \Lambda(x) > \kappa} q(x) + \sum_{x:\Lambda(x) = \kappa} \gamma = \alpha$. This might be considered a form of [[external randomization]]. 