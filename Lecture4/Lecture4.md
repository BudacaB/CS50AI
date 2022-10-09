# Learning

https://cs50.harvard.edu/ai/2020/notes/4/

---

## Machine Learning

- machine learning provides a computer with data, rather than explicit instructions. Using these data, the computer learns to recognize patterns and becomes able to execute tasks on its own.

## Supervised Learning

- given a data set of input-output pairs, learn a function to map inputs to outputs
- there are a couple of different tasks within supervised learning

### Clasification

- supervised learning task of learning a function mapping an input point to a discrete category
- if you want to make a prediction you have access to data with historical info about days when it was raining and days when it was not raining
  - you can ask the computer to look for patterns in that data - we could structure the data in a table (see table.png) 
  - what makes this a supervised learning exercise is that a human has gone in and labeled each of these data points
- you can think of this as a function that takes two inputs - e.g. humidity and pressure:

```aidl
f(humidity, pressure)
    f(93, 999.7) = Rain
    f(49, 1015.5) = No Rain
    f(79, 1031.1) = No Rain
```

- this function f is what you would like to approximate - the computer and the human don't really know exactly how this function works because it's quite complex
  - instead you can attempt to estimate it - come up with a hypothesis function which tries to approximate what f does

```aidl
h(humidity, pressure)
```

- we can try to plot on a graph, the rainy (blue) and non rainy days (red) (see classification.png)
  - the computer should train a model such that if you are presented with a new input that does not have a label (the white dot), it can predict in which category it would most likely fit into
  - graphically the dot probably belongs to the blue category - it's closer to the blue dots

## Nearest-neighbor Classification

- algorithm that, given an input, chooses the class of the nearest data point to that input
- there are exceptions, for example a point that is closest to a red point, but is surrounded by blue points -> considering more than just a single neighbor, but multiple neighbors can sometimes give us a better result

### K-nearest-neighbor classification

- algorithm that, given an input, chooses the most common class out of the k nearest data points to that input
  - e.g. if we look at the five nearest points and three say it's raining and two say it's not, then you'll go with the three instead of the two
- algorithms have their trade-offs depending on the data
- ML research ends up being about trying multiple different algorithms to see what will bring the best results
- a drawback of the k-nearest-neighbors classification is that, using a naive approach, the algorithm will have to measure the distance of every single point to the point in question, which is computationally expensive
  - this can be sped up by using data structures that enable finding neighbors more quickly or by pruning irrelevant observation.

## Perceptron Learning

- another way of going about a classification problem, as opposed to the nearest-neighbor strategy, is looking at the data as a whole and trying to create a decision boundary (see decisionboundary.png)
  - in two-dimensional data, we can draw a line between the two types of observations - every additional data point will be classified based on the side of the line on which it is plotted
  - the technique used is called <b>linear regression</b>
  - realistically this example is cleaner than many data sets will actually be, often times the data is messy, there are outliers, or random noise etc. - in practice the data will not always be linearly separable
  - there may not be a line that perfectly separates one half of the inputs from the other half but we can say it does a pretty good job - this will be later better formalized
- formalizing:
  - inputs:
    - x<sub>1</sub> = Humidity
    - x<sub>2</sub> = Pressure
  - hypothesis function h(x<sub>1</sub>, x<sub>2</sub>) = Rain (1) if w<sub>0</sub> + w<sub>1</sub>x<sub>1</sub> + w<sub>2</sub>x<sub>2</sub> >= 0 ; No Rain (0) otherwise
    - how do we formalize the boundary - the boundary's generally going to be a linear combination of these input variables in this particular case
      - you take each of these inputs and multiply them by some number that you're going to have to figure out - generally called a <em>weight</em> - for how important should these variables be in trying to determine the answer
      - you'll weight each of these variables with some weight and you might add a constant to it just to try and make the function a little bit different (e.g. w<sub>0</sub>) because the function might require you to shift the value up or down by a certain amount
      - the result you just need to compare - is it greater than 0 or is it less than 0 - does it belong on one side of the line, or the other
      - the function expression is in this case going to refer to just some line if you were to plot that graphically - what it looks like depends upon the weights
      - often times this kind of expression will instead express using vector math (a sequence of numerical values - e.g. in python that could be a list of numerical values or a tuple)
      - here we have a couple of vectors - one is for the individual weights  -> you can construct a Weight Vector w: (w<sub>0</sub>, w<sub>1</sub>, w<sub>2</sub>)
        - to be able to calculate based on those weights whether you think it's raining or not raining, you're going to multiply each of those weights by one of the input variables
        - in this way you will also have an Input Vector x: (1, x<sub>1</sub>, x<sub>2</sub>)
      - so now you've represented two distinct vectors
        - a vector of weights that you need to somehow learn - this is the goal of the ML algorithm
        - an input vector - represents a particular input to the function, a data point for which we'd like to estimate
        - to do the calculation - you calculate the function expression - that's what's called the <b>dot product</b> of these two vectors
          - the dot product is the multiplication of each of the terms of the vectors and then adding the results
            - w . x = w<sub>0</sub> + w<sub>1</sub>x<sub>1</sub> + w<sub>2</sub>x<sub>2</sub>
    - a simpler representation: h<sub>w</sub>(x) = 1 if w . x >=0 ; 0 otherwise
      - we say that the hypothesis is parametrized by the weight - depending on what weights we choose we end up getting a diff hypothesis
