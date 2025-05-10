import tkinter as tk
from tkinter import messagebox

# Define win conditions
win_conditions = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
    [0, 4, 8], [2, 4, 6]              # Diagonal
]

# Check for winner
def check_winner():
    global winner
    for combo in win_conditions:
        if buttons[combo[0]]['text'] == buttons[combo[1]]['text'] == buttons[combo[2]]['text'] != "":
            # Highlight winning combination
            for index in combo:
                buttons[index].config(bg='green')
            winner = True
            messagebox.showinfo("Tic Tac Toe", f"Player {buttons[combo[0]]['text']} wins!")
            root.quit()

    # Check for draw
    if all(button['text'] != "" for button in buttons) and not winner:
        messagebox.showinfo("Tic Tac Toe", "It's a Draw!")
        root.quit()

# Handle button clicks
def button_click(index):
    global winner
    if buttons[index]['text'] == "" and not winner:
        buttons[index]['text'] = current_player
        check_winner()
        toggle_player()

# Toggle between players
def toggle_player():
    global current_player
    current_player = "X" if current_player == "O" else "O"
    label.config(text=f"Player {current_player}'s turn")

# GUI setup
root = tk.Tk()
root.geometry('370x350')
root.title('Tic Tac Toe')

# Initialize variables
buttons = []
current_player = "X"
winner = False

# Create buttons for the board
for i in range(9):
    button = tk.Button(root, text="", font=('normal', 25), height=2, width=6, 
                       command=lambda i=i: button_click(i))
    button.grid(row=i // 3, column=i % 3)
    buttons.append(button)

# Add label to display current player's turn
label = tk.Label(root, text=f"Player {current_player}'s turn", font=('normal', 16))
label.grid(row=3, column=0, columnspan=3)

root.mainloop()
