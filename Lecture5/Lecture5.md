# Neural Networks

https://cs50.harvard.edu/ai/2020/notes/5/

---

Neuroscience:
- Neurons are connected to and receive electrical signals from other neurons
- Neurons process input signals and can be activated

Artificial neural network:
- mathematical model for learning inspired by biological neural networks

---

## Artificial Neural Networks

- model mathematical function from inputs to outputs based on the structure and parameters of the network
- allows for learning the network's parameters based on data
- when implemented in AI, the parallel of each neuron is a <b>unit</b> - can be represented like a node in a graph
- e.g. given some input variables you want to perform some sort of task (e.g. predict if it's going to rain - i.e. a boolean classification)
  - using some function h (hypothesis) and weights to multiply the input variables (w<sub>0</sub> just servers to move the function's value up for down - i.e. a 'bias')
  - h(x<sub>1</sub>, x<sub>2</sub>) = w<subb>0</sub> + w<sub>1</sub>x<sub>1</sub> + w<sub>2</sub>x<sub>2</sub>
  - in order to define a hypothesis function, you need to decide and determine what the weights should be
- at the end of this, you need to make some sort of classification (e.g. rainy or not rainy) - to do that you use some sort of function that defines some sort of threshold (see step.png)
  - step function - this is what will be called an <b>activation function</b>
- if you don't just want a purely binary classification, but allow for some in between real number values - there are a number of different function that can be used
  - e.g. <b>logistic sigmoid</b> (see logistic.png) - could provide a probability of rain of 0.8 for example
- there are many other types of activation functions - an activation function just takes the output of the hypothesis function and figures out what the actual output should be - h(x<sub>1</sub>, x<sub>2</sub>) = g(w<subb>0</sub> + w<sub>1</sub>x<sub>1</sub> + w<sub>2</sub>x<sub>2</sub>)
  - another popular one is <b>rectified linear unit</b> (ReLU) (see relu.png)

## Neural Networks Structure

- the graphical representation of this mathematical model can be expressed as (see nnstructure.png)
- a neural network should be able to learn how to calculate some function - learn what should the values of w<sub>0</sub>, w<sub>1</sub> and w<sub>2</sub> be, what should the activation function be in order to get the result
- for example the Or logical function can be represented as a function <em>f</em> with the following truth table:

|  x  |  y  | f(x, y) |
|:---:|:---:|:-------:|
 |  0  |  0  |    0    |
|  0  |  1  |    1    |
|  1  |  0  |    1    |
|  1  |  1  |    1    |

- how can you train a NN to be able to learn this particular function - what would those weights look like
- you can use a NN like (see nnor.png) to model the Or function - use a value of 1 for each of the weights and a bias of -1 - and a step function as the activation function
  - e.g. for 0 and 0 the result will be -1, if you plot that on the activation function, -1 is before the 0 threshold - the output will be 0
  - for 1 and 0 - the output will be 0 - that's just at the threshold so the result will be 1
  - for 1 and 1 - the output will be 1 - that's well beyond the threshold so the result will be 1
- another example is the And function

|  x  |  y  | f(x, y) |
|:---:|:---:|:-------:|
|  0  |  0  |    0    |
|  0  |  1  |    0    |
|  1  |  0  |    0    |
|  1  |  1  |    1    |

- you can do it in the same way as the Or function except instead of -1 as the bias, you can use -2
- or maybe given the humidity and the pressure you want to calculate what's the probability of rain
- or a regression style problem where given some amount of advertising and what month it is, you want to predict what the sales are going to be for that particular month
- in some problems you're not just going to have two inputs, but multiple units can be composed together to make the network more complex
  - this scales up in the same way - e.g. 5 units as inputs - g(<sup>5</sup>Σ<sub>i=1</sub> x<sub>i</sub>w<sub>i</sub> + w<sub>0</sub>)

## Gradient Descent

- algorithm for minimizing loss when training neural networks
- in general, with more complex functions like predicting sales, or whether it's going to rain, it's trickier to figure out what the weights should be
  - the computer can provide some sort of mechanism for calculating what it is that the weights should be, so you can accurately model the function that you're trying to estimate
  - gradient descent is the strategy for this inspired by the domain of calculus
- recall that loss refers to how bad the hypothesis function happens to be - you can define loss functions that provide a number for any particular hypothesis saying how poorly does it model the data
  - this loss function is just a mathematical function - when you have a math function, in calculus you can calculate the gradient - it's like a slope, the direction in which a loss function is moving at any particular point
  - it tells us in which direction you should be moving these weights in order to minimize the amount of loss
- how does it work:
  - start with a random choice of weights
  - repeat:
    - calculate the gradient based on all the data points: direction that will lead to decreasing loss (ultimately the gradient is is a vector - a sequence of numbers)
    - update weights according to the gradient
- what is expensive in this algorithm? - <b>all data points</b> - we can employ faster methods

### Stochastic Gradient Descent

- start with a random choice of weights
- repeat:
  - calculate the gradient based on <b>one data point</b>: direction that will lead to decreasing loss
  - update weights according to the gradient

### Mini-Batch Gradient Descent

- start with a random choice of weights
- repeat:
  - calculate the gradient based on <b>one small batch</b>: direction that will lead to decreasing loss
  - update weights according to the gradient

### Multiple outputs

- in the same way that you can take a NN and add units to the input layer, you can likewise add outputs to the output layer as well
- to keep this network connected between the two layers, we need to add more weights - e.g. each of four input nodes has four weights associated with each of the four outputs
- e.g. you might not care just whether it's raining or not raining, there might be multiple categories of weather that you would like to categorize the weather into
  - with just a single output variable you can do a binary classification, with multiple output variables, you might be able to use each one to predict something a little different (see weather.png)
- this was sort of the idea of <b>supervised machine learning</b> - giving the NN a bunch of data, and the algo can use gradient descent to figure out what all the weights should be in order to create some sort of model that hopefully allows you a way to predict what you think the weather is going to be
- NN have a lot of other applications as well, for example applying the same sort of idea to <b>reinforcement learning</b> - train some sort of agent to learn what action to take depending on what state it currently happens to be in
  - each of the input variables can represent some info about the state, and the output can be each of the various different actions that the agent can take
  - the outputs could model which action is better than other actions