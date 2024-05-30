
These are [[concentration inequalities]] that concern functions of random variables that obey a bounded differences condition. Intuitively this means that if you change one argument, the function value doesn't change too much. 

The most famous example of a bounded difference inequality is McDiarmid's inequality, which is the following. Suppose $f:\Re^n \to \Re$ obeys 
$$\sup_{z_1,\dots,z_n,z_i'} |f(z_{-i}, z_i) - f(z_{-i},z_i')|\leq c_i,$$
for all $i$. (Here $z_{-i}$ is the vector of arguments that omits $z_i$). Then $$\Pr(|f(X^n) - \E[f(X^n)]|\geq \eps)\leq 2\exp\left(-\frac{2\eps^2}{\sum_{i=1}^n c_i^2}\right).$$
Note this is a generalization of the [[light-tailed scalar concentration#Hoeffding bound]]: If we take $f(x^n) = \frac{1}{n}\sum_{i=1}^n x_i$ then we recover it. 