import tkinter as tk
from tkinter import messagebox
from player import Player
from game import Game

class GameGUI:
    def __init__ (self, root):
        self.root = root
        self.root.title("Rock, Paper, Scissors")
        
        self.game = Game()
        
        self.round_label = tk.Label(self.root, text="Round 0")
        self.round_label.pack()
        
        self.play_button = tk.Button(self.root, text="Play Round", command=self.play_round)
        self.play_button.pack()
        
    def play_round(self):
        self.game.play_match()
        self.game.print_totals()
        self.round_label.config(text=f"Round {self.game.round}")
        messagebox.showinfo("Round Results", self.get_round_results())
        
    def get_round_results(self):
        results = (f"Total Players: {self.game.totalPlayers}\n"
                f"Rock: {self.game.totalRock}\n"
                f"Paper: {self.game.totalPaper}\n"
                f"Scissors: {self.game.totalScissors}")
        return results  