---
created: 2024-09-12
lastmod: 2025-01-02
---

Also known as the data-processing inequality. Let $X\to Y\to Z$ form a Markov chain, i.e., $p(x,y,z) = p(x) p(y|x) p(z|x,y)$. Then the [[mutual information]] between $X$ and $Y$ cannot be increased by using $Z$ instead of $Y$:  
$$
I(X;Z) \leq I(X;Y).
$$
This is a fundamental inequality in [[information theory]], telling us that any post-processing if $Y$ (resulting in $Z$), cannot increase the mutual information with the original source $X$.  In other words, no transformation of the received code can give more information than the code itself. 