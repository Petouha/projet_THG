import numpy as np
from tools import deMaTL
# import os,sys
# parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# sys.path.append(parent_dir)

# from sudoku import *

def isSafe(v, graph, colors, c):
    # Vérifier si le sommet v peut être coloré avec la couleur c sans conflit
    for i in graph[v+1]:
        if colors[i - 1] == c:
            return False
    return True

def welshPowell(graph,colors=None):
    dico = deMaTL(graph)
    # Tri du dictionnaire par le nombre de successeurs, en ordre décroissant
    sorted_list = sorted(dico.items(), key=lambda x: len(x[1]), reverse=True)
    # Initialiser les couleurs de tous les sommets à -1 (aucune couleur) si colors est None
    if not colors:
        colors = len(dico) * [-1]
    # Assigner des couleurs aux sommets
    for i in range(len(sorted_list)):
        vertex = sorted_list[i][0]
        if colors[vertex - 1] == -1:
            for c in range(len(dico)):
                if isSafe(vertex - 1, dico, colors, c):
                    colors[vertex - 1] = c
                    break
    return colors

graph = np.array([[0, 1, 0, 0, 1, 1, 1], 
    [1, 0, 1, 1, 0, 0, 0], 
    [0, 1, 0, 1, 0, 0, 1], 
    [0, 1, 1, 0, 1, 0, 0], 
    [1, 0, 0, 1, 0, 1, 1], 
    [1, 0, 0, 0, 1, 0, 1], 
    [1, 0, 1, 0, 1, 1, 0 ]])

# Application de l'algorithme Welsh-Powell pour la coloration du graphe
print(welshPowell(graph))

