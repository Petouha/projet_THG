import tkinter as tk
from tkinter import messagebox
from sudoku import *
from random import *

def validate_input(value):
    if value == "" or (value.isdigit() and 1 <= int(value) <= 9):
        return True
    return False

# Function to generate a new Sudoku puzzle
def generate_sudoku(difficulty=0.1, size=3):
    reset_sudoku()

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
    print(list_to_graph(get_sudoku_numbers()))
    solved = (solve_sudoku(list_to_graph(get_sudoku_numbers())))
    print(solved)
    
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
        padx_value = 1 if (j + 1) % 3 == 0 and j < 8 else 0  # Add black strip after every 3 columns
        pady_value = 1 if (i + 1) % 3 == 0 and i < 8 else 0  # Add black strip after every 3 rows
        sudoku_cells[i][j].grid(row=i, column=j, sticky="nsew", padx=(padx_value), pady=pady_value)

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
