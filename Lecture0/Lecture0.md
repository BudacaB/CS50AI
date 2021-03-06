## Search

https://cs50.harvard.edu/ai/2020/notes/0/

---

### Search problems

- Terminology:
    - agent - entity that perceives its environment and acts upon that environment
    - state - a configuration of the agent and its environment
    - initial state - the state in which the agent begins
    - actions - choices that can be made in a state -> we can define actions as a function - e.g. ACTIONS(s) returns the set of actions that can be executed in state <em>s</em>
    - transition model - a description of what state results from performing any applicable action in any state -> define as a function - e.g. RESULT(s, a) returns the state resulting from performing action <em>a</em> in state <em>s</em>
    - state space - the set of all states reachable from the initial state by any sequence of actions -> can be represented by a graph where the nodes are the states and the edges are the actions that we can take in any particular state
    - goal test - way to determine whether a given state is a goal state
    - path cost - numerical cost associated with a given path -> can be added to the state space graph for each action - actions can have different costs for some problems; or cost the same for others and in this case only the total number of steps matters

- Search Problems:
    - initial state
    - actions
    - transition model
    - goal test
    - path cost function

### Solving Search Problems

- Solution - a sequence of actions that leads from the initial state to the goal state
- Optimal solution - a solution that has the lowest path cost among all solutions
- In a search process, data is often stored in a <b>node</b>, a data structure that contains the following data:
    - a <em>state</em>
    - its parent node, through which the current node was generated
    - the action that was applied to the state of the parent to get to the current node
    - the path cost from the initial state to this node

### Approach

- Start the search algorithm with a <b>frontier</b> that contains just the initial state (frontier = data structure that represents all of the things that we could explore next, that we haven't yet explored or visited)
- Repeat:
    - if the frontier is empty, then no solution
    - otherwise, remove a node from the frontier (work on the node - for example in the beginning the frontier contains just one node)
    - if node contains goal state, return the solution
    - otherwise, expand the node (look at all of the neighbors of that node), add resulting nodes to the frontier
- <b>Sometimes an infite loop can appear if for example if node A points to node B and node B points to node A as well</b>

### Revised approach

- Start with a frontier that contains the initial state
- Start with an empty explored set
- Repeat:
    - if the frontier is empty, then no solution
    - remove a node from the frontier
    - if node contains goal state, return the solution
    - add the node to the explored set
    - expand the node, add resulting nodes to the frontier if they aren't already in the frontier or in the explored set

### DFS and BFS

- It's also important how the frontier is structured, how we add and remove nodes from this data structure
    - <b>Depth-first search (DFS) - search algorithm that always expands the deepest node in the frontier</b>
        - <b>uses a stack for the frontier - data structure that is a last-in first-out (LIFO) data type</b>
    - <b>Breadth-first search (BFS) - search algorithm that always expands the shallowest node in the frontier</b>
        - <b>uses a queue (first-in first-out data type - FIFO) for the frontier</b>

### Types of search algorithms

- uninformed search - search strategy that uses no problem-specific knowledge -> DFS and BFS
- informed search - search strategy that uses problem-specific knowledge to find solutions more efficiently
    - e.g. for a maze, this problem specific knowledge is something like: being in a square that's geographically closer to the goal is better than being in a square that's geographically further away
    - this we can only know by thinking about this problem and reasoning about what knowledge might be helpful for our AI agent to know a little something about

### Types of informed search algorithms

- Greedy best-first search (GBFS) 
    - search algorithm that expands the node that is closesd to the goal, as estimated by a heuristic function <em>h(n)</em>
    - 'greedy' because it selects the best option locally, which isn't necessarily optimal in the big picture
    - heuristic function - takes a state as input and returns an estimate of how close we are to the goal
        - e.g. for a maze, it can estimate based on (x, y) coordinates if a square is closer to the goal than another
        - it can use the <b>'Manhattan distance'</b> for a maze as the heuristic type - ignoring the walls to 'relax' the problem, how many squares / steps, vertically and horizontally (not diagonally), are needed to get to the goal from a specific square
        - it isn't a guarantee of how many steps it's going to take, it's only an estimation
    - we will always explore the node that has the smallest value for the heuristic function - if it has the smallest Manhattan distance to the goal
- A* search
    - search algorithm that expands the node with the lowest value of <em>g(n) + h(n)</em>
        - g(n) = cost to reach node
        - h(n) = estimated cost to goal
    - optimal if:
        - <em>h(n)</em> is admissible (never overestimates the true cost - get it exactly right or underestimate), and
        - <em>h(n)</em> is consistent (for every node <em>n</em> and successor <em>n'</em> with step cost <em>c, h(n) <= h(n') + c</em>)
    - it does have a tendency to use quite a bit of memory
