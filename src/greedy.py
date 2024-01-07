import numpy as np


def successeurs(graph,indice):
    if np.shape(graph)[0] < indice:
        return 0
    temp=(graph[indice-1])
    liste_successeurs=[]
    for index,element in enumerate(temp):
        if(element==1):
            liste_successeurs.append(index+1)
    return liste_successeurs

def greedyColoring(liste_suc, number):
     
    # tableau qui contient la couleur de chaque sommet
    #initialisé à -1 au début
    result = [-1] * number
    
    #le 1er sommet a sa couleur
    result[0] = 0
    
    used_colors = [False] * number
    
    for i in range(number):
        
       #mettre à vrai les couleurs utilisées
       for j in liste_suc[i]:
           if(result[j-1] != -1 ):
               used_colors[result[j-1]] = True
       #initialiser la couleur à 0
       color = 0
       
       #trouver la 1ère couleur non utilisée
       while color < number:
           if(used_colors[color] == False):
               break
           color += 1
       
       #attribuer la couleur trouvée au sommet i
       result[i] = color
       
       #réinitialiser les couleurs
       for j in liste_suc[i]:
           if(result[j-1] != -1):
               used_colors[result[j-1]] = False
    return result
    

graph = np.array([[0, 1, 0, 0, 1, 1, 1], 
[1, 0, 1, 1, 0, 0, 0], 
[0, 1, 0, 1, 0, 0, 1], 
[0, 1, 1, 0, 1, 0, 0], 
[1, 0, 0, 1, 0, 1, 1], 
[1, 0, 0, 0, 1, 0, 1], 
[1, 0, 1, 0, 1, 1, 0 ]])

list_succ = []

for i in range(len(graph)):
    list_succ.append(successeurs(graph,i+1))

    
    

         
print(list_succ)



print(greedyColoring(list_succ,len(list_succ)))