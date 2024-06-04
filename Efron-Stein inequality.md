Let $X_1,\dots,X_n$ be independent random variables and let $f:\calX^n\to\Re$ obey $\E[f^2(X)]<\infty$ where $X = (X_1,\dots,X_n)$. The Efron-Stein inequality states that,
$$\Var(f(X)) \leq \inf_{f_i}\sum_{i=1}^n \E[(f(X) - \E[f(X)|X^{(i)}])^2]=v,$$
where the infimum is over all such functions $f_i$. We can write $v$ in several different ways. First we can write it as a function of $f$ acting on iid copies: 
$$v = \frac{1}{2} \sum_{i=1}^n \E[(f(X) - f(\bs{X}_i'))^2],$$
where $\bs{X}_i'=(X_1,\dots,X_{i-1}, X_i', X_{i+1}, \dots, X_n)$ and $X_i'$ is an iid copy of $X_i$.  Next we can write it as 
$$ v = \inf_{f_i}\sum_{i=1}\E[(f(X) - f_i(X^{(i)})^2],$$
where $f_i : \calX^{n-1}\to\Re$ and the infimum is over all such functions. 

# References 
- Concentration Inequalities by Boucheron, Lugosi, Massart, Chapter 3.1 
