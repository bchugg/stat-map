---
lastmod: 2024-11-27
created: 2024-11-27
---

Huber's contamination model in [[robust statistics]] dates back to the work of Peter Huber in 1964 (see [Robust Estimation of a Location Parameter](https://link.springer.com/chapter/10.1007/978-1-4612-4380-9_35)). We assume we are trying to do inference on some distribution $P$, but we see a contaminated sample drawn from the mixture distribution 
$$
R = \eps Q + (1- \eps) P, 
$$
for some $\eps\geq 0$ (known to us), and some "contamination distribution" $Q$. This is a weaker contamination model than the [[adversarial contamination model]]. 

We can also make Huber's model slightly more general by assuming that the contaminated sample is drawn from $R$, where $R \in \mathbb{B}_\tv (P,\eps) = \{ R: \tv(R, P)\leq \eps\}$, where $\tv$ is the [[total variation distance]]. This is a superset of the mixture distributions $\eps Q + (1-\eps)P$. 