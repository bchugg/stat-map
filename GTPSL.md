
# Designing Gamble spaces 

Let $f_1, \dots, f_k, g_1,\dots,g_m:\Re\to\Re$. Set 
$$\cZ = \{\omega\mapsto \sum_{i}\beta_i f_i(X(\omega)) + \sum_j \gamma_jg_j(X(\omega)) : \beta\in\Re^k, \gamma\in\Re^m_+. \}.$$
If $\cZ$ is AF, then ${\E}f_i(X) = 0$ and $\ov{\E}[g_j(X)]\leq 0$ for all $i$ and $j$. 

# Minimax theorem 

Exploring the connection between GTP and MTP. Have some underlying probability space $(\Omega, \cF, \mu)$. Let $M(\Omega)$ be the set of all probability measures. 

$\ov{\E}^{\cP}X = \sup_{P\in \cP} \E^P X$. 
$\ov{\E}^{mg}[X] = \sup_{P\in \cP}\inf_Z \E^P[X-Z]$. 
$\ov{\E}^g[X] = \inf_Z\sup_\omega X(\omega) - Z(\omega)$. 

- Gamble space is "measurable" if every $Z\in\cZ$ is measurable (in the MTP sense).   
- $P\in M(\Omega)$ and $Z\in\cZ$ are consistent if $\E^P[Z] \leq 0$ (i.e., in expectation you don't make money). 
- $\cP\subset M(\Omega)$ and $\cZ$ are consistent if $P$ and $Z$ are consitent for all $P\in\cP$ and $Z\in\cZ$. 

$\Delta_0(\cZ) = \{ P\in M(\Omega): \E^P Z\leq 0, \forall Z\in\cZ\}$. i.e., the set of all distributions that are consistent with $\cZ$. 
$\ov{\E}^0 X = \ov{\E}^{\Delta_0(\cZ)} X$ (for convenience). 

Thm: Let $(\Omega, \cZ)$ be measurable gamble space, $X$ be a measurable variable. Then 
$\un{\E}^g X \leq \un{\E}^{mg}X$ and $\ov{\E}^{mg} X\leq \ov{\E}^g X$. 
If $\Delta_0(\cZ)$ is nonempty, then 
$$\un{\E}^g X \leq \un{\E}^{mg} X\leq \un{\E}^0 X \leq \ov{\E}^0 X\leq \ov{\E}^{mg}X\leq \ov{\E}^g X.$$

When are the first and last quantities equal? The q is when does the minimax theorem hold? (wait why is this?) 

[Sion's minimax theorem](https://en.wikipedia.org/wiki/Sion%27s_minimax_theorem)

Cor: If $\cZ$ is positive-linear and $\Omega$ is compact then $\ov{\E}^{mg} X= \ov{\E}^g X$ for any variable $X$. 
How to deal with non-measurable $X$? Then define $\ov{\E}^P X = \inf_{X'}\E^P X' where inf is taken over all measurable $X'$ st $X'\leq X$. Similarly for lower expectation. 

Thm: PL, measurable space such that $\Delta_0(\cZ)$ non empty. Let $X$ be measurable. Then $\ov{\E}^0 X=\ov{\E}^{mg}X$.  


— - -

lady tasting tea experiment. $p$-value 1/70. Want to transform this into games. 

Game 1. $L = 1 + \lambda Z$, where $\E_{H_0}[Z]\leq 0$, $Z\geq -1$. So $L$ is an [[e-value]]. 
suppose she bets single shot on identifying all four cups at once. Z(right) = 69, Z(wrong)=-1. this gives $\E_{H_0}[L]=0$ if $\lambda=1$. If she wins, she ends with 70. 

Game 2 : sequential prediction. 


# Point nulls 
Following Shafer's paper 
bet is admissible iff it is a 




