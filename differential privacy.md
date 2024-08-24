Differential privacy is the study of how to make mechanisms which act on databases (i.e., make queries) secure from leaking information. 

Intuitively, a differentially private mechanism should be one which is not excessively reactive to small changes in the dataset. Let $\calD$ be the set of all databases, and consider a function $g$ which acts on $\calD$. (Think of a database as just some big data table where, e.g., each row corresponds to a different user.) For instance, given a database $x\in \calD$, $g(x)$ might be the size of $x$, or the total amount user deposits in $x$, or it might ask for the number of users with some property (a "counting query"). We want to add noise to $g$ in such a way that, regardless of how it queries the database, it cannot back out sensitive information. 

Formally, we call a (randomized) mechanism $f$ which acts on databases $(\eps,\delta)$-differentially private if, for all outputs $A\subset \text{Range}(f)$ and all databases $x$ and $z$ such that $x$ and $z$ differ by one row, 

$\Pr(f(x)\in A)\leq e^\eps \Pr(f(z)\in A) + \delta.$

If $\delta=0$, we call $f$ $\eps$-differentially private. 

The intuition behind the definition is easier to grasp if we negate it. If $f$ is _not_ differentially private, this means there exists some $A$ such that $\Pr(f(x)\in A)\gg \Pr(f(z) \in A)$. That is, swapping just a single row of $x$ to $z$ changed the output distribution considerably, meaning that $f$ is sensitive to the data. If $f$ is differentiably private then, roughly speaking, small changes in the input result in small changes in the output. 

A popular to write $\eps$-differential privacy is as the likelihood ratio

$$
\sup_{A\in \image(f)} \sup_{x_1,x_2:x_1\in \delta_1(x_2)}\frac{\Pr(f(x_1)\in A)}{\Pr(f(x_2)\in A)}\leq e^\eps,
$$

where $\delta_1(x)$ is the set of databases which different by at most 1 row from $x$. 

# Example: The Laplace Mechanism

Consider a deterministic function $g:\calD\to \Re^k$.  Define 
$$
\Delta = \sup_{x,y:x\in \delta_1(x)} ||g(x) - g(y)||_1 = \sup_{x,y:x\in\delta_1(y)} \sum_{i=1}^k |g(x)_i - g(y)_i|.
$$
$\Delta$ is often called the $\ell_1$-_sensitivity_ of $g$. The Laplace mechanism is defined as 
$$
f(x) = g(x) + (Y_1,\dots,Y_k),
$$
where $Y_1,\dots,,Y_k\sim\lap(0,\Delta/\eps)$ independently. Recall that the Laplacian distribution $\lap(a,b)$ has pdf $p(x) = (2b)^{-1}\exp(-|x-a|/b)$. To show that this mechanism is differentially private, we show that 
$$
\int_A \Pr(f(x)=z)dz \leq e^\eps \int_A \Pr(f(y)=z)dz,
$$
for all $x\in\delta_1(y)$. To see this, it suffices to show that for all $z\in A$, $\Pr(f(z)=z)\leq e^\eps \Pr(f(y)=z$) and then to integrate over $A$. Note that, 
$$\begin{align}
\Pr(f(x)=z) &= \prod_{i=1}^k \Pr(M(x)_i = z_i) = \prod_{i=1}^k \Pr(Y_i = z_i - g(x)_i) \\
&= \prod_{i=1}^k \frac{\eps}{\Delta} \exp(-\frac{\eps}{\Delta}|z_i - g(x)_i|).
\end{align}$$
Therefore, by the reverse triangle inequality, 
$$\begin{align}
\frac{\Pr(f(x)=z)}{\Pr(f(y)=z)} &= \prod_{i=1}^k \exp\bigg(\frac{\eps}{\Delta}(|z_i - g(y)_i| - |z_i - g(x)_i|)\bigg) \\ 
&\leq \prod_{i=1}^k \exp\bigg(\frac{\eps}{\Delta}(|g(y)_i- g(x)_i|)\bigg) \\ 
&= \exp\bigg(\frac{\eps}{\Delta}\sum_{i=1}^k |g(y)_i - g(x)_i|\bigg) \leq \exp(\eps).
\end{align}
$$

# Composition 

One immediate question is how differentially private mechanisms behave under composition. For instance, can we employ multiple differentially private algorithms in tandem and retain differential privacy? Sort of. 

