"""
A module for test cases of the tic tac toe game.
"""

import unittest
from tic_tac_toe import (
    create_board,
    is_board_full,
    check_winner,
)


class TestTicTacToe(unittest.TestCase):
    """
    Test cases for the tic tac toe game.
    """

    def test_empty_state_generation(self):
        """
        Test case for an empty board
        """
        board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.assertEqual(create_board(), board)

    def test_if_board_is_full(self):
        """
        Test case for full board.
        """
        board = [["X", "O", "O"], ["O", "O", "O"], ["X", " X", "X"]]
        self.assertEqual(is_board_full(board), True)

    def test_partially_full(self):
        """
        Test partially full board.
        """
        board = [[" ", " ", "O"], ["O", "O", " "], ["X", "  ", "X"]]
        self.assertEqual(is_board_full(board), False)

    def test_x_winner(self):
        """
        Test case for X as winner
        """
        board = [[" ", " ", "O"], ["O", "O", " "], ["X", "X", "X"]]
        self.assertEqual(check_winner(board), "X")

    def test_o_winner(self):
        """
        Test case for O as winner
        """
        board = [[" ", " ", "O"], ["O", "O", " "], ["O", "X", "X"]]
        self.assertEqual(check_winner(board), "O")


if __name__ == "__main__":
    unittest.main()
