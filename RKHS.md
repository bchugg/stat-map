---
created: 2024-08-29
lastmod: 2024-09-02
---

A Reproducing Kernel Hilbert Space (RKHS) is a [[Hilbert space]] endowed with more structure that makes it amenable to statistical learning. Specifically, it is defined by a [[Mercer kernel]] $K(\cdot,\cdot)$, and consists of functions $f$ that can be written as linear combinations of the Kernel, i.e., 
$$
\calH_0 = \bigg\{f: \exists x_1,\dots,x_k, f(x) = \sum_i \alpha_k K(x_i,x)\bigg\},
$$
Write $K_{x_i}(\cdot)$ for $K(x_i,\cdot)$. The inner product is defined as 
$$
\la f,g\ra = \sum_{i,j} \alpha_i\beta_j K(x_i,y_j),
$$
if $f = \sum_i \alpha_i K_{x_i}$ and $g = \sum_i \beta_i K_{y_i}$. This defines the norm 
$$
||f||_K = \sqrt{\la f,f\ra} = \sqrt{\alpha^T \bs{K}\alpha},
$$
where $\bs{K}_{i,j} = K(x_i,x_j)$. To rigorously define the RKHS, we complete $\calH_0$ with respect to $||\cdot||_K$, i.e., we ensure it contains its limit points. This is then a well-defined Hilbert space. We label this $\calH_K$. 

RKHSs are highly useful for [[nonparametric regression]] (see [[RKHS regression]] specifically) via the [[representer theorem]], which states that the regularized empirical risk minimizer can be represented as a function in a RKHS. 

## Representation in $L_2$ basis 

Using the $L_2$ basis representation of the [[Mercer kernel]], we can also write functions in $\calH_K$ with respect to those orthonormal functions as 
$$
f(x) = \sum_i\alpha_i K(x_i,x) = \sum_i a_i \psi_i(x),
$$
for some $\alpha_i$ and $a_i$ (probably distinct). If $g(x) = \sum_i b_i \psi_i(x)$, then we can show that 
show that
$$
 \la f,g\ra \sum_i \frac{\alpha_i\beta_i}{\lambda_i},
$$
where $\lambda_i$ are the eigenvalues: $K(x,y) = \sum_i \lambda_i \psi_i(x)\psi_i(y)$. 



