An example of an algorithm which is locally differentially private ([[local differential privacy]]) is Warner's method for survey responses. The idea is to enable respondents to answer potentially sensitive survey questions while maintaining plausible deniability. 

Consider a survey with a sensitive yes/no question and fix some $r\in(0,1]$. The respondent answers truthfully with probability $r$, otherwise flips an unbiased coin. That is, the privatized response is 

$$Z\sim \begin{cases} X,& \text{w.p. } r\\ Y\sim \text{Bernoulli(1/2)},&\text{w.p }1-r
\end{cases}
$$

Note that $\Pr(Z=z|X=x) = r\ind(z=x) + (1-r)/2$. Therefore, 

$\max_z\max_x \frac{\Pr(Z|X=x)}{\Pr(Z|X=x')} = \max_x\max_z \frac{r\ind(z=x) + (1-r)/2}{r\ind(z=x') + (1-r)/2} = 1 + \frac{2r}{1-r}.$

If we set $\eps=\log(1 + 2r/(1-r))$, we see that Warner's randomized response is $\eps$-locally differentiably private. 
$$\newcommand{\eps}{\epsilon}
\newcommand{\ind}{\mathbf{1}}$$




