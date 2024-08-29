The usual model in [[differential privacy]] is one in which there exists some large database $x\in \calX$ which contains all users data, and then some administrator or custodian of the data privatizes it. In practice, this isn't terribly secure. Do we trust the custodian? Does she delete the original database after it's privatized? What if another company offers her a lot of money for $x$, or her company is bought by another? 

For all these reasons, we might consider _local_ differentially privacy. Here, the data is privatized on the users end before reaching any centralized database. Thus, no one sees the raw data besides the user themselves. Google [uses](https://ai.google/research/pubs/pub42852) local differential privacy to collect information from users' browsers, and Apple [uses](https://machinelearning.apple.com/2017/12/06/learning-with-privacy-at-scale.html) local differential privacy to collect emoji data. 

In the local setting, instead of considering functions which act on the set of databases $\calD$, we consider functions which act on a users private data. If $h$ is such a function, then we say that $h$ is $\eps$-local differentially private if, for all user data $x$ and $y$ and all $A\subset \image(h)$, 
$$

\Pr(h(x)\in A)\leq e^\eps \Pr(h(y)\in A).

$$
Mathematically, therefore, this looks precisely the same as the definition of $(\eps,0)$-differential privacy, except that the function $h$ is acting on a different space than the function $f$. 

An example of a locally-differentially private mechanism is [[Warner's randomized response]]