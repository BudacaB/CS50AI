from re import A
from logic import *

rain = Symbol("rain") # it is raining
hagrid = Symbol("hagrid") # Harry visited Hagrid
dumbledore = Symbol("dumbledore") # Harry visited Dumbledore

knowledge = And(
    Implication(Not(rain), hagrid),
    Or(hagrid, dumbledore),
    Not(And(hagrid, dumbledore)),
    dumbledore
)

# print(knowledge.formula())
print(model_check(knowledge, rain)) # in every world that this knowledge is true, it is raining / there is no world where this knowledge is true and it is not raining
