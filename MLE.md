---
created: 2023-05-01
lastmod: 2024-10-13
---

Dan Dennett once said of Darwin's theory of evolution that it was the best idea that anyone has ever had. You could say the same about the MLE in the realm of [[statistical inference]]. It's simple and elegant and sometimes optimal. 

Given a parametric model $\{P_\theta:\theta\in\Theta\}$ ([[parametric versus nonparametric statistics]]) and data $X^n$ we solve 
$$
\sup_{\theta\in\Theta} L(\theta), \quad \text{ where }\quad L(\theta) = P_\theta(X^n).
$$
So, given the data, we just optimize over the parameters that could have generated that data. Badaboom-badabing. 

#todo guarantees etc. 