
# Bounded random vectors 

## Dimension-free Bernstein bound 

Let $X_1, \dots, X_n\in\Re^d$ obey $\norm{X_t}\leq c_t$ and $\E[\norm{X_t}^2]\leq v_t^2$. Let $V_n = \sum_{i\leq n}v_i^2$. Using the martingale-variance inequality [[martingale concentration#Variance bound|martingale concentration:Variance bound]], we obtain 
$$
\Pr( \norm{S_n} \geq \sqrt{V_n} + \eps) \geq \exp\left(\frac{-\eps^2}{4V_n}\right),
$$
for $\eps \leq V / \max_t c_t$. A bound of this form was first given by David Gross [here](https://arxiv.org/pdf/0910.1879). 

Note that a weaker form of this bound can be obtained by appealing to the Azuma-Hoeffding inequality ([[martingale concentration#Azuma-Hoeffding inequality|martingale concentration:Azuma-Hoeffding inequality]]). The difference is equivalent to the difference between the Hoeffding bound and the Bernstein/Bennett bound in the scalar case (see [[light-tailed scalar concentration]]).   
