import unittest
from Pig import high_score


class TestGameClass(unittest.TestCase):

    def test_high_score_init(self):
        res = high_score.ScoreBoared()
        exp = high_score.ScoreBoared
        self.assertIsInstance(res, exp)

    def test_up_date_name(self):
        boared = high_score.ScoreBoared()
        boared.up_date_games_played("test_name")
        self.assertTrue("test_name" in boared.players)

    def test_up_date_played(self):
        boared = high_score.ScoreBoared()
        boared.up_date_games_played("test_name")
        self.assertTrue(1 == boared.players["test_name"]["played"])

    def test_up_date_wins(self):
        boared = high_score.ScoreBoared()
        boared.up_date_games_played("test_name")
        boared.up_date_games_won("test_name")
        self.assertTrue(1 == boared.players["test_name"]["wins"])

    def test_not_name_exists(self):
        boared = high_score.ScoreBoared()
        self.assertFalse(boared.name_exists("test_name"))

    def test_name_exists(self):
        boared = high_score.ScoreBoared()
        boared.up_date_games_played("test_name")
        self.assertTrue(boared.name_exists("test_name"))


if __name__ == "__main__":
    unittest.main()
