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
    print()
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print()


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
        board (list): Game board with positions
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
        board (list): Game board with positions
    Return:
        Boolean (bool): True if board full, False otherwise
    """
    return all(cell != " " for row in board for cell in row)


def minimax(board: list, depth: int, is_maximizing: bool) -> int:
    """
    Minimax algorithm to calculate the best move for the AI.

    Parameters:
        board (list): Game board with positions
        depth (int): Depth of recursion
        is_maximizing (bool): Whether it's the AI's turn (True) or the player's turn (False)
    Return:
        int: Best score for the current player
    """
    winner = check_winner(board)
    if winner == "X":
        return -1  # Player wins
    if winner == "O":
        return 1  # AI wins
    if is_board_full(board):
        return 0  # Draw

    if is_maximizing:
        best_score = -float("inf")
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    board[row][col] = "O"  # AI's move
                    score = minimax(board, depth + 1, False)
                    board[row][col] = " "
                    best_score = max(score, best_score)
        return best_score

    best_score = float("inf")
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                board[row][col] = "X"  # Player's move
                score = minimax(board, depth + 1, True)
                board[row][col] = " "
                best_score = min(score, best_score)
    return best_score


def ai_move(board: list) -> None:
    """
    Determines the best move for the AI using the minimax algorithm.

    Parameters:
        board (list): Game board with positions
    Return:
        None
    """
    best_move = None
    best_score = -float("inf")
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                board[row][col] = "O"
                score = minimax(board, 0, False)
                board[row][col] = " "
                if score > best_score:
                    best_score = score
                    best_move = (row, col)

    if best_move:
        board[best_move[0]][best_move[1]] = "O"


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
    print("2. Player vs AI")
    while True:
        try:
            choice = int(input("Please enter your choice (1 or 2): "))
            if choice in [1, 2]:
                break
        except TypeError as e:
            print(f"Invalid input, please enter number between 1 or 2. {e}")

    if choice == 2:
        print("You are 'X' and the AI is 'O'.")
    elif choice == 1:
        print("Player 1 is 'X' and Player 2 is 'O'")

    board = create_board()

    while True:
        print_board(board)

        # Player turn
        if choice == 2 and not is_board_full(board):
            # Player turn
            while True:
                try:
                    move = int(input("Enter your move (1-9): ")) - 1
                    row, col = divmod(move, 3)
                    if board[row][col] == " ":
                        board[row][col] = "X"
                        break

                    print("Invalid move, try again.")
                except (ValueError, IndexError):
                    print("Invalid input, please enter a number between 1 and 9.")

            if check_winner(board) == "X":
                print_board(board)
                print("Congratulations! You win!")
                return

            if is_board_full(board):
                print_board(board)
                print("It's a draw!")
                return

            # AI's turn
            ai_move(board)
            if check_winner(board) == "O":
                print_board(board)
                print("AI wins!")
                return

            if is_board_full(board):
                print_board(board)
                print("It's a draw!")
                return


if __name__ == "__main__":
    tic_tac_toe()
