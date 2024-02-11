import unittest
from Pig import HighScore


class TestGameClass(unittest.TestCase):

    def test_HighScore_init(self):
        res = HighScore.ScoreBoared()
        exp = HighScore.ScoreBoared
        self.assertIsInstance(res, exp)
    
    def test_upDate_Name(self):
        boared = HighScore.ScoreBoared()
        boared.upDateGamesPlayed("test_name")
        self.assertTrue("test_name" in boared.players)

    def test_upDate_played(self):
        boared = HighScore.ScoreBoared()
        boared.upDateGamesPlayed("test_name")
        self.assertTrue(1 == boared.players['test_name']['played'])

    def test_upDate_wins(self):
        boared = HighScore.ScoreBoared()
        boared.upDateGamesPlayed("test_name")
        boared.upDateGamesWon('test_name')
        self.assertTrue(1 == boared.players['test_name']['wins'])

    def test_not__nameExists(self):
        boared = HighScore.ScoreBoared()
        self.assertFalse(boared.nameExists('test_name'))

    def test_nameExists(self):
        boared = HighScore.ScoreBoared()
        boared.upDateGamesPlayed("test_name")
        self.assertTrue(boared.nameExists('test_name'))

    


if __name__ == '__main__':
    unittest.main()