---
lastmod: 2025-01-07
created: 2025-01-07
---

Uniform convergence (UC) are a type of worst case, high probability [[concentration inequalities|concentration inequality]] that one might prove for a class of functions $\calF$. Let $\calF$ consist of some set of functions $f:\calX\to\Re$ (could replace $\Re$ with any [[Banach space]] in theory, but that's rarely done). A UC bound has the form: 
$$
\Pr\left(\sup_{f\in\calF} |P_nf - Pf|\geq \eps\right)\leq \delta,
$$
where $P_n f = \frac{1}{n}\sum_{i\leq n} f(X_i)$ and $P f = \E f(X)$ and $X_1,\dots,X_n\sim \Pr$ are random variables. 

Uniform convergence bounds are applied in [[empirical process theory]] to show that $\calF$ is a [[Glivenko-Cantelli class]], for instance. They're also applied in [[learning theory]], eg [[PAC learning]], to give finite-sample bounds on estimators. 

Depending on the problem, we might find $\eps$ or $\delta$ first. Eg, that bound might have the form "for all $\eps>0$, there exists some $\delta = \delta(\eps,n)$ that goes to 0 as $n\to\infty$" which implies that we obtain convergence in probability of $\sup_f |P_n f - Pf|$. This would be the case when showing that $\calF$ is a [[Glivenko-Cantelli class]]. But in [[PAC learning]], we usually want to fix $\delta$ first, and then find $\eps = \eps(\delta,n)$ such that $\sup_f |P_n f - Pf|\leq \eps$. 

As is common in [[empirical process theory]], $\eps$ will typically depend on some notion of complexity of $\calF$, such as [[covering and packing|covering numbers]], [[Vapnik-Chervonenkis theory|VC dimension]], or [[Rademacher complexity]]. 