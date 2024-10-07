---
lastmod: 2024-10-07
created: 2024-10-07
---

The extremely general technique of combining several different estimators (often called "weak learners", "base estimators", "base models") into a master estimator which (hopefully) performs better than each individual base estimator.  

People often differentiate two different kinds of ensemble learning: boosting and bagging. 

## Bagging 
Usually refers to the setting the weak learners are trained independently of one another, and then combined by some sort of weighted averaging. The conventional wisdom says to use bagging when the weak learners have low bias but high variance. You can then use standard [[concentration inequalities]] or [[central limit theorems]] to analyze their performance. 

[[median-of-means|Median-of-means]] can be considered bagging. 

## Boosting 
Usually refers to the setting when the weak learners are trained sequentially. The most famous example is [AdaBoost](https://en.wikipedia.org/wiki/AdaBoost), invented by Freund and Schapire in 1995. Many variations and extensions of adaboost have been proposed. 

