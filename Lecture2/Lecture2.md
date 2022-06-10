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

## Joint probability

Joint probability is the likelihood of multiple events all occurring.

- E.g. let's consider these probability distributions:
    - clouds in the morning: c = cloud 0.4 ; c = ¬cloud 0.6
    - rain in the afternoon: r = rain 0.1 ; r = ¬rain 0.9
    - joint probability distribution:
    
    |  | r = rain | r = ¬rain |
    | ---- | ----- | ----- |
    | c = cloud |  0.08 | 0.32 |
    | c = ¬cloud | 0.02 | 0.58 |

    - for the probability distribution of P(c | r):
        - P(c | r) = P(c, r) / P(r) 
            -  <em>comma can be used for ^ (and)</em>
            - P(r) - a numerical constant used for the division, or put another way, for the multiplication with its inverse
        - to simplify mathematically: αP(c, r)
        - so the conditional distribution of c given r <em>P(c | r)</em> is proportional to (using a factor α for multiplication) the joint probability distribution of c and r <em>P(c, r)</em>
        - αP(c, r) = α<0.08, 0.02>
        - in a probability distribution, if you consider all of the possible values, they must sum up to a probability of 1 -> the constant for α to 'normalize' our values is 10 -> <0.8, 0.2>

## Probability rules

- Negation: P(¬a) = 1 - P(a)
- Inclusion-Exclusion: P(a v b) = P(a) + P(b) - P(a ^ b)
    - Here is an example from outside lecture that can elucidate this. Suppose I eat ice cream 80% of days and cookies 70% of days. If we’re calculating the probability that today I eat ice cream or cookies P(ice cream ∨ cookies) without subtracting P(ice cream ∧ cookies), we erroneously end up with 0.7 + 0.8 = 1.5. This contradicts the axiom that probability ranges between 0 and 1. To correct for counting twice the days when I ate both ice cream and cookies, we need to subtract P(ice cream ∧ cookies) once
- Marginalization: P(a) = P(a, b) + P(a, ¬b)
    - how do I figure out the probability of a, using some other variable that I might have access to like b?
    - using disjoint events - either b happens or b doesn't happen
    - Marginalization can be expressed for random variables the following way:
        - P(X = x<sub>i</sub>) = Σ<sub>j</sub>P(X = x<sub>i</sub>, Y = y<sub>j</sub>)
            - if we have two random variables, X and Y, the probability of X being equal to some value x<sub>i</sub> can be figured out by summing up over j (where j is going to range over all of the possible values that Y can take on) all of the possible cases for this joint probability distribution - that X takes the value that I care about given all of the possible values for Y -> we can get the unconditional probability of what X is equal to
            - e.g. from before P(c = cloud) = P(c = cloud, r = rain) + P(c = cloud, r = ¬rain) = 0.08 + 0.32 = 0.4.
- Conditioning: P(a) = P(a | b)P(b) + P(a | ¬b)P(¬b)
    - similar to marginalization, for two events a and b, but instead of having access to their joint probabilities, we have access to their <em>conditional probabilities</em> i.e. how they relate to eachother
        - for random variables that can take on multiple possible values in a domain of possible values, conditioning that this equivalent rule:
        P(X = x<sub>i</sub>) = Σ<sub>j</sub>P(X = x<sub>i</sub> | Y = y<sub>j</sub>)*P(Y = y<sub>j</sub>)
            - again there is a summation over all of the possible values that some random variable Y can take on between the chance that Y takes on some value and multiply it by the conditional probability that X takes on a value x<sub>i</sub> given that Y took on that value y<sub>j</sub>

## Bayesian network

Data structure that represents the dependencies among random variables

- Description:
    - directed graph
    - each node represents a random variable
    - arrow from X to Y means X is a parent of Y
    - each node X has a probability distribution <b>P</b>(X | Parents(X))
- E.g. - see bayesiannetwork.png
    - probability distribution for the root node Rain

    | none | light | heavy |
    | ---- | ----- | ----- |
    | 0.7 |  0.2 | 0.1 |

    - probability distribution for Maintenance node (child or Rain -> conditional probability distribution)

    | R | yes | no |
    | ---- | ----- | ----- |
    | none |  0.4 | 0.6 |
    | light | 0.2 | 0.8 |
    | heavy | 0.1 | 0.9 |

    - probability distribution for Train node (child of Rain and Maintenance -> a larger conditional probability distribution)

    | R | M | on time | delayed |
    | ---- | ---- | ----- | ----- |
    | none | yes |  0.8 | 0.2 |
    | none | no | 0.9 | 0.1 |
    | light | yes | 0.6 | 0.4 |
    | light | no | 0.7 | 0.3 |
    | heavy | yes | 0.4 | 0.6 |
    | heavy | no | 0.5 | 0.5 |

    - probability distribution for Appointment (child of Train -> conditional probability distribution)

    | T | attend | miss |
    | ---- | ----- | ----- |
    | on time |  0.9 | 0.1 |
    | delayed | 0.6 | 0.4 |

    - e.g. of calculations
        - P(light) - known
        - P(light, no) = P(light)*P(no | light)
        - P(light, no, delayed) = P(light)*P(no | light)*P(delayed | light, no)
        - P(light, no, delayed, miss) = P(light)*P(no | light)*P(delayed | light, no)*P(miss | delayed)

