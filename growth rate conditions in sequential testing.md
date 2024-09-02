---
created: 2024-08-29
lastmod: 2024-09-02
---

In [[sequential hypothesis testing]] based on [[e-value|e-values]] (i.e., [[game-theoretic hypothesis testing]]), one wants to find e-values and [[e-process|e-processes]] which grow quickly under the alternative. "Quickly" is a non-technical condition, however. What exactly should be maximized? Various authors have used different conditions based on the particular problem at hand. 

See: 
- [[GRO e-variable]] for simple alternatives, equivalent to [[maximizing log-wealth]]. 
- [[GROW e-variable]] for composite alternatives. 
- [[REGROW e-variable]] for composite alternatives 

Often, we do not have a particular alternative that we are considering (eg when building [[confidence sequences]] via [[estimating means by betting]], or in many financial applications). In that case, pursuing explicit GRO-like strategies may not make sense. Still, we want the wealth to grow when the null is not true so we still study [[betting strategies]] in this case. They are often motivated by the conditions above but not necessarily identical to any of them. 