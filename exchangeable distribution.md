We say the observations $(X_1,\dots,X_n)$ are _exchangeable_ if for any permutation $\sigma:[n]\to[n]$,
$$
(X_1,\dots,X_n) = (X_{\sigma(1)},\dots,X_{\sigma(n)})\text{ in distribution.}
$$
Exchangeability is clearly a weaker notion than independent and identically distributed. It's also a strictly stronger notion, as there are distributions that are exchangeable and not iid.

Consider drawing balls from an urn without replacement. The observations are not iid. But they are exchangeable: the probability of drawing red, blue, red is the same as drawing blue, red, blue. 
