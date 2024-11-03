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


def create_board() -> list:
    """
    Generates empty board.

    Parameters:
        None
    Return:
        board (list): Empty board
    """
    return [[" " for _ in range(3)] for _ in range(3)]


def check_winner(board: list) -> str:
    """
    Checks if there is a winner.

    Parameters:
        board (int): Game board with positions
    Return:
        symbol (str): Winner's symbol or None
    """
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None


def is_board_full(board: list) -> bool:
    """
    Checks if the board is full

    Parameters:
        board (int): Game board with positions
    Return:
        Boolen (bool): True if board full, False otherwise
    """
    return all(cell != " " for row in board for cell in row)


if __name__ == "__main__":
    board = [[" " for _ in range(3)] for _ in range(3)]
    print_board(board)