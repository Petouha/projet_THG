import numpy as np
from src.backtracking_clean import Backtracking
from src.tools import *
from sudoku import create_sudoku_empty
import matplotlib.pyplot as plt

def display_sudoku_image(ax, graph, title):
    cmap = 'tab10'
    ax.imshow(graph, cmap=cmap, vmin=-1, vmax=10, interpolation='none')

    for i in range(9):
        for j in range(9):
            value = graph[i, j]
            if value != -1:
                ax.text(j, i, str(value), color='black', ha='center', va='center', fontsize=12)

    ax.set_title(title)
    ax.set_xticks([])
    ax.set_yticks([])
    

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


for i in range(np.shape(graph)[0]):
    for j in range(np.shape(graph)[0]):
        graph[i][j]=graph[i][j]-1
        

   
list_succ = []

for i in range(len(graph)):
    list_succ.append(successeurs(graph,i+1))


liste = create_sudoku_empty(3)
solved = list_to_graph(Backtracking(liste,9,list(graph.flatten())))


for i in range(np.shape(solved)[0]):
    for j in range(np.shape(solved)[0]):
        solved[i][j]=solved[i][j]+1
   
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

plt.ion()

# Display the original Sudoku
fig, axs = plt.subplots(1, 2, figsize=(10, 5))
display_sudoku_image(axs[0], graph, 'Original Sudoku')

# Display the solved Sudoku
display_sudoku_image(axs[1], solved, 'Solved Sudoku')

# Disable interactive mode
plt.ioff()

# Show both plots
plt.show()

print(graph)

print(solved)