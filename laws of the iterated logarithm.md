---
lastmod: 2024-11-15
created: 2024-11-15
---

Laws of the iterated logarithm (LILs) are statements about the almost sure fluctuations of sums of random variables. Perhaps the first LIL was due to Kinchine in 1924 (an article titled über einen satz der wahrscheinlichkeitsrechnung, have fun reading that). Kolmogorov [proved a LIL for bounded random variables](https://gdz.sub.uni-goettingen.de/id/PPN235181684_0101) in 1929. 

The most famous LIL, and one often appealed to when building [[confidence sequences]] (see also [[stitching for LIL rates]]), is the following. It is due to [Hartman and Wintner](https://www.jstor.org/stable/2371287?searchText=&searchUri=&ab_segments=&searchKey=&refreqid=fastly-default%3A42a70f0027909456545091c3674ca77b&initiator=recommender). See a nice survey [here](https://link.springer.com/content/pdf/10.1007/0-387-27332-8_8). Let $X_1,\dots,X_n$ be independent with variance $\Var(X_i) = \sigma^2<\infty$.  Let $S_n = \sum_{i\leq n} (X_i - \E X_i)$. A classical law of the iterated logarithm states that, with probability 1,  
$$
\lim\sup_n \frac{S_n}{\sqrt{2n \log\log n}}=\sigma, 
$$
and 
$$
\lim\inf_n \frac{S_n}{\sqrt{2n\log\log n}} = -\sigma.
$$
There is also a converse. If 
$$
\Pr\left(\lim\sup_n \frac{|S_n|}{\sqrt{n\log\log n}} <\infty\right)>0,
$$
then $\sigma^2<\infty$. 

## Relationship to LLNs and CLTs 
LILs are often viewed as sitting between laws of large numbers and [[central limit theorems]]. The strong LLN states that $S_n /n \to 0$ a.s. The [[Lindeberg-Levy CLT]] says that $S_n / \sqrt{n}$ converges to a normal in distribution. A LIL is trying to find the boundary, asking what kind of sequence $(a_n)$ exists such that $S_n / a_n$ does not converge to 0, but does not diverge. 

## Infinite variance
It's natural to ask what we can say if we don't assume the variance is finite. In this case it can be shown that $\lim\sup S_n / \sqrt{2n\log\log n} = \infty$. Does there exist some sequence such that $\lim\sup S_n / a_n = 1?$ It turns out that yes, under specific circumstances. Namely, the distribution must sit in the basin of attraction of a Gaussian. See [this paper](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/BCCBF35E0BDAE1FE02BEEB6EBFE52447/S1446788700021868a.pdf/on_the_law_of_the_iterated_logarithm_in_the_infinite_variance_case.pdf) by Maller. 
