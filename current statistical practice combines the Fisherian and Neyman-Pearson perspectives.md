
Current norms around [[hypothesis testing]] combine [[Fisher's paradigm]] and [[Neyman-Pearson paradigm]]. 

Fisher was focused on evidence and introduced the [[p-value]] as a measure of [[evidence against the null]]. Neyman and Pearson, on the other hand, were focused on decision-making.  Current practice is a combination of these two perspectives. We make decisions _and_ report the evidence. For instance, we reject the null _and_ report the p-value.  

This is odd, as observing $p\ll\alpha$ compared to $p<\alpha$ is not decision-relevant in the Neyman-Pearson setting. Or, at least, it should _not_ be decision-relevant. You should not do anything different upon observing a smaller or larger p-value, as long as both are less than your predetermined significance level, $\alpha$. 

But intuitively, a smaller p-value _is_ more evidence against the null, and it seems like that should be useful in some way. Part of the draw of replacing p-values with [[e-value|e-values]] is that more extreme e-values can be used to make more extreme decisions (see [[post-hoc hypothesis testing]] and [[e-values enable post-hoc hypothesis testing]]). 

