# Optimization

https://cs50.harvard.edu/ai/2020/notes/3/

---

<b>Optimization</b> - choosing the best option from a set of options

## Local Search

- search algorithm that maintains a single node and searches by moving to a neighboring node
    - the other algos that we've looked at so far - e.g. breadth-first search or A-star search etc., generally maintain a whole bunch of different paths that we're simultaneously exploring and we're looking at a bunch of different paths once trying to find our way to the solution
    - in local search, this is going to be a search algo that's only going to maintain a single node, looking at a single state and we'll generally run that algo by mainintaing that single node and then moving ourselves to one of the neighboring node throughout the search process
    - local search isn't appropiate for problems like before, when we were trying to find our way through a maze from the initial state to a goal by following some path; local search is most applicable when we really don't care about the path at all, and all we care about is what the solution / goal is -> cases where figuring out exactly what the solution is, exactly what the goal looks like, is actually the heart of the challenge
    - E.g.: (see hospitals1.png)
        - we want to place two hospitals on a map with the objective of trying to minimize the distance of any of the houses from a hospital
        - place the two hospitals and calculate the total Cost of their distances - Cost of 17
        - can we minimize that cost / total amount for the distances?
    - abstracting this concept, we can represent each configuration of houses and hospitals as the <b>state-space landscape</b> (see statespace.png). Each of the bars in the picture represents a value of a state, which in our example would be the cost of a certain configuration of houses and hospitals.
        - the height of a vertical bar is generally going to represent some function of that state / some value of that state - i.e. what is the cost of this particular config of hospitals in terms of what is the sum total of all the distances from all the houses to their nearest hospital
- when we have a state-space landscape we want to do one of two things
    - we might want to maximize the value of this function - trying to find the <b>global maximum</b> so to speak, of this state-space landscape - a single state whose value is higher than all of the other states that we can possibly choose from - (see maxima.png / minima.png) 
        - generally when we're trying to find the global maximum we'll call the function that we're trying to optimize - <b>objective function</b> - some function that measures for any given state how good is that state
        - we can take any state, pass it into the objective function and get a value for how good that state is
        - ultimately our goal is to find one of these states that has the highest possible value for that objective function
    - an equivalent but reverse problem is the problem of finding the <b>global minimum</b> - some state that has a value after we pass it into this function that is lower than all of the other possibl values that we might choose from
        - generally speaking when we're trying to find the global minimum, we call the function that we're calculating a <b>cost function</b>
        - generally each state has some sort of cost - whether that's a monetary cost, or a time cost, or a distance cost etc. - and we're trying to minimize the cost / find the state that has the lowest possible value of that cost
- how do we get a global maximum or a global minimum - in local search we generally operate this algo by maintaining just <b>a single state</b> - just a current state represented inside of some node maybe inside of a data structure, where we're keeping track where we are currently
    - ultimately from that state, we're going to move to one of its neighbor states - i.e. some state that is close to our current state, e.g. moving a hospital one space to the left, right, up or down etc. -> might have a slightly different value in terms of its objective function or cost function

## Hill Climbing

- example of such a local search algorithm
- you start by trying to maximize the value of your state - figure out the global maximum
    - we start at a state and then consider the neighbors of that state
    - for maximizing you will move to the higher state
    - this happents until you get to a state which is higher than any of its neighbors
- trying then to find the global minimum, the algo works in the exact same way in reverse
    - you then get to a state that is lower than any of its neighbors
- pseudocode:
```
function HILL-CLIMB(problem):
    current = initial state of problem 
    # some problems lend themselves to an initial state (some place where you begin), in other cases maybe not, in which case we might just randomly generate some initial state - e.g. choosing two locations for hospitals at random and figuring out from there how you might be able to improve
    repeat:
        neighbor = highest value neighbor of current
        # lowest for minimizing the value
        # if multiple neighbors each have an equally high value or an equally low value - we can choose randomly from among them and save it inside the 'neighbor' variable
        if neighbor not better than current:
            return current
        current = neighbor  
```
- with hospitals2.png you've improved the total cost from 17 to 11, however there is a better position for the hospital on the left, and that is right between the two houses, however you can't get to that state because in order to get there you have to go through a state that actually wasn't any better
    - this is a limitation when trying to implement a hill climbing algorithm, it might not always give you the optimal solution
    - if you're trying to find the global maximum, you could get stuck at one of the local maxima
    - likewise in the case of the hospitals, you're trying to find the global minimum, but you have the potential to get stuck at one of the local minima
    - plateaus are also possible - flat local maximum, or another variant called 'shoulder'
- there are a number of different varieties or variations on the hill climbing algo that help to solve the problem better depending on the context:

| Variant | Definition |
| ---- | ---- |
| steepest-ascent | choose the highest-valued neighbor |
| stochastic | choose randomly from higher-valued neighbors - e.g. choose randomly from five better neighbors because there's potential for improvement, even if it's not locally the best option that you can choose  |
| first-choice | choose the first higher-valued neighbor |
| random-restart | conduct hill climbing multiple times - e.g. if you apply steepest-ascent hill climbing, you start at some random state, try and figure out how to solve the problem, and the randomly restart and try again with a new starting config; do this some number of times, you can pick the best one |
| local beam search | chooses the <em>k</em> highest-valued neighbors - rather than keep track of just one current best state, such that rather than starting at one random initial config, you might start with three or four etc., randomly generate all the neighbors and then pick the three or four etc. best of the neighbors that you find and continue to repeat this process -> more options to consider or ways to navigate to the optimal solution that might exist for a particular problem |

## Simulated Annealing

- early on, high 'temperature': more likely to accept neighbors that are worse that current state
- later on, lower 'temperature': less likely to accept neighbors that are worse than current state
- pseudocode:

```
function SIMULATED-ANNEALING(problem, max):
    current = initial state of problem
    for t = 1 to max:
        T = temperature(t) // based on the proportion of time - less likely to choose a worse spot as time decreases
        neighbor = random neighbor of current
        ΔE = how much better neighbor is than current
        if ΔE > 0:
            current = neighbor // based on temp / time but also on ΔE - if the neighbor is much worse than the current state we are less likely to choose it
        with probability e^(ΔE/T) set current = neighbor // e is a constant -> result will be between 0 and 1
    return current
```