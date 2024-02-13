import sys
import player
import pig_game
import pig_ai
import high_score

class Game:
    score_boare = high_score.ScoreBoared()
    game = None

    def ui(self):
        while True:
            print(
                """Hello to Pig:
                1. Start game
                2. Continue game
                3. rules 
                4. leader boared
                5. change name
                6. quit"""
            )
            choice = get_input(6)

            match choice:
                case 1:
                    if self.game is not None and self.continue_game():
                        self.play_game(self.game)
                    else:
                        self.game_set_up()
                        self.play_game(self.game)
                case 2:
                    if self.game is not None:
                        self.play_game(self.game)
                    else:
                        print("no game currently running")
                case 3:
                    pass
                case 4:
                    print(self.score_boare)
                case 5:
                    self.change_name()
                case 6:
                    self.score_boare.save_boared()
                    sys.exit()

    def game_set_up(self):
        print(
            """Game setting:
            1. Player VS Player
            2. Player VS Ai"""
        )
        choice = get_input(2)
        match choice:
            case 1:
                player1 = player.Player(get_player_name(1))
                player2 = player.Player(get_player_name(2))
            case 2:
                player1 = player.Player(get_player_name(1))
                player2 = self.select_ai()
        self.game = pig_game.Pig(player1, player2, self.score_boare)

    def select_ai(self):
        print(
            """Ai difficulty:
            1. Pig-let
            2. Hog
            3. Boar"""
        )
        choice = get_input(3)
        return pig_ai.Ai(choice)

    def continue_game(self):
        print("game is currently running, continue old game?")
        return get_choice()

    def change_name(self):
        old_name = get_player_name("old")
        new_name = get_player_name("new")
        self.score_boare.up_date_name(old_name, new_name)
        if self.game is not None:
            if self.game.player1.name == old_name:
                self.game.player1.name = new_name
            elif self.game.player2.name == old_name:
                self.game.player2.name = new_name

    def play_game(self, game):
        self.game = game.test()


def get_player_name(i):
    name = input(f"player {i} name: ")
    if name in ["pig-let", "hog", "Boar"]:
        print("\033[A                             \033[A")
        print("name unavalable")
        return get_player_name(i)
    return name


def get_choice():
    while True:
        choice = input("[y/n]")
        match choice:
            case "y":
                return True
            case "n":
                return False
            case _:
                print("\033[A                             \033[A")


def get_input(max_options):
    choice = input("enter your choice: ")
    if choice.isnumeric() and int(choice) in range(1, max_options + 1):
        return int(choice)
    print("\033[A                             \033[A")
    return get_input(max_options)


if __name__ == "__main__":
    pg = Game()
    pg.ui()
