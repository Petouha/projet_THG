import numpy as np
from backtracking_clean import *

graph = np.array(
    [
        [0, 4, 3, 0, 8, 0, 2, 5, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 9, 4],
        [9, 0, 0, 0, 0, 4, 0, 7, 0],
        [0, 0, 0, 6, 0, 8, 0, 0, 0],
        [0, 1, 0, 2, 0, 0, 0, 0, 3],
        [8, 2, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
        [0, 3, 4, 0, 9, 0, 7, 1, 0],
    ]
)

list_succ = []

for i in range(len(graph)):
    list_succ.append(successeurs(graph,i+1))

print(graph)

Backtracking(list_succ,9)
