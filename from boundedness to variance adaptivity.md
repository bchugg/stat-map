---
created: 2024-08-29
lastmod: 2024-09-02
---

This is simply the observation that in various [[concentration inequalities]] for bounded observations, we often begin with a result that takes advantage only of these known bounds. 

For scalar-valued concentration this is Hoeffding's bound ([[bounded scalar concentration]]), for martingale bounds this is the Azuma-Hoeffding bound ([[martingale concentration]]). Such bounds assume a worst case variance (because they assume nothing about it). 

Such bounds can usually be strengthened to include the variance of the observations, which might give tighter results. This gives Bernstein's bound in the scalar case ([[bounded scalar concentration#Bernstein bound|light-tailed scalar concentration:Bernstein bound]]), a variance-adaptive bound in the martingale case ([[martingale concentration#Variance bound|martingale concentration:Variance bound]]) and a Bernstein-type bound in the matrix case ([[operator norm inequalities#Bernstein inequality|operator norm inequalities:Bernstein inequality]]). 

Once variance adaptivity is achieved, one often tries to find [[empirical Bernstein bounds]]. 