## Inference

At the last lecture, we looked at inference through entailment. This means that we could definitively conclude new information based on the information that we already had. We can also infer new information based on probabilities. While this does not allow us to know new information for certain, it allows us to figure out the probability distributions for some values

- Inference has multiple properties:
    - Query <b>X</b>: a variable for which to compute the probability distribution
    - Evidence variables <b>E</b>: observed variables for event <b>e</b> - e.g. we might have observed that there is light rain, and this observation helps us compute the probability that the train will be delayed
    - Hidden variables <b>Y</b>: non-evidence, non-query variables - e.g. standing at the train station we can't know if there is maintenance on the track further down the road
    - The goal: <b>P</b>(X | e) - e.g. compute the probability distribution of the Train variable (the query) based on the evidence <b>e</b> that we know there is light rain
- E.g. <b>P</b>(Appointment | light, no) - light rain and no track maintenance ; the hidden variable is variable Train
    - we know from above that a <em>conditional probability is proportional to the joint probability</em> (P(a | b) = αP(a, b))
    - P(Appointment | light, no) = αP(Appointment, light, no)
    - we also need the Train variable because the Appointment variable depends on it; we can use <em>marginalization</em> for it - there are only two ways can get a configuration of Appointment, light rain and no track maintenance, either this particular setting happens and the train is on time, either this particular setting happens and the train is delayed, so we can add up all of the posibilities for the hidden variable
    - αP(Appointment, light, no) = α[P(Appointment, light, no, on time) + P(Appointment, light, no, delayed)]
    - we can do these calculations and the normalize them at the end to make sure that everything adds up to 1

## Inference by enumeration

Inference by enumeration is a process of finding the probability distribution of variable X given observed evidence e and some hidden variables Y.

- P(X | e) = αP(X, e)  = αΣ<sub>y</sub>P(X, e, y)
    - x is the query variable
    - e is the evidence
    - y ranges over values of hidden variables
    - α normalizes the result
- Multiple libraries exist in Python to ease the process of probabilistic inference. We will take a look at the library <em>pomegranate</em> to see how the above data can be represented in code

However, this way of computing probability is inefficient, especially when there are many variables in the model. A different way to go about this would be abandoning exact inference in favor of approximate inference. Doing this, we lose some precision in the generated probabilities, but often this imprecision is negligible. Instead, we gain a scalable method of calculating probabilities.

## Approximate Inference - Sampling

Sampling is one technique of approximate inference. In sampling, each variable is sampled for a value according to its probability distribution

- E.g. unconditional probability - based on our Bayesian network from before, we start sampling by choosing different values from each node - for child nodes we will only select possible values for the parent choices
    - we start randomly with R = none, then go with M = yes, then go with T = on time, then A = attend
    - so one possible sample from this Bayesian network according to the probability distributions is: R = none ; M = yes ; T = on time ; A = attend
    - if we do this many times we will generate a whole bunch of different samples from this distribution
    - then if ever faced with a question like P(Train = on time)? we could do an exact inference procedure or just sample / approximate it to get close -> we look at the samples where the Train is on time (e.g. 6 out of 8 cases) and we can consider that as the likelihood
    - the more samples we have - the better inference procedure


- Rejection Sampling
    - E.g. conditional probability P(Rain = light | Train = on time)
        - we add one more step and start by rejecting all of the samples that don't match my evidence Train = on time
        - then from the remaining samples we consider only the ones where Rain = light
        - a disadvantage of this method is that if the evidence we're looking for is a fairly unlikely event -> a lot of samples are going to be rejected

- Likelihood Weighting
    - we follow a different procedure in which the goal is to avoid throwing out samples that didn't match the evidence
    - procedure:
        - start by fixing the values for evidence variables - we won't sample those
        - sample the non-evidence variables using conditional probabilities in the Bayesian Network
        - weight each sample by its <b>likelihood</b>: the probability of all of the evidence 
            - if we have a sample where the evidence was much more likely to show up than another sample, then I want to weight the likely one higher
            - before, all our sample were weighted equally (had a weight of 1) - now we will multiply each sample by its likelihood to get the more accurate distribution
    - for P(Rain = light | Train = on time)
        - we fix the evidence variable Train = on time and only sample things where I know the value of the variable Train and so not throw anything out
        - we sample the rest of the nodes and then we weight samples according to the probability of the evidence, e.g. for sample: R = light ; M = yes ; T = on time ; A = attend we look at the values table to get the likelihood of the evidence - in this case 0.6 -> this sample would have a weight of 0.6:

        | R | M | on time | delayed |
        | ---- | ---- | ----- | ----- |
        | none | yes |  0.8 | 0.2 |
        | none | no | 0.9 | 0.1 |
        | light | yes | 0.6 | 0.4 |
        | light | no | 0.7 | 0.3 |
        | heavy | yes | 0.4 | 0.6 |
        | heavy | no | 0.5 | 0.5 |


