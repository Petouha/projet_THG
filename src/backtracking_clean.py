import numpy as np
from src.tools import *

def peutColorier(graph,colors,sommet,color):
    # Test if any neighbors of the vertex have the same color
    # Return true if none of the adjacent vertices are colored this way
    for element in graph[sommet-1]:
        if(colors[element -1] == color):
            return False
    return True

def testerBackTracking(graph, color_nbr, colors, sommet):
    # Stop condition: if we reach vertex n+1, we've successfully colored all vertices
    if sommet == len(graph) + 1:
        return True

    # Skip the vertex if it already has a pre-assigned color (not -1)
    if colors[sommet - 1] != -1:
        return testerBackTracking(graph, color_nbr, colors, sommet + 1)

    # Try each color for the current vertex
    for c in range(color_nbr):
        # Check if the current vertex can be colored with color c
        if peutColorier(graph, colors, sommet, c):
            colors[sommet - 1] = c  # Assign color c to the vertex
            # Recursively try to color the next vertex
            if testerBackTracking(graph, color_nbr, colors, sommet + 1):
                return True
            # No solution found with color c, reset the vertex color to -1
            colors[sommet - 1] = -1
    return False

def Backtracking(graph, color_nbr, colors):
    if not colors:
        colors = [-1] * len(graph)
    sommet = 1
    if testerBackTracking(graph, color_nbr, colors, sommet) == None:
        print("Impossible to find a solution")
        return None
    return colors


# graph = np.array([[0, 1, 0, 0, 1, 1, 1], 
# [1, 0, 1, 1, 0, 0, 0], 
# [0, 1, 0, 1, 0, 0, 1], 
# [0, 1, 1, 0, 1, 0, 0], 
# [1, 0, 0, 1, 0, 1, 1], 
# [1, 0, 0, 0, 1, 0, 1], 
# [1, 0, 1, 0, 1, 1, 0 ]])

# graph2 = np.array([[0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0,],
#  [1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0,],
#  [1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0,],
#  [1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1,],
#  [1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0,],
#  [1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0,],
#  [0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0,],
#  [0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1,],
#  [1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0,],
#  [0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0,],
#  [0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1,],
#  [0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1,],
#  [1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1,],
#  [0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1,],
#  [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1,],
#  [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0,]])

# #print(graph2)


# list_succ = liste_successeurs(graph2)

# colors = []

# for i in range(16):
#     colors.append(-1)

# colors[0]=3
# colors[5]=0
# colors[10]=1
# colors[7]=1
# colors[15]=2

# print(list_to_graph(Backtracking(list_succ,4,colors)))