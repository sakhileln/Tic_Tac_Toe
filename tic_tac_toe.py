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