A specific approach to [[nonparametric density estimation]], which can be viewed as a kind of "smoothed out" histogram. Let $K$ be a smoothing Kernel, i.e., $\int K(x)dx=1$, $\int x K(x)dx=0$ and $\int x^2 K(x)dx>0$. That is, $K$ enduces a distribution on the space $\cX$ which is symmetric. 

Our estimate for $p(x)$ is 
$$\wh{p}(x) = \frac{1}{n}\sum_{i=1}^n \frac{1}{h^d}K\bigg(\frac{x-X_i}{h}\bigg).$$
The parameter $h$ is called the bandwidth. We can generalize the above to allow for positive definite bandwidth matrices $H$ and write 
$$\wh{p}(x) = \sum_{i=1}^n K_H(x-X_i),$$
where $K_H(z) = |H|^{-1/2}K(H^{-1/2}z)$.  Taking $H=h^2I$ recover the previous formula. 

