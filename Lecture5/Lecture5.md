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