import random
import os
import subprocess
from player import Player

class Game:
    def __init__(self):
        self.players = []
        self.livingPlayers = []
        self.playerCount = 0
        self.playersNeedingToBeMatched = []
        self.round = 0
        self.matches = []
        self.totalRock = 0
        self.totalPaper = 0
        self.totalScissors = 0
        self.totalPlayers = 0
        self.selectedPlayer = None
        
        self.start_up()
        
    def start_up(self):
        self.create_players(1000)
        self.livingPlayers = self.players[:]
        self.create_matches()
        self.count_players() 
        
    def create_players(self, amount):
        for x in range(amount): #change to user input later also make sure user input is even
            self.playerCount =+ 1
            self.players.append(Player(x))
    
    def birth(self, parent: Player):
        baby = Player(self.playerCount)
        baby.parentId = parent.id
        self.playerCount =+1
        parent.had_child(baby.id)
        self.players.append(baby)
        self.livingPlayers.append(baby)
        
    def death(self, deadPlayer: Player):
        for index, player in enumerate(self.livingPlayers):
            if player.id == deadPlayer.id:
                player.died()
                del self.livingPlayers[index]
                
    def create_matches(self):
        self.playersNeedingToBeMatched = self.livingPlayers[:]
        
        while len(self.playersNeedingToBeMatched) >= 2:
            player1 = random.choice(self.playersNeedingToBeMatched)
            self.playersNeedingToBeMatched.remove(player1)
            player2 = random.choice(self.playersNeedingToBeMatched)
            self.playersNeedingToBeMatched.remove(player2)
            self.matches.append((player1, player2))
            
    def add_loser(self, player:Player):
        player.add_loss()
        if self.chance(90):
            self.death(player)
        
    def add_winner(self, player:Player):
        player.add_win()
        if self.chance(100):
            self.birth(player)
            self.birth(player)
        else:
            return
        
    def handle_tie(self, player1:Player, player2:Player):
        player1.add_tie()
        if self.chance(.05):
            self.death(player1)
        player2.add_tie()
        if self.chance(.05):
            self.death(player2)
            
    def play_match(self):
        self.round += 1
        for match in self.matches:
            player1, player2 = match
            self.determine_winner(player1, player2)
            self.add_to_player_memory(player1, player2)
        self.cleanup()
            
    def determine_winner(self, player1: Player, player2: Player):
        outcomes = {
                1:3, # rock beats scissors
                3:2, # scissors beat paper
                2:1  # paper beats rock
            }
        
        if player1.choice == player2.choice:
            self.handle_tie(player1, player2)
            
        elif outcomes[player1.choice] == player2.choice:
            self.add_winner(player1)
            self.add_loser(player2)
            
        else:
            self.add_winner(player2)
            self.add_loser(player1)
            
    def cleanup(self):
        self.playersNeedingToBeMatched = []
        self.matches = []
        self.create_matches()
        self.count_players()
        
    def count_players(self):
        counts = {1: 0, 2: 0, 3: 0}
        for player in self.livingPlayers:
            if player.choice in counts:
                counts[player.choice] += 1
                
        self.totalRock = counts[1]
        self.totalPaper = counts[2]
        self.totalScissors = counts[3]
        self.totalPlayers = self.totalRock + self.totalPaper + self.totalScissors
        
    def clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def print_totals(self):
        self.clear_console()
        print(f"Round {self.round} Results:")
        print(f"Total Players: {self.totalPlayers}")
        print(f"Rock: {self.totalRock}")
        print(f"Paper: {self.totalPaper}")
        print(f"Scissors: {self.totalScissors}")
        
    def add_to_player_memory(self, player1: Player, player2: Player):
        player1.add_to_match_memory(player2.id, player2.choice, player1.lastMatch)
        player2.add_to_match_memory(player1.id, player1.choice, player2.lastMatch)

    def set_selected_player(self, id: int):
        if id is None:
            return (print('No ID input'))
        else:
            for player in self.players:
                if player.id == id:
                    self.selectedPlayer = player
                    break
            
    def print_player_match_history(self):
        print(f"Here's {self.selectedPlayer.id}'s last 5 matches: ")
        for x in self.selectedPlayer.matchMemory:
            print(f"Opponent: {x[0]}")
            print(f"Opponent Choice: {x[1]}")
            print(f"Outcome: {x[2]}\n")
    
    def chance(self, chance):
        if random.random() < (chance/100):
            return True
        else:
            return False
        