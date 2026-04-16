import tkinter as tk
import random
from player import GeniusComputerPlayer
from game import Tictactoe

def next_turn(row,col):

    square = row * 3 + col

    if game.board[square] == ' ' and game.winner is None:

        # human_player makes a move.
        game.make_move(square, human_player)
        buttons[row][col]['text'] = human_player

        result = check_winner()

        if result:
            return

        # ai_player makes a move.
        window.after(300, ai_move)  # small delay.

def ai_move():

    if game.winner is None:
        square = ai_player.get_move(game)
        game.make_move(square, 'o')

        row = square // 3
        col = square % 3

        buttons[row][col]['text'] = 'o'

        check_winner()

def highlight_winner(cells):
    for row, col in cells:
        buttons[row][col].config(bg="lightgreen")

def check_winner():

    if game.winner == 'x':
        cells = get_winning_cells()
        if cells:
            highlight_winner(cells)
        label.config(text="You win!")
        return True

    elif game.winner == 'o':
        cells = get_winning_cells()
        if cells:
            highlight_winner(cells)
        label.config(text="AI wins!")
        return True

    elif not game.empty_squares():
        for row in range(3):
            for col in range(3):
                buttons[row][col].config(bg="yellow")
        label.config(text="Tie!")
        return True

    return False

def get_winning_cells():
    board = game.board

    # rows
    for row in range(3):
        if board[row*3] == board[row*3+1] == board[row*3+2] != ' ':
            return [(row, 0), (row, 1), (row, 2)]

    # columns
    for col in range(3):
        if board[col] == board[col+3] == board[col+6] != ' ':
            return [(0, col), (1, col), (2, col)]

    # diagonals
    if board[0] == board[4] == board[8] != ' ':
        return [(0, 0), (1, 1), (2, 2)]

    if board[2] == board[4] == board[6] != ' ':
        return [(0, 2), (1, 1), (2, 0)]

    return None

def check_empty_spaces():

    for row in range(3):
        for col in range(3):
            if buttons[row][col]['text'] =="":
                return True
    return False

def new_game():
    global game
    game = Tictactoe()

    label.config(text="Your turn")

    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text="", bg="SystemButtonFace")


#My gui window.
window = tk.Tk()
window.title("Tic Tac Toe")

#i have two playes. One that uses x and one that uses o.
players = ["x","o"]
game = Tictactoe()
ai_player = GeniusComputerPlayer('o')
human_player = 'x'

#My 3x3 matrix for the classic tictactoe game.
buttons = [[None for _ in range(3)] for _ in range(3)]

#Indicate whose turn it is.
label = tk.Label(window, text='Your turn')
label.pack(side="top")

#Adding three new button.
reset_button = tk.Button(window, text="Reset", command=new_game)
reset_button.pack(side="bottom")

#I want to put my buttons on a frame.
frame = tk.Frame(window)
frame.pack()

for row in range(3):
    for col in range(3):
        buttons[row][col] = tk.Button(frame,
                                    text = "",
                                    width = 4,
                                    height = 2,
                                    font = ("Arial", 19),
                                    command =lambda r=row, c=col: next_turn(r,c))

        buttons[row][col].grid(row= row,column= col)

window.update_idletasks()
width = window.winfo_width()
height = window.winfo_height()
x = (window.winfo_screenwidth() // 2) - (width // 2)
y = (window.winfo_screenheight() // 2) - (height // 2)
window.geometry(f"{width}x{height}+{x}+{y}")

window.mainloop()
