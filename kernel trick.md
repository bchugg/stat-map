Let $K$ be a [[Mercer kernel]] such that $\sup_{x,y}K(x,y)<\infty$. Then there exists an orthonormal basis for $L_2(\calX)$, $\{\psi_i\}$ and eigenvalues $\lambda_1\geq \lambda_2 \geq \dots$ such that  
$$

K(x,y) = \sum_i \lambda_i \psi_i(x)\psi_i(y).

$$
The Kernel is thus "ordering" the basis, in the sense that it assigns higher weight to $\psi_1$ than $\psi_2$ and so on. If we gather the first $r$ eigenfunctions, then we can think of this as [[dimensionality reduction]].  

However, we can do something better by appealing to the kernel trick. For each $x\in\cX$, define the map 
$$

\Phi(x) = (\sqrt{\lambda_i}\psi_i(x))_{i=1}^\infty,

$$
which is an infinite dimensional feature map for $x$. Then, 
$$

\la \Phi(x),\Phi(y)\ra = \sum_i \lambda_i \psi_i(x)\psi_i(y) = K(x,y).

$$
That is, the Kernel embeds the information about these infinite dimensional sequences. Thus, if we can structure our computation to only require computations of $K(x,y)$, then we can essentially use the entire feature maps (sans dimensionality reduction), which having to represent them explicitly. This is known as the Kernel trick. 