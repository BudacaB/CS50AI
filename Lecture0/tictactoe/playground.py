import copy


X = "X"
O = "O"
EMPTY = None

board = [[X, O, X],
        [O, X, EMPTY],
        [EMPTY, EMPTY, EMPTY]]

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_counter = 0
    zero_counter = 0
    for row in board:
        for cell in row:
            if cell == X:
                x_counter += 1
            elif cell == O:
                zero_counter += 1
    if x_counter > zero_counter:
        return O
    else:
        return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for row_idx, row in enumerate(board):
        for cell_idx, cell in enumerate(row):
            if cell == EMPTY:
                actions.add((row_idx, cell_idx))
    return actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    possible_actions = actions(board)
    if action not in possible_actions:
        raise Exception("Invalid move")
    board_copy = copy.deepcopy(board)
    board_copy[action[0]][action[1]] = player(board)
    return board_copy
    

# result(board, (1, 1))
print(result(board, (1, 2)))
