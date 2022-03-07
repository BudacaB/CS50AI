# Knowledge

https://cs50.harvard.edu/ai/2020/notes/1/

---

<b>knowledge-based agents</b> - agents that reason by operating on internal representations of knowledge

## Reasoning based on knowledge

<br>
Example of 3 facts inside a knowledge base:

- If it didn't rain, Harry visited Hagrid today.
- Harry visited Hagrid or Dumbledore today, but not both.
- Harry visited Dumbledore today.

We can conclude or draw these inferences:

- Harry did not visit Hagrid today
- It rained today

## Propositional Logic / Logical deduction

- based on a logic of propositions, or statements about the world
- sentence - an assertion about the world in a knowledge representation language

## Proposition Symbols

- each symbol can represent some fact or sentence about the world, e.g.:
    - P - 'it is raining'
    - Q - 'Harry visited Hagrid today'
    - R - ...
- in addition to just having these individual facts about the world, we want some way to connect these propositional symbols together in order to reason more complexly about other facts that might exist inside of the world in which we're reasoning

## Logical Connectives

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

## Entailment

α |= β - alpha entails beta (alpha and beta are sentences in propositional logic)

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

## Inference Algorithms

- Does KB |= α ? (using the knowledge that we have access to, can we conclude that this sentence α is true?)
- There are a couple of algorithms for checking this, and perhaps one of the simplest is known as model checking


### Model checking

- Model - just some assignment of all of the propositional symbols inside of our language to a truth value, true or false
    - like a possible world ; there are many possible worlds where different things might be true or false and we can enumerate all of them - the <b>model checking algorithm</b> does exactly that
- To determine if KB |= α:
    - enumerate all possible models
    - if in every model where KB is true, α is also true, <b>then KB entails α</b>
    - otherwise, KB does not entail α
- Example:
    - Description:
        - P: It is a Tuesday
        - Q: It is raining
        - R: Harry will go for a run
    - KB: 
        - (P ^ ~Q) -> R
        - P
        - ~Q
    - Query: R (the thing we want to ask - α - is it entailed that Hary will go for a run)
    - We have 2<sup>3</sup> possible models
    - In which of this worlds is our KB true

| P | Q | R | KB |
| ---- | ----- | ----- | ----- |
| false |  false | false | false |
| false | false | true | false |
| false | true | false | false |
| false | true | true | false |
| true |  false | false | false |
| true | false | true | true |
| true | true | false | false |
| true | true | true | false |

## Knowledge Engineering

- If confronted with a problem where some sort of logical deduction can be used in order to try to solve it, you might try thinking about what propositional symbols you might need in order to represent that information, and what statements and propositional logic you might use to encode that info which you know
- This process of taking a problem and trying to figure out what propositional symbols to use in order to encode that idea, or how to represent it logically is known as knowledge engineering
- Software engineers and AI engineers will take a problem and try to figure out how to distill it down into knowledge that is representable by a computer
- If we can take any general purpose problem, some problem that we find in the human world and turn it into a problem that computers know how to solve, as by using any number of different variables, then we can take a computer that is able to do something like model checking or some other inference algorithm and actually figure out how to solve that problem

### Clue (game)

- Propositional symbols:
    - people:
        - mustard
        - plum
        - scarlet
    - rooms:
        - ballroom
        - kitchen
        - library
    - weapons:
        - knife
        - revolver
        - wrench
- Knowledge:
    - (mustard v plum v scarlet)
    - (ballroom v kitchen v library)
    - (knife v revolver v wrench)
    - ~ plum (for e.g. if the plum card is in my hand, plum can't be the killer)
    - ~ mustard v ~ library v ~ revolver (for e.g. if someone guesses that it's col. mustard, in the library with a revolver and it's wrong)

### Logical puzzles

- Initial knowledge:
    - Gilderoy, Minerva, Pomona and Horace each belong to a different one of the four houses: Gryffindor, Hufflepuff, Ravenclaw, and Slytherin House
    - Gilderoy belongs to Gryffindor or Ravenclaw
    - Pomona does not belong in Slytherin
    - Minerva belongs to Gryffindor

- Propositional symbols:
    - GilderoyGryffindor
    - GilderoyHufflepuff
    - GilderoyRavenclaw
    - GilderoySlytherin
    - MinervaGryffindor
    - MinervaHufflepuff
    - MinervaRavenclaw
    - MinervaSlytherin
    - PomonaGryffindor
    - PomonaHufflepuff
    - PomonaRavenclaw
    - PomonaSlytherin
    - HoraceGryffindor
    - HoraceHufflepuff
    - HoraceRavenclaw
    - HoraceSlytherin

- Types of logical sentences we can say about the puzzle, examples:
    - (PomonaSlytherin -> ~PomonaHufflepuff) - each one person can be in only one house
    - (MinervaRavenclaw -> ~GilderoyRavenclaw) - each person must be in a different house

- Received knowledge example:
    - (GilderoyGryffindor v GilderoyRavenclaw)

## Inference Rules

- Some sort of rules that we can apply to take knowledge that already exists and translate it into new forms of knowledge
- E.g. (using a line - above the line are premises, something that we know to be true, and anything below the line will be the conclusion that we can arrive at after applying the logic):

If it is raining, then Harry is inside <br>
It is raining

```---------------------------```

Harry is inside

- This is called <b>Modus Ponens</b> (inference rule)

α -> β <br>
α

```---------------------------```

β

- More examples:

Harry is friends with Ron and Hermione <br>

```---------------------------```

Harry is friends with Hermione

- This inference rule is known as <b>And Elimination</b>

α ^ β <br>

```---------------------------```

α

- More examples:

It is not true that Harry didn't pass the test <br>

```---------------------------```

Harry passed the test

- This is called <b>Double Negation Elimination</b>

~ (~α) <br>

```---------------------------```

α

- More examples:

If it is raining, then Harry is inside <br>

```---------------------------```

It is not raining or Harry is inside

- This is know as <b>Implication Elimination</b> - translate <em>if/then</em> statements into <em>or</em> statements (either alpha is true or alpha is not true; so either alpha is not true, or alpha is true, in which case beta is also true)

α -> β <br>

```---------------------------```

~α v β