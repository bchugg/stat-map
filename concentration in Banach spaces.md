---
created: 2024-09-05
lastmod: 2024-09-05
---
Pinelis is responsible for both a Hoeffding and Bernstein bound in smooth and separable [[Banach space|Banach spaces]]. At the core of his proof is the construction of a [[supermartingale]]; his results can therefore be made [[time-uniform]] by applying [[Ville's inequality]] instead of Markov's inequality (though they're usually stated as [[fixed-time]] bounds). 


# Hoeffding 

Consider a $(2,D)$-smooth separable Banach space with norm $\norm{\cdot}$. Let $X_1,X_2,\dots$ have conditional mean $0$ with $\norm{X_t}\leq B$. Then: 
$$
\Pr\left(\norm{\sum_{i\leq n}X_i}\geq u\right) \leq 2\exp\left(-\frac{u^2}{2nD^2B^2}\right).
$$
Note the similarity to the usual Hoeffding bound ([[light-tailed scalar concentration]]) but with the extra factor of $D$. This is because [[Hilbert space|Hilbert spaces]] are $(2,1)$-smooth Banach spaces. 

# Bernstein 

Consider a $(2,D)$-smooth separable Banach space with norm $\norm{\cdot}$. Let $X_1,X_2,\dots$ have conditional mean $0$ with $\norm{X_t}\leq B$. Then #todo 


