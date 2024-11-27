---
lastmod: 2024-11-27
created: 2024-11-27
---

Broadly speaking, robust statistics is the study of how to perform reliable [[statistical inference]] under distributions that are misbehaved in some way. 

"Misbheaving" usually refers to three possible things: 
- The [[adversarial contamination model]], where an adversary is allowed to inspect the data and choose some fraction of the sample to corrupt; 
- The [[Huber contamination model]], where the adversary chooses a corruption distribution $Q$ and then a sample is drawn from the mixture distribution $\eps Q + (1-\eps) P$. This is weaker than adversarial contamination. 
- Heavy-tailed contamination, meaning that the data are drawn from a heavy-tailed distribution (see eg [[heavy-tailed concentration]] or [[scalar heavy-tailed mean estimation]]). A paper by Cherapanamjeri and Lee [argues that heavy-tailed contamination is easier than adversarial contamination](https://arxiv.org/pdf/2411.15306). 