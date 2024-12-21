---
created: 2024-08-29
lastmod: 2024-12-16
---

OLS for [[linear regression]] makes the assumption that the variance for all covariates is the same. If this is not the case we use weighted least squares. In particular, the model is 
$$
\bf{Y} = \bs{\beta}^t\bf{X} + \bs{\eps},
$$
where $\bs{\eps} = \sigma^2 \bs{W}^{-1}$ and $\bs{W}$ is a diagonal matrix with $w_i$ on the diagonal and $\Var(Y | x=x_i) = \Var(\eps_i) = \sigma^2/w_i$.  We solve for an estimate of $\bs{\beta}$ by minimizing the "weighted residual sum of squares", which as we'd suspect, is 
$$
(\bs{Y} - \wh{\bs{\beta}}^t \bs{X})^t\bs{W}(\bs{Y} - \wh{\bs{\beta}}^t \bs{X}), 
$$
which generalizes the usual residual sum of squares, in which $\bs{W} = \bs{I}$. The solution is $\wh{\bs{\beta}} = (\bs{X}^t \bs{W}\bs{X})^{-1} \bs{X} \bs{W} \bs{Y}$.  
