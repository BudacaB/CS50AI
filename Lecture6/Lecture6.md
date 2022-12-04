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

## Naive Bayes

- another well suited approach for classification on positive / negative sentiment, or just trying to categorize some text in two possible categories
- based on Bayes' Rule (see bayesrule.png)
- calculate P(positive) or P(negative) - for example given 'My grandson loved it!' -> P(positive | 'My grandson loved it!')
  - P(positive | 'my', 'grandson', 'loved', 'it') - treat it as separate words
  - this <b>equals</b> P('my', 'grandson', 'loved', 'it' | positive) P(positive) / P('my', 'grandson', 'loved', 'it')
  - the denominator will be the same whether we look at positive or negative messages
    - then instead of equal to the above expression, you can say it's <b>proportional</b> just to P('my', 'grandson', 'loved', 'it' | positive) P(positive)
    - instead if getting the exact probability, you will figure out what the probability is proportional to and at the end you have to normalize the probability distribution - make sure it ultimately sums up to 1
  - now you can really calculate this as a joint probability of all of these things happening
    - P('my', 'grandson', 'loved', 'it' | positive) P(positive) -> is proportional to P(positive, 'my', 'grandson', 'loved', 'it')
  - calculating joint probabilities means multiplying all the conditional probabilities - e.g. P(a, b, c) -> P(a) * P(b | a) * P(c | a, b) etc.
  - this could get complicated, and this is where the 'naive' part comes in - you will assume that for example these words are going to effectively be independent of each other, if you know that it's already a positive message
    - basically it wouldn't matter, if it's a positive message, it doesn't change the probability that the word 'grandson' is in the message, if you know that the word 'loved' is in the message
    - that might not necessarily be true in practice, but you assume it to simplify the model, and it turns out that that simplification still gets you pretty good results
      - so you assume that the probability of all those words showing up, depends only on whether it's positive or negative
- ultimately you can say that P(positive | 'my', 'grandson', 'loved', 'it') is proportional to P(positive, 'my', 'grandson', 'loved', 'it') and <b>naively proportional</b> to P(positive)P('my' | positive)P('grandson' | positive)P('loved' | positive)P('it' | positive)
  - you can calculate these terms - given some data available
    - e.g. P(positive) = number of positive samples / number of total samples
    - e.g. P('loved' | positive) = number of positive samples with 'loved' / number of positive samples
  - P(positive)P('my' | positive)P('grandson' | positive)P('loved' | positive)P('it' | positive) and P(negative)P('my' | negative)P('grandson' | negative)P('loved' | negative)P('it' | negative) can be resolved to (see naivebayes.png)
  - these two values should be treated as a probability distribution, and you need to normalize them - i.e. sum them up, and then divide each value by the total - so that both of these values sum up to 1
  - you don't only get a classification, but also a probability for confidence - so Naive Bayes can achieve this just by using this 'bag of words' model
- one potential drawback is what happens if zeroes are inside this data somewhere - e.g. a word has never showed up inside you data for 'positive'
  - you need to make sure to never multiply by a zero

### Additive smoothing

- adding a value α to each value in your distribution to smooth out the data

### Laplace smoothing

- adding 1 to each value in our distribution: pretending we've seen each value one more time than we actually have

## Information retrieval

- the task of finding relevant documents in response to a user query

### Topic modeling

- models for discovering the topics for a set of documents

### Term frequency

- number of times a term appears in document

### Function words

- words that have little meaning on their own, but are used to grammatically connect other words - e.g. am, by, do, is, which, with, yet, the etc.
- the good part is that this is a pretty much fixed list of words in any lang

### Content words

- words that carry meaning independently
- even if they are not function words, some might still be very relevant - e.g. 'holmes' will come up most often in Holmes stories
- however you want to know the words that apper most in one story, and not in the others - to figure out what the story is about

### Inverse document frequency

- measure of how common or rare a word is across documents (see idf.png)
  - with this formula, if 'holmes' shows up in all the docs, then the result of the division will be 1 and log of 1 is 0
  - so if 'holmes' shows up in all the docs, it has an inverse document frequency of 0 - i.e. how rare does this word show up

### tf-idf

- ranking of what words are important in a document by multiplying term frequency (TF) by inverse document frequency (IDF)

## Semantics

- you are starting to go into the world of semantics - what it is that words actually mean when talking about lang
- now you don't think about a sample of text as a bag of words anymore, now you care what it is that these words actually mean, how it is these words relate to each other and in particular how you can extract info out of that text

### Information extraction

- the task of extracting knowledge from documents
- e.g. how can you extract when Facebook and Amazon were founded from two text samples from magazines which describe them
- this can be done looking for templates or patterns - things that happen to show up across multiple diff docs and which can give some sense as to what the info can mean
  - e.g. 'when Facebook / Amazon was founded in 2004 / 1994,'
  - these two templates give you a mechanism to extract info - 'When {company} was founded in {year},'
  - other e.g. 'The {book} was written by {author}' etc.
