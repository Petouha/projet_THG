import numpy as np
import math
from src.backtracking_clean import *
from src.greedy import *

def create_sudoku_empty(taille):
    
    liste =[]
    for i in range(taille*taille):
        
        for j in range(taille*taille):
            sublist = []
            for k in range(taille*taille):
                if k!=j:
                    sublist.append(((i)*taille*taille)+k)
            
            for k in range(taille*taille):  
                if k!=i:
                    sublist.append((j)+k*taille*taille)
            
            for k in range((i // taille)*taille,((i // taille)*taille+taille)):
                for l in range((j // taille)*taille,((j // taille)*taille+taille)):
                    if k!=i:
                        sublist.append(k*taille*taille+l)
            
            sublist = list(set(sublist))
            liste.append(sublist)
            
    return liste

def deTLaM(dico):
    num_nodes = len(dico)
    M = np.zeros((num_nodes, num_nodes))

    for node, successors in dico.items():
        for successor in successors:
            M[node, successor] = 1

    return M


def list_to_graph(lst):
    taille = int(math.sqrt(len(lst)))
    graph = np.zeros((taille, taille))
    i = 0
    for j in range(len(lst)):
        i = j // taille
        graph[i][j % taille] = lst[j]
    return graph
            

list = create_sudoku_empty(3)

dico = {}
for i, sublist in enumerate(list):
    dico[i] = sublist

test = (liste_successeurs(deTLaM(dico)))

print(list_to_graph(Backtracking(test,9)))

#greedyColoring(list,4)

