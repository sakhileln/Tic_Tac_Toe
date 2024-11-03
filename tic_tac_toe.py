def generate_empty_state() -> list:
    """
    Generate the empty game board.

    Parameters:
        None
    Return:
        None
    """
    state = [[0 for _ in range(3)] for _ in range(3)]
    return state


def draw_state(state: list) -> None:
    """
    Draw the game board given the state.

    Parameters:
        None
    Return:
        None
    """
    print("-------------------")
    for i in range(3):
        print(f"|",end="")
        for j in range(3):
            if state[i][j] == 0:
                piece = " "
            elif state[i][j] == 1:
                piece = "X"
            elif state[i][j] == 2:
                piece = "O"
            # Print state
            print(f"  {piece}  |", end="")
        print("")
        print("-------------------")


test_state = [
    [0, 2, 0],
    [0, 1, 0],
    [0, 0, 0]
]


if __name__ == "__main__":
    draw_state(test_state)