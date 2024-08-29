Let $h: \calX\to \{1,\dots,K\}$ denote a classifier on $\calX$.  Nonparametric classification is concerned with estimating $h$ without making parametric assumptions on it's form. 

The optimal ominiscient classifier is the Bayes classifier, given by 
$$

h^*(x) = \arg\max_k p(y=k|x),

$$
and it is typically against this standard that we judge our solutions. 

We can use [[nonparametric density estimation]] methods for this setting. By Bayes rule, 
$$

p(y=k|x) \propto p(x|y=k)p(y=k).

$$
The term $p(x|y=k)$ can be estimated using nonparametric regression (simply throw out everything that did not have label $k$), and the term $p(y=k)$ can be estimated by simple looking at the fraction of training data with the label $k$. 

Suppose $h:\calX\to\{0,1\}$ is just a binary classifier. Then the Bayes optimal classifier is 
$$

h^*(x) = \ind(p(y=1|x) > 1/2).

$$
Since $p(y=1|x) = \E[Y | X=x]$, we can thus approximate $h^*$ by using [[nonparametric regression]] to estimate $m(x) = \E[Y|X=x]$ with $\wh{x}$ and defining
$$

\wh{h}(x) = \ind(\wh{m}(x) > 1/2).

$$




