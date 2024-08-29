
We assume the model $y = \beta^t X + \eps$, where we make various different assumptions on $\eps$. 

Given $X_1,\dots,X_n$, introduce the _design matrix_ $\bb{X}$ which rows correspond to $X_1,\dots,X_n$. Common practice is to add a 1 to each vector $X_i$ so that the first column of $\bb{X}$ is all 1s, which enables us to model non-zero offsets (i.e., $y = \beta_0 + \beta^t X+\eps$).    

A common loss is to minimize the "residual sum-of-squares (RSS)", which is the $\ell_2$ distance between our predictions ($\wh{y} = \wh{\beta}^t X$ ) and the true values $y$, i.e.,
$$
\min_{\beta} = \norm{Y - \bb{X}\beta}_2^2.
$$
The resulting $\wh{\beta}$ is the least squares estimate. 

Once you've ft a model, you should run [[linear regression diagnostics]]. 

