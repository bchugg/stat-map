
An approach to the [[foundations of statistics]]. The Neyman-Pearson (NP) paradigm is focused on decision-making above all else, as opposed to simply quantifying [[evidence against the null]] as Fisher wanted (see [[Fisher's paradigm]]). 

 NP believed that a null hypothesis $H_0$ should always be tested against an alternative hypothesis $H_1$. They want to decide when and how to reject $H_0$ in favor of $H_1$, and therefore introduce the notion of type-I error, type-II error, and power. The NP paradigm cashes out correct in terms of the frequentist principle (see [[frequentist statistics]]): 

> In repeated practical use of a statistical procedure, the long-run average actual error should not be greater than (and ideally should equal) the long-run average reported error. 
> - From [Berger](https://www2.stat.duke.edu/~berger/papers/02-01.pdf). 

The NP procedure looks like: 
- Define a test statistic $T$ based on the data. 
- Reject $H_0$ if $T\geq c$, where $c$ is some pre-chosen critical value. (Being pre-chosen is crucial, see [[issues with p-values]]). 
- (Perhaps more generally, compute a [[p-value]] $p$ and reject if $p\leq \alpha$ where $\alpha$ is pre-chosen. Usually the p-value is computed by means of the test-statistic above). 


