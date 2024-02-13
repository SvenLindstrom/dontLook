import pickle


class ScoreBoared:

    players = {"sven": {}, "niko": {}, "isacce": {}, "marta": {}}

    def __init__(self) -> None:
        try:
            with open("HighScore.bin", "rb") as f:
                self.players = pickle.load(f)
        except FileNotFoundError:
            for player in self.players:
                self.players[player] = {"wins": 0, "played": 0}

    def name_exists(self, name):
        return name in self.players

    def up_date_games_played(self, name):
        self.players[name] = self.players.get(name, {"wins": 0, "played": 0})
        self.players[name]["played"] += 1

    def up_date_games_won(self, name):
        self.players[name]["wins"] += 1

    def up_date_name(self, old_name, new_name):
        self.players[new_name] = self.players[old_name]
        del self.players[old_name]

    def save_boared(self):
        with open("HighScore.bin", "wb") as f:
            pickle.dump(self.players, f)

    def __str__(self) -> str:
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

        print(f"{'Name':<10}{'wins':<10}{'played':<10}{'Percent':<10}")
        i = 1
        for tub in player_percent:
            wins = self.players[tub[0]]["wins"]
            played = self.players[tub[0]]["played"]

            print(f"{i}: {tub[0]:<7}{wins:>7}{played:>7}{tub[1]:>10.2f}")
            i += 1
        return ""
