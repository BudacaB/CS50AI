from re import A
from logic import *

rain = Symbol("rain") # it is raining
hagrid = Symbol("hagrid") # Harry visited Hagrid
dumbledore = Symbol("dumbledore") # Harry visited Dumbledore

sentence = And(rain, hagrid)

print(sentence.formula())