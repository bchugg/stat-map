In [[hypothesis testing]], for a given $\alpha$, a uniformly most powerful (UMP) test is a test whose type-I error is bounded by $\alpha$ and, among all other tests with type-I error bounded by $\alpha$, has the most power. 

More formally, suppose we are testing $H_0$ vs $H_1$. Consider the family of all tests $\psi$ such that $\Pr_{H_0}(\psi(X) = 1)\leq \alpha$. We say a test $\phi$ is UMP if for all other tests $\psi$, we have 
$$

\Pr_{H_1} (\phi(X) = 1) \geq \Pr_{H_1}(\psi(X)=1).

$$
The [[Neyman-Pearson lemma]] states that the [[likelihood-ratio test]] is UMP for testing simple hypothesis (i.e. simple null vs simple alternative). 