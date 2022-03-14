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

- This is known as <b>Implication Elimination</b> - translate <em>if/then</em> statements into <em>or</em> statements (either alpha is true or alpha is not true; so either alpha is not true, or alpha is true, in which case beta is also true)

α -> β <br>

```---------------------------```

~α v β

- More examples:

It is raining if and only if Harry is inside <br>

```---------------------------```

If it is raining, then Harry is inside, and if Harry is inside, then it is raining

- This is known as <b>Biconditional Elimination</b> 

α <-> β <br>

```---------------------------```

(α -> β) ^ (β -> α)

- More examples:

It is not true that both Harry and Ron passed the test <br>

```---------------------------```

Harry didn't pass the test, or Ron didn't pass the test

- This type of law is knows as <b>De Morgan's Law</b> - turning an 'and' into an 'or' (the negation moves inwards and the 'and' is flipped to an 'or')

~(α ^ β) <br>

```---------------------------```

~α v ~β

- A reverse of <b>De Morgan's Law</b>:

It is not true that Harry or Ron passed the test <br>

```---------------------------```

Harry didn't pass the test and Ron didn't pass the test

<br>

~(α v β) <br>

```---------------------------```

~α ^ ~β

- <b>Distributive Property</b>

(α ^ (β v γ)) <br>

```---------------------------```

(α ^ β) v (α ^ γ)

- <b>Reverse Distributive Property</b>

(α v (β ^ γ)) <br>

```---------------------------```

(α v β) ^ (α v γ)

## Search Problems

- initial state
- actions
- transition model
- goal test
- path cost function

## Theorem proving

- initial state: starting knowledge base
- actions: inference rules
- transition model: new knowledge base after inference
- goal test: check statement we're trying to prove
- path cost function: number of steps in proof

## Resolution

- A powerful inference rule
- Resolution relies on <b>Complementary Literals</b>, two of the same atomic propositions where one is negated and the other is not, such as P and ~P.

(Ron is in the Great Hall) v (Hermione is in the library) <br>
Ron is not in the Great Hall

```---------------------------```

Hermione is in the library

<br>

P v Q <br>
~P

```---------------------------```

Q

- It also applies for multiple propositional symbols chained together in a single <em>clause</em>

P v Q<sub>1</sub> v Q<sub>2</sub> v ... v Q<sub>n</sub> <br>
~P

```---------------------------```

Q<sub>1</sub> v Q<sub>2</sub> v ... v Q<sub>n</sub>

- Another property of this resolution rule:

(Ron is in the Great Hall) v (Hermione is in the library) <br>
(Ron is not in the Great Hall) v (Harry is sleeping)

```---------------------------```

(Hermione is in the library) v (Harry is sleeping)

<br>

P v Q <br>
~P v R

```---------------------------```

Q v R

<br>

P v Q<sub>1</sub> v Q<sub>2</sub> v ... v Q<sub>n</sub> <br>
~P v R<sub>1</sub> v R<sub>2</sub> v ... v R<sub>m</sub>

```---------------------------```

Q<sub>1</sub> v Q<sub>2</sub> v ... v Q<sub>n</sub> v R<sub>1</sub> v R<sub>2</sub> v ... v R<sub>m</sub>

---

- <b>Clause</b> - a disjunction of literals - e.g. P v Q v R
    - disjunction - connected with 'or'
    - conjunction - connected with 'and'
    - literal - a propositional symbol or its opposite

- <b>Conjunctive normal form (CNF)</b> - logical sentence that is a conjunction of clauses - e.g. (A v B v C) ^ (D v ~E) ^ (F v G)

---

## Conversion to CNF

- What is the process for taking a logical formula and converting it into CNF?
    - eliminate biconditionals
        - turn (α <-> β) into (α -> β) ^ (β -> α)
    - eliminate implications
        - turn (α -> β) into turn ~α v β
    - move ~ inwards using De Morgan's Laws
        - turn ~(α ^ β) into ~α v ~β
    - use distributive law to distribute v wherever possible

