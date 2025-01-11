---
lastmod: 2025-01-11
created: 2025-01-11
---

A real-valued function $f$ on a normed space $(\calX, \|\cdot\|)$ satisfies a holder condition with exponent $p>0$ if 
$$
|f(x) - f(y)| \leq C \| x -y \|^p,
$$
for all $x,y\in\calX$. A Hölder _space_ is a set of functions on a common space that obey the  Hölder condition with the same exponent. If $p=1$ then the function is Lipschitz. 

In statistics, these come up when analyzing estimators ([[statistical inference]]); eg [[statistical decision theory|rates]] in [[density estimation]]. This makes sense intuitively: we're trying to learn functions from a finite number of observations (the function evaluated noisily at various points). If the function varies too wildly from point to point, then inference is going to be impossible. A Hölder condition (or another kind of continuity condition) is saying that the function isn't too chaotic and is learnable. 

Sometimes Hölder spaces are defined in terms of derivatives. You'll see the Holder space $C^{k,\alpha}(\calX)$ defined as the space of functions $f:\calX\to\Re$ which satisfy 
$$
|D^k f(x) - D^k f(y)| \leq C \|x - y\|^\alpha,
$$
for $k\geq 0$ and $\alpha\in (0,1]$. This is equivalent to the previous definition with $p = k + \alpha$. 