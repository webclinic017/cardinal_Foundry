#dependencies
import random
import numpy as np
import pandas as pd
#function
def generate(x=int):
    sequence = [i for i in range(x)]
    for i in range(x):
        selection = random.choice(sequence)
        return print(selection)

generate(4)
