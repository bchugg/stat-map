---
lastmod: 2024-12-20
created: 2024-12-16
---

Who's to say that the mean response is a linear function of $\beta ^t X$ as in [[linear regression]]? It's no law of the universe, surely. In particular, a linear model—obviously—predicts that a change in the input results in a linear change in the output. But we may instead expect that changes in the input reflects multiplicative (say) changes in the output, in order to reflect rates or probabilities. 

GLMs thus replace the linear function with an invertible function $m$ and model $\E[Y | X] = m(\beta^t X)$. The inverse $m^{-1}$ is often called the link function. 