---
lastmod: 2024-12-20
created: 2024-12-20
---

A solution to [[the problem of approximate inference in deep learning]]. More accurate, but slower than [[variational inference]]. 

The idea is relatively straightforward: Given a model $p(x,z) = p(x|z)p(z)$ where $z$ is latent, we construct a Markov chain on $z$ whose stationary distribution is the posterior $p(z|x)$ that we wish to estimate. We then sample from the chain to collect samples from the stationary distribution and an empirical estimate is constructed from the samples. 

Quoting [Blei, Kucukelbir, and McAuliffe](https://arxiv.org/pdf/1601.00670) on when to use MCMC vs VI: 
> variational inference is suited to large data sets and scenarios where we want to quickly explore many models; MCMC is suited to smaller data sets and scenarios where we happily pay a heavier computational cost for more precise samples. For example, we might use MCMC in a setting where we spent 20 years collecting a small but expensive data set, where we are confident that our model is appropriate, and where we require precise inferences. We might use variational inference when fitting a probabilistic model of text to one billion text documents and where the inferences will be used to serve search results to a large population of users. In this scenario, we can use distributed computation and stochastic optimization to scale and speed up inference, and we can easily explore many different models of the data.