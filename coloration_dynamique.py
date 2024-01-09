def add_sommet(courant, liste_voisins, graphe, colors):
    # Assurer que colors a une entrée pour chaque sommet jusqu'au sommet courant
    while len(colors) < courant + 1:
        colors.append(0)
    
    # Vérifier si la liste de voisins est vide
    if not liste_voisins or liste_voisins[0] == '':
        graphe[courant] = []
        colors[courant] = 1
    else:
        # Vérifier si tous les voisins existent dans le graphe
        for voisin in liste_voisins:
            if voisin not in graphe:
                print("Tous les voisins doivent exister.")
                return False
        
        # Ajouter le sommet au graphe avec ses voisins
        graphe[courant] = liste_voisins
        
        # Assurer que chaque voisin a le sommet courant dans sa liste de voisins
        for voisin in liste_voisins:
            if courant not in graphe[voisin]:
                graphe[voisin].append(courant)
        
        # Trouver la première couleur disponible pour le sommet
        voisins_couleurs = {colors[voisin] for voisin in liste_voisins}
        for couleur in range(1, 17):
            if couleur not in voisins_couleurs:
                colors[courant] = couleur
                break

# Exemple d'utilisation de la fonction
graphe = {}
colors = []
add_sommet(0, [], graphe, colors)
add_sommet(1, [0], graphe, colors)  # Ajouter un sommet avec le voisin 0
add_sommet(2,[0,1],graphe,colors)
add_sommet(3,[0],graphe,colors)
print(graphe)  # Afficher le graphe
print(colors)  # Afficher les couleurs des sommets
