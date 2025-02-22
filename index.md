---
title: Home
created: 2024-08-29
lastmod: 2025-01-08
---

Welcome to the stats map, a (growing) collection of notes on various topics in statistics, probability, and theoretical computer science. 

Unlike a traditional textbook, these notes prioritize the connections between subjects instead of giving a full treatment of each subject on its own. I don't provide many proofs or formal definitions. This is an attempt to understand how the world of statistics hangs together; to chart the outlines of what we know and the techniques we use. It is an attempt at a [Zettelkasten](https://en.wikipedia.org/wiki/Zettelkasten)—or second brain—for statistics and probability.  

![[zettel.jpeg|center|500]]

These are, obviously, my notes. They are not unbiased. They reflect my opinions on what's interesting and what's not. There will be significant detail on some topics and a total absence of many topics. That said, this is still in it's early stages (it's missing even basic material from a standard first year grad course in theoretical statistics), and it will continue to be expanded in the coming months and years. 

These notes suffer from the fractal nature of knowledge: the more you know, the more you realize you don't know. This results in many incomplete pages, and many `todo` tags flying around. I'm planning to get around to these, but for each one I tame several more are likely to pop up. Sorry, but I don't think there's any escape from this problem for an ever-growing note collection. 

> [!info] How to navigate 
> If you click on a link you will follow it. You can see a list of all notes on the left hand side of the page, and backlinks to the current note on the right hand side (or on the bottom if you're on a small screen).

# What's in here

Possible places to start: 
- [[game-theoretic statistics]] and [[game-theoretic probability]]
- [[e-value|e-values]] and [[e-process|e-processes]]
- [[concentration inequalities]] or [[techniques for multivariate concentration]]
- [[maximal inequalities]]
- [[central limit theorems]]
- [[hypothesis testing]]

Or if you're interested in the philosophical foundations of statistics: 
- The [[foundations of statistics]] or arguments therein, like [[Fisher's paradigm]] versus the [[Neyman-Pearson paradigm|NP paradigm]] or why [[current statistical practice combines the Fisherian and Neyman-Pearson perspectives]].  
- Various statistical schools of thoughts and their methods (non-contradictory): [[Bayesian statistics]], [[frequentist statistics]], and [[game-theoretic statistics]]. 
- Various philosophies of probability (very much contradictory): [[Bayesian interpretation of probability]], [[frequentist interpretation of probability]], [[instrumentalist theory of probability]]. 
- More than you wanted to know about [[issues with p-values|some philosophical issues with p-values]]. 

# Why make this? 

1. Writing helps me digest and aggregate information. You haven't truly understood something until you can teach it, and you can't teach it until you can write it down coherently. 
2. You can know a lot of material but not know how it's connected. The best researchers don't simply have detailed knowledge of many areas, they have a mental map of how all these areas fit together. I am not one of the best researchers but, so help me God, I still have a mental map. This is my exported (very much incomplete) mental map. 
3. Emphasizing the connections between topics helps you spot patterns. Similar techniques are often used in different areas. 
4. It helps you spot holes in the literature. Writing down what is known helps carve out what is unknown. 

# More on the philosophy

This is inspired by the [Zettelkasten method](https://en.wikipedia.org/wiki/Zettelkasten), an approach to note-taking and personal knowledge management. 

Most note taking methods are based on hierarchies. You keep folders on various topics, subfolders on subtopics, and so on. In statistics, you might have a folders on [[concentration inequalities]], [[information theory]], and [[hypothesis testing]]. But this makes it hard to see the connections between these areas. For instance, there is an explicit connection between concentration and hypothesis testing (see [[duality between hypothesis tests and CIs]]), and information theoretic methods are often used to construct [[concentration inequalities]] (see [[techniques for multivariate concentration]]). Where should you put the notes on these connections? 

Zettelkasten systems solve this problem by abolishing hierarchical note-taking. They instead adopt a network-like architecture, prioritizing the connections between ideas just as much as the ideas themselves. Concretely, it consists of small files (_zettels_) that are linked to each other. Here this is done via hyperlinks between markdown files, but historically it was done with index cards. Zettelkasten systems have a long history: 

> Born out of the commonplace tradition with modifications by Conrad Gessner (1516-1565) and descriptions by Johann Jacob Moser (1701–1785), the Zettelkasten, a German word translated as “slip box”, is generally a collection of highly curated atomic notes collected on slips of paper or index cards. Zettelkasten were made simpler to create and maintain with the introduction of the mass manufacture of index cards (and card boxes and furniture) in the early 20th century.
> - Chris Aldrich [on the history of note-taking tools](https://boffosocko.com/2021/07/03/differentiating-online-variations-of-the-commonplace-book-digital-gardens-wikis-zettlekasten-waste-books-florilegia-and-second-brains/). 

There has been a renewed interest in Zettelkasten and related note-taking systems in recent years.  Common keywords in this space are [evergreen notes](https://notes.andymatuschak.org/Evergreen_notes), [second-brain](https://www.buildingasecondbrain.com/), [digital garden](https://maggieappleton.com/garden-history), and [personal knowledge management](https://en.wikipedia.org/wiki/Personal_knowledge_management). Some public examples of these kind of note taking systems come from [Andy Matushack,](https://notes.andymatuschak.org/About_these_notes) [Nitin Pai](https://notes.nitinpai.in/Sta), and [Joschua](https://notes.joschua.io/). 

Zettelkasten systems are typically used to construct and grow an inventory of your own thoughts and insights. Seeing as I did not invent the vast majority of the maths discussed here, this note set deviates from this philosophy. But I think network-style note taking systems for technical subjects are an under-explored medium (for both research and pedagogy), so here we are. 

# Who am I? 

I am [Ben](https://benchugg.com). I'm a PhD student in the machine learning and statistics program at CMU. I study things like [[sequential statistics]], [[e-value|e-values]], and [[concentration of measure]]. Occasionally I also [read](https://doyouevenlit.podbean.com/), [write](https://benchugg.com/writing/), and [yell about philosophy](http://incrementspodcast.com/). 

Here is my face, cartoonified. 
![[images/me.png|center|250]]

If you spot any mistakes, you can email me at benchugg $\alpha\tau$ cmu.edu or submit a PR request [here](https://github.com/bchugg/stat-map). 