---
created: 2024-08-29
lastmod: 2024-09-02
---
The e-BH procedure is the equivalent of the [[BH procedure]] for [[FDR control]] but using [[e-value|e-values]]. The main benefit is this procedure allows for arbitrary dependence between the e-values, which is not the case for the BH procedure and p-values. 

We are in a [[multiple testing]] setup with $k$ hypotheses, each of which has an associated e-value. 
The procedure rejects the hypotheses with _largest_ $k^*$ e-values where 
$$

k^* = \max\bigg\{k: \frac{k e_{[k]}}{K}\geq \frac{1}{\alpha}\bigg\}

$$
and $e_{[1]}\geq e_{[2]} \geq \dots \geq e_{[K]}$. 

This has $\E[F_D/|D|]] \leq \alpha K_0/K$, i.e., it has no dependence on $\ell_K$, even without the [[PRDS]] assumption (this is an improvement over the BH procedure). 

The proof is actually quite straightforward:  We have $k^* e_{[k^*]}/K  \geq \frac{1}{\alpha}$ by definition. Therefore,
$$
\frac{1}{\alpha}\leq \frac{k^*e_{k^*}}{K}\leq \frac{k^* e_{\ell}}{K}
$$
for all $\ell\leq k^*$. Those indices, $\ell\leq k^*$ are precisely the indices of the rejected hypothesis - the discoveries. That is, $|D|=k^*$. Therefore, $|D|\geq K/(\alpha e_{[\ell]})$ for all $\ell\in N$, the set of rejected hypotheses. So,
$$

\frac{F_D}{|D|} = \sum_{k} \frac{\ind(k \in D\cap N)}{|D|} = \sum_{k\in N}\frac{\ind(k \in D)}{|D|} \leq \sum_{k\in N}\frac{\ind(k\in D)\alpha E_{[k]}}{K} \leq \alpha \sum_{k\in N}\frac{E_{[k]}}{|D|}.

$$
Since $\E[E_{[k]}]\leq 1$, we have $\E[F_D/|D|]\leq \alpha |N|/|D| = \alpha K_0/|D|$.  

**Boosting e-values**
If other information is available, we can also _boost_ the e-values. This might be info on the joint distribution, some structure of the problem, etc. But without such additional information, it is better to just use the non-boosted approach above. 

# References 

- [False discovery rate control with e-values](https://arxiv.org/pdf/2009.02824.pdf) by Ruodo Wang and Aaditya Ramdas 
 
