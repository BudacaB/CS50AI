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

### Traveling Salesman Problem

- in the traveling salesman problem, the task is to connect all points while choosing the shortest possible distance. This is, for example, what delivery companies need to do: find the shortest route from the store to all the customers’ houses and back
- in this case, a neighbor state might be seen as a state where two arrows swap places. Calculating every possible combination makes this problem computationally demanding (having just 10 points gives us 10!, or 3,628,800 possible routes). By using the simulated annealing algorithm, a good solution can be found for a lower computational cost
    - NP-complete problem - any of a class of computational problems for which no efficient solution algorithm has been found

## Linear Programming

- family of types of problems, possible problem to solve:
    - minimize (/maximize) a cost function c<sub>1</sub>x<sub>1</sub> + c<sub>2</sub>x<sub>2</sub> + ... + c<sub>n</sub>x<sub>n</sub>
    - with constraints of form a<sub>1</sub>x<sub>1</sub> + a<sub>2</sub>x<sub>2</sub> + ... + a<sub>n</sub>x<sub>n</sub> <= b or of form a<sub>1</sub>x<sub>1</sub> + a<sub>2</sub>x<sub>2</sub> + ... + a<sub>n</sub>x<sub>n</sub> = b
    - with bounds for each variable l<sub>i</sub> <= x<sub>i</sub> <= u<sub>i</sub>
- (from notes):
    -  A cost function that we want to minimize: c₁x₁ + c₂x₂ + … + cₙxₙ. Here, each x₋ is a variable and it is associated with some cost c₋.
    - A constraint that’s represented as a sum of variables that is either less than or equal to a value (a₁x₁ + a₂x₂ + … + aₙxₙ ≤ b) or precisely equal to this value (a₁x₁ + a₂x₂ + … + aₙxₙ = b). In this case, x₋ is a variable, and a₋ is some resource associated with it, and b is how much resources we can dedicate to this problem.
    - Individual bounds on variables (for example, that a variable can’t be negative) of the form lᵢ ≤ xᵢ ≤ uᵢ.

### Example

- two machines X<sub>1</sub> and X<sub>2</sub>. X<sub>1</sub> costs $50/hour to run, X<sub>2</sub> costs $80/hour to run.Goal is to minimize cost.
- X<sub>1</sub> requires 5 units of labor per hour. X<sub>2</sub> requires 2 unis of labor per hour. Total of 20 units of labor to spend
- X<sub>1</sub> produces 10 units of output per hour. X<sub>2</sub> produces 12 units of output per hour. Company needs 90 units of output
- cost function: 50x<sub>1</sub> + 80x<sub>2</sub>
- constraint: 5x<sub>1</sub> + 2x<sub>2</sub> <= 20
- constraint: 10x<sub>1</sub> + 12X<sub>2</sub> >=90
    - for keeping the <= we can re-write as
        -10x<sub>1</sub> + (-12x<sub>2</sub>) <= -90

### Algorithms

- Simplex
- Interior-Point

## Constraint Satisfaction

- a class of problems 
    - basic idea is that we have some number of variables that need to take on some values
    - we need to figure out what values each of those variables should take on
    - those variables are subject to particular constraints that are going to limit what values those variables can actually take on
