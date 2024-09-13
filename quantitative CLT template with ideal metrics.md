Let $X_1,\dots,X_n$ be independent with mean 0 and variance $\Var(X_i) = \sigma_i^2$. Let $\rho_s$ be an ideal metric of order $s$ (see [[distributional distance]]) and set $\Sigma_n^2 = \sum_{i\leq n} \sigma_i^2$.  Then, 
$$ 
\begin{align}
\rho_s\left(\frac{1}{\Sigma_n}\sum_{i}X_i, N(0,1)\right)  = \rho_s\left(\frac{1}{\Sigma_n}\sum_i X_i, \frac{1}{\Sigma_n}\sum_i N(0,\sigma_i^2)\right),
\end{align}
$$
and the definition of an ideal metric gives 
$$
\rho_s\left(\frac{1}{\Sigma_n}\sum_i X_i, \frac{1}{\Sigma_n}\sum_i N(0,\sigma_i^2)\right) \leq \sum_{i\leq n}\rho_s\left(\frac{X_i}{\Sigma_n}, \frac{N(0,\sigma_i^2)}{\Sigma_n}\right) \leq \frac{1}{\Sigma_n^s}\sum_{i\leq n}\rho_s\left(X_i, N(0,\sigma_i^2)\right).
$$
Hence, if one shows the right hand side approaches 0 and converge to 0 of the ideal metric implies convergence in distribution (eg with [[KS distance]]) you obtain a [[central limit theorems|CLT]]. 