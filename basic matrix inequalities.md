---
created: 2024-08-29
lastmod: 2024-09-02
---
Let $<$ denote the matrix (Loewner order). Most the following inequalities apply to more general linear operators. 

# Basic inequalities 

As you'd expect, there are matrix versions of the Markov and Chebyshev inequalities. 
A good overview is given in Appendix C here: https://arxiv.org/pdf/quant-ph/0012127

## Markov 

For matrix $X$ and PSD $A$, 
$$

\Pr(X \not\le A) \leq \Tr(\E[X]A^{-1}).

$$
Of course, this reduces to usual  Markov inequality ([[basic inequalities#Markov's inequality|basic inequalities:Markov's inequality]]).  

## Chebyshev 

Markov's inequality extends to Chebyshev's inequality in the same way as in the scalar case: 
$$

\Pr(|X-\E X| \not\leq A) \leq \Tr(\E|X-\E X|^2 A^{-2}).

$$

## A Chernoff-like inequality 

For matrix $Y$, symmetric matrix $B$ and matrix $T$ such that $T^* T >0$ where $T^*$ is the [[conjugate transpose]] of $T$, we have 
$$

\Pr(Y\not\leq B)\leq \Tr(\E\exp(TYT^* - TBT^*)).

$$
We can prove this easily using Markov's inequality: 
$$

\begin{align}
\Pr(Y\not\leq B) &= \Pr(Y - B\not\leq 0) \\
&= \Pr(T YT^* - TBT^* \not\leq 0) \\
&= \Pr(\exp(TYT^* - TBT^*)\not\leq I) \\
&\leq \Tr(\E\exp(TYT^* - TBT^*)I^{-1}).
\end{align}

$$
Here we've used that the exponential of the zero matrix is the identity. Note also that since the trace is a linear operator, so 
$$

\Tr(\E\exp(TYT^* - TBT^*)) = \E\Tr(\exp(TYT^* - TBT^*)).

$$
