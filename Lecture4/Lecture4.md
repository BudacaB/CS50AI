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