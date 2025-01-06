---
created: 2024-08-29
lastmod: 2025-01-05
---

Exactly what it sounds like. Worth a note just because it keeps coming up. 

Actually, you know what, the bias-variance decomposition is possibly worth discussing. Given a predictor $\wh{f}:\calX\to\Re$ and a target $f^* :\calX\to\Re$, the squared error can be decomposed as 
$$
\E[(\wh{f}(X) - f^*(X))^2] = \text{Bias}^2(\wh{f}) + \Var(\wh{f}) + \sigma^2,
$$
where $\text{Bias}(\wh{f}) = \E[\wh{f}(X) - f^*(X)]$, $\Var(\wh{f}) = \E[(\wh{f}(X) - \E[\wh{f}(X)])^2]$ and $\sigma^2$ is the irreducible noise in the data (i.e., given $X$, outcomes are drawn as  $Y = f^*(X) +\eps$ where $\eps$ has variance $\sigma^2$. 

As you increase model complexity, bias typically decreases and variance increases. This is known as the bias-variance tradeoff. So to minimize squared-error, you want to find a appropriate compromise between the two. 