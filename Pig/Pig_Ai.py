import random
import pickle

class Ai:
    def __init__(self, level) -> None:
        self.points = 0
        self.name = ""
        self.perfect_play = None
        self.pause_game = False
        self.roll_dice = self.behaviour_select(level)

    def load_perfection(self) -> None:
        with open("pig_Perfect_play.bin", "rb") as f:
            self.perfect_play = pickle.load(f)

    def behaviour_select(self, difficulty) -> function:
        def simple(game) -> bool:
            return not random.randint(1, 10) == 4

        def normal(game) -> bool:
            return game.round_points < 20

        def hard(game) -> bool:
            return self.perfect_play[self.points][game.player1.points] > game.round_points

        match difficulty:
            case 1:
                self.name = "pig-let"
                return simple
            case 2:
                self.name = "hog"
                return normal
            case 3:
                self.load_perfection()
                self.name = "Boar"
                return hard
