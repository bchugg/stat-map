---
lastmod: 2024-10-27
created: 2024-10-27
---

Suppose you're interested in some [[concentration inequalities|concentration inequality]] of the form $\Pr( X - \E X \in (-a,b))$. Suppose we want to control this quantity for all $X$ with $\E X = \mu$ and variance upper bounded by $\sigma^2$. The measure maximizing this probability solves the optimization problem: 
$$
 
\begin{align}
\sup_{\nu} &\int_\Omega \ind\{x\notin (a,b)\}\d \nu \\ 
\text{s.t.} \quad &\int (x -\mu)\d\nu = 0, \\
& \int ( x - \mu)^2 \leq \sigma^2, \\ 
&\int \d\nu = 1.
\end{align}
$$
One can prove both [[basic inequalities#Markov's inequality]] and [[basic inequalities#Chebyshev's inequality]] like this. Indeed, this is how these inequalities were first proved. (In the case of Markov you don't have the variance constraint). The [[optimization perspective on Markov's inequality]] is actually this technique in disguise. 

One can of course generalize the above program to include constraints on third, fourth, etc., moments. This has been done (eg [here](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=6e47a78872fbc48e8112d3a9a1a3847a368e0668)). In 2013, [Pinelis proved an inequality](https://arxiv.org/pdf/1011.6065) that interpolates between Chebyshev's inequality and [[basic inequalities#Cantelli's inequality]] in this way. 

The above program is a linear program, so the solution will lie on a vertex of the polytope induced by the constraints. This also implies a certain form to the solutions: A distribution that solves a program with $k$ constraints will be supported on at most $k+1$ points. This was proved by [Hoeffding in 1955](https://link.springer.com/chapter/10.1007/978-1-4612-0865-5_18). 

This approach to concentration is optimal by construction, so if the program can be solved then it will yield the best results. If you are interested in concentration inequalities for practical purposes, it's therefore worth investigating if you can solve the relevant convex optimization problem. By contrast, the [[Chernoff method]] is easier to work with (hence significantly more popular) but gives suboptimal results. 

## Refs 
- [Optimal Tail Comparison Based on Comparison of Moments](https://link.springer.com/chapter/10.1007/978-3-0348-8829-5_19), Pinelis 1998. 
- [Optimal Inequalities in Probability Theory: A Convex Optimization Approach](https://epubs.siam.org/doi/abs/10.1137/S1052623401399903?casa_token=Bt-2iIWlbngAAAAA:X0wIqinGV-90275RFukRxzSo8MDnVuzDQLG6wgkyyinW_dJyRhcNBmgYB3pdHeePNeelivFFnolN), Bertsimas and Popescu, 2005. 