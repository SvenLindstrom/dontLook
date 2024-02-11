import random
import pickle

class Ai:
    def __init__(self, level) -> None:
        self.points = 0
        self.name = ''
        self.Perfect_play = None
        self.pause_Game = False
        self.rollDice = self.behaviour_select(level)


    def load_Perfection(self):
        with open('pig_Perfect_play.bin', 'rb') as f:
            self.Perfect_play = pickle.load(f)

    def behaviour_select(self, difficulty):
        def simple(player1, round_points):
            return not random.randint(1,10) == 4

        def normal(player1, round_points):
            return round_points < 20
        
        def hard(player1, round_points):
            return self.Perfect_play[self.points][player1.points] > round_points 
        
        match difficulty:
            case 1:
                self.name = 'pig-let'
                return simple
            case 2:
                self.name = 'hog'
                return normal
            case 3: 
                self.load_Perfection()
                self.name = 'Boar'
                return hard