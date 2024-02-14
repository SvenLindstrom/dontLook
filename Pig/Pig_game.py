import random


class Pig:
    def __init__(self, player1, player2, score_boared) -> None:
        self.player1 = player1
        self.player2 = player2
        self.current_turn = player1
        self.current_score = 0
        self.score_boared = score_boared

    def test(self):
        self.print_game_state()

        while True:
            if self.rolled_one():
                continue

            if self.current_turn.roll_dice(self.player1, self.current_score):
                continue

            if self.current_turn.pause_game:
                return self
            
            if self.is_game_over():
                return None
            
            self.change_player()
    
    def print_game_state(self):
        print(f"\n{self.player1.name} has {self.player1.points} points")
        print(f"{self.player2.name} has {self.player2.points} points\n")
        print(f"{self.current_turn.name}s turn\n")
        

    def is_game_over(self):
        self.end_turn()
        if self.current_turn.points > 100:
            print(f"{self.current_turn.name} won this round")
            self.update_boared()
            return True
        return False 
    

    def end_turn(self):
        self.current_turn.points += self.current_score
        self.current_score = 0


    def update_boared(self):
        self.score_boared.up_date_games_played(self.player1)
        self.score_boared.up_date_games_played(self.player1)
        self.score_boared.up_date_games_won(self.current_turn)

    def change_player(self):
        self.current_turn = (
                self.player2 if self.current_turn == self.player1 else self.player1
            )
        self.print_game_state() 
   
    def rolled_one(self):
        if not self.current_turn.pause_game:
            dice_roll = random.randint(1, 6)
            print(f"the dice rolle is {dice_roll}")
            if dice_roll == 1:
                self.current_score = 0
                self.change_player()
                return True
            self.current_score += dice_roll
        else:
            self.current_turn.pause_game = False
        return False





    def check_win(self):
        return self.current_turn.points > 100

    def play_round(self):
        while True:
            print(f"\n{self.player1.name} has {self.player1.points} points")
            print(f"{self.player2.name} has {self.player2.points} points\n")
            print(f"{self.current_turn.name}s turn\n")

            if self.current_turn.pause_game is True:
                if not self.un_pause_game():
                    return self

            if not self.player_turn(self.current_turn):
                return self 

            if self.check_win():
                print(f"{self.current_turn.name} won this round")
                return None

            self.current_turn = (
                self.player2 if self.current_turn == self.player1 else self.player1
            )

    def un_pause_game(self):
        self.current_turn.pause_game = False
        if self.current_turn.roll_dice(self.player1, self.current_score):
            return True
        if not self.game_not_paused(self.current_turn):
            return False
        self.current_turn = (
            self.player2 if self.current_turn == self.player1 else self.player1
        )
        return True

    def player_turn(self, player):
        while True:
            dice_roll = random.randint(1, 6)
            print(f"the dice rolle is {dice_roll}")
            self.current_score += dice_roll
            if dice_roll == 1:
                self.current_score = 0
                return True

            if player.rollDice(self.player1, self.current_score):
                continue
            return self.game_not_paused(player)

    def game_not_paused(self, player):
        if player.pause_Game:
            return False
        player.points += self.current_score
        self.current_score = 0
        return True
