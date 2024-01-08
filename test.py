
# Fonction pour ajouter un sommet au graphe
def add_sommet(courant,liste_voisins,colors):
    
    # Vérifier si la liste de voisins est vide
    if not liste_voisins or liste_voisins[0] == '':
        g[courant] = []
        colors[courant] = 1
    else:
        # Vérifier si tous les voisins existent dans le graphe
        for voisin in liste_voisins:
            if voisin not in g:
                print("Tous les voisins doivent exister.")
                return False
        
        # Ajouter le sommet au graphe avec ses voisins
        g[courant] = liste_voisins
        
        # Ajouter le sommet comme voisin de chaque voisin
        for voisin in liste_voisins:
            g[voisin].append(courant)
        
        # Trouver la première couleur disponible pour le sommet
        voisins_couleurs = {colors[voisin] for voisin in liste_voisins if voisin in colors}
        for couleur in range(1, 17):
            if couleur not in voisins_couleurs:
                colors[courant] = couleur
                break
    
    # Incrémenter le sommet courant
    courant += 1

g = {}
colors = []
# Exemple d'utilisation de la fonction
add_sommet(len(g),[],colors)
add_sommet(len(g),[1, 3],colors)  # Ajouter un sommet avec les voisins 2 et 3
print(g)  # Afficher le graphe
print(colors)  # Afficher les couleurs des sommets
