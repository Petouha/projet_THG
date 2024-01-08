import numpy as np
import math


def deMaTL(M):
    dico = {}
    for i in range(np.shape(M)[0]):
        dico[i+1]=[]
        for (j) in range(np.shape(M)[1]):
            if(M[i,j]==1 and i!=j):
                dico[i+1].append(j+1)
    return dico

def deTLaM(dico):
    num_nodes = len(dico)
    M = np.zeros((num_nodes, num_nodes))

    for node, successors in dico.items():
        for successor in successors:
            M[node, successor] = 1

    return M


def list_to_graph(lst):
    if lst is None:
        return None
    taille = int(math.sqrt(len(lst)))
    graph = np.zeros((taille, taille))
    i = 0
    for j in range(len(lst)):
        i = j // taille
        graph[i][j % taille] = lst[j]
    return graph


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


