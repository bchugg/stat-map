---
created: 2024-08-29
lastmod: 2025-08-13
---

In [[light-tailed, unbounded scalar concentration|light-tailed settings]], mean estimation is usually treated as synonymous with [[concentration inequalities|concentration]], since the sample-mean is the natural estimate of the mean and we're usually interested in concentration of the sum or mean of random variables. In heavy-tailed settings this is not the case, as the sample mean is a suboptimal estimate of the mean. 

So when it comes to heavy-tailed distributions, we use estimates of the mean that are not the sample mean. These are summarized in [[scalar heavy-tailed mean estimation]] and [[multivariate heavy-tailed mean estimation]]. 

In terms of actual concentration of the sample mean around the true mean in heavy-tailed settings, there's not much hope to get beyond polynomial rates. When the distribution has finite variance, then you can apply [[basic inequalities#Chebyshev's inequality]]. I don't think you can go beyond this in general. 

There's an interesting class of results for the sample mean under general distributional assumptions which rely on approximating arbitrary observations with truncated observations. Given $X_1,\dots,X_n$, write 
$$
X_i = Y_i + Z_i,
$$
where $Y_i = \min\{X_i,c\}$ and $Z_i = X_i - Y_i$. One can show that 
$$
\Pr(\ov{X}_n \geq u) \leq \Pr(\ov{Y}_n \geq u) + \Pr( \max_i X_i\geq c).
$$
Since the $Y_i$ are upper bounded, many well-known (one-sided) concentration inequalities are known for the first term on the right hand side; see [[bounded scalar concentration]]. So if one can control the second term on the rhs for particular values of $c$, this can lead to good concentration. 

Inequalities of this type are known as Fuk-Nagaev inequalities. See eg [Rio 2017](https://projecteuclid.org/journals/electronic-communications-in-probability/volume-22/issue-none/About-the-constants-in-the-Fuk-Nagaev-inequalities/10.1214/17-ECP57.full) who explores some of them. There are also [[Banach space]] versions of the Fuk-Nagaev inequalities; see [here](https://arxiv.org/pdf/math/0608687) and [here](https://books.google.ca/books?hl=en&lr=&id=aW7jBwAAQBAJ&oi=fnd&pg=PA1&dq=Decoupling:+from+dependence+to+independence.&ots=gr5SGedHwL&sig=yg46EE1gPoF8nnmy_D8EULXxZ9M#v=onepage&q=Decoupling%3A%20from%20dependence%20to%20independence.&f=false). [Hanh & Klass (1997, AoP)](https://www.jstor.org/stable/2959567) give similar style of results, giving tight and achievable upper bounds on the sum of iid random variables in terms of the conditional MGF.  