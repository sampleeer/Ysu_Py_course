"""
import json
with open('output.json ', 'r') as f:
    data = json.load(f)

for item in data["subordinates"].items():
    print(item[0], item[1])
"""


import numpy as np
from itertools import groupby

def encode(a):
    #YOUR CODE
    smth = [(k, sum(1 for i in g)) for k,g in groupby(a)]
    #print(smth)
    arr = np.array([x[0] for x in smth])
    arr2 = np.array([x[1] for x in smth])
    #print(arr, arr2)
    result = np.array([arr, arr2])
    return result


a = np.array([1, 2, 2, 3, 3, 1, 1, 5, 5, 2, 3, 3])
print(encode(a))