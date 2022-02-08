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

- not - negation - ~ A
- and - conjunction - A ^ B
- or - disjunction - A V B
- implies - implication - A -> b
- if and only if - biconditional - A <-> B
<br><br>

- <b>Not</b> (~) truth table:

| P | ~P |
| ---- | ----- |
| false |  true | 
| true | false |