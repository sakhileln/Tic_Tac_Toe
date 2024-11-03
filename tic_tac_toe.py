def print_board(board: list) -> None:
    """
    Prints the Tic Tac Toe board.

    Parameters:
        board (list): Game board with all the positions
    Return:
        None
    """
    print("-" * 9)
    for row in board:
        print(" | ".join(row))
        print("-" * 9)



if __name__ == "__main__":
    board = [[" " for _ in range(3)] for _ in range(3)]
    print_board(board)