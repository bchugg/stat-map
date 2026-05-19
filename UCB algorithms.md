---
lastmod: 2026-05-18
created: 2026-05-18
---

A broad class of algorithm which makes a selection among competing options by computing an optimistic bound for each option (typically based on a [[frequentist statistics|frequentist]] [[confidence intervals|CI]] but not always), and then selecting the option with the highest such bound. Typically applied in [[bandits]] and [[multi-armed bandits|multi-armed bandits]]. 

# History 
- Agrawal in 1995 was the first to propose UCB-style indices for each arm in MAB problems that were computable, and achieved the optimal regret asymptotically. 
- In 2022 Auer et al extended this work to provide the now-famous UCB algorithm for [[multi-armed bandits]] that gave non-asymptotic regret guarantees. 