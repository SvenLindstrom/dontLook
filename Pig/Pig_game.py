import random


class Pig:
    def __init__(self, player1, player2) -> None:
        self.player1 = player1
        self.player2 = player2
        self.current_turn = player1
        self.current_score = 0

    def test(self):

        while True:
            print(f"\n{self.player1.name} has {self.player1.points} points")
            print(f"{self.player2.name} has {self.player2.points} points\n")
            print(f"{self.current_turn.name}s turn\n")
            while True:
                if not self.current_turn.pause_Game:
                    dice_roll = random.randint(1, 6)
                    print(f"the dice rolle is {dice_roll}")
                    if dice_roll == 1:
                        self.current_score = 0
                        break
                    self.current_score += dice_roll
                else:
                    self.current_turn.pause_Game = False

                if self.current_turn.rollDice(self.player1, self.current_score):
                    continue

                elif self.current_turn.pause_Game:
                    return True, None

                else:
                    self.current_turn.points += self.current_score
                    self.current_score = 0
                    if self.current_turn.points > 100:
                        print(f"{self.current_turn.name} won this round")
                        return False, self.current_turn
                    break

            self.current_turn = (
                self.player2 if self.current_turn == self.player1 else self.player1
            )

    def checkWin(self):
        return self.current_turn.points > 100

    def playRound(self):
        while True:
            print(f"\n{self.player1.name} has {self.player1.points} points")
            print(f"{self.player2.name} has {self.player2.points} points\n")
            print(f"{self.current_turn.name}s turn\n")

            if self.current_turn.pause_Game == True:
                if not self.unPauseGame():
                    return True, None

            if not self.playerTurn(self.current_turn):
                return True, None

            if self.checkWin(self.current_turn):
                print(f"{self.current_turn.name} won this round")
                return False, self.current_turn

            self.current_turn = (
                self.player2 if self.current_turn == self.player1 else self.player1
            )

    def unPauseGame(self):
        self.current_turn.pause_Game = False
        if self.current_turn.rollDice(self.player1, self.current_score):
            return True
        elif not self.game_not_paused(self.current_turn):
            return False
        self.current_turn = (
            self.player2 if self.current_turn == self.player1 else self.player1
        )
        return True

    def playerTurn(self, player):
        while True:
            dice_roll = random.randint(1, 6)
            print(f"the dice rolle is {dice_roll}")
            self.current_score += dice_roll
            if dice_roll == 1:
                self.current_score = 0
                return True

            elif player.rollDice(self.player1, self.current_score):
                continue
            else:
                return self.game_not_paused(player)

    def game_not_paused(self, player):
        if player.pause_Game:
            return False
        player.points += self.current_score
        self.current_score = 0
        return True
