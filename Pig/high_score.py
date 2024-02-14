import pickle

class ScoreBoared:

    def __init__(self) -> None:
        self.players = self.load_file()

    def load_file(self) -> dict:
        try:
            with open("HighScore.bin", "rb") as f:
                players = pickle.load(f)
        except FileNotFoundError:
            players = {"sven": {}, "niko": {}, "isacce": {}, "marta": {}}
            for player in players:
                players[player] = {"wins": 0, "played": 0}
        return players

    def name_exists(self, name) -> str:
        return name in self.players

    def up_date_games_played(self, name) -> None:
        self.players[name] = self.players.get(name, {"wins": 0, "played": 0})
        self.players[name]["played"] += 1

    def up_date_games_won(self, name) -> None:
        self.players[name]["wins"] += 1

    def up_date_name(self, old_name, new_name) -> None:
        self.players[new_name] = self.players[old_name]
        del self.players[old_name]

    def save_boared(self) -> None:
        with open("HighScore.bin", "wb") as f:
            pickle.dump(self.players, f)

    def calc_percent(self) -> list:
        player_percent = []
        for player in self.players:
            wins = self.players[player]["wins"]
            played = self.players[player]["played"]
            if played > 0:
                percent = (wins / played) * 100
            else:
                percent = 0
            player_percent.append((player, percent))

        player_percent.sort(key=lambda x: x[1], reverse=True)
        return player_percent
       
    def __str__(self) -> str:
        player_percent = self.calc_percent()
        score_boared = f"{'Name':<10}{'wins':<10}{'played':<10}{'Percent':<10}\n"
        i = 1
        for tub in player_percent:
            wins = self.players[tub[0]]["wins"]
            played = self.players[tub[0]]["played"]
            score_boared += f"{i}: {tub[0]:<7}{wins:>7}{played:>7}{tub[1]:>10.2f}\n"
            i += 1
        return score_boared
