import numpy as np
from src.backtracking_clean import Backtracking
from src.tools import *
from sudoku import *
import matplotlib.pyplot as plt

def display_sudoku_image(ax, graph, title):
    cmap = 'tab10'
    ax.imshow(graph, cmap=cmap, vmin=-1, vmax=10, interpolation='none')

    for i in range(np.shape(graph)[0]):
        for j in range(np.shape(graph)[0]):
            value = graph[i, j]
            if value != -1:
                ax.text(j, i, str(int(value)), color='black', ha='center', va='center', fontsize=12)

    ax.set_title(title)
    ax.set_xticks([])
    ax.set_yticks([])
    



graph = np.array(
    [
        [0, 4, 3, 0, 8, 0, 2, 5, 0],
        [6, 7, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 9, 4],
        [9, 0, 0, 0, 0, 4, 0, 7, 0],
        [0, 0, 0, 6, 0, 8, 0, 0, 0],
        [0, 1, 0, 2, 0, 0, 0, 0, 3],
        [8, 2, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
        [0, 3, 4, 0, 9, 0, 7, 1, 0],
    ]
)

solved = solve_sudoku(np.copy(graph))

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