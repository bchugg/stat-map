
Welcome to the stats map, a collection of notes on various subtopics in statistics, probability, and theoretical computer science. 

Unlike a traditional textbook, these notes prioritize the connections between subjects instead of giving a full treatment of each subject on its own. I don't provide many proofs or formal definitions. This is an attempt to understand how the world of statistics hangs together; to chart the outlines of what we know and the techniques we use. It is an attempt at a [Zettelkasten](https://en.wikipedia.org/wiki/Zettelkasten)—or second brain—for statistics. 

![[zettel.jpeg|center|500]]

These are, obviously, my notes. They are not unbiased. They reflect my opinions on what's interesting (and what's not). There will be significant detail on some topics and a total absence of many topics. 

> [!info] How to navigate 
> If you click on a link you will follow it. You can see a list of all notes on the left hand side of the page, and backlinks to the current note on the right hand side. 

# Where should I start?

If you're just here poking around, here are some places you might like to start: 
- [[game-theoretic statistics]] and [[game-theoretic probability]]
- [[e-value|e-values]], [[e-process|e-processes]], or [[issues with p-values]]
- [[concentration inequalities]] or [[techniques for multivariate concentration]]
- [[uncertainty quantification]]

Otherwise, you can find a long list of all notes on the left hand side. 

# More on the philosophy

This is inspired by the [Zettelkasten method](https://en.wikipedia.org/wiki/Zettelkasten), an approach to note-taking and personal knowledge management. 

Most note taking methods are based on hierarchies. You keep folders on various topics, subfolders on subtopics, and so on. In statistics, you might have a folders on [[concentration inequalities]], [[information theory]], and [[hypothesis testing]]. But this makes it hard to see the connections between these areas. For instance, there is an explicit connection between concentration and hypothesis testing (see [[duality between hypothesis tests and CIs]]), and information theoretic methods are often used to construct [[concentration inequalities]] (see [[techniques for multivariate concentration]]). Where should you put the notes on these connections? 

Zettelkasten systems solve this problem by abolishing hierarchical note-taking. They instead adopt a network-like architecture, prioritizing the connections between ideas just as much as the ideas themselves. Concretely, it consists of small files (_zettels_) that are linked to each other. Here this is done via hyperlinks between markdown files, but historically it was done with index cards. Zettelkasten systems have a long history: 

> Born out of the commonplace tradition with modifications by Conrad Gessner (1516-1565) and descriptions by Johann Jacob Moser (1701–1785), the Zettelkasten, a German word translated as “slip box”, is generally a collection of highly curated atomic notes collected on slips of paper or index cards. Zettelkasten were made simpler to create and maintain with the introduction of the mass manufacture of index cards (and card boxes and furniture) in the early 20th century.
> - Chris Aldrich [on the history of note-taking tools](https://boffosocko.com/2021/07/03/differentiating-online-variations-of-the-commonplace-book-digital-gardens-wikis-zettlekasten-waste-books-florilegia-and-second-brains/). 

There has been a renewed interest in Zettelkasten and related note-taking systems in recent years.  Common keywords in this space are [evergreen notes](https://notes.andymatuschak.org/Evergreen_notes), [second-brain](https://www.buildingasecondbrain.com/), [digital garden](https://maggieappleton.com/garden-history), and [personal knowledge management](https://en.wikipedia.org/wiki/Personal_knowledge_management). Some excellent public examples of these kind of note taking systems come from [Andy Matushack,](https://notes.andymatuschak.org/About_these_notes) and [Nitin Pai](https://notes.nitinpai.in/Sta), and [Joschua](https://notes.joschua.io/). 

Zettelkasten systems are typically used to construct and grow an inventory of your own thoughts and knowledge. Seeing as I did not invent most of the statistics discussed here, this note set deviates from this philosophy. Still, I think network-style note taking systems for technical subjects are an under-explored medium (for both research and pedagogy). So here we are. 

## Here's why you should start one: 

1. Writing your own notes is helpful. 
2. You can know a lot of material but not know how it's connected together. 
3. It helps you spot patterns. 
4. It helps you spot holes in the literature. 

# Who am I? 

I am [Ben](https://benchugg.com). I'm a PhD student in the machine learning and statistics program at CMU. I study things like [[sequential statistics]], [[e-value|e-values]], and [[concentration of measure]]. Occasionally I also read, write, and dance. 

This is my face. ![[images/me.jpg|center|300]] 