import numpy as np
from src.backtracking_clean import *


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
            
    dico = {}
    for i, sublist in enumerate(liste):
        dico[i] = sublist
    return liste_successeurs(deTLaM(dico)) 

    
def solve_sudoku(graph):
    taille = np.shape(graph)[0]
    for i in range(taille):
        for j in range(taille):
            graph[i][j]=graph[i][j]-1
        

    liste = create_sudoku_empty(int(math.sqrt(taille)))
    solved = list_to_graph(Backtracking(liste,taille,list(graph.flatten())))

    if solved is None:
        return None
    
    for i in range(np.shape(solved)[0]):
        for j in range(np.shape(solved)[0]):
            solved[i][j]=solved[i][j]+1
    return solved
