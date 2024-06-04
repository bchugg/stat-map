
Some mathematical drawbacks of [[p-value|p-values]] that can lead to (possibly inadvertent) [[p-hacking]].  

Let $P_n$ be a p-value which is a calculated based on $n$ observations $X_1, \dots, X_n$. As a reminder, the p-value guarantee reads: 
$$\forall n, \forall\alpha,\; \Pr_{H_0}(P_n \leq \alpha) \leq \alpha.$$
The issues with p-values explored here are all consequences of the fact that $n$ (the sample size) and $\alpha$ (the significance level) are outside of the probability statement. Consequently, they should not depend on the data. This basic property has many consequences. 

> [!note] 
> In the case of $n$, the sample size, this issue is fixed with [[anytime-valid p-values]], but these must be specially constructed. Most p-values are not [[anytime-valid]], and these are the focus of this note.)

# Significance adjustments 


 The significance level $\alpha$ cannot be chosen with respect to the data —  it must be fixed in advance. This often confuses practitioners. If you run an experiment and obtain a p-value of 0.10, why can't you say you reject at level 0.1? Because then what you're saying is, 


# Peeking and early stopping

Suppose you set out to test the efficacy of a new drug. You gather 10,000 participants, give half of them the drug and give the other half a placebo. You want to see whether there is a significant difference between the recovery rates of the two groups (with a [[t-test]], say). 

You don't get all the data at once, of course, the trial is run over several months. Every day you get the results for a few more patients. **You should not monitor this data as it comes in, re-computing your p-value each day, and checking if it's significant**. 

Significance can only be calculated on the final sample of 10,000 people, since 10,000 was the initial number of observations chosen independently of the data. If you continuously monitor the result there's a possibility that you will stop early, in which case the [[stopping-time]] is a function of the data and your p-value is invalid. 

Of course, the act of simply looking at the data and re-computing the p-value is itself harmless. However, you cannot act on any if this information, otherwise it will contaminate your results. If there is even a possibility that you would stop early depending on the results then your p-value is invalid (see the counterfactual reasoning section below). 

# Optional continuation 

Optional continuation is the flip side of peeking and early stopping. Suppose you calculate your p-value after gathering the data from your 10,000 participants. The p-value is 0.07 but your significance level is $\alpha=0.05$. It's very tempting to gather a few more participants and see if your p-value will go down. But this is illegal: it would mean your sample size is a function of your data. So continuing the experiment by gathering more participants is invalid. 

But the problems don't stop there. Suppose you run a first clinical trial and, based on the results, run a second. In practice, we would consider this to be a completely separate study and compute its p-value independently of the first study. Is this correct? We only did the second study because of the results of the first, after all. So in some sense, the sample size of the second study data dependent. 

Unfortunately, there's no great answer to this question. Doubly unfortunately, this issues arises constantly in practice. Here are two examples: 

In October 2021 the LHC recorded a $3\sigma$ event against the null, where the null hypothesis represented the standard model of physics. That is, they recorded an event that was extremely unlikely according to the standard model. Like good scientists, they were skeptical of the results, so they opted to collect data for 6 more months and then compute a new p-value. 

During the covid trials, many labs were running many experiments on potential vaccines. When a vaccine looked promising, that lab would either conduct a larger experiment, or other labs would conduct experiments on the same vaccine. Should this be considered the same study? Clearly not all of these trials are independent. 


# Counterfactual reasoning 

The two issues above can be viewed as facets of a more general problem with p-values, which is the issue of counterfactual worlds. 

We keep emphasizing that the sample size needs to be fixed in advance. But the p-value requirement is stronger than this. It actually says that _the sample size needs to be same in all counterfactual worlds_. If it's not, it means that the sample size was actually data-dependent, which is not allowed. In other words, no matter what happens in the experiment, the sample size cannot change. 

(Mathematically, it can help to view the sample size as a deterministic random variable. That is, if $N$ is the sample size, then for all outcomes $\omega\in\Omega$, we require that $N(\omega) = c$ for some $c$ if the p-value is valid.)

This is an incredibly frustrating property. For one, it is unverifiable: how do you know the sample size would not have changed in every possible world? Second, it makes it extremely easy to start doubting p-values.  



Counterfactual worlds. Even if you fix sample size in advance and then compute p-value, it may not be valid. The same size needs to be the same in _all counterfactual worlds_. i.e, $\forall \omega\in\Omega: N(\omega)=52$. 
the validity of $P_N$ in ouor world depends on your answer to counterfactuals. this is obviously non-verifiable. So we have to assume this. [[e-value]] don't have this property and depend only on what happens in our world. 

