import unittest
from game_logic import NumberGuessingGame

class TestNumberGuessingGame(unittest.TestCase):
    def test_evaluate_guess(self):
        game = NumberGuessingGame()
        game.target_number = "58947"

        self.assertEqual(game.evaluate_guess("58123"), (2, 0))
        self.assertEqual(game.evaluate_guess("57123"), (1, 1))
        # Add more test cases

if __name__ == '__main__':
    unittest.main()
