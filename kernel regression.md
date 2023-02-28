
Let $K:\Re \to \Re$ be a 1-d _smoothing kernel_ (distinct from a [[Mercer kernel]]) i.e., 
$$\int K(x)dx =1, \qquad \int xK(x)dx=0,\qquad \int x^2K(x)dx>0$$
So $K$ is essentially a well-behaved single dimensional probability distribution. Kernel regression is characterized by the Kernel function and a parameter $h$ called the bandwidth.  The estimated regression function is 
$$\widehat{m}(x) = \frac{\sum_{i=1}^n Y_i K_h(||x - X_i||)}{\sum_i K_h(||x - X_i||)},$$
where $K_h(z) = K(z/h)$. Kernel regression can therefore be considered a kind of "smoothed" [[knn]] regression, in which our prediction is the average of nearby points. Here, the definition "nearby" is given by the Kernel function and the bandwidth $h$: Larger values of $h$ lead to more dependence on nearby points and less influence of points further away. Gaussian kernels are a common choice. 

Kernel regression is a special case of [[local polynomial regression]] (in turn a special case of [[linear smoothers]]). 



## Properties 

Kernel estimators were once of the first [[nonparametric regression]] estimators shown to be universally consistent, meaning that 
$$\E[||\widehat{m} - m||] \to 0$$
as the sample size goes to infinity. The only assumption required on the true regression function, $m$ is that $\E[Y^2]<\infty$ where $Y=m(X) + \eps$.  

If we take the bandwidth $h$ to be $\asymp n^{-1/(4+d)}$, then the risk of kernel regression is $n^{-4(4+d)}$ (assuming the distribution generating $X$ has a density).  