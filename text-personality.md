<!--
Title: Literature review regarding the association between personality and language use
Author: Yiming Li
-->
#Associating language with personality: an informal literature review 

*By <a href="http://www.google.com/recaptcha/mailhide/d?k=01csXFRp7K1dsFA4c9tNF-_g==&amp;c=SPBmIG77uJ7ktz_OiFkTkA==" onclick="window.open('http://www.google.com/recaptcha/mailhide/d?k\x3d01csXFRp7K1dsFA4c9tNF-_g\x3d\x3d\x26c\x3dSPBmIG77uJ7ktz_OiFkTkA\x3d\x3d', '', 'toolbar=0,scrollbars=0,location=0,statusbar=0,menubar=0,resizable=0,width=500,height=300'); return false;" title="Reveal this e-mail address">Yiming Li</a>; last updated 27 Mar 2017*

#Table of contents

[TOC]

#Short summary

##Benchmark data sets and other resources

[Linguistic Inquiry and Word Count](https://liwc.wpengine.com/) (LIWC) is used in almost all the analyses for characterising text data.

[The Big Five](https://en.wikipedia.org/wiki/Big_five_personality_traits) (along with its derivative [Big Five Aspect Scales](https://en.wikipedia.org/wiki/Big_Five_Aspect_Scales)) is widely used as a measure for personality.

##Quick summary of the results in the reviewed papers

Personality features more related to language use:

* The Big Five
    * ==Openness== (Scales: Openness/Creativity and Intellect)
    * ==Agreeableness== (Scales: Politeness and Compassion)
    * Extraversion (Scales: Enthusiasm and ==Assertiveness==)
    * Conscientiousness (Scales: Orderliness and Industriousness)
    * Neuroticism (Scales: Withdrawal and Volatility)
* Other attributes
    * Being depressive
    * Aspiration
    * Being dissociative
    * etc.

Language features more related to personality:

* Word-wise
    * Vocabulary
    * Emotionally loaded words
    * Category
        * Certainty, physical, body, sexuality, etc.
* Sentence-wise
    * Usage of future tense
    * Negations
    * Quantifiers
    * Punctuation
        * Exclamation marks
* Others
    * Self-references

#Thoughts

##Defining personality, emotions and memory in our context

What is "personality"?

A bot's ***memory*** simply consists of the previous user inputs to the algorithm (along with its pre-defined "life events").

##Proposed pseudo-algorithm

I think we could directly extract text features from the conclusions (e.g. significant word usage pattern associated with personalities) of the papers, and next try to implement a "translator" based on these features, i.e. after "translation", the sentence would be transformed so that the pattern associated with the input features are included.

The engine could be summarized as:

~~~
Engine for "translation"

1. Input
    * From user
        * Sentence for translation y
        * Personality features pf
    * (Constant) From literature
        * A set of rules A defining mapping (or rather, association) between personality and text features
2. Algorithm: To be decided
3. Output
    * New sentence z "loaded with" personality
~~~

This could be further wrapped up in a chatbot engine:

~~~
Engine for chatbot

1. Input
    * From user
        * Sentence in dialog x
        * Personality features pf
    * (Constant) From literature
        * A set of rules A defining mapping (or rather, association) between personality and text features
2. Algorithm for generating response (plenty available)
    * Input: x
    * Output: a personality-wise neutral response w
3. Engine for "translation"
    * Input: w as y, pf and A
    * Output: z
4. Output z as the response "loaded with" personality
~~~

#Detailed summary

The PDF files for all the papers are also embedded in this page for easy download.

##Personality vs. language

All these papers mainly do research on the **association** between personality and language.

The findings could be interpreted in two ways:

* How **language reflects personality**
    * Analogous to sentiment analysis, just that it is in terms of personality and not positiveness, mood, etc.
* How **personality influences language**
    * If we would like to write a "personality translator", this is more relevant.

The papers are ordered (subjectively) according to decreasing usefulness (with the papers I have not gone through at the end).

###Personality in 100,000 Words: A large-scale analysis of personality and word use among bloggers

Yarkoni, Tal. "Personality in 100,000 words: A large-scale analysis of personality and word use among bloggers." *Journal of research in personality* 44.3 (2010): 363-373.

Very comprehensive.

* Main direction: **Language &harr; personality**
* Personality features
    * [The Big Five](https://en.wikipedia.org/wiki/Big_five_personality_traits) with facet-level scores
* Text features
    * Blogging data
        * [Linguistic Inquiry and Word Count](https://liwc.wpengine.com/) (LIWC)
* Methods
    * Correlation between text feature scores and personality scores
    * Word-based analysis: top words associated with personality traits are identified
* Conclusions
    * Please c.f. Tables 1-3 in the article.
    * Usage of **emotional words** are related to personality
    * Personality is related to preferred blog genre
        * **Extraversion** and **agreeableness** were more accurately judged with journal entries
        * **Conscientiousness** and **emotional stability** were more accurately judged with commentary entries

###Personality as manifest in word use: Correlations with self-report, acquaintance report, and behavior

Fast, Lisa A., and David C. Funder. "Personality as manifest in word use: correlations with self-report, acquaintance report, and behavior." *Journal of personality and social psychology* 94.2 (2008): 334.

This is interesting in that it does not actually use [the Big Five](https://en.wikipedia.org/wiki/Big_five_personality_traits) as the measurement for personality.

* Main direction: **Language &harr; personality**
* Personality features
    * [The Riverside Accuracy Project–Phase II](http://www.rap.ucr.edu/) (RAP-II) data set (The California Adult Q-set / The Riverside Behavioral Q-sort)
* Text features
    * Life history interview
        * [Linguistic Inquiry and Word Count](https://liwc.wpengine.com/) (LIWC)
* Methods
    * Extract significant word categories related to personality ratings and check what categories of word use have a similar pattern of personality correlates across gender
    * Calculate correlation between **certainty** / **sexuality word** use and personality features
* Conclusions
    * Please c.f. Tables 2-5 in the article.
        * The usage of **certainty**, **physical**, **body**, and **sexuality words** is more related to personality.
    * The usage of **sad words** and **self-references** is more related to personality.
        * More sad words and self-references &rarr; more depressive
        * Notice that, though, "use of sad words correlates with being socially undesirable (e.g. expresses hostility and does not smilefrequently), whereas use of self-references correlates with being socially desirable (e.g. enthusiastic, cheerful, and warm)".

###Predicting personality from Twitter

Golbeck, Jennifer, et al. "Predicting personality from twitter." *2011 IEEE Third International Conference on Privacy, Security, Risk and Trust and 2011 IEEE Third International Conference on Social Computing*, 2011.

An IEEE conference paper, more computational and leaning towards prediction.

* Main direction: **Language &rarr; personality**
* Personality features
    * [The Big Five](https://en.wikipedia.org/wiki/Big_five_personality_traits)
* Text features
    * Twitter data 
        * [Linguistic Inquiry and Word Count](https://liwc.wpengine.com/) (LIWC)
        * [MRC Psycholinguistic Database](http://websites.psychology.uwa.edu.au/school/MRCDatabase/uwa_mrc.htm)
        * Word-by-word sentiment analysis using the [General Inquirer](http://www.wjh.harvard.edu/~inquirer/) dataset
        * Twitter-related features, e.g. number of hashtags, words or links per tweet
* Methods
    * Pearson correlation between text feature scores and personality scores
    * Regression (Gaussian process and ZeroR)
* Conclusions
    * Please c.f. Table II. in the article.
    * Able to predict scores on each of the five personality traits to within 11% - 18% of their actual value.
      * **Openness** and **agreeableness** have the best results.

###Birds of a feather: How personality influences blog writing and reading

Li, Jamy, and Mark Chignell. "Birds of a feather: How personality influences blog writing and reading." *International Journal of Human-Computer Studies* 68.9 (2010): 589-602.

This paper also uses blog genre as a text feature.

* Main direction: **Language &harr; personality**
* Personality features
    * [The Big Five](https://en.wikipedia.org/wiki/Big_five_personality_traits)
* Text features
    * Blogging data 
        * [Linguistic Inquiry and Word Count](https://liwc.wpengine.com/) (LIWC)
        * Blog genre
* Methods
    * Correlation between text feature scores and personality scores
    * ANOVA (for blog genre)
* Conclusions
    * Usage of **emotional words** are related to personality
    * Personality is related to preferred blog genre
        * **Extraversion** and **agreeableness** were more accurately judged with journal entries
        * **Conscientiousness** and **emotional stability** were more accurately judged with commentary entries

###Personality and language use in self-narratives

Hirsh, Jacob B., and Jordan B. Peterson. "Personality and language use in self-narratives." *Journal of research in personality* 43.3 (2009): 524-527.

Rather short.

* Main direction: **Language &harr; personality**
* Personality features
    * The [Big Five Aspect Scales](https://en.wikipedia.org/wiki/Big_Five_Aspect_Scales)
* Text features
    * Writing exercise data 
        * [Linguistic Inquiry and Word Count](https://liwc.wpengine.com/) (LIWC)
* Methods
    * Correlation between text feature scores and personality scores
* Conclusions
    * Please c.f. Tables 1-2 in the article.
    * Personality traits appear significantly and strongly related to**patterns of word use** during the **telling of the past** and the **planning of the future**

###Personality, attitudes, and affect as predictors of second language communication

`Not yet read.`

MacIntyre, Peter D., and Catherine Charos. "Personality, attitudes, and affect as predictors of second language communication." *Journal of language and social psychology* 15.1 (1996): 3-26.

One of the more ancient papers.

###What are they blogging about? Personality, topic and motivation in blogs

`Not yet read.`

Gill, Alastair J., Scott Nowson, and Jon Oberlander. "What Are They Blogging About? Personality, Topic and Motivation in Blogs." *ICWSM*. 2009.

##Mood effects vs. language

All these papers mainly do research on the association between mood and language.

###On feeling good and being rude: Affective influences on language use and request formulations

`Not yet read.`

Forgas, Joseph P. "On feeling good and being rude: Affective influences on language use and request formulations." *Journal of Personality and Social Psychology* 76.6 (1999): 928.

