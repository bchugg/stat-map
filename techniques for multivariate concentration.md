---
created: 2024-08-29
lastmod: 2024-10-13
---

Suppose we have a stochastic process $(S_t)$ evolving in some space. What techniques are available for bounding $\norm{S_t}$? If $S_t\in\Re$, then we usually argue about $S_t$ and $- S_t$ and take a union bound to get a bound on $|S_t|$ (see [[light-tailed scalar concentration]] and [[heavy-tailed scalar concentration]]). However, in higher-dimensional spaces (in $\Re^d$, $d\geq 2$, say) a union bound doesn't suffice: there are infinitely many directions one has to worry about. 

There are several techniques for dealing with this problem. 

# Working directly with the norm 

The idea is to form a Doob martingale from the increments of the process and then apply well-known martingale bounds.  Set
$$
Z_t = \E[\norm{S_n} | \calF_t] - \E[\norm{S_n}].
$$
So $(Z_t)$ is a martingale with $Z_0=0$. Let $D_t = Z_t - Z_{t-1}$, be the increments of the process. Various [[martingale concentration]] bounds are stated as conditions on the increments of the process. For instance:
- If $S_t$ is bounded for each $t$, then we can use the Azuma-Hoeffding inequality ([[martingale concentration#Azuma-Hoeffding inequality|martingale concentration:Azuma-Hoeffding inequality]]) 
- If a bound on the variance of $D_t$ is known, then we can use the equivalent of a Bernstein inequality ([[martingale concentration#Variance bound|martingale concentration:Variance bound]]). 

The [[Pinelis approach to concentration]] is another method which works directly with the norm. 

# Covering arguments 

See [[concentration via covering]] for an overview. The idea is to bound cover the unit ball with an finite net, and then take a union bound. You suffer the covering number ([[covering and packing]]) of the underlying space in the bound. 

This means covering arguments lead to dimension-dependent bounds because covering numbers will depend geometrically on the underlying space.  You also have to be able to calculate the covering number. 

# Chaining 

See [[chaining]] for an overview of chaining. Chaining provides high probability guarantees of the form 
$$
\Pr(\sup_{\theta\in\dsphere} \la \theta, S_n\ra \geq tS)\lesssim \exp(-t^2),
$$
where
$$
 S = \sup_{\theta\in\dsphere} \sum_{n\leq N}2^{n/2} \rho(\theta, \Theta_n),
$$
and $\Theta_0\subset\Theta_1\subset\dots\subset\Theta_N$ are a selected sequence of sets which slowly "approximate" $\Theta=\dsphere$. The difference between [[generic chaining]] and [[Dudley chaining]] is how they choose to handle $S$. The latter typically bounds it using covering numbers and [[metric entropy]].  

# The variational approach 

See [[variational approach to concentration]]. The idea is to use [[PAC-Bayes]] inequalities which are high probability guarantees over all probabilities measures into a simultaneous guarantee over all directions. 

In some scenarios they allow you to escape-dimension dependence (eg for sub-Gaussian random vectors) which neither chaining nor covering arguments allow you to do. 