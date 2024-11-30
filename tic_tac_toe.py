"""
A module for playing simple terminal interface Tic Tac Toe.
"""


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


def tic_tac_toe() -> None:
    """
    Main function to play Tic Tac Toe.

    Parameters:
        None
    Return:
        None
    """
    print("Welcome to Tic Tac Toe!")
    print("1. Player 1 vs Player 2")
    print("2. Plater vs AI")
    while True:
        try:
            choice = int(input("Please enter your choice (1, 2 or 3): "))
            if choice in [1, 2, 3]:
                break
        except Exception as e:
            print("Invalid input, please enter number between 1, 2 or 3.")
    if choice == 3:
        exit()
    elif choice == 2:
        print("You are 'X' and the AI is 'O'.")
    elif choice == 1:
        print("Player 1 is 'X' and Player 2 is 'O'")

    board = create_board()
    while True:
        print_board(board)

        # Player turn
        while True:
            try:
                move = int(input("Enter your move (1-9): ")) - 1
                row, col = divmod(move, 3)
                if board[row][col] == " ":
                    board[row][col] = "X"
                    break
                else:
                    print("Invalid move, try again.")
            except (ValueError, IndexError):
                print("Invalid input, please enter a number between 1 and 9.")

        if check_winner(board) == "X":
            print_board(board)
            print("Congratualions! You win!")
            return

        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            return

        # AI's turn


if __name__ == "__main__":
    tic_tac_toe()