## Markov Models

So far, we have looked at questions of probability given some information that we observed. In this kind of paradigm, the dimension of time is not represented in any way. However, many tasks do rely on the dimension of time, such as prediction. To represent the variable of time we will create a new variable, X, and change it based on the event of interest, such that X<sub>t</sub> is the current event, X<sub>t+1</sub> is the next event, and so on. To be able to predict events in the future, we will use Markov Models.

- here we would have a variable for weather for example, for every possible time step (we could define it as days in our case)
    - X<sub>t</sub> - weather at time t - X<sub>0</sub>, X<sub>1</sub> etc.
    - if we start doing this over longer and longer periods of time there's an incredible amount of data that might go into this
    - when we try to do this kind of inference inside a computer it's helpful to make some simplifying assumptions about the problem even if they're not 100% accurate, close is enough

- <b>Markov Assumption</b>
    - the assumption that the current state depends on only a finite fixed number of previous states - for example the weather does not depent on the full history of weather, but we can predict today's weather just based on yesterday (just the one previous state usually), or on last few days etc.

- <b>Markov Chain</b>
    - a sequence of random variables where the distribution of each variable follows the Markov assumption
    - e.g. I can predict the weather and come up with a probability distribution - is it sunny or rainy (we consider just these two possibilites for now) - just based on the previous day's weather

        | | Sunny tomorrow X<sub>t+1</sub> | Rainy tomorrow X<sub>t+1</sub> |
        | ---- | ----- | ----- |
        | Sunny today X<sub>t</sub> |  0.8 | 0.2 |
        | Rainy today X<sub>t</sub> | 0.3 | 0.7 |

    - <b>Transition Model</b>
        - how we transition from one state to the next state in the above matrix - for example we sample tomorrow's weather based on how the weather is today
        - X<sub>0</sub> sunny -> X<sub>1</sub> sunny -> X<sub>2</sub> rainy -> X<sub>3</sub> rainy -> X<sub>4</sub> rainy -> ...
        - we can do analysis on this kind of chain and try to get the probability for a sequence of a few days as well
        - Markov models rely on us knowing the values of these individual states to be able to draw inferences

## Sensor Models

- in practice, often times we don't know the state of the world but we can sense some info about that state - for example a robot or an AI doesn't have exact knowledge about the world but has some sort of sensor, like a camera, a mic, a distance detector - that data is related to the state of the world even if the AI doesn't know what the underlying true state of the world actually is

- sensor models - how we translate what the <b>Hidden State</b> (underlying true state of the world) is, with what the <b>Observation</b> (what it is or what it is that the AI has access to) actually is - could have 'noise'

| Hidden State | Observation |
| ---- | ----- |
| robot's position - what the true hidden state is influences the observation of the sensor data | robot's sensor data - the robot can sense how far away are possible obstacles for example and using that observed info it can infer something about the hidden state |
| words spoken | audio waveforms - infer based on these what the spoken words likely were |
| user engagement | website or app analytics |
| weather (camera inside a building) | umbrella (seeing if employees bring in umbrellas) |

## Hidden Markov Model

A Markov model for a system with hidden states that generate some observed event

Here is our <b>sensor model</b> (also called <b>emission model</b> - the the underlying state emits some sort of emission that we then observe) that represents these probabilities:

- State (X<sub>t</sub>)
- Observation (E<sub>t</sub>)

|  | Observation = Yes umbrella | Observation = No umbrella |
| ---- | ----- | ----- |
| State = sunny  |  0.2 | 0.8 |
| State = rainy | 0.9 | 0.1 |

- <b>Sensor Markov assumption</b> - the assumption that the evidence variable (the thing we observe i.e. the emission) depends only on the corresponding state -> I can predict whether or not people will bring an umbrella entirely dependent just on whether it is sunny or rainy today (of course, this assumption might not hold in practice) just to allow us to reason more easily about these probabilities and approximate

- A hidden Markov model can be represented in a Markov chain with two layers. The top layer, variable X, stands for the hidden state. The bottom layer, variable E, stands for the evidence, the observations that we have (see hiddenmarkovchain.png)

- There are a number of possible tasks that we might want to do given this information - trying to infer something about the future or the past or about these sort of hidden states that might exist (all based on the same idea - conditional probabilities and using the probability distributions we have to draw these sort of conclusion):

| Task | Definition |
| ---- | ---- |
| filtering | given observation from start until now, calculate distribution for current state |
| prediction | given observations from start until now, calculate distribution for a future state |
| smoothing | given observations from start until now, calculate distribution for past state |
| most likely explanation | given observations from start until now, calculate most likely sequence of states |



