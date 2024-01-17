
A $(1-\alpha)$-CI for a parameter $\theta$ based on observations $X_1, X_2,\dots,X_n$ is a set $C_n = C(X_1,\dots,X_n)$ such that 
$$ \Pr(\theta\notin C_n)\leq \alpha.$$ 
CIs are fundamental tools in uncertainty quantification. They can be obtained directly, or via inverting hypothesis tests (see [[duality between hypothesis tests and CIs]]). 

They also have some problems. If you repeatedly compute confidence intervals after receiving new data, your intervals will eventually contradict one another (with probability 1). That is, there will be at least two intervals with no overlap, $C_n \cap C_m =\emptyset$. This implies they are not _sequentially valid_, in the sense that they do not guarantee that $\theta$ is contained $C_n$ for all $n$ with probability $1-\alpha$. This issue is solved with [[confidence sequences]]. 




