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
  - another popular one is <b>rectified linear unit</b> (ReLU) - allows the output to be any positive value, if the value is negative, ReLU sets it to 0. (see relu.png)

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
    - calculate the gradient based on all the data points: direction that will lead to decreasing loss (ultimately the gradient is a vector - a sequence of numbers)
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
    - here you might imagine four NNs with three inputs each
- this was sort of the idea of <b>supervised machine learning</b> - giving the NN a bunch of data, and the algo can use gradient descent to figure out what all the weights should be in order to create some sort of model that hopefully allows you a way to predict what you think the weather is going to be
- NN have a lot of other applications as well, for example applying the same sort of idea to <b>reinforcement learning</b> - train some sort of agent to learn what action to take depending on what state it currently happens to be in
  - each of the input variables can represent some info about the state, and the output can be each of the various different actions that the agent can take
  - the outputs could model which action is better than other actions
- possible limitations - just taking some linear combination of inputs and passing it into some sort of activation function
  - when we do this in the case of binary classification we can only predict things that are linearly separable because of the linear combination of inputs and using that to define some decision boundary or threshold 
  - we can predict a line that separates linearly (see linearnonlinear.png)
  - but a single unit that is making a binary classification (aka <b>perceptron</b>) can't deal with a situation that is non-linear (see linearnonlinear.png)
  - the <b>perceptron</b> is only capable of learning a linearly separable decision boundary
  - the solution could be multilayer neural networks

## Multilayer Neutral Network

- artificial neural network with an input layer, an output layer, and at least one hidden layer (see multilayer.png)
- it gives us the ability to model more complex functions - instead of having a single decision boundary (i.e. a single line dividing the red and blue dots), each of the hidden nodes can learn a different decision boundary, and we can combine them to figure out what the ultimate output is going to be
- as you can begin to imagine more complex situations, you can imagine each of these nodes learning some useful property / feature of all the inputs, and you learning how to combine those features together in order to get the output
- how do you train a NN that has hidden layers inside of it?
  - you get values for all the inputs and what the value of the output should be (what the category is) - but the input data doesn't tell you what the values for the hidden nodes should be
  - a strategy you could use - if you know what the error or the loss is on the output node, then based on what the weights leading up to it are, if one of these weights is higher than another, you can calculate an estimate for how much the error from the output node was due to what part of the previous hidden layer, which node
  - in effect, based on the error from the output, you can back-propagate the error and figure out and estimate for what the error is for each of the nodes in the hidden layer

### Backpropagation

- algorithm for training neural networks with hidden layers
- pseudocode for example on gradient descent with backpropagation:
  - start with a random choice of weights
  - repeat:
    - calculate error for the output layer
    - for each layer, starting with output layer, and moving inwards towards the earliest hidden layer:
      - propagate error back one layer
      - update weights
  - this can be extended to any number of hidden layers, creating <b>deep neural networks</b>, which are NNs that have more than one hidden layer (see deepnn.png)
- this is really the key algo that makes NNs possible - to take these multi-leveled structures and be able to train them depending on what the values of the weights are in order to figure out how it is that you should go about updating those weights in order to create some function, that is able to minimize the total amount of loss - to figure out some good setting of the weights that will take the inputs and translate into the output that we expect

## Overfitting

- generally happens when you fit too closely to the training data and as a result you don't generalize well to other situations as well
- one risk with a NN that has many diff nodes is that you might over fit based on the input data - you might grow over reliant on certain nodes to calculate things just purely based on the input data, that doesn't allow you to generalize very well to the output
- there are multiple techniques for dealing with overfitting

### Dropout

- temporarily removing units - selected at random - from a NN to prevent over-reliance on certain units (see dropout.png)
- there are a number of diff ML libraries - NN libraries that you can use

## TensorFlow

- playground.tensorflow.org

## Computer Vision

- computational methods for analyzing and understanding digital images
- you can look at an image as a grid of pixels, each with some sort of color
  - each pixel can be represented as a number - on a 0 to 255 range - so it can be represented with 8 bits - black & white, or RGB with three numerical values
  - with this each pixel would be a numerical value to be used to perform some sort of prediction task
- you can imagine a NN with a lot of inputs - for each of the pixels - one, or three for a colored image
  - they are connected to a deep NN which might take all the pixels and the output might be then ten neurons that would tell you what that digit might be (if you try to predict what digit was hand written for example)
- there are some drawbacks
  - a lot of different inputs
  - by flattening everything into this structure of all the pixels, you lose access to a lot of the info about the structure of the image
- you can introduce a couple of algos that allow you to take the image and extract some useful info

## Image Convolution

- applying a filter that adds each pixel value of an image to its neighbors, weighted according to a kernel matrix
  - the purpose is to extract some sort of info out of an image - take a pixel and based on its neighboring pixels predict something like whether there's some sort of curve inside the image
  - combining these various different features to enable them to say something meaningful about an image