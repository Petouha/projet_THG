from src.backtracking_clean import *
from src.greedy import *
from src.welsh_powell import *

############################## GREEDY ##############################

def greedy_coloring(graph):
    n = len(graph)
    result = [-1] * n  # stocke la couleur assignée à chaque sommet

    result[0] = 0  # colorie le premier sommet avec la couleur 0

    for u in range(1, n):
        # Marque les couleurs indisponibles pour les sommets adjacents à u
        forbidden = set()

        for i in range(n):
            if graph[u][i] == 1 and result[i] != -1:
                forbidden.add(result[i])

        # Trouve la première couleur disponible et l'assigner
        result[u] = next(color for color in range(n) if color not in forbidden)

        # Réinitialise les couleurs disponibles pour le prochain sommet
    return result

############################## WELSH POWELL ##############################


def welsh_powell(graph):
    n = len(graph)
    degree = [sum(row) for row in graph]  # Calculer le degré de chaque sommet
    order = sorted(range(n), key=lambda x: -degree[x])  # Trier les sommets par degré

    result = [-1] * n

    for u in order:
        forbidden = set()
        for i in range(n):
            if graph[u][i] == 1 and result[i] != -1:
                forbidden.add(result[i])
        result[u] = next(color for color in range(n) if color not in forbidden)
    
    return result


############################## BACKTRACKING ##############################

def is_safe(graph, color, v, c):
    for i in range(len(graph)):
        if graph[v][i] == 1 and color[i] == c:
            return False
    return True

def graph_coloring_util(graph, m, color, v):
    if v == len(graph):
        return True

    for c in range(1, m + 1):
        if is_safe(graph, color, v, c):
            color[v] = c
            if graph_coloring_util(graph, m, color, v + 1):
                return True 
            color[v] = 0
    return False

def graph_coloring(graph, m):
    color = [0] * len(graph)
    if graph_coloring_util(graph, m, color, 0):
        return color
    return None

########################### TEST #############################

graph = [[0, 1, 1, 1, 0],
         [1, 0, 1, 0, 0],
         [1, 1, 0, 0, 0],
         [1, 0, 0, 0, 1],
         [0, 0, 0, 1, 0]]

print("Greedy Coloring:", greedy_coloring(graph))
print("Welsh-Powell Coloring:", welsh_powell(graph))
m = 4  # Nombre de couleurs
print("Backtracking Coloring:", Backtracking(liste_successeurs(graph), 3))
