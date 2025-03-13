---
created: 2024-08-29
lastmod: 2024-09-02
---

For a strictly increasing function $\psi: \Re_+\to\Re_+$, the $\psi$-Orlicz norm is 
$$
\norm{X}_\psi := \inf \{u>0 \;|\; \E \psi\left(\frac{|X|}{u}\right)\leq 1\}.
$$
The $\psi$-Orlicz norm is a norm on the space of those random variables $X$ such that $\norm{X}_\psi$ is finite. Such a space is called an Orlicz space. It is a linear space. 

Note that the Orlicz norm is a functional of the distribution, not a function of the random variable itself. 

## Relationship to $L^p$ spaces 
Orlicz norms/spaces generalize [[Lp norm|Lp norms and spaces]]. This can be seen by taking $\psi(a) = a^p$ in which case 
$$
\E_P \psi(|X|/u) = \int \frac{|X|^p}{u^p}dP.
$$
This attains one iff $u = \int |X|^pdP$ meaning that $\norm{X}_\psi = \norm{X}_p= \int |X|^pdP$. 

## Defining sub-Gaussian and sub-exponential random variables 
Orlicz norms also provide a nice, unified way of dealing with [[sub-Gaussian distributions]] and [[sub-exponential distributions]].  

In particular, if we take $\psi(x) = \psi_2(x) = \exp(x^2)-1$, then $\norm{\cdot}_{\psi_2}$ is called the sub-Gaussian norm. A random variable is sub-Gaussian iff it is an element of the $\psi_2$-Orlicz space, i.e., if $\norm{X}_{\psi_2}<\infty$. Note that 
$$
\norm{X}_{\psi_2} = \inf\{u>0 \; | \; \E\exp(|X|^2/u^2)\leq 2\}.
$$
Meanwhile, if we take $\psi(x) = \psi_1(x) = \exp(x) -1$, then $\norm{\cdot}_{\psi_1}$ is the sub-exponential norm. A random variable is sub-exponential iff it is an element of the $\psi_1$-Orlicz space. Here
$$
\norm{X}_{\psi_1} = \inf\{u>0 \; | \; \E\exp (|X|/u)\leq 2\}.
$$ 
