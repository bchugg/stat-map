---
created: 2024-08-29
lastmod: 2024-10-13
---


One solution to the problem of [[testing by betting—composite vs composite]].  

In [[sequential hypothesis testing]], suppose we are testing a composite null. Universal inference is one way to construct [[e-value|e-values]] and [[e-process|e-processes]] in this setting. It was introduced by [Wasserman, Ramdas, and Balakrishnan](https://arxiv.org/abs/1912.11436) (2020). 

Let $X_1,X_2, \dots$ be a stream of observations. We are testing the composite null $\calP$ vs a composite null $\calQ$ (though of course this could be a simple null). 

# Split UI 

Consider the [[fixed-time]] setting, where we have observations $X_1, \dots, X_n$. The most basic UI procedure is split UI. The general split UI procedure is the following: 
- split data into $D_0$, $D_1$. 
- pick some $\wh{q}$ using $D_1$. 
- Compute $\sup_{p\in \calP} p(D_0)$ using $D_0$. 

The UI e-value is
$$
E_t = \frac{\wh{q}(D_0)}{\sup_{P\in \calP} p(D_0)}.
$$
If the [[MLE]] is well-defined, then the denominator is the MLE. Since we're taking the supremum, it's easy to see that
$$
\E_P E_t \leq \E_P \left[\frac{\hat{q}(D_0)}{p(D_0)}\right] = 1,
$$
where we use that $\wh{q}$ is independent of $D_1$ due to the data-splitting.

Note that no regularity conditions were required. This approach can be applied to [[irregular problems in hypothesis testing]], which many traditional methods struggle with. This is why the method is considered _universal_. 

$E_t$ is an [[e-value]] for any distribution $\wh{q}$. But the choice of $\wh{q}$ matters for the power of the test. As in [[testing by betting—simple vs composite]], $\wh{q}$ can be chosen via the method of mixtures or the plug-in method. 
 
The randomness can be minimized by doing this over several splits of the data, not just one. 

# UI e-process 

The above e-value doesn't immediately lend itself to sequentialization. Here's how to construct an [[e-process]] using similar ideas. 

Let $\wh{q}_t$ be any distribution chosen using the first $t$ observations. Consider
$$
E_t = \frac{\prod_{i\leq t}\wh{q}_{i-1}(X_i)}{\prod_{i\leq t} \wh{p}_t (X_i)},
$$
where $\wh{p}_t$ is the MLE based on $X_1, \dots, X_t$.  This is an e-process under $\calP$, which can be seen by upper bounding $E_t$ using the MLE in the denominator.  This is the plug-in-method. We can also consider a mixture method, where we integrate the alternative densities over some distribution. Similar ideas occur in [[testing by betting—composite vs composite]] and also when constructing [[confidence sequences]]: [[confidence sequences via conjugate mixtures]] (mixture method) and [[confidence sequences via predictable plug-ins]] (plug-in method). 

Tartatovsky actually wrote down this e-process in his 2014 book, [Sequential Analysis](https://books.google.co.uk/books?hl=en&lr=&id=zhsbBAAAQBAJ&oi=fnd&pg=PP1&dq=info:2pwLAYxRg4EJ:scholar.google.com&ots=_1sb59Yuwk&sig=XgCw22Mvgo2a0KYa618i2To8gFY&redir_esc=y#v=onepage&q&f=false). 