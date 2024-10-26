---
created: 2024-08-29
lastmod: 2024-10-26
---

Suppose you observe data $X_1,\dots,X_n$ from some Bernoulli distribution and want to test whether the mean is 0.2 or 0.5 ([[hypothesis testing]]). If $n=1000$ and you observe 463 tails and 537 heads, this is evidence against the mean being 0.2. Moreover, the precise amount of evidence it is in favor of 0.5 is quantifiable. 

This is perhaps obvious to statisticians but is a fairly deep point. And the reason it's deep is because this only works because of the artificial assumptions we've introduced into our statistical model. The real-world does not work this way.  

Suppose you believe your dog is in the basement. You walk into the basement and don't see him. How much evidence is this against the proposition that he's in the basement? After all, he could be hiding, you could be in the wrong basement, or you could be dreaming. Or, perhaps he's not in the basement. But to _quantify_ the evidence (eg, the dog is not in the basement with probability 0.82), we need to introduce many auxiliary assumptions about the set of possible places the dog could be, the likelihood you are dreaming, or drink, or simply don't see your dog even if he's there. In other words, we need to place mathematical/distributional assumptions over everything that could possibly happen. This is what Jimmie Savage called a "small-world". 

Statistical guarantees are in the realm of small worlds. The role of mathematical modeling is come up with a small-world which is reminiscent enough of the real world as to be useful for decision-making (in some context). 

