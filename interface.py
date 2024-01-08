import tkinter as tk
from tkinter import messagebox, simpledialog,ttk
from sudoku import *
from random import *

def validate_input(value):
    if value == "" or (value.isdigit() and 1 <= int(value) <= 9):
        return True
    return False

# Function to generate a new Sudoku puzzle
def generate_sudoku(size=3):
    reset_sudoku()
    difficulty = choose_difficulty()

    if difficulty < 0:
        return False
    
    # Generate a random completed Sudoku puzzle
    grid = solve_sudoku(np.zeros((size*size,size*size)))
    
    # Remove numbers to achieve desired difficulty
    cells_to_remove = int(81 * (1 - difficulty))
    for _ in range(cells_to_remove):
        row, col = randint(0, 8), randint(0, 8)
        while grid[row, col] == -1:
            row, col = randint(0, 8), randint(0, 8)
        grid[row, col] = -1

    # Display the puzzle in the GUI
    for i in range(9):
        for j in range(9):
            value = int(grid[i, j])
            if value != -1:
                sudoku_cells[i][j].delete(0, tk.END)
                sudoku_cells[i][j].insert(0, str(value))
                window.update()
                window.after(10)
# Function to solve the current Sudoku puzzle
def solve():
    # Implement Sudoku solving logic here
    solved = (solve_sudoku(list_to_graph(get_sudoku_numbers())))
    
    if(solved is None):
        messagebox.showerror("ERREUR DES VALEURS","Votre sudoku est faux")
        return False
    
    generate_button.config(state="disabled")
    reset_button.config(state="disabled")
    solve_button.config(state="disabled")
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


# Function to reset the Sudoku grid to empty
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
    
    

# Function to get the numbers from the Sudoku grid as a flat list
def get_sudoku_numbers():
    sudoku_numbers = [int(cell.get()) if cell.get() else 0 for row in sudoku_cells for cell in row]
    return sudoku_numbers

# Create the main window
window = tk.Tk()
window.title("Sudoku Game")

def choose_difficulty():
    difficulties = ['Easy', 'Medium', 'Difficult']
    
    
    
    difficulty_var = tk.StringVar(window)
    difficulty_var.set(None)  # Set default value
    
    dialog = tk.Toplevel(window)
    dialog.title("Choose Difficulty") 
    
    label = tk.Label(dialog, text="Select the difficulty level:")
    label.pack(pady=10)
    
    combobox = ttk.Combobox(dialog, values=difficulties, textvariable=difficulty_var, state="readonly")
    combobox.pack(pady=10)
    
    ok_button = tk.Button(dialog, text="OK", command=dialog.destroy)
    ok_button.pack(pady=10)
    
    dialog.wait_window(dialog)
    
    result = difficulty_var.get()
    print(result)
    if result == 'Easy':
        return 0.7
    elif result == 'Medium':
        return 0.45
    elif result == 'Difficult':
        return 0.2
    else:
        return -1  # Default to Medium if canceled



# Create a 9x9 grid of entry widgets
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
        # if i % 3 == 0 and j % 3 == 0:
        sudoku_cells[i][j].grid(row=i, column=j, sticky="nsew", padx=(1), pady=1)

# Create the buttons
generate_button = tk.Button(window, text="Generate", command=generate_sudoku)
solve_button = tk.Button(window, text="Solve", command=solve)
reset_button = tk.Button(window, text="Reset", command=reset_sudoku)

# Position the buttons
generate_button.grid(row=9, column=0, columnspan=3)
solve_button.grid(row=9, column=3, columnspan=3)
reset_button.grid(row=9, column=6, columnspan=3)

# Start the GUI event loop
window.mainloop()
