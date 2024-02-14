class Player  :
    def __init__(self, name) -> None:
        self.name = name
        self.points = 0
        self.roll_dice = self.player_behaviour
        self.pause_game = False

    def player_behaviour(self, game) -> bool:
        print(f"the round score is {game.round_points}")
        return self.get_input()

    def get_input(self) -> bool:
        while True:
            choice = input(
                "roll again?[y/n] press p to pause the game: "
            )
            match choice:
                case "y":
                    return True
                case "n":
                    return False
                case "p":
                    self.pause_game = True
                    return False
                case _:
                    print("\033[A                             \033[A")
