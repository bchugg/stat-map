---
created: 2024-08-29
lastmod: 2024-09-02
---
Here's an intuitive explanation of Markov's inequality. Suppose we fix the probability $p_\alpha = \Pr(X\geq \alpha)$ and ask the question: How small can we make $\E[X]$ subject to the constraint that $X\geq 0$ a.s.? 

That is, we want to solve
$$

\begin{align*}
\min_{P} \quad & \E_{X\sim P}[X] \\
\text{s.t}\quad & p_\alpha = \Pr_P(X\geq \alpha) \\
& X\geq 0.
\end{align*}

$$
This is easy. If we could, we'd put all of $X$'s mass at 0, which would minimize $\E[X]$ subject to $X\geq 0$. But we have to move at least some of the mass to $\alpha$ or beyond. So we'll put mass $p$ at $\alpha$, and mass $1-p$ at 0. It should be clear that any other alteration would simply increase $\E[X]$. With these choices, we have $\E[X] = \alpha p_\alpha$. Since this minimized $\E[X]$, we have $\E[X]\geq \alpha p_\alpha$ for all other $X$ which is precisely Markov's inequality.



