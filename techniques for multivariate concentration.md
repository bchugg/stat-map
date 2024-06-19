
Suppose we have a stochastic process $(S_t)$ evolving in some space. What techniques are available for bounding $\norm{S_t}$? If $S_t\in\Re$, then we usually argue about $S_t$ and $- S_t$ and take a union bound to get a bound on $|S_t|$ (see [[light-tailed scalar concentration]] and [[heavy-tailed scalar concentration]]). However, in higher-dimensional spaces (in $\Re^d$, $d\geq 2$, say) a union bound doesn't suffice: there are infinitely many directions one has to worry about. 

Here we explore some techniques to deal with this problem. 

# Working directly with the norm 

The idea is to form a Doob martingale from the increments of the process and then apply well-known martingale bounds.  Set $$Z_t = \E[\norm{S_n} | \calF_t] - \E[\norm{S_n}].$$So $(Z_t)$ is a martingale with $Z_0=0$. Let $$D_t = Z_t - Z_{t-1},$$be the increments of the process. Various [[martingale concentration]] bounds are stated as conditions on the increments of the process. For instance: 
- If $S_t$ is bounded for each $t$, then we can use the Azuma-Hoeffding inequality ([[martingale concentration#Azuma-Hoeffding inequality]]) 
- If a bound on the variance of $D_t$ is known, then we can use the equivalent of a Bernstein inequality ([[martingale concentration#Variance bound]]). 



# Covering arguments 

The general approach is as follows. Let $C_\eps$ be an $\epsilon$-cover of $\ball^{d-1}$ (see [[covering and packing]]). Then 
$$\sup_{v\in \balld} \la v, S_n\ra \leq \sup_{v\in C_\eps}\la v,S_n\ra + \sup_{v\in \eps \balld} \la v,S_n\ra = \sup_{v\in C_\eps}\la v,S_n\ra + \eps \sup_{v\in \balld} \la v,S_n\ra,$$
so $$\sup_{v\in \balld}\la v,S_n\ra \leq \frac{1}{1-\eps} \sup_{v\in C_\eps}\la v,S_n\ra.$$From here, $C_\eps$ is a finite set, so we can apply well-known [[maximal inequalities]] over finite sets. For instance, if $S_n=X$ is sub-Gaussian, then [[light-tailed maximal inequalities]]   gives $$\E\sup_{v\in C_\eps} \la v,X\ra \leq \sqrt{2\Var(X) \log|C_\eps|} \leq \sqrt{2 \Var(X) d\log(3/\eps)},$$where we use an upper bound on the $\eps$-covering number of $\balld$. This gives $$\E \norm{S_n}\leq \frac{1}{1-\eps} \sqrt{2\Var(X) \log|C_\eps|}.$$We can then optimize over $\eps$ to get a final bound. The sub-Gaussian case usually takes $\eps = 1/2$ (e.g., Theorem 1.19 in [high-dimensional statistics](https://arxiv.org/abs/2310.19244) by Rigollet and Hutter). We can also get a high-probability bound by noticing that $$\Pr(\sup_{v\in \balld}\la v,S_n\ra\geq t) \leq \Pr\left(\frac{1}{1-\eps}\sup_{v\in C_\eps}\la v,S_n\ra\geq t\right),$$which can be bounded with a union bound and a tail bound and then maybe a Chernoff bound ([[Chernoff method]]) based on the properties of $S_n$. 

Covering arguments were shown to be 

## Drawbacks: 
- Dimension-dependent because covering numbers will depend geometrically on the underlying space 
- Have to be able to calculate the covering number 

# Chaining 

See [[chaining]] for an overview of chaining. Chaining provides high probability guarantees of the form 
$$\Pr(\sup_{\theta\in\sd} \la \theta, S_n\ra \geq tS)\lesssim \exp(-t^2),$$
where $$ S = \sup_{\theta\in\sd} \sum_{n\leq N}2^{n/2} \rho(\theta, \Theta_n),$$
where $\Theta_0\subset\Theta_1\subset\dots\subset\Theta_N$ are a selected sequence of sets which slowly "approximate" $\Theta=\sd$. The difference between [[generic chaining]] and [[Dudley chaining]] is how they choose to handle $S$. The latter typically bounds it using covering numbers and [[metric entropy]]. 


# The variational approach 

See [[variational approach to concentration]]. The idea is to use [[PAC-Bayes]] inequalities which are high probability guarantees over all probabilities measures into a simultaneous guarantee over all directions. 