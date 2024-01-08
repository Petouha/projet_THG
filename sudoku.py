import numpy as np
from src.backtracking_clean import *


def create_sudoku_empty(taille):
    
    liste =[]
    #boucler sur le sudoku en mettant les relations dans une liste de listes
    for i in range(taille*taille):
        for j in range(taille*taille):
            #pour chaque sommet, relier avec la ligne
            sublist = []
            for k in range(taille*taille):
                if k!=j:
                    sublist.append(((i)*taille*taille)+k)
            #relier avec la colonne
            for k in range(taille*taille):  
                if k!=i:
                    sublist.append((j)+k*taille*taille)
            #relier avec le carré correspondant
            for k in range((i // taille)*taille,((i // taille)*taille+taille)):
                for l in range((j // taille)*taille,((j // taille)*taille+taille)):
                    if k!=i:
                        sublist.append(k*taille*taille+l)
            #enlever les doublons
            sublist = list(set(sublist))
            liste.append(sublist)
            
    #retourner le graph
    dico = {}
    for i, sublist in enumerate(liste):
        dico[i] = sublist
    return liste_successeurs(deTLaM(dico)) 

    
def solve_sudoku(graph):
    
    if not is_valid_sudoku(graph):
        return None
    
    #mettre les cases entre 0 et 8
    taille = np.shape(graph)[0]
    for i in range(taille):
        for j in range(taille):
            graph[i][j]=graph[i][j]-1
        

    liste = create_sudoku_empty(int(math.sqrt(taille)))
    solved = list_to_graph(Backtracking(liste,taille,list(graph.flatten())))

    if solved is None:
        return None
    #remettre les cases entre 1 et 9
    for i in range(np.shape(solved)[0]):
        for j in range(np.shape(solved)[0]):
            solved[i][j]=solved[i][j]+1
    return solved

def is_valid_sudoku(grid):
    size = np.shape(grid)[0]
    for i in range(size):
        # Check each row
        if not is_valid_group(grid[i, :]):
            return False
        # Check each column
        if not is_valid_group(grid[:, i]):
            return False

    # Check each 3x3 subgrid
    for i in range(0, size, 3):
        for j in range(0, size, 3):
            if not is_valid_group(grid[i:i+3, j:j+3].flatten()):
                return False

    return True

def is_valid_group(group):
    group = [num for num in group if num != 0]  # Remove zeros (empty cells)
    return len(group) == len(set(group))
