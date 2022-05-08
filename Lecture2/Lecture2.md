# Uncertainty

https://cs50.harvard.edu/ai/2020/notes/2/

---

Often, in reality, the AI has only partial knowledge of the world, leaving space for uncertainty. Still, we would like our AI to make the best possible decision in these situations.

## Probability

Uncertainty can be represented as a number of events and the likelihood, or probability, of each of them happening.

- Possible Worlds
    - Every possible situation can be thought of as a world, represented by the lowercase Greek letter omega ω. 
    - For example, rolling a die can result in six possible worlds: a world where the die yields a 1, a world where the die yields a 2, and so on. To represent the probability of a certain world, we write P(ω).

- Axioms of probability:
    - 0 <= P(ω) <= 1 (0 is an impossible event, 1 is a certain event)
    - Σ<sub>ω∈Ω</sub>P(ω) = 1 (summing up all of the probabilities P(ω) of the worlds ω that are in the set of all possible worlds Ω we ultimately get 1)
        - e.g. the probability of rolling a number R with a standard die can be represented as P(R). In our case, P(R) = 1/6, because there are six possible worlds (rolling any number from 1 through 6) and each is equally likely to happen. 
        - now, consider the event of rolling two dice. Now, there are 36 possible events, which are, again, equally as likely.
    - However, what happens if we try to predict the sum of the two dice? In this case, we have only 11 possible values (the sum has to range from 2 to 12), and they do not occur equally as often.
        - To get the probability of an event, we divide the number of worlds in which it occurs by the number of total possible worlds
            - e.g. there are 36 possible worlds when rolling two dice - only in one of these worlds, when both dice yield a 6, do we get the sum of 12. Thus, P(12) = 1/36, or, in words, the probability of rolling two dice and getting two numbers whose sum is 12 is 1/36. What is P(7)? We count and see that the sum 7 occurs in 6 worlds. Thus, P(7) = 6/36 = 1/6

- Unconditional probability
    - the degree of belief in a proposition in the absence of any other evidence. All the questions that we have asked so far were questions of unconditional probability, because the result of rolling a die is not dependent on previous events.

## Conditional probability

Conditional probability is the degree of belief in a proposition given some evidence that has already been revealed. AI can use partial information to make educated guesses about the future. To use this information, which affects the probability that the event occurs in the future, we rely on conditional probability.

- P(a | b) - probability that a is true given evidence b -> what is the probability of a given b
    - e.g. P(route change | traffic conditions), P(diseara | test results) etc.
- P(a | b) = P(a ^ b) / P(b)
    - algebraically equivalent forms:
        - P(a ^ b) = P(b)*P(a | b)
        - P(a ^ b) = P(a)*P(b | a)
    -  the probability that a given b is true is equal to the probability of a and b being true, divided by the probability of b. An intuitive way of reasoning about this is the thought “we are interested in the events where both a and b are true (the numerator), but only from the worlds where we know b to be true (the denominator).” Dividing by b restricts the possible worlds to the ones where b is true
- E.g. P(sum 12 | roll six on one die)
    - P(roll six on one die) = 1/6
    - P(sum 12) = 1/36
    = P(sum 12 | roll six on one die) = 1/36 / 1/6 = 1/6

## Random variables

- a random variable is a variable in probability theory with a domain of possible values that it can take on
    - e.g. a variable <b>roll</b> that can take on the values {1, 2, 3, 4, 5, 6} ; a variable <b>weather</b> with values {sun, cloud, rain, wind, snow} ; a variable <b>flight</b> with values {on time, delayed, cancelled}
- <b>probability distribution</b>
    - P(flight = on time) = 0.6
    - P(flight = delayed) = 0.3
    - P(flight = cancelled) = 0.1
    - a probability distribution can be represented more succinctly as a vector: <b>P</b>(flight) = <0.6, 0.3, 0.1>
        - for this notation to be interpretable, the values have a set order (in our case, on time, delayed, canceled).
- <b>independence</b> is the knowledge that the occurrence of one event does not affect the probability of the other event
    - e.g. P(a ^ b) = P(a)*P(b | a) - if a being true doesn't make a difference for b being true -> P(a ^ b) = P(a)*P(b)
    - independence can be defined mathematically: events a and b are independent if and only if the probability of a and b is equal to the probability of a times the probability of b: P(a ∧ b) = P(a)P(b).

## Bayes' Rule

- definition:
    - P(a ^ b) = P(b)*P(a | b)
    - P(a ^ b) = P(a)*P(b | a)
    - P(a)*P(b | a) = P(b)*P(a | b) -> P(b | a) = P(b)*P(a | b) / P(a)
- E.g. two events - cloudy in the AM, rain in the PM
    - given clouds in the morning, what is the probability of rain in the afternoon?
    - data:
        - 80% of rainy afternoons start with cloudy mornings
        - 40% of days have cloudy mornings
        - 10% of days have rainy afternoons
    - P(rain | clouds) = P(clouds | rain)*P(rain) / P(clouds) = (.8)(.1) / .4 = 0.2
- knowing P(cloudy morning | rainy afternoon) we can calculate P(rainy afternoon | cloudy morning)
- knowing P(visible effect | unknown cause) we can calculate P(unknown cause | visible effect) -> e.g. knowing P(medical test result | disease) we can calculate P(disease | medical test result) or knowing P(blurry text | counterfeit bill) we can calculate P(counterfeit bill | blurry text)


