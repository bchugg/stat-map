---
created: 2023-03-07
lastmod: 2026-05-19
---

Perhaps the simplest, and the most studied, instance of a [[bandits|bandit]] problem. We have $K$ arms (typically $K$ is taken to be finite) each with an unknown reward distribution. We then pull the arms sequentially, attempting either [[best-arm identification]] or [[regret minimization]]. 

# History 
- The introduction of the MAB problem is typically credited to Lai and Robbins. They gave lower bounds on regret.  
- In 1995, Agrawal gave the precursor to the UCB algorithm, associating with each arm an index 
- In 2002, Peter Auer and others introduced the famous UCB algorithm. 

# Known results 
-  For Bayesian bandits with discounted rewards, the Gittins Index algorithm is optimal. 