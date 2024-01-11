
# Checking residuals 

The residuals are the errors between the predicted values and the true values, i.e., 
$$\wh{\eps} = Y - \wh{Y}.$$
Under least squares, $\wh{Y} = \bb{X}\wh{\beta} = \bb{H}Y$, so $\E[\wh{\eps}|\bb{X}] = 0$ and $\Var[\wh{\eps}|\bb{X}] = \sigma^2 (I - \bb{H})$ if $Var(\eps) = \sigma^2$ (the variance of the errors). So we should plot the residuals against any combination of the predictors (or the fitted values) and the means should be roughly zero (but the variance need not be constant). 

If the residuals do not have a constant mean or display significant curvature, it is suggestive that the model may be misspecified. 

# Curvature 