- Search algorithms tend to be optimised for different use cases but it's choosing the heuristic that can be the interesting challenge

### Adversarial Search

- A case when there isn't a single agent, and each agent tried to find the solution while stopping the other agent from finding it - e.g. games like tic-tac-toe
- Minimax algorithm - works very well for these deterministic games where there are two players, for the example of tic-tac-toe
    - the outcomes are represented mathematically as -1 if O wins, 0 if it's a draw and 1 if X wins
    - MAX (X) aims to maximize score
    - MIN (O) aims to minimize the score 
    - Game:
        - S<sub>0</sub>: initial state
        - PLAYER(s): function that returns which players to move in state <em>s</em>
        - ACTIONS(s): returns legal moves in state <em>s</em>
        - RESULT(s, a): returns state after action <em>a</em> taken in state <em>s</em>
        - TERMINAL(s): checks if state <em>s</em> is a terminal state - a player has gotten three in a row or all of the squares of the tic-tac-toe board are filled
        - UTILITY(s): final numerical value for terminal state <em>s</em> - if X wins the game, value of 1, if O wins the game, value of -1, if nobody has won the game, value of 0
    - pseudocode:
        - given a state <em>s</em>:
            - MAX picks action <em>a</em> in ACTIONS(s) that produces highest value of MIN-VALUE(RESULT(s, a)) - the possible values that the MIN player will pick when trying to minimize the result of the action picked by the MAX player
            - MIN picks action in <em>a</em> in ACTIONS(s) that produces smallest value of MAX-VALUE(RESULT(s, a)) - doing the same thing but backwards, considering what the MAX player would choose to do

            ```
            function MAX-VALUE(state):
                if TERMINAL(state):
                    return UTILITY(state)
                v = -???
                for action in ACTIONS(state):
                    v = MAX(v, MIN-VALUE(RESULT(state, action)))
                return v
            ```

            ```
            function MIN-VALUE(state):
                if TERMINAL(state):
                    return UTILITY(state)
                v = ???
                for action in ACTIONS(state):
                    v = MIN(v, MAX-VALUE(RESULT(state, action)))
                return v
            ```

### Optimizations for Minimax

- Alpha-Beta Pruning
    - For example, for 3 possible actions for the MAX player, if one can have a possible maximum value of 4, as the mininum value that the MIN player will pick for its next possible actions, and the next possible immediate action can have a possible maximum value of 3 based on the first possible next action from that state, no need to consider the other possible next actions, the MIN player would choose a value smaller than 4 anyway based on that 3
    - alpha and beta are the two values to keep track, the best you can do so far and the worst that you can do so far
    - pruning is the idea that if I have a big, long, deep search tree, I might be able to search more efficiently if I don't need to search through everything, if I can remove some of the nodes
- Depth-Limited Minimax
    - for example the more complex a game is, the more possible games there can be and the harder it gets for one computer to process all of those - 255168 possible tic-tac-toe games ; 280 billion possible games of chess after 4 moves for each player ; 10<sup>29000</sup> total possible chess games
    - normally Minimax is depth-unlimited, we just keep going layer after layer, move after move, until the end of the game
    - depth-limited Minimax is going to look ahead only for a certain number of moves, e.g. 10, 12 etc., but after that point we will stop and not look at additional moves that might come after that just because it would be computationally intractable to consider all those possible options
    - depth-limited Minimax still needs a way to assign a score to that last game board or game state it looks at to figure out what its current value is - we need to add an <b>evaluation function</b>
    - evaluation function - function that estimates the expected utility of the game from a given state
        - e.g. in a game of chess, if a game value of 1 means that 'white' wins and 0 means it's a draw and -1 means that 'black' wins, a score of 0.8 means 'white' is very likely to win, but certainly not guaranteed - the evaluation function estimates how good the game state happens to be
        - depending on how good the evaluation function is, that's ultimately what's going to constraint how good the AI is going to be