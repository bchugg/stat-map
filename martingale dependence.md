---
lastmod: 2025-01-15
created: 2025-01-14
---

Assuming that your data is iid is becoming less and less cool (get with it!). If you don't want to make such a strong assumption, a natural question is what kind of dependency you want to introduce. Martingale dependency is usually the go to option after iid. After that, you get into the complicated world of Markov dependencies or time-series data. 

Martingale dependence posits that there is a constant conditional mean: For data $X_1,\dots,X_n$ there exists some $\mu$ such that $\E[X_t | \calF_{t-1}]=\mu$ for all $t$ and some filtration $(\calF_t)$. This conditional often comes up in [[multiarmed bandit]] and [[contextual bandit]] problems. 

Martingale dependence is very naturally handled by [[supermartingale|supermartingales]] and, more generally, [[e-process|e-processes]]. Bounds based on [[sub-psi process|sub-psi processes]] typically handle martingale dependence (eg [[estimating means by betting]]) which means many [[confidence sequences]] do as well. 