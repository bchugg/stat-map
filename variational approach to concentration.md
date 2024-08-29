
A technique for [[multivariate concentration]]. Let $(S_t)$ be some stochastic process, say in $\Re^d$. For instance, $S_n = \sum_{i=1}^n X_i$ for multivariate observations $X_i\in\Re^d$. We are aiming to generate a high probability bound on 
$$

\norm{S_n} = \sup_{v:\norm{v}=1} \la v,S_n\ra.

$$
The idea is to use a [[PAC-Bayes]] approach (which is itself based on variational inequalities, hence the name), in order to simultaneously bound $\la v,S_t\ra$ in each direction $v$. Recall that a PAC-Bayes bound has the form 
$$

\Pr( \forall \rho \in \Mspace{\Theta}: \text{Something holds}) \geq 1-\delta.

$$
That is, a PAC-Bayes bound provides a high probability bound _simultaneously_ over all posteriors. The variational approach to concentration translates this into a high probability bound over all directions. 

This approach was pioneered by Catoni and Giulini (here and here), and has now been used by a few authors—myself included—to prove bounds in a variety of settings: 
- [Zhivotovskiy](https://arxiv.org/pdf/2108.08198) for bounding the singular values of random matrices 
- [Nakakita et al.](https://ui.adsabs.harvard.edu/abs/2022arXiv221009756N/abstract) for bounding the mean of high-dimensional random matrices under heavy-tails; 
- [Giulini](https://arxiv.org/pdf/1511.06259) for estimating the Gram operator in [[Hilbert space|Hilbert spaces]]. 
- [Myself and others](https://arxiv.org/abs/2311.08168) for estimating the mean of random vectors. 

Recall a very general [[PAC-Bayes]] inequality: 
![[PAC-Bayes#Master theorem|PAC-Bayes:Master theorem]]

To see how this works, let's consider two use cases. 

# Example 1: Sub-Gaussian random vectors 

This comes from our paper on [[time-uniform confidence spheres]]. Consider $n$ iid copies $X_1,\dots,X_n$ of a $\Sigma$-sub-Gaussian random vector $X\in\Re^d$ (see [[sub-Gaussian distributions]]). That is, 
$$

\E\exp(\lambda \la \theta, X\ra) \leq \exp\left(\frac{\lambda^2}{2}\la\theta,\Sigma\theta\ra\right),

$$
for all $\lambda\in\Re$ and $\theta\in\Re^d$. This implies that 
$$

N(\theta) = \exp\left\{\lambda\sum_{i\leq n}\la \theta, X_i\ra - \frac{n\lambda^2}{2}\la\theta,\Sigma\theta\ra\right\},

$$
has expectation at most 1 (i.e., it is an [[e-value]]). Let $\nu$ be a Gaussian with mean 0 and covariance $\beta^{-1}I$ for some $\beta>0$. Consider the family of distributions $\{\rho_u:\norm{u}=1\}$ where $\rho_u$ is a Gaussian with mean $u$ and covariance $\beta^{-1}I$. Then the [[KL divergence]] between $\rho_u$ and $\nu$ is $\kl(\rho_u\|\nu) = \beta/2$. Using the master theorem above, we obtain that, with probability $1-\delta$, _simultaneously for all distributions $\rho$_, 
$$

\lambda\sum_{i\leq n} \E_\rho \la\theta, X_i\ra \leq \frac{n\lambda^2}{2}\E_\rho \la \theta, \Sigma\theta\ra + \frac{\beta}{2} + \log(1/\delta).

$$
Now, for $\rho=\rho_u$, $\E_\rho \la \theta, X_i\ra = \la u,X_i\ra$ and
$$
\E_\rho \la \theta, \Sigma\theta\ra = \la u,\Sigma u\ra + \beta^{-1}\Tr(\Sigma) \leq \norm{\Sigma} + \beta^{-1}\Tr(\Sigma),
$$
using basic properties of the expectation of quadratic forms under Gaussian distributions (see eg [here](https://statproofbook.github.io/P/mean-qf.html)), and definition of the [[operator norm]] as $\norm{A} = \sup_{u,v:\norm{u}=\norm{v}=1}\la u,\Sigma v \ra$. Since this holds simultaneously for all $\rho_u$, we obtain that, with probability $1-\delta$,
$$

\sup_u \lambda \sum_{i\leq n} \la u,X_i\ra \leq \frac{n\lambda^2}{2}(\norm{\Sigma} + \beta^{-1}\Tr(\Sigma)) + \frac{\beta}{2} + \log(1/\delta).

$$
The left hand side is equal to $\lambda \norm{\sum_{i\leq n}X_i}$, which gives us our concentration result. One can then optimize $\lambda$ using some calculus. 

# Example 2: Random matrices with finite Orlicz-norm

This example is adapted from [Zhivotovskiy (2024)](https://arxiv.org/pdf/2108.08198). Let $M_1,\dots,M_n$ be iid copies of a zero-mean random matrix $M$ with finite sub-exponential [[Orlicz norm]], in the sense that, for some $C>0$, 
$$

\norm{\la \theta, M\phi\ra}_{\psi_1} \leq C \la\theta, \Sigma\phi\ra,

$$
for all $\theta, \phi\in\Re^d$ where $Q = \E M$. 

Here we highlight the main ingredients that are used in Zhivotovskiy's results. For the details, see his paper or [my blog post](https://benchugg.com/research_notes/variational_approach_to_concentration/). 

We take our parameter space in the master theorem above to be $\Theta = \Re^d\times \Re^d$. Let $\nu$ again be Gaussian with mean 0 and covariance $\beta^{-1}\Sigma$ and let $\mu_u$ be a _truncated_ Gaussian mean $u$, covariance $\beta^{-1}\Sigma$ and radius $r$. For a vector $u\in \Sigma^{1/2}\mathbb{S}^{d-1}$, the KL-divergence between a truncated normal $\mu_u$ and $\nu$ is $\log(1/Z) + \beta/2$, where $Z = \Pr(\norm{\theta - u}\leq r)$ where $\theta\sim \rho_{u}$. Equivalently, $Z=\Pr(\norm{Y}\leq r)$ where $Y$ is a normal with mean $0$ and covariance $\beta^{-1}\Sigma$. Hence $1 - Z = \Pr(\norm{Y}>r)\leq \E\norm{Y}^2/r^2 = \beta^{-1}\Tr(\Sigma)/r^2$. Thus, taking $r = \sqrt{2 \beta^{-1}\Tr(\Sigma)}$ yields $Z\geq 1/2$, and we obtain 
$$

\begin{align}
\kl(\mu_u\|\nu) \leq \log(2) + \frac{\beta}{2}. 
\end{align}

$$
Now it remains to construct a relevant quantity to use in the PAC-Bayes theorem. Consider 
$$

N(\theta,\phi) = \exp\left\{\lambda\sum_{i\leq n}\la\theta, \Sigma^{-1/2}M_i\Sigma^{-1/2}\phi\ra - n\log\E\exp(\lambda\la \theta, \Sigma^{-1/2}M\Sigma^{-1/2}\phi\ra)\right\},

$$
where the expectation is over $M$. It's easy to see this has expectation at most 1 (it can be written as the product of terms each with expectation exactly one). Apply the master theorem with the product distribution $\mu_u\times \mu_v$ for $u,v$ in the unit sphere. Then, to bound the right hand side of the process, use one of the [[exponential inequalities]]. In particular, for a random variable $Y$, 
$$

\E[\exp(\lambda (Y - \E Y))]\leq \exp(4\lambda^2\norm{Y-\E Y}_{\psi_1}),\quad \forall |\lambda| \leq \frac{1}{2\norm{Y-\E Y}_{\psi_1}}.

$$

A bunch of algebra then gives the result. 

- 