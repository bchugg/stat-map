---
lastmod: 2024-12-31
created: 2024-12-31
---

There are three kinds of $\alpha$-divergences: the generic version, the Renyi $\alpha$-divergence and the Tsallis $\alpha$-divergence. 

If $\d\rho$ and $\d\nu$ are the densities of $\rho$ and $\nu$ respectively, the generic $\alpha$-divergence is defined as 
$$
D_\alpha(\rho\|\nu) = \frac{1}{\alpha(\alpha-1)}\left(\int\d \rho^\alpha(x) \d\nu^{1-\alpha}(x)\d x -1 \right),
$$
for any $\alpha \neq 0,1$. This is a special case of an [[f-divergence]], thus admits the same variational inequality. This also means it's a convex [[distributional distance]]. It convergences to the [[KL divergence]] as $\alpha\to 1$, the reverse KL as $\alpha\to 0$ and to the [[Hellinger distance]] at $\alpha = 0.5$. For $\alpha=2$ it's the [[chi-squared divergence]]. 

## Renyi $\alpha$-divergence
The Renyi $\alpha$-divergence is 
$$
R_\alpha(\rho\|\nu) = \frac{1}{\alpha-1} \log \int \d\rho^\alpha(x) \d\nu^{1-\alpha}(x) \d x.
$$
This obeys: $\alpha < 0 \Rightarrow R_\alpha \leq 0$, $\alpha = 0 \Rightarrow R_\alpha = 0$, $\alpha > 0\Rightarrow R_\alpha \geq 0$, and $\alpha =1$ this converges to the [[KL divergence]]. The Renyi divergence admits the variational inequality 
$$
D_\alpha(\rho\|\nu) \geq \frac{\alpha}{\alpha-1} \log \E_\rho h(\theta) - \log \E_\nu h(\theta)^{\frac{\alpha}{\alpha-1}},
$$
for all measurable $h$ and $\alpha >0$, $\alpha\neq 1$. 

## Tsallis $\alpha$-divergence
The Tsallis divergence is 
$$
 T_\alpha (\rho) = \frac{1}{\alpha-1} \left(\int \d\rho^\alpha(x) \d\nu^{1-\alpha}(x)\d x -1\right).
$$
Like the Renyi-divergence, this obeys $\alpha < 0 \Rightarrow T_\alpha \leq 0$, $\alpha = 0 \Rightarrow T_\alpha = 0$, $\alpha > 0\Rightarrow T_\alpha \geq 0$. 
