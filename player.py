import random
from collections import deque

class Player:
    def __init__(self, player_id):
        self.id = player_id
        self.choice = 0
        self.wins = 0
        self.loss = 0
        self.ties = 0
        self.changes = 0
        self.lossStreak = 0
        self.winStreak = 0
        self.tieStreak = 0
        self.matchMemory = deque(maxlen=5) #id, other's choice, outcome
        self.lastMatch = None
        self.choiceMap = {
            1: "Rock",
            2: "Paper",
            3: "Scissors"
            }
        self.outcomeMap = {
            0: "Loss",
            1: "Win",
            2: "Tie"
            }
        self.childCount = 0
        self.children = []
        self.parentId = -1
        self.isDead = False
        
        self.make_choice()

    def make_choice(self):
        self.choice = random.choice([1, 2, 3])

    def add_win(self):
        self.lastMatch = 1
        self.wins += 1
        self.winStreak += 1
        self.lossStreak = 0
        self.tieStreak = 0
        self.evolve()
        
    def add_loss(self):
        self.lastMatch = 0
        self.loss += 1
        self.winStreak = 0
        self.lossStreak += 1
        self.tieStreak = 0
        self.evolve()
        
    def add_tie(self):
        self.lastMatch = 2
        self.ties += 1
        self.winStreak = 0
        self.lossStreak = 0
        self.tieStreak += 1
        self.evolve()
        
    def chance_to_evolve(self) -> float:
        if self.lossStreak > 1: #will think about evolving after losing twice in a row
            return (self.lossStreak * 5)
        elif self.tieStreak > 2: #will think about evolving after three ties
            return (self.tieStreak * 1.5)
        else: 
            return 5
        
    def evolve(self):
        rate = (self.chance_to_evolve()/100)
        if random.random() < rate:
            self.changes += 1
            if self.choice == 1:
                self.choice = random.choice([2, 3])
            elif self.choice == 2:
                self.choice = random.choice([1, 3])
            elif self.choice == 3:
                self.choice = random.choice([1, 2])
            else:
                self.make_choice()
                
    def add_to_match_memory(self, other_id, other_choice, result):
        self.matchMemory.appendleft((other_id, self.choiceMap[other_choice], self.outcomeMap[result]))            
        
    def had_child(self, child_id):
        self.childCount += 1
        self.children.append(child_id)
        
    def died(self):
        self.isDead = True
        