Suppose $f_1,f_2$ are $(\eps_1,\delta_1)$, $(\eps_2,\delta_2)$ differentially private, respectively. Considering concatenating the output so that, given a database $x$, we construct a new map $g$ such that $g(x) = (f_1(x), f_2(x))$, where we run $f_1$ and $f_2$ independently of one another. Will $g$ be differentially private? 

It turns out that $g$ will be $(\eps_1+\eps_2,\delta_1+\delta_2)$ differentially private. You'll often see this result referred to as "the epsilons and deltas add up." Unfortunately, when people cite this result, they typically cite Theorem 1 of [this paper](https://www.iacr.org/archive/eurocrypt2006/40040493/40040493.pdf), which has an incorrect proof.  There is a corrected proof in the [book by Dwork and Roth](https://www.cis.upenn.edu/~aaroth/Papers/privacybook.pdf), but I think it's more complicated than necessary. Here's a simpler proof. 

Note the range of $g$ is the product space $\range(f_1)\times\range(f_2)$.  Since we run $f_1$ and $f_2$ independently, we have, for any $A\times B\in range(g)$ and any neighboring databases $x$ and $z$, 

$$
\begin{align*}\Pr(g(x)\in A\times B)&=\Pr((f_1(x),f_2(x))\in A\times B) \\ &= \Pr(f_1(x)\in A)\Pr(f_2(x)\in B)  \\ 
&\leq \min\{e^{\eps_1}\Pr(f_1(z)\in A+\delta_1,1\}\Pr(f_2(x)\in B) \\ 
&\leq (\min\{e^{\eps_1}\Pr(f_1(z)\in A),1\} + \delta_1)\Pr(f_2(x)\in B) \\ 
&\leq \min\{e^{\eps_1}\Pr(f_1(z)\in A),1\}\Pr(f_2(x)\in B) + \delta_1 \\ 
&\leq \min\{e^{\eps_1}\Pr(f_1(z)\in A),1\}(e^{\eps_2}\Pr(f_2(z)\in B) + \delta_2) + \delta_1 \\ 
&\leq \min\{e^{\eps_1}\Pr(f_1(z)\in A),1\}(e^{\eps_2}\Pr(f_2(z)\in B)  + \delta_2 + \delta_1 \\ 
&\leq e^{\eps_1+\eps_2} \Pr(f_1(z) \in A)\Pr(f_2(z)\in B) + \delta_1+\delta_2 \\ 
&= e^{\eps_1+\eps_2} \Pr(g(z) \in A\times B) + \delta_1+\delta_2.
\end{align*}
$$

Here we've just used basic facts of the min function and recognized that probabilities can be at most 1. Of course, we can extend this result by induction and conclude that given finitely many mechanisms $\{f_i\}$ where $f_i$ is $(\eps_i,\delta_i)$-differentially private, then the mechanism $g:\calX\to \bigotimes_i \range(f_i)$ given by  $g:x\mapsto \otimes_i f_i(x)$ is $(\sum_i \eps_i,\sum_i\delta_i)$ differentially private. 

We can also consider deterministic composition, and demonstrate that it does not affect the privacy guarantees. Indeed, suppose $f:\calD\to U$ is $(\eps,\delta)$ private and let $g:U\to V$ be deterministic and invertible. Then for any $W\subset V$,
$$
\begin{align}
\Pr(f\circ g(x) \in W) &= \Pr(f(x) \in g^{-1}(W)) \\
&\leq e^\eps \Pr(f(y) \in g^{-1}(W)) = \Pr(f\circ g(y)\in W),
\end{align}$$ so $f\circ g$ is  $(\eps,\delta)$ private. 

# DP in practice 

Differential privacy is now used in a lot of applications. Apple [started using it in macOS Sierra](https://www.apple.com/privacy/docs/Differential_Privacy_Overview.pdf) and has since expanded its application to Safari. Google [used differential privacy](https://arxiv.org/pdf/2107.01179.pdf) when gathering insights from searches related to Covid-19, and for their [Covid-19 mobility reports](https://arxiv.org/pdf/2004.04145.pdf). Other examples include [LinkedIn](https://arxiv.org/pdf/2010.13981.pdf), [Microsoft](https://proceedings.neurips.cc/paper/2017/file/253614bbac999b38b5b60cae531c4969-Paper.pdf) and [Uber](https://www.usenix.org/conference/enigma2018/presentation/ensign). 