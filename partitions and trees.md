Suppose $X\in \cX$. The idea behind tree based nonparametric regression is to construct a partition $R_1,\dots,R_m$ of  $\cX$ and estimate $m(x) = \E[Y|X=x]$ separately in each partition. 

The simplest thing is to simply take the average of the labels of points in each region $R_i$, i.e., for $x\in R_k$, 
$$\widehat{m}(x) = \sum_{i=1}^n \frac{\ind(X_i \in R_k) Y_i}{\sum_j \ind(X_j\in R_k)}.$$
If the labels are discrete (i.e., we're doing [[nonparametric classification]]), then instead of taking the average label, we might take the majority label in the region $R_k$. In this case, it's similar to [[knn]] (but still possibly distinct, depending on how the regions are chosen). 

The above conversation assumes that the regions are already selected. But how do we select them? 

You must just split the space evenly a priori. E.g., if $\cX = [0,1]^d$, then we could partition $\cX$ into smaller $d$-dimensional cubes. We might also choose them to be a function of the given samples (e.g., in [[splines]]). 

Trees are a general method of constructing the partition via training. They can be used for [[nonparametric regression]] or [[nonparametric classification]]. The idea is to recursively decide how to partition the space based on the covariates of the $i$-th training example. We decide to split on the $j$-th feature if the resulting partition would  maximize some score function. Note that trees can be considered either parametric or nonparametric ([[parametric versus nonparametric statistics]]) depending on whether we let them grow arbirarily large with the training data, or whether we impose maximum depths, widths, etc. 

Partitions and trees are a special case of [[local polynomial regression]]. 

