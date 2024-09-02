---
created: 2024-08-29
lastmod: 2024-09-02
---
A problem in [[sequential hypothesis testing]] where we want to test whether a sequence of observations is [[exchangeable distribution|exchangeable]]. That is, we observe $X_1,X_2,\dots$ and test 
$$

H_0: X_1,X_2,\dots\text{ are exchangeable}.

$$
In some sense, this the same probability as testing the iid assumption. [Ramdas et al. (Corollary 16)](http://www.maths.lse.ac.uk/Personal/jruf/papers/shafer.pdf) show that a sequence is an [[e-process]] under exchangeability iff it is an e-process under the iid assumption. 

Vovk tests exchangeability with [[conformal prediction]]: [Testing randomness online](https://pure.royalholloway.ac.uk/ws/portalfiles/portal/39327896/authors_accepted_manuscript.pdf) This works in a coarsened filtration, by examining only the conformal p-values. This is an instance when [[coarsened filtrations can increase power]]. 

[Ramdas, Ruf, Larsson, Koolen](http://www.maths.lse.ac.uk/Personal/jruf/papers/shafer.pdf) study testing exchangeability against [[Markovian alternatives]]. Interestingly, they also show that every [[test-martingale]] under exchangeability is non-increasing, therefore powerless. To employ the framework of [[game-theoretic hypothesis testing]], one must therefore study [[e-process|e-processes]] instead of supermartingales. 

[Saha and Ramdas also test exchangeability](https://proceedings.mlr.press/v238/saha24b/saha24b.pdf) under Markovian alternatives. They also work in a coarsened filtration, examining the data in pairs instead of one at a time. 

