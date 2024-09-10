> [!Definition]
> A distribution $P$ is infinitely divisible if for all $n$, there exist $n$ iid random variables $X_1,\dots,X_n$ such that $\sum_i X_i \equald X\sim P$. Equivalently, if $P$ has [[characteristic function]] $\varphi$, there exists a characteristic function $\phi$ such that $\varphi(t) = \phi^n(t)$. 

Under the condition of uniform asymptotic negligibility (which basically says that the contribution of any individual element of the sum is small) infinitely divisible distributions are the set of all distributions which are the limiting distributions for [[central limit theorems]]. (This is pretty intuitive; its the set of distributions that can be represented by sums). For instance, $N(\mu,\sigma^2)$ be can be written as the sum of $n$ independent $N(\mu/n,\sigma^2/n)$ random variables. 

Petrov proved that a distribution $P$ is infinitely divisible iff its characteristic function has the following form: 
$$
\E_P[\exp(itX)] = \exp\left(i\gamma t + \int_\Re \left(e^{itx} - 1 - \frac{itx}{1 + x^2}\right)\frac{1+x^2}{x^2}\d G(x)\right).
$$