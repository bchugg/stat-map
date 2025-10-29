---
created: 2024-09-23
lastmod: 2025-10-29
---

A philosophical principle that the likelihood function contains all the relevant information of the data for hypothesis testing. 

If comparing a null and alternative, we might say that the comparison between two hypotheses should be based on their likelihoods. Put like this, the likelihood is principle is similar to, but weaker than, the [[law of likelihood]]. That is, one can adopt the likelihood principle but not the law of likelihood, but if one adopts the law of likelihood then you are implicitly adopting the likelihood principle as well. 

Fisher, who didn't require the notion of an alternative hypothesis (see [[Fisher's paradigm]]), [stated the likelihood principle as](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/7A05FB68C83B36C0E91D42C76AB177D4/S0305004100009580a.pdf/theory_of_statistical_estimation.pdf): 

> Likelihood serves all the purposes necessary for the problem of statistical estimation.

That said, Fisher didn't necessarily endorse the likelihood principle. Indeed, the LP seems to clash with much of [[frequentist statistics|frequentism]], because frequentists often want to consider guarantees that depend on ancillary information other than the likelihood ratio. Eg, frequentists want to control type-I/II error, design [[confidence intervals]], and give guarantees on long-run average performance. These are not strict evidentiary notions—they are more concerned with properties of decision-making procedures. But the LP states that $L(\theta|X)$ is all you need. 

This makes me think that there actually _isn't_ a conflict between frequentism and the likelihood principle, at least in theory.  But in practice, many frequentists do appeal to various procedures as giving evidence (eg Neyman even said this about confidence intervals!). Perhaps another way to say it is that while frequentists are often focused on guarantees on decision-making procedures, they often want the _input_ to those procedures to be some statistic which summarizes the evidence. 
## Birnbaum's theorem 

In 1962, Birnbaum proved that sufficiency + conditionality implies the likelihood principle. The result is somewhat controversial, both mathematically (see Evans' [overview](https://arxiv.org/pdf/1302.5468)) and because it rubs frequentists the wrong way. 

The sufficiency principle: This says that if there is a [[sufficient statistic]] for your statistical model, then it captures everything about evidence. In other words, if two sets of data have the same sufficient statistic, then they correspond to the same amount of evidence. 

The conditionality principle: This says that your evidence should only depend on which experiment you actually run. Eg: If you decided between two experiments by flipping a coin (and thus the choice was probabilistic), any evidence you obtain should not depend on the experiment you didn't run. 