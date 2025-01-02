---
created: 2024-08-29
lastmod: 2025-01-01
---

The branch of statistics concerned with analyzing data as it arrives sequentially over time. In particular, we assume that the sample size is not fixed in advance of seeing the data, which is the case of the majority of statistics (see, e.g., [[issues with p-values]]). 

A modern approach to sequential statistics is [[safe, anytime-valid inference (SAVI)]]. In fact, these are often used interchangeably. 

## History 
During WWII, the [statistical research group (SRG)](https://en.wikipedia.org/wiki/Statistical_Research_Group) at Columbia gathered several statisticians and economists to help with the war effort. Allen Wallis and Milton Friedman were interested in the problem of ordnance testing, in particular how to compare and test the number of munition rounds required achieve various tasks (eg bring down a bomber plane with a given probability). 

Some mathematical formulas were given which gave bounds on the number of rounds required for testing. But when seasoned experts were around, they could often tell much sooner whether a given method was going to work. So the officials wanted to know if a formal rule could be devised telling the engineers if they could stop the test early, thereby saving rounds. 

Milton and Wallis started thinking about the problem, wondering if they could develop [[sequential hypothesis testing|sequential hypothesis tests]] (though they wouldn't have called it that) which would allow them to stop early (see [[optional stopping]]). They developed a couple simple formulas and thought they may be onto something, but feeling they were out of their mathematical depth they decided to hand the problem to a mathematician. They tried to interest Jack Wolfowitz but couldn't. Finally they got Abraham Wald interested, and Wald eventually produced a couple papers and a book on the subject, which is what really kickstarted the field. Read Allen Wallis' account of this time [here](https://www.jstor.org/stable/2287451). 

The field lay somewhat dormant for several decades after, until Lai, Robbins, and Siegmund produced several seminal papers on [[confidence sequences]] and [[anytime-valid]] methods in the 1970s. 

From there the field had another dormant period, which only a handful of papers being published on these subjects every few years, until there was an explosion of interest around 2018/2019, when ideas from [[game-theoretic statistics]] and [[game-theoretic probability]] started being understood by the community and applied to sequential problems. 