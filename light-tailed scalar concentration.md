
Here we list [[concentration inequalities]] for scalar-valued random variables under various light-tailed conditions (which typically means that the [[MGF]] exists in some neighborhood).  This is contrast to [[heavy-tailed scalar concentration]], where we assume only a few moments. 

For rvs $X_1,\dots,X_n$ let $\overline{X}_n = \frac{1}{n}\sum_ {i=1}^n X_i$. 

Many of these concentration inequalities are proven using corresponding [[exponential inequalities]]. There are also [[time-uniform]] versions of these inequalities which stem from the [[sub-psi process]] given by the corresponding exponential inequality. 
# Bounded random variables 

## Hoeffding bound 

Let $X_1, \dots, X_n$ be independent with $a_i\leq X_i\leq b_i$. Hoeffding showed that 
$$

\Pr( |\overline{X}_n - \mu|\geq \eps)\leq 2\exp\left(\frac{-\eps^2n^2}{\sum_{i=1}^n (b_i - a_i)}\right).

$$
The natural one sided versions also exist. This is generalized by McDiarmid's inequality ([[bounded difference inequalities]]). 

## Bernstein bound 

Hoeffding's bound uses only the fact that the random variables are bounded. It doesn't use any information about their variance. Bernstein's bound fixes this. For $|X_i| \leq c$ and $\sigma^2 = \frac{1}{n}\sum_{i=1}^n \Var(X_i)$, Bernstein's bound says that 
$$

\Pr(|\Xbar_n - \mu| >\eps) \leq 2\exp\left(\frac{-n\eps^2}{2\sigma^2 + 2c\eps/3}\right).

$$

This trend of first presenting a result using only the boundedness of observations and then giving a variance-adaptive result is a common one, see [[from boundedness to variance adaptivity]]. 

## Bennett's bound 

$$

|\Xbar_n - \mu| \leq \sqrt{\frac{2\sigma^2\log(2/\delta)}{n}} + \frac{\log(2/\delta)}{3n}.

$$

# References 
- Concentration inequalities by Boucheron, Lugosi, and Massart. 