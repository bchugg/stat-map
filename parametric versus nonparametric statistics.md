---
created: 2024-08-29
lastmod: 2024-10-13
---

The distinction between finite and infinite parameter families. [[statistical inference|Inference]] is of course easier in parametric families since we're making more assumptions on the underlying data generating process. Nonparametric methods are thus more flexible and useful but have worse guarantees (eg convergence rates). 

The canonical example of a nonparametric families of distributions is 
$$
\calF = \bigg\{f: \int (f''(x))^2 dx <\infty\bigg\}.
$$
This is nonparametric because there's no obvious parameters associated with such a family, besides simply letting $\Theta=\calF$, which is a trivial way to describe it. Contrast this to, e.g., the family of Gaussians, which can be described by two parameters: the mean and the variance. 
 