- Example (P v Q) -> R:
    - eliminate implication ~(P v Q) v R
    - De Morgan's Law (~P ^ ~Q) v R
    - distributive law (~P v R) ^ (~Q v R) - this is now in <em>conjunctive normal form</em>

## Inference by Resolution (using the resolution rule to draw some sort of inference)

- once we have the above clauses in this form, these clauses are the inputs to the resolution inference rule - if I have two clauses where there's something that conflicts or something complementary between these two clauses, I can resolve them to get a new clause, to draw a new conclusion - we call this <b>inference by resolution</b>

P v Q <br>
~P v R

```---------------------------```

(Q v R)

- redundancy:


P v Q v S <br>
~P v R v S

```---------------------------```

(Q v S v R v S) - factoring this to (Q v R v S)

- empty clause (basis for the inference by resolution algorithm):

P <br>
~P

```---------------------------```

() - equivalent to just being false

- How to perform inference by resolution at a high level:
    - to determine if KB |= α:
        - check if (KB ^ ~α) is a contradiction? - this is a common idea in CS, proving something by contradiction - by first assuming that it is false, and showing that it would be contradictory, then it must be true
            - if so, then KB |= α
            - otherwise, no entailment

- to determine if KB |= α (resolution algorithm):
    - convert (KB ^ ~α) to CNF
    - keep checking to see if we can use resolution to produce a new clause
        - if ever we produce the empty clause (equivalent to False), we have a contradiction, and <b>KB |= α</b>
        - otherwise, if we can't add new clauses, no entailment

- Example:

Does (A v B) ^ (~B v C) ^ (~C) entail A?

- Solving:
    - assume A is false and see if that leads to a contradiction
        - (A v B) ^ (~B v C) ^ (~C) ^ (~A)
            - (~B v C) ^ (~C) resolve to ~B
            - (A v B) and ~B resolve to A
            - (~A) and (A) resolve to () - false so we have a contradiction, so A is true

- Instead of enumerating all the possibl worlds that we might be in in order to try to figure out in which cases is our KB true and in which cases our query is true, we can instead use this resolution algorithm, to keep trying to figure out what conclusions we can draw and see if we reach a contradiction
    - if we reach a contradiction that tells us something about whether our knowledge actually entails the query or not

## First-Order Logic

- A bit more powerful than propositional logic and it makes it easier to express certain types of ideas
- <b>Propositional Logic / propositional symbols</b>:
    - MinervaGryffindor
    - MinervaHufflepuff
    - MinervaRavenclaw
    - MinervaSlytherin
    - ...
- <b>First-Order Logic</b>
    - Constant symbol:
        - Minerva
        - Pomona
        - Horace
        - Gilderoy
        - Gryffindor
        - Hufflepuff
        - Ravenclaw
        - Slytherin
    - Predicate symbol (properties that might hold true or false of the individual constants - like an evaluation function):
        - Person
        - House
        - BelongsTo
- Examples of sentences in first-order logic:
    - Person(Minerva) - Minerva is a person
    - House(Gryffindor) - Gryffindor is a house
    - ~House(Minerva) - Minerva is not a house
    - BelongsTo(Minerva, Gryffindor) - Minerva belongs to Gryffindor
- First-order logic gives us a couple of additional features that we can use to express even more complex ideas - quantifiers

### Quantifiers

- Universal quantification - let's me express an idea like something is going to be true for all values of a variable
    - ∀x. BelongsTo(x, Gryffindor) -> ~BelongsTo(x, Hufflepuff)
        - for all values of x, if x belongs to Gryffindor then x does not belong to Hufflepuff / anyone in Gryffindor is not in Hufflepuff

- Existential quantification - says that some expression is going to be true for some value of a variable (at least one value of that variable)
    - ∃x. House(x) ^ BelongsTo(Minerva, x)
        - there exists an object x such that x is a house and Minerva belongs to x / Minerva belongs to a house
- Combining the two
    - ∀x. Person(x) -> (∃y. House(y) ^ BelongsTo(x, y))
        - for all objects x, if x is a person, then there exists an object y such that y is a house and x belongs to y / every person belongs to a house