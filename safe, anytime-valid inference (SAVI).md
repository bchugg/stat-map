---
created: 2024-08-29
lastmod: 2024-09-02
---
A sub-field of statistics concerned with estimation and uncertainty quantification which are sequentially valid, i.e., remain valid at all [[stopping-time|stopping times]]. This enables procedures that are (i) immune to (many forms of) p-hacking (see [[issues with p-values]]), (ii) allow stopping rules to be data-dependent, and (iii) allow one to continuously monitor incoming data. 

Though valid measure-theoretically, SAVI results typically rely on [[game-theoretic statistics]] and [[game-theoretic probability]], both intuitively and mathematically. 

Common tools in SAVI include: 
- [[confidence sequences]]
- [[e-value|e-values]] and [[e-process|e-processes]] 
- [[test-martingale|test-martingales]]
- non-negative [[supermartingale|supermartingales]] and submartingales (indeed, in some sense, SAVI must rely on these: https://arxiv.org/abs/2009.03167)

# References 

- [Game-Theoretic Statistics and Safe Anytime-Valid Inference](https://arxiv.org/pdf/2210.01948.pdf)
