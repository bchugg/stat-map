---
lastmod: 2024-11-17
created: 2024-11-17
---

One way to see that [[bounded scalar concentration#Hoeffding's bound]] and [[bounded scalar concentration#Hoeffding's bound remastered]] are suboptimal, is to note that  $\frac{1}{\sqrt{n}}\sum_i (X_i - \E X_i)$ is roughly $N(0,\sigma^2)$ by the [[Lindeberg-Levy CLT]], and $\Pr(N(0,1)\geq u) \asymp \frac{1}{u}e^{-u^2/2}$. So there is a missing factor of $1/t$ in the  bound. 

This is well-known and is called [the missing factor in Hoeffding's bound](http://www.numdam.org/item/AIHPB_1995__31_4_689_0.pdf). It suggests that Hoeffding's bound can be improved with a more careful analysis. Talagrand was the first to do this—see [[bounded scalar concentration#Talagrand's inequality]]. It can also be done with Bentkus style bounds (see [[bounded scalar concentration#Bentkus' inequality]] or [[interpolating between Markov and Chernoff]]). 

Also see [the missing factor in Bennett's inequality](https://www.researchgate.net/profile/Ion-Grama/publication/225297239_Sharp_large_deviation_results_under_Bernstein's_condition/links/02e7e52cdc2559c109000000/Sharp-large-deviation-results-under-Bernsteins-condition.pdf) by Fan, Grama, and Liu for a similar discussion around Bennett and Bernstein inequalities. 