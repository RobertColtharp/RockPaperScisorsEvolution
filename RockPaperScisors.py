from game import Game
from player import Player
import tkinter as tk
from tkinter import messagebox
from menu import GameGUI 

def main():
    
    game = Game()
    
    while True:
        game.play_match()
        game.print_totals()
        
        #play_again = input("Press (y) to play another round. Press (s) to select a player.").strip().lower()
        #if play_again == 'y':
        #    continue
        #elif play_again == 's':
        #    player_id = input("Input the Id of the player you'd like to select.").strip()
        #    if player_id.isdigit():
        #        game.set_selected_player(int(player_id))
        #        game.print_player_match_history()
        
main()

#if __name__ == "__main__":
#    root = tk.Tk()
#    app = GameGUI(root)
#    root.mainloop()