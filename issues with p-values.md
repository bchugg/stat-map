
Some mathematical drawbacks of [[p-value|p-values]] that can lead to (possibly inadvertent) [[p-hacking]].  

Let $P_n$ be a p-value which is a calculated based on $n$ observations $X_1, \dots, X_n$. As a reminder, the p-value guarantee reads: 
$$\forall n, \forall\alpha,\; \Pr_{H_0}(P_n \leq \alpha) \leq \alpha.$$
The issues with p-values explored here all consequences of the fact that the $n$ and $\alpha$ above are outside of the probability the statement. Consequently, they should not be random and should not depend on the data. This basic property has many consequences. 

> [!note] 
> In the case of $n$, the sample size, this issue is fixed with [[anytime-valid p-values]], but these must be specially constructed. Most p-values are not [[anytime-valid]], and these are the focus of this note.)

# Peeking and optional stopping

Suppose you set out to test the efficacy of a new drug. You gather 10,000 participants, give half of them the drug and give the other half a placebo. You want to see whether there is a significant difference between the recovery rates of the two groups (with a [[t-test]], say). 

You don't get all the data at once, of course, the trial is run over several months. Every day you get the results for a few more patients. **You should not monitor this data as it comes in, re-computing your p-value each day, and checking if it's significant**. 

Significance can only be calculated on the final sample of 10,000 people, since 10,000 was the initial number of observations chosen independently of the data. If you continuously monitor the result there's a possibility that you will stop early, in which case the [[stopping-time]] is a function of the data and your p-value is invalid. 

Of course, the act of simply looking at the data and re-computing the p-value is itself harmless. However, you cannot act on any if this information, otherwise it will contaminate your results. If there is even a possibility that you would stop early depending on the results then your p-value is invalid (see the counterfactual reasoning section below). 

# Optional continuation 

Suppose you compute 

LHC 
in oct 2021 saw a $3\sigma$ effect against the null, which was basically the standard model of physics. 
so they collected 6 months more data, computed another p-value. 
how we combine p1 and p2?
if they are independent can do Fisher combination. 
but here the data are not independent and there joint disttribution is unknown. p2 exists only because of p1, so in some worlds it exists and in some it doesn't. 
"optional continuation" 

lady tasting tea. 
muriel got all correct, p-value = 1/70. four tea in milk four milk in tea (she knew there were 4 of each). 
but if muriel made 1 mistake, then p-value is 17/70. this is getting 3 correct, there are 16 ways to get one wrong. 
but this also suffers from the counterfactual world problem. If she had gotten 1 wrong, would she have tried to convince fisher to run the experimetn again? if you think it's _possible_, then the p-value is not valid. 

covid trials. 


# Significance adjustments 



# Counterfactual reasoning 

Counterfactual worlds. Even if you fix sample size in advance and then compute p-value, it may not be valid. The same size needs to be the same in _all counterfactual worlds_. i.e, $\forall \omega\in\Omega: N(\omega)=52$. 
the validity of $P_N$ in ouor world depends on your answer to counterfactuals. this is obviously non-verifiable. So we have to assume this. [[e-value]] don't have this property and depend only on what happens in our world. 