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

# list = create_sudoku_empty(3)



# print("----------------------")
# print(list)
# print("----------------------")
# colors = []

# for i in range(81):
#     colors.append(-1)

# colors[44] = -1
# colors[1]=7


# print(colors)

# #print(list_to_graph(Backtracking(test,9,colors)))
# print("\n")
# print(list_to_graph(Backtracking(list,9,0)))


# #greedyColoring(list,4)

