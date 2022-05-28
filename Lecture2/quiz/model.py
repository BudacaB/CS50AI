from pomegranate import *

# Factory node has no parents
factory = Node(DiscreteDistribution({
    "A": 0.6,
    "B": 0.4,
}), name="factory")

# Defect node is conditional on factory
defect = Node(ConditionalProbabilityTable([
    ["A", "yes", 0.02],
    ["A", "no", 0.98],
    ["B", "yes", 0.04],
    ["B", "no", 0.96]
], [factory.distribution]), name="defect")

# Create a Bayesian Network and add states
model = BayesianNetwork()
model.add_states(factory, defect)

# Add edges connecting nodes
model.add_edge(factory, defect)

# Finalize model
model.bake()
