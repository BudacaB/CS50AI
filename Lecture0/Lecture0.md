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