- how do you figure out how these weights should be?

### Perceptron learning rule

- given data point (x, y) - input x and output y where y is like 1 for Rain and 0 for No Rain - update each weight according to: 
  - w<sub>i</sub> = w<sub>i</sub> + α(y - h<sub>w</sub>(x)) * x<sub>i</sub>
- the big picture idea is that you can start with random weights but then learn from the data
  - take the data points one at a time and for each of them figure out what parameters do you need to change inside of the weights in order to better match that input
  - the formula is equivalent to w<sub>i</sub> = w<sub>i</sub> + α(actual - estimate) * x<sub>i</sub>
  - if you are able to predict what category the data point belongs to (actual - estimate = 0), then the weight wouldn't change
  - if not then the weights must be adjusted for the future - adjust the actual value and the estimate as needed
    - if the actual value was bigger than the estimate - you need to increase the weight in order to make it such that the output is bigger
    - if the actual value is less than an estimate you want to decrease the value of the weight in order to lower the output
- α is what is called the 'learning rate' - it's some parameter you choose for how quicly we're' actually going to be updateding these weight values
- after all this you end up with a threshold function (see hardthreshold.png)
  - anything on each side of the line belongs to a diff category
  - the issue with this is that it leaves two possible outcomes
  - since it uses only 1 and 0, it employs a <b>hard thresohold</b>
- a way to go around this is by using a logistic function, which employs a soft threshold (see softthreshold.png)

## Support Vector Machines

- in addition to nearest-neighbor and linear regression, another approach to classification is the Support Vector Machine
- this approach uses an additional vector (support vector) near the decision boundary to make the best decision when separating the data
- they are trying to find the <b>maximum margin separator</b>
  - boundary that maximizes the distance between any of the data points (see supportvector.png)
  - this can be done both in 2D and also in higher dimensions; or even if the data isn't linearly separable (see circleboundary.png)


## Regression

- regression is a supervised learning task of a function that maps an input point to a continuous value, some real number 
  - this differs from classification in that classification problems map an input to discrete values (Rain or No Rain)
- e.g. sales generated based on ad expenses

```aidl
f(advertising)
f(1200) = 5800
f(2800) = 13400
etc.
```

- and you would like to predict some sort of hypothesis function - that can predict, given the amount spent on advertising, some real number estimate of how much sales can be expected

```aidl
h(advertising)
```

- we could try to use linear regression - this time not approximating discrete categories, but instead approximate this relationship between advertising and sales (see regression.png)

## Evaluating Hypotheses

- this is kind of like an optimization problem - either try to maximize some objective function by trying to find a global maximum, or trying to minimize some cost function by trying to find a global minimum
- in the case of evaluating hypotheses - this cost function, the thing you're trying to minimize, you might be trying to minimize a <b>loss function</b>
  - function that expresses how poorly our hypothesis performs - or a loss of utility -> whenever you predict something that is wrong, that's a loss of utility that's going to add to the output of the loss function

### 0-1 loss function

- L(actual, predicted) = 0 if actual = predicted, 1 otherwise (see 01loss.png)

### L1 loss function

- L(actual, predicted) = |actual - predicted|
- for continuous values, we want to take into account also the difference between the prediction and reality (see l1.png)
- better for cases where there are a lot of outliers, and you don't necessarily care about modelling them

### L2 loss function

- L(actual, predicted) = (actual-predicted)<sup>2</sup>
- penalizes much more harshly anything that is a worse prediction
- better suited to minimize the error on more outlier cases

## Overfitting

