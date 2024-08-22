$$
\newcommand{\cX}{\mathcal{X}}
\newcommand{\Re}{\mathbb{R}}
$$
Wasserstein distances are a class of distance between distributions $P$ and $Q$ over some common space $\cX$. They come from considering the [[optimal transport]] cost when the cost function is a metric. In particular, if $d:\cX\times\cX\to\Re$ is a metric, set 
$$ W_p(\mu,\nu) = \bigg(\min_{\pi\in \Gamma(\mu,\nu)} \E_{X,Y\sim \pi} [d(X,Y)^p]\bigg)^{1/p},$$
where $\Gamma(\mu,\nu)$ is the set of joint distributions on $\cX\times\cX$ who marginals are $\mu$ and $\nu$, that is 
$$\Gamma(\mu,\nu) = \bigg\{\pi: \int \pi(x,y)dy = \mu(x),\;\int \pi(x,y)dx = \nu(y)\bigg\}.$$
Wasserstein distances are an optimal class of distances because they take advantage of the underlying geometry of the space $\cX$ (as enduced by $d$). This is contradistinction to, e.g., the [[KL divergence]] and the [[total variation distance]]. 
