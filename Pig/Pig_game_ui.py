import HighScore
import Player
import Pig_game
import Pig_Ai


class Game:
    scoreBoare = HighScore.ScoreBoared()
    game_running = False
    game = None
    scoreBoare = HighScore.ScoreBoared()

    def ui(self):
        while(True):
            print("""Hello to Pig:
                1. Start game
                2. Continue game
                3. rules 
                4. leader boared
                5. change name
                6. quit""")
            choice = getinput(6)
            
            match choice:
                case 1:
                    if self.game_running and self.ContinueGame():
                        self.playGame(self.game)
                    else:
                        self.GameSetUp()
                        self.playGame(self.game)
                case 2:
                    if self.game_running:
                        self.playGame(self.game)
                    else:
                        print('no game currently running')
                case 3:
                    pass
                case 4:
                    print(self.scoreBoare)
                case 5:
                    self.changeName()
                case 6:
                    self.scoreBoare.saveBoared()
                    exit()

    def GameSetUp(self):
        print("""Game setting:
            1. Player VS Player
            2. Player VS Ai""")
        choice = getinput(2)
        match choice:
            case 1:
                player1 = Player.Player(getPlayerName(1))
                player2 = Player.Player(getPlayerName(2))
            case 2:
                player1 = Player.Player(getPlayerName(1))
                player2 = self.selectAi()
        self.game = Pig_game.Pig(player1, player2)

    def selectAi(self):
        print("""Ai difficulty:
            1. Pig-let
            2. Hog
            3. Boar""")
        choice = getinput(3)
        return Pig_Ai.Ai(choice)
    
    def ContinueGame(self):
        print('game is currently running, continue old game?')
        return getChoice()
    
    
    def changeName(self):
        old_name = self.getPlayerName('old')
        new_name = self.getPlayerName('new')
        self.scoreBoare.upDateName(old_name, new_name)
        if self.game_running:
            if self.game.player1.name == old_name:
                self.game.player1.name = new_name
            elif self.game.player2.name == old_name:
                self.game.player2.name = new_name

    def playGame(self, game):
        self.game_running, winer = game.test()
        if winer is not None:
            self.scoreBoare.upDateGamesPlayed(self.game.player1.name)
            self.scoreBoare.upDateGamesPlayed(self.game.player2.name)
            self.scoreBoare.upDateGamesWon(winer.name)

def getPlayerName(i):
    name = input(f'player {i} name: ')
    if name in ['pig-let', 'hog', 'Boar']:
        print("\033[A                             \033[A")
        print('name unavalable')
        return getPlayerName(i)
    return name

def getChoice():
    while True:
        choice = input("[y/n]")
        match choice:
            case 'y': return True
            case 'n': return False
            case _: print("\033[A                             \033[A")

def getinput(max):
    choice = input("enter your choice: ")
    if choice.isnumeric() and int(choice) in range(1,max+1):
        return int(choice)
    else:
        print("\033[A                             \033[A")
        return getinput(max)

if __name__ == "__main__":
    pg = Game()
    pg.ui()