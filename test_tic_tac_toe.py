"""
A module for test cases of the tic tac toe game.
"""

from tic_tac_toe import create_board
import unittest


class TestTicTacToe(unittest.TestCase):
    """
    Test cases for the tic tac toe game.
    """
    def test_empty_state_generation(self):
        """
        Test case for an empty board
        """
        board = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]
        self.assertEqual(create_board(), board)


if __name__ == "__main__":
    unittest.main()
