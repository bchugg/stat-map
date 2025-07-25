---
created: 2024-08-29
lastmod: 2025-07-05
---

Let $M=(M_t)$ be a $P$-[[supermartingale]]. Ville's inequality is a [[time-uniform]] version of Markov's inequality ([[basic inequalities#Markov's inequality|basic inequalities:Markov's inequality]]), stating that, for any $t_0$, 
$$
\Pr(\exists t\geq t_0: M_t \geq x)\leq \frac{\E[M_{t_0}]}{x},
$$
for all $x>0$. Note this bound is _uniform over all time_. If we take $x = 1/\alpha$, then this says that the probability that $M$ will _ever_ exceed $1/\alpha$ is at most $\E[M_1]/x$. 

Ville's inequality can also be written as 
$$
\forall \tau: \Pr(M_\tau \geq x) \leq \frac{\E[M_1]}{x},
$$
where $\tau$ represents a [[stopping-time]]. This is what enables statistical inference procedures based on Ville's inequality to be valid at arbitrary stopping times (which are data dependent). 

Ville himself in 1939 was actually interested in the case of $\alpha=0$. His original statement reads: On any event $A$ with $P(A)=0$, there exists a nonnegative supermartingale that increases to infinity on $A$. 

Ville's inequality also implies the classical result that a nonnegative supermartingale will reach infinity with probability 0. Let $(M_t)$ be a nonnegative supermartingale and define the event $A_k = \{\sup_t M_t \geq 2^k\}$. By Ville, $\Pr(A_k) \leq 2^{-k} \E[M_1]$. Since the events $(A_k)$ are monotonically decreasing, i.e., $A_{k+1} \subset A_k$ for all $k$, we have 
$$
\Pr(\sup_t M_t = \infty) = \Pr(\cap_{k\geq 1}A_k) = \lim_k \Pr(A_k) = \lim_k 2^{-k} \E[M_1]=0.
$$
Much of [[game-theoretic statistics]], and [[sequential hypothesis testing]] in particular, relies on Ville's inequality, where we often construct some [[test-martingale]] or [[e-process]] under the null. Ville's implies that this process is unlikely to ever become large. Thus, if it does became large, this is [[evidence against the null]]. 

## Proof of Ville 
Define the [[stopping-time]] $\tau = \inf\{ t\in \mathbb{N} \cup \{\infty\}: M_t \geq 1/\alpha\}$. The optional stopping theorem (which says that $\E M_\tau \leq \E M_0$) gives 
$$
1 \geq \E M_0 \geq \E M_\tau \geq \E [M_\tau \ind\{\tau <\infty\}] \geq \frac{1}{\alpha} \E \ind\{\tau < \infty\},
$$
since $M_\tau \geq 1/\alpha$ by construction. Noting that $\E \ind{\tau<\infty} = \Pr(\sup_t M_t \geq 1/\alpha)$ concludes the proof. 

# Extensions 
- **Reverse Ville.** There is also a reverse-time Ville's inequality which holds for nonnegative reverse [[submartingale|submartingales]]. If $(R_t)$ is a reverse submartingale with respect to a reverse filtration, then for all $t_0$, 
	$$
	\Pr( \exists t\geq t_0: R_t >1/\alpha)\leq \alpha \E[R_{t_0}].
	
$$
- **Composite generalization.** Ville's inequality also holds for an [[e-process]], since they are upper bounded by a [[test-martingale]]. The [composite generalization of Ville's inequality](https://arxiv.org/pdf/2203.04485) actually requires the notion of an e-process, and reads 
$$
\sup_{P\in\calP}\Pr(\exists t\geq 1: E_t\geq 1/\alpha)\leq \alpha,
$$
	if $(E_t)$ is an e-process for $\calP$. The e-process is necessary here! The statement fails if we replace e-process with martingale or supermartingale. 
- **Non-integrable processes.** [The extended Ville's inequality for nonintegrable nonnegative supermartingales](https://arxiv.org/abs/2304.01163). 
- [A Generalisation of Ville’s Inequality to Monotonic Lower Bounds and Thresholds](https://arxiv.org/pdf/2502.16019) extends the threshold $1/\alpha$ to more general functions. 