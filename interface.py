import tkinter as tk
from tkinter import messagebox, simpledialog,ttk
from sudoku import *
from random import *

def validate_input(value):
    if value == "" or (value.isdigit() and 1 <= int(value) <= 9):
        return True
    return False

# Fonction pour générer une nouvelle grille de Sudoku
def generate_sudoku(size=3):
    reset_sudoku()
    difficulty = choose_difficulty()

    if difficulty < 0:
        return False
    
      # Générer une grille complète de Sudoku aléatoirement
    grid = solve_sudoku(np.zeros((size*size,size*size)))
    
    # Enlever des chiffres pour obtenir la difficulté voulue
    cells_to_remove = int(81 * (1 - difficulty))
    for _ in range(cells_to_remove):
        row, col = randint(0, 8), randint(0, 8)
        while grid[row, col] == -1:
            row, col = randint(0, 8), randint(0, 8)
        grid[row, col] = -1

    # Afficher la grille dans l'interface graphique
    for i in range(9):
        for j in range(9):
            value = int(grid[i, j])
            if value != -1:
                sudoku_cells[i][j].delete(0, tk.END)
                sudoku_cells[i][j].insert(0, str(value))
                window.update()
                window.after(10)
# Fonction pour résoudre le Sudoku actuel
def solve():
    solved = (solve_sudoku(list_to_graph(get_sudoku_numbers())))
    #Si il n'y a pas de solution c'est que le sudoku est faux
    if(solved is None):
        messagebox.showerror("ERREUR DES VALEURS","Votre sudoku est faux")
        return False
    
    generate_button.config(state="disabled")
    reset_button.config(state="disabled")
    solve_button.config(state="disabled")
    
    #Remplir les cases avec la solution
    
    for i in range(9):
        for j in range(9):
            value = int(solved[i, j])
            sudoku_cells[i][j].delete(0,tk.END)
            sudoku_cells[i][j].insert(0, str(value) if value != -1 else '')
            window.update()
            window.after(10)
            
    generate_button.config(state="normal")
    reset_button.config(state="normal")
    solve_button.config(state="normal")


# Fonction pour réinitialiser la grille de Sudoku
def reset_sudoku():
    generate_button.config(state="disabled")
    reset_button.config(state="disabled")
    solve_button.config(state="disabled")
    
    for i in range(9):
        for j in range(9):
            sudoku_cells[i][j].delete(0, tk.END)
            window.update()
            window.after(5)
            
    generate_button.config(state="normal")
    reset_button.config(state="normal")
    solve_button.config(state="normal")
    
    

# Fonction pour obtenir les numéros de la grille de Sudoku sous forme de liste 
def get_sudoku_numbers():
    sudoku_numbers = [int(cell.get()) if cell.get() else 0 for row in sudoku_cells for cell in row]
    return sudoku_numbers

# Créer la fenêtre principale
window = tk.Tk()
window.title("Sudoku Game")

def choose_difficulty():
    # Définir les niveaux de difficulté disponibles
    difficulties = ['Facile', 'Moyen', 'Difficile']
    
    # Variable de contrôle pour stocker la difficulté sélectionnée
    difficulty_var = tk.StringVar(window)
    difficulty_var.set(None)
    
    # Créer une boîte de dialogue pour choisir la difficulté
    dialog = tk.Toplevel(window)
    dialog.title("Choisir la difficulté") 
    
    # Ajouter une étiquette à la boîte de dialogue
    label = tk.Label(dialog, text="Sélectionnez le niveau de difficulté :")
    label.pack(pady=10)
    
    # Ajouter une liste déroulante avec les niveaux de difficulté
    combobox = ttk.Combobox(dialog, values=difficulties, textvariable=difficulty_var, state="readonly")
    combobox.pack(pady=10)
    
    # Ajouter un bouton OK pour fermer la boîte de dialogue
    ok_button = tk.Button(dialog, text="OK", command=dialog.destroy)
    ok_button.pack(pady=10)
    
    # Attendre que la boîte de dialogue se ferme
    dialog.wait_window(dialog)
    
    # Récupérer la difficulté sélectionnée
    result = difficulty_var.get()
    print(result)
    
    # Assigner une valeur de poids en fonction de la difficulté choisie
    if result == 'Facile':
        return 0.7
    elif result == 'Moyen':
        return 0.45
    elif result == 'Difficile':
        return 0.2
    else:
        return -1



# Créer une grille 9x9 de champs de saisie
validate_cmd = window.register(validate_input)
sudoku_cells = [
    [
        tk.Entry(
            window, width=2, font=('Arial', 24), justify='center',
            validate="key", validatecommand=(validate_cmd, '%P')
        ) for j in range(9)
    ] for i in range(9)
]

for i in range(9):
    for j in range(9):
        sudoku_cells[i][j].grid(row=i, column=j, sticky="nsew", padx=(1), pady=1)


# Créer les boutons
generate_button = tk.Button(window, text="Générer", command=generate_sudoku)
solve_button = tk.Button(window, text="Résoudre", command=solve)
reset_button = tk.Button(window, text="Effacer", command=reset_sudoku)

# Positionner les boutons
generate_button.grid(row=9, column=0, columnspan=3)
solve_button.grid(row=9, column=3, columnspan=3)
reset_button.grid(row=9, column=6, columnspan=3)


window.mainloop()
