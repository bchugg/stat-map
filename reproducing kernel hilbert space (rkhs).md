A RKHS is a [[Hilbert space]] endowed with more structure that makes it amenable to statistical learning. Specifically, it is defined by a [[Mercer kernel]] $K(\cdot,\cdot)$. 

The RKHS consists of functions $f$ that can be written as linear combinations of the Kernel, i.e., 
$$\cH_0 = \bigg\{f: \exists x_1,\dots,x_k, f(x) = \sum_i \alpha_k K(x_i,x)\bigg\},$$
Write $K_{x_i}(\cdot)$ for $K(x_i,\cdot)$. The inner product is defined as 
$$\la f,g\ra = \sum_{i,j} \alpha_i\beta_j K(x_i,y_j),$$
if $f = \sum_i \alpha_i K_{x_i}$ and $g = \sum_i \beta_i K_{y_i}$. This defines the norm 
$$||f||_K = \sqrt{\la f,f\ra} = \sqrt{\alpha^T \bK\alpha},$$
where $\bK_{i,j} = K(x_i,x_j)$. To rigorously define the RKHS, we complete $\cH_0$ with respect to $||\cdot||_K$, i.e., we ensure it contains its limit points. This is then a well-defined Hilbert space. 

RKHSs are highly useful for [[nonparametric regression]] (see [[rkhs regression]] specifically) via the [[representer theorem]], which states that the regularized empirical risk minimizer can be represented as a function in a RKHS. 