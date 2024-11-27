---
lastmod: 2024-11-27
created: 2024-11-27
---

A choice of contamination model in [[robust statistics]]. 

The idea is to allow an adversary to corrupt an $\eps$-fraction of the data. This causes immediate problems. For instance, if no limits are placed on the corruption, then an adversary allowed to change even one observation can arbitrarily skew the sample, making inference infinitely poor. 

There are two kinds of adversarial contamination: 
- **Strong contamination model**: The adversary sees the original data $X_1,\dots,X_n$ and then decides both what fraction of the data to contaminate and which observations in the original sample to replace with the contaminated sample. 
- **Weak (or oblivious) contamination model**: The adversary _first_ chooses the fraction, the indices to replace, and the contaminated observations, and then sees the original data.  

Note that both the strong and weak contamination models are stronger than the [[Huber contamination model]]. 