- example (see constraintsatisfaction1.png):
    - exam schedule
    - you have 4 students 1, 2, 3 and 4
    - each one of them is taking on some number of diff classes
        - 1 - A, B, C
        - 2 - B, D, E
        - 3 - C, E, F
        - 4 - E, F, G
    - say the uni is trying to schedule exams for all of these courses, but there are only 3 exam slots - Mon, Tue, Wed
    - we have to schedule an exam for each of these courses but the constraint that we have is that we don't want anyone to have to take two exams on the same day
    - how to solve:
        - let's represent every class as a node inside of a graph (see constraintsatisfaction2.png)
        - we create an edge between two nodes on the graph if there is a constraint between those two nodes (e.g. the three classes taken by student A can't have an exam at the same time)
        - we can call this the contraint graph - a graphical representation of all of your variables and the constraints between those possible variables (i.e. each constraint is an inequality constraint in this case)
- put simple:
    - set of variables {X<sub>1</sub>, X<sub>2</sub>, ... , X<sub>n</sub>}
    - set of domains for each variable (D<sub>1</sub>, D<sub>2</sub>, ... , D<sub>n</sub>)
    - set of constraints C
- example:
    - sudoku game (see sudoku.png)
    - variables - all of the empty squares - {(0, 2), (1,1), (1, 2), (2, 0), ...}
    - domains - any number from 1 to 9 that I could fill in for each variable - {1, 2, 3, 4, 5, 6, 7, 8, 9}
    - constraints - cells need to be different in the 3 x 3 squares and by row and column - e.g {(0, 2) != (1, 1) != (1, 2) != (2, 0), ...}
- back to the exam schedule example:
    - variables - {A, B, C, D, E, F, G}
    - domain - Mon, Tue, Wed
    - constraints - {A != B, A != C, B != C, B != D, B != E, C != E, C != F, D != E, E != F, E != G, F != G } - formally i.e. for A and B for example, these two variable can't take on the same value within their domain
- types of constrains:
    - hard constraints - constraints that must be satisfied in a correct solution
    - soft constraints - constraints that express some notion of which solutions are preferred over others - e.g. maybe A and B can't have an exam on the same day, but someone has a preference A's exam is earlier than B's exam - you can try to optimize for maximizing people's preferences, to be satisfied as much as possible
- constrains classification
    - unary constraints - constraint involving only one variable - e.g. {A != Monday} if the instructor isn't available for example
    - binary constraint - constraint involving two variables - e.g. {A != B}
-  <b>node consistency</b> - when all the values in a variable's domain satisfy the variable's unary constraints - we can say that the problem, or the variable, is node consistent
    - example: classes A and B, each of which has an exam on either {Mon, Tue, Wed} (their domains)
        - imagine we have these constraints: {A != Mon, B != Tue, B != Mon, A != B}
        - we can try to enforce node consistency - we make sure that all of the values for any variable's domain satisfy it's unary constraints
        - to start we can try to make A node consistent -> we remove Mon from its domain - now it's node consistent
        - for B we remove Mon and Tue
- <b>arc (edge) consistency</b> - when all the values in a variable's domain satisfy the variable's binary constraints
    - to make X arc-consistent with respect to Y, remove elements from X's domain until every choice for X has a possible choice for Y
    - going back to the previous example after node consistency A - {Tue, Wed} and B - {Wed} - to make A arc consistent with respect to B - you remove Wed from A's domain such that the binary constraint can't be violated
    - you can try to apply the consistency to a larger graph and formalize an algorithm with pseudo-code that would enforce that consistency

### Arc Consistency

```
function REVISE(csp, X, Y): //csp = constraint satisfaction problem ; make X arc consistent with respect to Y
    revise = false
    for x in X.domain:
        if no y in Y.domain satisfies constraint for (X, Y):
            delete x from X.domain
            revised = true
    return revised
```

- to enforce arc consistency across the entire problem:

```
function AC-3(csp):
    queue = all arcs in csp
    while queue non-empty:
        (X, Y) = DEQUEUE(queue)
        if REVISE(csp, X, Y): // if we do remove a value from X's domain, there's a risk that it was needed for another arc to be arc consistent
            if size of X.domain == 0:
                return false
            for each Z in X.neighbors - {Y}:
                ENQUEUE(queue, (Z, X))
    return true
```

- the AC-3 can reduce domains in a larger graph, given enough options for values, to make it arc consistent - we only consider consistency between binary constraints between two nodes and we're not really considering all of the rest of the nodes
- however it will not always actually solve the problem, we might still need to somehow search to try and find a solution - we can use classical, traditional search algos to try to do so

## Search Problems

- initial state
- actions
- transition model
- goal test
- path cost function

## CSPs as Search Problems

- initial state: empty assignment (no variables)
- actions: add a {variable = value} to assignment
- transition model: shows how adding an assignment changes the assignment
- goal test: check if all variables assigned and constraints all satisfied
- path cost function: all paths have same cost - we just care about the solution itself

If we just implement this naive search algo by just implement DFS or BFS, this is going to be very inefficient, there are ways we can take advantage of the structure of the CSP
- one of the key ideas is that the order that we assign the variables in doesn't matter
- we can try to revise the search algo to apply it specifically for a problem like a CSP

## Backtracking Search

- backtracking search is a type of a search algorithm that takes into account the structure of a constraint satisfaction search problem
- in general, it is a recursive function that attempts to continue assigning values as long as they satisfy the constraints - if constraints are violated, it tries a different assignment

```
function BACKTRACK(assignment, csp): // assignment is initially empty - no values yet assigned to variables
    if assignment complete: return assignment
    var = SELECT-UNASSIGNED-VAR(assignment, csp)
    for value in DOMAIN-VALUES(var, assignment, csp):
        if value consistent with assignment:
            add {var = value} to assignment
            result = BACKTRACK(assignment, csp)
            if result != failure: return result
        remove {var = value} from assignment
    return failure
```

- we can try to solve a problem like (see backtracking.png) - Mon, Tue, Wed as domain values and linked nodes can't have an exam on the same day
- ultimately you might be able to be a little bit more intelligent about how you do this in order to improve the efficiency of how you solve these sorts of problems

## Inference

- using the knowledge you know to be able to draw conclusions in order to make the rest of the problem solving process a little bit easier
- is there anything you can do to avoid getting into a situation or path that's ultimately not going to lead anywhere by taking advantage of the knowledge that you have initially?
- <b>maintaining arc-consistency</b> algorithm for enforcing arc-consistency every time we make a new assignment
    - sometimes you can enforce arc-consistency using the AC-3 algo at the very beginning of the problem, before you even begin searching in order to limit the domain and the variables in order to make it easier to search
    - you can also take advantage of the interleaving of enforcing arc-consistency with search such that every time you make a new assignment in the search process, you go ahead and enforce arc consistency as well, to make sure that you eliminate possible values from domains whenever possible
    - when you make a new assignment to X, call AC-3, starting with a queue of all arcs (Y, X) where Y is a neighbor of X
- revised version of the backtrack function:

```
function BACKTRACK(assignment, csp): // assignment is initially empty - no values yet assigned to variables
    if assignment complete: return assignment
    var = SELECT-UNASSIGNED-VAR(assignment, csp)
    for value in DOMAIN-VALUES(var, assignment, csp):
        if value consistent with assignment:
            add {var = value} to assignment
            inferences = INFERENCE(assignment, csp)
            if inferences != failure: add inferences to assignment
            result = BACKTRACK(assignment, csp)
            if result != failure: return result
        remove {var = value} and inferences from assignment
    return failure
```

- there are other heuristics you can use to try and improve the efficiency of the search process
    - SELECT-UNASSIGNED-VAR() from the backtrack function - selecting some variable in the csp that has not yet been assigned - so far random, but by following certain heuristics you might be able to make the search process much more efficient just by choosing very carefully which variable we should explore next
        - minimum remaining values (MRV) heuristic: select the variable that has the smallest domain
        - degree heuristic (the degree of a node is the number of nodes that are attached to that node): select the variable that has the highest degree - this is immediately constrain the rest of the variables more and eliminate large senctions of the state space that you don't need to search through
    - DOMAIN-VALUES() - getting back a sequence of all of the values inside a variable's domain - so far you've went in order -e.g. Mon, Tue, Wed ...
        - it might be more efficient to choose values that are more likely to be solutions first
        - least-constraining values heuristic: return variables in order by number of choices that are ruled out of neighboring variables
            - try least-constraining value first

## Conclusions

- Problem formulation:
    - local search
    - linear programming
    - constraint satisfaction