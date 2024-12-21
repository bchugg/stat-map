---
created: 2024-08-29
lastmod: 2024-12-20
---

There's obviously a lot to say about linear regression, which is the workhorse of applied statistics. I don't want to say (type) most of it, quite frankly. But what kind of map would this be if it didn't at least have a small page on linear regression. If you're deeply interested in applied linear regression, perhaps you should go read [Applied Linear Regression](https://onlinelibrary.wiley.com/doi/book/10.1002/0471704091). 

Linear regression assumes the mean response is a linear function of the covariates: 
$$
\E[Y | x_1,\dots,x_k] = \bs{\beta}^t \bs{x},
$$
and we assume that $\Var(Y | x -= x_i)=\sigma^2$. (For non-constant variance use [[weighted least squares]])). We thus assume the model 
$$
 
\bs{Y} = \bs{\beta}^t \bs{X} + \bs{\eps},
$$
where the errors $\eps_i$ are assumed to be mean zero and capture the differences between the observed response and the expected response. (Add a constant column to $\bs{X}$ if it makes you happy.)

Typically one estimates $\bs{\beta}$ by minimizing the "residual sum-of-squares (RSS)", which is the $\ell_2$ distance between our predictions ($\wh{y} = \wh{\beta}^t X$ ) and the true values $y$, i.e.,
$$
\min_{\beta} = \norm{Y - \bb{X}\beta}_2^2.
$$
The resulting $\wh{\beta}$ is the (ordinary) least squares estimate. 

The main assumptions behind linear regression are: 
- linear relationship between response and covariates (surprise surprise)
- errors are independent and _homoscedastic_ (fancy way of saying they're the same for each covariate)
- covariates are non-colinear (if broken then your coefficients can be unstable and lose meaning, making statistics computed on them useless). 
- You'll often see people make the assumption that the errors are normally distributed. This isn't strictly necessary for actually fitting your model, but if you want to construct [[confidence intervals]] or perform any [[hypothesis testing]] on the coefficients, then you need this kind of assumption. 

Linear regression is, of course, a [[generalized linear model]] with a linear link function, 

In practice, once you've fit a model, you should run some diagnostic checks. This usually involves plotting the residuals (the differences between your model predictions and the labels) and ensuring they are roughly mean-zero and random. 

