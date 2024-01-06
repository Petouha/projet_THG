import numpy as np

def deMaTL(M):
    dico = {}
    for i in range(np.shape(M)[0]):
        dico[i+1]=[]
        for (j) in range(np.shape(M)[1]):
            if(M[i,j]==1 and i!=j):
                dico[i+1].append(j+1)
    return dico

def isSafe(v, graph, colors, c):
    for i in range(len(graph)):
        if graph[v][i] == 1 and colors[i] == c:
            return False
    return True

def welshPowell2(dico):
    # Tri du dico de manière décroissante selon la taille, ...
    sorted_list = sorted(dico.items(),  key=lambda x: len(x[1]), reverse=True)
    # Initialisation du tableau des couleurs à -1
    colors = len(dico) * [-1]
    # Initialisation de la première couleur
    color = 0
    # Boucle principale qui parcourt l'ensemble des sommets
    for i in range(len(sorted_list)):
        # Continuer si il y a des sommets sans couleurs
        if -1 in colors:
            vertex = sorted_list[i][0] - 1
            if colors[vertex] == -1:
                # Chercher une couleur sûre pour le sommet
                for c in range(len(dico)):
                    if isSafe(vertex, graph, colors, c):
                        colors[vertex] = c
                        break
            # Colorier les sommets non adjacents avec la même couleur
            for k in range(len(dico)):
                if isSafe(k, graph, colors, colors[vertex]):
                    colors[k] = colors[vertex]
        else:
            break
    return colors

graph = np.array([[0, 1, 0, 0, 1, 1, 1], 
    [1, 0, 1, 1, 0, 0, 0], 
    [0, 1, 0, 1, 0, 0, 1], 
    [0, 1, 1, 0, 1, 0, 0], 
    [1, 0, 0, 1, 0, 1, 1], 
    [1, 0, 0, 0, 1, 0, 1], 
    [1, 0, 1, 0, 1, 1, 0 ]])

dico = deMaTL(graph)
print(dico)
# for i in range(np.shape(graph)[0]):
#     list_succ.append(successeurs(graph,i+1))
# print(list_succ)



print(welshPowell2(dico))
