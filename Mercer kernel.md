A Mercer Kernel on a space $\calX$ is a symmetric function $K:\calX\times\calX\to\Re$ which is symmetric and positive semi-definite. That is, $K(x,y) = K(y,x)$ for all $x$ and $y$ and 
$$

\int\int K(x,y)f(x)f(y)p(x)p(y)dxdy\geq 0,

$$
for all $f:\calX\to\Re$, where $p$ is a probability measure on $\calX$. This means that $K$ is positive semi-definite. In a discrete space this reduces to the usual definition: $x^t K x\geq 0$ for all $x$. 

Mercer kernels can be used to construct an [[RKHS]] (indeed, each $K$ uniquely defines an RKHS and each RKHS is defined some $K$) and are therefore a major feature of [[RKHS regression]]. They are also used in [[nonparametric density estimation]]. 

Note that Mercer Kernels are distinct from smoothing kernels, which are used in [[kernel regression]], for instance. 

## $L_2$ basis 

If the Kernel obeys $\sup_{x,y} K(x,y)$ then we can find a series of orthonormal functions $\{\psi_i\}$ such that
$$
\int K(x,y)\psi_i(x)dx = \lambda_i\psi_i(y),
$$
for some $\lambda_i$. This impliest that $K(x,y) = \sum_{i}\lambda_i \psi_i(x)\psi_i(y)$ where we can order $\lambda_1\geq \lambda_2\geq \dots$. 


