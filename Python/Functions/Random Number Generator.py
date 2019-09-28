#dependencies
import random
import numpy
import pandas
#function
def generate(x=int):
    sequence = [i for i in range(x)]
    for i in range(x):
        selection = random.choice(sequence)
        return print(selection)

generate(4)
