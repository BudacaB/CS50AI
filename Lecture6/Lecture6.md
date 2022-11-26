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
