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