# Language

https://cs50.harvard.edu/ai/2020/notes/6/

---

## Natural Language Processing

- automatic summarization
- info extraction
- language identification
- machine translation
- named entity recognition
- speech recognition
- text classification
- word sense disambiguation
- ...

## Syntax and semantics

- <b>Syntax</b> is sentence structure. As native speakers of some human language, we don’t struggle with producing grammatical sentences and flagging non-grammatical sentences as wrong. 
For example, the sentence “Just before nine o’clock Sherlock Holmes stepped briskly into the room” is grammatical, whereas the sentence “Just before Sherlock Holmes nine o’clock stepped briskly the room” is non-grammatical. 
Syntax can be grammatical and ambiguous at the same time, as in “I saw the man with the telescope.” Did I see (the man with the telescope) or did I see (the man), doing so by looking through the telescope? 
To be able to parse human speech and produce it, the AI needs to command syntax.
- <b>Semantics</b> is the meaning of words or sentences. While the sentence “Just before nine o’clock Sherlock Holmes stepped briskly into the room” is syntactically different from “Sherlock Holmes stepped briskly into the room just before nine o’clock,” their content is effectively identical. 
Similarly, although the sentence “A few minutes before nine, Sherlock Holmes walked quickly into the room” uses different words from the previous sentences, it still carries a very similar meaning. 
Moreover, a sentence can be perfectly grammatical while being completely nonsensical, as in Chomsky’s example, “Colorless green ideas sleep furiously.” To be able to parse human speech and produce it, the AI needs to command semantics.

## Formal grammar

- a system of rules for generating sentences in a language

## Context-free grammar

- generating sentences in a language via 'rewriting rules' - replacing a symbol with other symbols
  - e.g. - she saw the city - each word is a 'terminal symbol' - will be associated with a 'non-terminal symbol'
  - she saw the city - N V D N - noun, verb, determiner, noun
  - to translate these non-terminal symbols into terminal symbols, you have what are known as rewriting rules, e.g.:

N -> she | city | car | Harry | ...

D -> the | a | an | ...

V - > saw | ate | walked | ...

P -> to | on | over | ...

AJD -> blue | busy | old | ...

NP (noun-phrase) -> N | ND

VP (verb phrase) -> V | V NP

etc.

S (sentence) -> NP VP (see syntactictree.png)

### n-gram

- a contiguous sequence of <em>n</em> items from a sample of text

### character n-gram

- a contiguous sequence of <em>n</em> characters from a sample of text

### word n-gram

- a contiguous sequence of <em>n</em> words from a sample of text

### unigram

- a contiguous sequence of 1 item from a sample of text

### bigram

- a contiguous sequence of 2 items from a sample of text

### trigram

- a contiguous sequence of 1 item from a sample of text

E.g. what are the trigrams that we can extract from this sentence:

“How often have I said to you that when you have eliminated the impossible whatever remains, however improbable, must be the truth?”

- the AI might've not seen this sentence before, but it might have a seen a trigram like e.g. 'to you that'

### tokenization

- the task of splitting a sequence of characters into pieces (tokens)

### word tokenization

- the task of splitting a sequence of characters into words

## Markov Models

- recall that it refers to some sequence of events that happen one time step after one time step, where every unit has some ability
to predict what the next unit is going to be (or maybe the past two units predict what the next unit is going to be, or the past three etc.)
- you can use a Markov Model and apply it to language for a very naive and simple approach, trying to generate natural language - getting the AI to be able to speak English like text
- how it's going to work - come up with some probability distribution - given two words, what is the probability distribution over what the third word could possibly be based on all the data
- if you keep doing this, your Markov Model can effectively start to generate text that was not in the original corpus, but that sounds kind'a like the original corpus


## Text Categorization

- really a classification problem - e.g. decide where an email belongs - inbox or spam, based on words that show up in the email
  - e.g. analyse if a text has a positive or negative sentiment for reviews (see reviews.png)

### bag-of-words model

- model that represents text as an unordered collection of words - you don't care about order - good for sentiment classifications

## Naive Bayes (see bayesrule.png)

- another well suited approach for classification on positive / negative sentiment, or just trying to categorize some text in two possible categories
- 


