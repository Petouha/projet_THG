import numpy as np

def liste_successeurs(graph):
    list_succ = []
    for i in range(len(graph)):
        list_succ.append(successeurs(graph,i+1))
    return list_succ


def successeurs(graph,sommet):
    if len(graph) < sommet:
        return 0
    
    temp=(graph[sommet-1])
    
    liste_successeurs=[]
    for index,element in enumerate(temp):
        if(element==1):
            liste_successeurs.append(index+1)
    return liste_successeurs

def peutColorier(graph,colors,sommet,color):
    #Teste pour chaque voisins du sommet s'il a la même couleur
    #Return vrai si aucun des sommets adjacents est colorié de cette manière
    for element in graph[sommet-1]:
        if(colors[element -1] == color):
            return False
        
    return True

def testerBackTracking(graph, color_nbr, colors, sommet):
    #condition d'arret
    #Si on arrive au sommet n+1, c'est qu'on a pu faire tous les autres
    
    if sommet == len(graph)+1:
        return True
    #on boucle sur toute les couleurs, une a une
    for c in range(color_nbr):
        #on teste si on peut colorier le sommet actuel avec la couleur c
        if (peutColorier(graph,colors,sommet,c) == True):
            #Cas de True:
                #on met la couleur du sommet à c
            colors[sommet-1] = c
            #on teste si pour le sommet+1 il existe une solution, sinon remonte et refais avec une autre couleur
            if testerBackTracking(graph,color_nbr,colors,sommet+1) == True:
                return True
            #On a pas trouver de solution avec la couleur c, on remet la couleur du sommet à -1
            colors[sommet-1] = -1
    

def Backtracking(graph, color_nbr):
    colors = [-1] * len(graph)
    sommet = 1
    if testerBackTracking( graph, color_nbr , colors , sommet) == None :
        print("impossible")
        return False
    print(colors)
    return True
        

graph = np.array([[0, 1, 0, 0, 1, 1, 1], 
[1, 0, 1, 1, 0, 0, 0], 
[0, 1, 0, 1, 0, 0, 1], 
[0, 1, 1, 0, 1, 0, 0], 
[1, 0, 0, 1, 0, 1, 1], 
[1, 0, 0, 0, 1, 0, 1], 
[1, 0, 1, 0, 1, 1, 0 ]])

list_succ = []


print(list_succ)


Backtracking(list_succ,4)