Sample space $\Omega$. 
Set of losses $\ell_b$ indexed by $\calB$. Loss $\ell_b$ associated with action space $\calA_b$, i.e., $\ell:\calA_b\to \Re_+$.  
Random variables $X$ with co-domain $\calX$. 
Testing hypotheses $H_0$ and $H_1$. 
## Compatibility 
Decision rule $\delta$ is compatible with $E$ if $$\ell_b(0, \delta_b(x))\leq E(x),\quad \forall x\in \calX, b\in \calB.$$$\delta$ is _maximally_ compatible with $E$ if it is compatible with $E$ and no other decision rule that is compatible with $E$ is type-II strictly better than $\delta$. 
## Type-I risk safety 
Decision rule $\delta$ is type-I risk safe if $$\sup_{P\in H_0} \E_P \sup_{b\in \calB} \ell_b(0,\delta_b(X))\leq 1.$$Note this generalizes type-I error in the [[Neyman-Pearson paradigm]]. 

## Type-II strictly better 
$\wh{\delta}$ is type-II strictly better than $\delta$ if for all $b\in\calB$, $$\ell_b(0, \wh{\delta}_b) \geq \ell_b(0,\delta_b),\; P\text{-a.s.} \quad \text{ for all }P\in H_0,$$and there is some $b$ and $P\in H_0$ for which the inequality is strict. That is, under the null, $\wh{\delta}$ has _greater_ loss. 

Why is this stated in terms of $H_0$ and not $H_1$? And why should $\wh{\delta}$ have greater loss? Because if $\wh{\delta}$ has greater loss under $H_0$, we may assume it has lower loss under $H_1$. This is because if not, then those $b$ and $x$ such that $\ell_b(1,\wh{\delta}_b(x))\leq \ell_b(1,\delta_b(x))$, we can replace $\widehat{\delta}_b(x)$ with $\delta_b(x)$ and the decision-maker will always be better off. 

This makes things easier, as can formulate the theory in terms of $H_0$ only. 

## Admissibility 
If both $\wh{\delta}$ and $\delta$ are Type-I risk safe and $\wh{\delta}$ is type-II strictly better than $\delta$, then we would always pick $\wh{\delta}$ over $\delta$. In this case we say $\delta$ is inadmissible. If $\delta$ is type-I risk safe and no other rule is type-II strictly better than $\delta$, then $\delta$ is _admissible_. 

## Richness 
The problem is rich relative to e-variable $E$ if for every $x$ there exists some loss $b$ and action $a\in\calA_b$ such that $\ell_b(0,a) = s$. 


