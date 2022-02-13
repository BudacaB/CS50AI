## Knowledge

https://cs50.harvard.edu/ai/2020/notes/1/

---

<b>knowledge-based agents</b> - agents that reason by operating on internal representations of knowledge

### Reasoning based on knowledge

<br>
Example of 3 facts inside a knowledge base:

- If it didn't rain, Harry visited Hagrid today.
- Harry visited Hagrid or Dumbledore today, but not both.
- Harry visited Dumbledore today.

We can conclude or draw these inferences:

- Harry did not visit Hagrid today
- It rained today

### Propositional Logic

- based on a logic of propositions, or statements about the world
- sentence - an assertion about the world in a knowledge representation language

### Proposition Symbols

- each symbol can represent some fact or sentence about the world, e.g.:
    - P - 'it is raining'
    - Q - 'Harry visited Hagrid today'
    - R - ...
- in addition to just having these individual facts about the world, we want some way to connect these propositional symbols together in order to reason more complexly about other facts that might exist inside of the world in which we're reasoning

### Logical Connectives

- not - negation - ¬ (or ~) A
- and - conjunction - A ^ B
- or - disjunction - A v B
- implies - implication - A -> b
- if and only if - biconditional - A <-> B
<br><br>

- <b>Not</b> (~) truth table:

| P | ~P |
| ---- | ----- |
| false |  true | 
| true | false |

- <b>And</b> (^):

| P | Q | P ^ Q |
| ---- | ----- | ----- |
| false |  false | false |
| false | true | false |
| true | false | false |
| true | true | true |

- <b>Or</b> (v):

| P | Q | P v Q |
| ---- | ----- | ----- |
| false |  false | false |
| false | true | true |
| true | false | true |
| true | true | true |

- <b>Implication</b> (->):

| P | Q | P -> Q |
| ---- | ----- | ----- |
| false |  false | true |
| false | true | true |
| true | false | false |
| true | true | true |

E.g.: If it is raining, I am indoors. <br>
- If the proposition (P) is true, then the conclusion (Q) also needs to be true. <br>
- But if P is false, the implication makes no claim at all, it doesn't matter what Q is. E.g. 'If it is raining, I am indoors.' and it turns out it's not raining, it doesn't matter if the implication is true or false.

- <b>Biconditional</b> (<->)

| P | Q | P <-> Q |
| ---- | ----- | ----- |
| false |  false | true |
| false | true | false |
| true | false | false |
| true | true | true |

E.g.: I will be indoors if and only if it is raining. So if it is raining, I will be indoors; and if I am indoors it's reasonable to conclude that it is raining.

--- 

<b>model</b> - assignment of a truth value (where a truth value is either true or false) to every propositional symbol (a 'possible world') <br>
- E.g.: <br>
P: It is raining. <br>
Q: It is a Tuesday. <br>
Sample: {P=true, Q=false} - in this model, in other words in this possible world, it is possible that P is true, meaning it is raining, and Q is false, meaning it is not a Tuesday.

- For N variables that are propositional symbols like this, that are either true or false, then the number of possible models is 2<sup>N</sup>

<b>knowledge base</b> - a set of sentences in propositional logic known by a knowledge-based agent / that the AI knows about the world
- the AI would use that info in the knowledge base to be able to draw conclusions about the rest of the world
- to understand those conclusions we need to introduce one more idea, one more symbol

### Entailment

α ⊨ β - alpha entails beta (alpha and beta are sentences in propositional logic)

- in every model in which sentence α is true, sentence β is also true
- E.g. If alpha is something like 'I know that it is a Tuesday in January', then a reasonable beta might be something like, 'I know that it is January' - because in all worlds, where it is a Tuesday in January, I know for sure that it must be January, just by definition.
    - the first statement, or sentence about the world, entails the second statement - we can reasonably use deduction, based on that first sentence, to figure out that the second sentence is, in fact, true as well (like the Harry Potter example in the beginning)

<b>inference</b> - the process of deriving new sentences from old ones

- E.g.:
    - P: It is a Tuesday
    - Q: It is raining
    - R: Harry will go for a run

    - KB (knowledge base): 
        - (P ^ ~Q) -> R ; P and not Q implies R => if it is a Tuesday and it's not raining, then Harry will go for a run
        - P - it is a Tuesday
        - ~Q - it is not raining
    - Inference: 
        - P and ~Q is true only if both P and not Q are true 
        - both P and not Q are true
        - by implication, if the left side is true then the right side must also be true
        - <b>R - Harry will go for a run</b>

### Inference Algorithms