- given such templates AI can for example search the web, or a big corpus of docs etc. looking for templates that match and extract that info
- this would require you to figure out and write these templates - this type of method isn't going to be able to extract all the info due to small differences
  - instead of giving the AI templates, you can give AI the data - e.g. tell the AI that FB was found in 2004, and Amazon was founded in 1994 - and then set the AI loose on the web
  - now the AI can begin to look for where do FB and 2004 show up together, where do Amazon and 1994 show up together -> and then discover the templates for itself
  - the above templates can be figured out in this manner and then tried for others as well - this ends up being like an automated template generation
- this works in still pretty limited contexts tied to the templates that it can generate
- thinking about semantics, the better solution would be some way to be able to come up with definitions for all words, being able to relate all words in the dictionary to each other - you need some representation of what it is that words mean

## WordNet

- one approach is this famous dataset called WordNet - human curated - a bunch of words and their definition, their various different senses, and how those words relate to one another
- researchers have also curated relationships between these various different words
- this however doesn't scale particularly well however

## Word Representation

- so far you've defined a word through a sentence that explains what that word is - but you need some way to represent the meaning of a word so that the AI can do something useful with it
- throughout the course you've seen that when you want the AI to represent something, it can be helpful having the AI represent it using number
  - e.g. win / lose / draw in a game as 1, -1, or 0; turn data into a vector of features with a bunch of numbers etc.
  - if you ever want to pass words into a NN - e.g. given some word translate this sentence into another sentence, or do interesting classifications on individual words etc. - you need some representation of words just in terms of vectors
  - using individual numbers to define the meaning of a word
  - e.g. - encode 'He wrote a book.':
    - he [1, 0, 0, 0]
    - wrote [0, 1, 0, 0]
    - a [0, 0, 1, 0]
    - book [0, 0, 0, 1]

### one-hot representation

- representation of meaning as a vector with a single 1, and with other values as 0
- this is practical for only a few words, otherwise the vector would be huge
- another more subtle problem - the vector should represent meaning in a way that you can extract useful info
  - e.g. having 'He wrote a book.' and 'He authored a novel.' - 'wrote' and 'authored', 'book' and 'novel' are going to be totally different vectors that have nothing to do with eachother
    - wrote [0, 1, 0, 0, 0, 0, 0, 0, 0]
    - authored [0, 0, 0, 0, 1, 0, 0, 0, 0]
    - book [0, 0, 0, 0, 0, 0, 1, 0, 0]
    - novel [0, 0, 0, 0, 0, 0, 0, 0, 1]
  - you would like for 'wrote' and 'authored' to have vectors that are similar, same for 'book' and 'novel' - because they have similar meaning

### distributed representation

- representation of meaning distributed across multiple values
- same 'He wrote a book.', bigger vectors but less than for a one-hot representation approach total:
  - [-0.34, -0.08, 0.02, -0.18, …] (he)
  - [-0.27, 0.40, 0.00, -0.65, …] (wrote)
  - [-0.12, -0.25, 0.29, -0.09, …] (a)
  - [-0.23, -0.16, -0.05, -0.57, …] (book)
- this is going to be the goal of a lot of what the statistical machine learning approach to natural language processing is about - using these vector representations of words
- but how you define a word as just as a bunch of sequences of numbers, what does it mean? - a famous quote tries to answer this, from a British linguist:
  - 'You shall know a word by the company that it keeps' (J. R. Firth, 1957)
- you can define a word in terms of the words that show up around it, based on it's context
  - for ___ he ate - in English, it might be 'lunch', 'dinner' etc.
  - in order to define what does 'lunch' or 'dinner' mean, you can define it in terms of what words happen to show up around it - if a word shows up in a particular context and another word happens to show up in very similar contexts, then those two words are probably related

## word2vec

- model for generating word vectors
- you give it a corpus of docs - it will produce vectors for each word
- it has a few ways of doing this

### skip-gram architecture

- NN architecture for predicting context words given a target word (see sgarchitecture.png)
  - one input cell for each word - the NN can be trained
  - it will figure out context words using the same methods seen before - back-propagating the error from the context word back through this NN
  - what you get, for example using the single layer of hidden nodes - for every single one of the input words - you get 5 edges, each of which has a weight to each of the five hidden nodes - i.e. five numbers that are going to represent the target word
  - the number of hidden nodes can be customized - the resulting values will be the numerical vector representation of that word
  - the idea is that if two words are similar, the values chosen in the vectors, the numerical values for the weights of these edges, are probably going to be similar
    - high level, given a bunch of words (see words.png), you start with the random initialisation of weights, over time as you train the NN, you adjust the weights, the vector representation of each of these words so that gradually words that show up in similar context, grow close to one another, and words that show up in different contexts get further away (see words_weighted.png)
- now a very interesting part - because these are vectors, you can do math with them and calculate the relationship between various different words (see vector_diff.png)
  - e.g. two words - 'man' and 'king' - you can take these two vectors and subtract them from each other and get another vector (i.e. king - man)
    - this will tell you what you need to do to get from one word to the other
    - you can also take this new vector, and add it to another vector of a word -> e.g. (king - man) + woman, what will you get around this new vector?
      - e.g. with vectors.py - closest_word(words['king'] - words['man'] + words['woman']) -> 'queen'
      - e.g. with vectors.py - closest_word(words['paris'] - words['france'] + words['england']) -> 'london'
      - 