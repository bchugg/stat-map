

- peeking 
- counterfactual reasoning
- optional continuation 
- 

p-values are not safe under peeking and optional stopping. See also [[p-hacking]]. 

Counterfactual worlds. Even if you fix sample size in advance and then compute p-value, it may not be valid. The same size needs to be the same in _all counterfactual worlds_. i.e, $\forall \omega\in\Omega: N(\omega)=52$. 
the validity of $P_N$ in ouor world depends on your answer to counterfactuals. this is obviously non-verifiable. So we have to assume this. [[e-value]] don't have this property and depend only on what happens in our world. 


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


we mix the fisher paradigm with the neyman-pearson paradigm. 
NP is focused on decision-making, i.e., hypothesis testing. wanted to trade off typei and type II errors. 
fisher was focused on evidence, and the p-value as a measure of evidence. 
now we ahve some weird combo of these two perspectives. we have decisions + evidence. "reject and the null _and_ report your p-value." 

covid trials. 