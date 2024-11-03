"""
A module for test cases of the tic tac toe game.
"""

from tic_tac_toe import generate_empty_state
import unittest


class TestTicTacToe(unittest.TestCase):
    """
    Test cases for the tic tac toe game.
    """
    def test_empty_state_generation(self):
        """
        Test case for an empty state
        """
        state = [
            [0,0,0],
            [0,0,0],
            [0,0,0]
        ]
        self.assertEqual(generate_empty_state(), state)


if __name__ == "__main__":
    unittest.main()
