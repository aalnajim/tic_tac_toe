'''
Author: Abdullah A. Alnajim
Email:  aalnajim1@hotmail.com

..: Tic Tac Toe Game :..
play against the computer
the computer uses the Minimax algorithm to make its moves
the computer's move is random

..: Requirements :..
- Python 3.x
- tkinter library

..: How to Run :..
python3.12 tic_tac_toe.py
'''

import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe - vs Computer")
        self.player = "X"
        self.computer = "O"
        self.board = [" "] * 9
        self.buttons = []
        
        # Create game board buttons
        for i in range(3):
            row = []
            for j in range(3):
                btn = tk.Button(root, text=" ", font=('Helvetica', 20), width=5, height=2,
                              command=lambda i=i, j=j: self.player_click(i, j))
                btn.grid(row=i, column=j)
                row.append(btn)
            self.buttons.append(row)
            
        # Reset button
        reset_btn = tk.Button(root, text="Reset Game", command=self.reset_game)
        reset_btn.grid(row=3, column=0, columnspan=3, sticky="we")
    
    def player_click(self, row, col):
        index = row * 3 + col
        if self.board[index] == " ":
            self.board[index] = self.player
            self.buttons[row][col].config(text=self.player, state=tk.DISABLED)
            
            if self.check_winner(self.player):
                messagebox.showinfo("Game Over", "Congratulations! You win!")
                self.reset_game()
                return
            elif self.check_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()
                return
                
            self.computer_move()
    
    def computer_move(self):
        # Use Minimax to find the best move
        best_score = float('-inf')
        best_move = None
        
        for i in range(9):
            if self.board[i] == " ":
                self.board[i] = self.computer
                score = self.minimax(self.board, 0, False)
                self.board[i] = " "
                
                if score > best_score:
                    best_score = score
                    best_move = i
        
        if best_move is not None:
            row, col = divmod(best_move, 3)
            self.board[best_move] = self.computer
            self.buttons[row][col].config(text=self.computer, state=tk.DISABLED)
            
            if self.check_winner(self.computer):
                messagebox.showinfo("Game Over", "Computer wins!")
                self.reset_game()
            elif self.check_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()
    
    def minimax(self, board, depth, is_maximizing):
        if self.check_winner(self.computer):
            return 10 - depth
        elif self.check_winner(self.player):
            return depth - 10
        elif self.check_draw():
            return 0
        
        if is_maximizing:
            best_score = float('-inf')
            for i in range(9):
                if board[i] == " ":
                    board[i] = self.computer
                    score = self.minimax(board, depth + 1, False)
                    board[i] = " "
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(9):
                if board[i] == " ":
                    board[i] = self.player
                    score = self.minimax(board, depth + 1, True)
                    board[i] = " "
                    best_score = min(score, best_score)
            return best_score
    
    def check_winner(self, player):
        # Check rows, columns, and diagonals
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]             # Diagonals
        ]
        for condition in win_conditions:
            if all(self.board[i] == player for i in condition):
                return True
        return False
    
    def check_draw(self):
        return " " not in self.board
    
    def reset_game(self):
        self.board = [" "] * 9
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=" ", state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()