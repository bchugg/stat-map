---
created: 2024-09-15
lastmod: 2024-09-15
---
In his 1975 textbook [_Sums of independent random variables_](https://link.springer.com/book/10.1007/978-3-642-65809-9) Petrov proved a number of useful [[central limit theorems|CLT]] templates. Here are two extremely useful ones. 

# Theorem 15 

Let $\{X_{k,n}\}$, $1\leq k\leq n$, $n=1,2,\dots$ be a set of sequences of random variables, where the random variables in each sequence are independent. Then 
$$
\frac{1}{n}\sum_{k\leq n} X_{k,n} \to N(\mu,\sigma^2),
$$
if and only if for all $\eps>0$ the following three conditions are all satisfied: 
- $\sum_{k\leq n} \Pr(|X_{n,k}|\geq \eps)\to 0,$
- $\sum_{k\leq n} \Var(X_{k,n}\ind(|X_{k,n}|<\eps)) \to\sigma^2$
- $\sum_{k\leq n} \E[X_{k,n}\ind(|X_{k,n}|<\eps)]\to \mu$.  

Note that this strengthens the [[Lindeberg-Feller CLT]] (and others) as these are necessary and sufficient conditions. 

# Theorem 21
Let $\{X_n\}$ be a sequence of independent random variables. Then 
$$
\rho_\ks\left(\frac{1}{a_n}\sum_{k\leq n}X_k - b_n, N(0,1)\right)\to 0,
$$
and $\max_{k\leq n}\Pr(|X_{k}|\geq \eps a_n)\to 0$ if and only if there exists some sequence $(c_n)$ with $c_n\to\infty$ and the following two conditions hold: 
- $\sum_{k\leq n} \Pr(|X_k|\leq c_n)\to 0$, 
- $\frac{1}{c_n^2} \sum_{k\leq n} \Var(X_k \ind(|X_k| < c_n))\to \infty$. 
In this case we can take 
$$
a_n ^2 = \sum_{k\leq n} \Var(X_k \ind(|X_k|<c_n)), \quad b_n = \frac{1}{a_n}\sum_{k\leq n} \E[X_k \ind {|X|<c_n}].
$$
Petrov also show that the condition $\sum_k \Pr(|X_{k,n}|\geq \eps)\to 0$ used in Theorem 15 is equivalent to $\Pr(\max_k |X_{k,n}|\geq \eps)\to 0$, which is stronger than what is used in Theorem 21. But intuitively, this is where these kind of "maximal" conditions come from. If such a condition doesn't hold, then the random variables are becoming too large over time to converge nicely. 

# Theorem 19 

Related to Theorem 21 but with slightly different conditions. Let $\{X_n\}$ be a sequence of independent random variables. Then 
$$
\rho_\ks\left(\frac{1}{a_n}\sum_{k\leq n}X_k, N(0,1)\right)\to 0,
$$
and $\max_{k\leq n}\Pr(|X_{k}|\geq \eps a_n)\to 0$ if and only if 
- $\sum_{k\leq n} \Pr(|X_k|\geq  \eps a_n)\to 0$ for all $\eps>0$, 
- $\frac{1}{a_n^2} \sum_{k\leq n} \Var(X_k \ind(|X_k| < a_n))\to 1$, and  
- $\frac{1}{a_n}\sum_{k\leq n}\E[X_k \ind(|X_k|<a_n)] \to 0$. 

This is arguably more useful than Theorem 21 as we don't have to find the sequence $c_n$; $a_n$ is often given. 