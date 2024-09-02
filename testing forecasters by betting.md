---
created: 2024-08-29
lastmod: 2024-09-02
---
We can use the paradigm of [[game-theoretic hypothesis testing]] to test forecasters. We can either bet against a single forecaster, or we can [[comparing forecasters by betting|compare forecasters]]. 

The setup is identical to hypothesis testing. A skeptic whose betting against the forecaster starts with wealth $K_0=1$. At each round $t=1,\dots$:  
- Forecaster issues a probability distribution $P_t$ over some event space $\calX_t$ of possible outcomes. 
- Skeptic issues a payoff function $S_t: \calX \to [0,\infty)$ such that $\E_{X_t\sim P_t} [S_t(X_t)|\calF_{t-1}]\leq 1$ where $\calF_t= \sigma(X_1,\dots,X_t)$ is the $\sigma$-algebra containing the information of what's happened so far. 
- Nature reveals an event $X_t$ 
- Skeptic's wealth is updated as $K_t = K_{t-1} S_t(X_t)$. 

We are treating the forecaster's posited distribution as the null. The alternative is the composite hypothesis that nature is not following the forecaster's distribution (unless we want to test the forecaster against some particular hypothesis.)

Clearly, the question is how to choose $S_t$, which depends on $\calX_t$ and $P_t$. 

# Binary outcomes 

An interesting and relevant case (because of all the superforecasting mumbo jumbo) is the case when $\calX_t$ is binary or finite. Eg $\calX_t = \{\text{Ukraine will win the war, Ukraine will not win the war}\}$. If we were testing $P_t$ against a particular alternative $Q_t$, this would reduce to a simple vs simple testing problem ([[testing by betting—simple vs simple]]). In general, we need to use the plug-in method or the mixture method because we don't have a particular alternative in mind (see [[testing by betting—simple vs composite]]). 