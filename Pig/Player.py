class Player:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.roll_dice = self.player_behaviour
        self.pause_game = False

    def player_behaviour(self, player1, round_points):
        print(f"the round score is {round_points}")
        return self.get_input()

    def get_input(self):
        while True:
            choice = input(
                "do you want to roll again?[y/n] press k to pause the game: "
            )
            match choice:
                case "y":
                    return True
                case "n":
                    return False
                case "k":
                    self.pause_game = True
                    return False
                case _:
                    print("\033[A                             \033[A")