- a model that fits too closely to a particular data set and therefore may fail to generalize to future data
- an extreme decision boundary can be not so good as a prediction even if more accurate - it won't generalize well (see overfitting.png)
- this can happen both in classification and also in regression (see overfitting.png)
- you want to use strategies to make sure that you don't overfit the model to a particular data set
  - one way is to examine what it is that you're optimizing for
    - in an optimization problem all you do is think about some cost and you want to minimize it
    - so far you've defined that function just as being cost(h) = loss(h)
    - you want to add something extra -> cost(h) = loss(h) + complexity(h) - how complicated does the line look? - Occam's razor type approach to give preference to a simpler decision boundary (e.g. a straight line)
    - if it's much more complex, you need to come up with some balance between loss and complexity - often represented as multiplying the complexity by some parameter (lambda)
      - cost(h) = loss(h) + λcomplexity(h) -> if lambda is greater, then you really penalize more complex hypotheses - if lambda is smaller you penalize more complex hypotheses a little bit

### Regularization

- penalizing hypotheses that are more complex to favor simpler, more general hypotheses
- cost(h) = loss(h) + λcomplexity(h)

### Holdout cross-validation

- splitting data into a training set and a test set, such that learning happens on the training set and is evaluated on the test set
- <b>k-fold cross-validation</b> - splitting data into <em>k</em> sets, and experimenting <em>k</em> times, using each set as a test set once, and using remaining data as training set

## scikit-learn

- as often is the case with Python, there are multiple libraries that allow us to conveniently use machine learning algorithms, one of such libraries is scikit-learn

## Reinforcement Learning

- given a set of rewards or punishments, some agent learns what actions to take in the future (see reinforcement.png)

## Markov Decision Process

- model for decision-making, representing states, actions, and their rewards - similar to a Markov Chain but with an agent (see markov.png)
- properties:
  - set of states S
  - set of actions ACTION(s)
  - transition model P(s' | s, a)
  - reward function R(s, a, s')

## Q-learning

- method for learning a function Q(s, a), estimate of the value of performing action <em>a</em> in state <em>s</em>
- start with Q(s, a) = 0 for all <em>s, a</em>
- when you take an action and receive an award
  - estimate the new value of Q(s, a) based on current reward and expected future rewards
  - update Q(s, a) to take into account old estimate as well as your new estimate
- how this works:
  - start with Q(s, a) = 0 for all s, a
  - every time you take an action a in state s and observe reward r, you update:
    - Q(s, a) <- Q(s, a) + α(new value estimate - Q(s, a))
      - the updated value of Q(s, a) is equal to the previous value of Q(s, a) in addition to some updating value - this value is determined as the difference between the new value and the old value, multiplied by α, a learning coefficient
      - when α = 1 the new estimate simply overwrites the old one. When α = 0, the estimated value is never updated - by raising and lowering α, you can determine how fast previous knowledge is being updated by new estimates
    - can be rewritten as Q(s, a) <- Q(s, a) + α((r + future reward estimate) - Q(s, a))
      - new value estimate is composed of what reward (r) did you just get from taking this action in this state, and what you can expect your future reward to be from this point forward
    - can be rewritten as Q(s, a) <- Q(s, a) + α((r + max<sub>a'</sub>Q(s', a')) - Q(s, a))
      - take the maximum across all possible actions you could take next - which one will have the highest reward
    - sometimes the value of the future reward estimate can sometimes appear with a coefficient gamma that controls how much future rewards are valued - reward now vs reward later
      - Q(s, a) <- Q(s, a) + α((r + γmax<sub>a'</sub>Q(s', a')) - Q(s, a))

### Greedy Decision-Making

- when in state <em>s</em>, choose action <em>a</em> with highest Q(s, a)

### Explore vs Exploit

- exploitation - using knowledge that the AI already has
- exploration - exploring other action that weren't explored before -> one of them might lead to better reward, faster

### ε-greedy (Epsilon greedy algorithm)

- set ε equal to how often we want to move randomly
- with probability 1 - ε, choose estimated best move
- with probability ε, choose a random move

### Function approximation

- approximating Q(s, a), often by a function combining various features, rather than storing one value for every state-action pair
- this type of approach can be quite helpful when dealing with reinforcement learning that exists in larger and larger state spaces where it's just not feasible to explore all the possible states that could actually exist

## Unsupervised Learning 

- given input data without any additional feedback, learn patterns

### Clustering

- organizing a set of objects into groups in such a way that similar objects tend to be in the same group
- some clustering applications
  - genetic research
  - image segmentation
  - market research
  - medical imaging
  - social network analysis

### k-means clustering

- algorithm for clustering data based on repeatedly assigning points to clusters and updating those clusters' centers (see kclustering.png)
- a cluster center is moved around - it will define that cluster (the middle of the cluster) - and then you re/assign points to that cluster based on which center is closest to that point

## Learning

- Supervised Learning
- Reinforcement Learning
- Unsupervised Learning