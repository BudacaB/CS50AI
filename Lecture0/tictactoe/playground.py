import copy
from queue import Empty


X = "X"
O = "O"
EMPTY = None

board = [[X, O, X],
        [O, X, O],
        [X, EMPTY, EMPTY]]

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
    

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row_idx, row in enumerate(board):
        for cell_idx, cell in enumerate(row):
            if row_idx == 0 and cell_idx == 0:
                if cell == X:
                    if board[row_idx][cell_idx + 1] == X and board[row_idx][cell_idx + 2] == X:
                        return X
                    elif board[row_idx + 1][cell_idx] == X and board[row_idx + 2][cell_idx] == X:
                        return X
                    elif board[row_idx + 1][cell_idx + 1] == X and board[row_idx + 2][cell_idx + 2] == X:
                        return X
            if row_idx == 0 and cell_idx == 1:
                if cell == X:
                    if board[row_idx + 1][cell_idx] == X and board[row_idx + 2][cell_idx] == X:
                        return X
            if row_idx == 0 and cell_idx == 2:
                if cell == X:
                    if board[row_idx + 1][cell_idx] == X and board[row_idx + 2][cell_idx] == X:
                        return X
                    elif board[row_idx + 1][cell_idx - 1] and board[row_idx + 2][cell_idx - 2] == X:
                        return X
            if row_idx == 1 and cell_idx == 0:
                if cell == X:
                    if board[row_idx][cell_idx + 1] == X and board[row_idx][cell_idx + 2] == X:
                        return X
            if row_idx == 2 and cell_idx == 0: 
                if cell == X:
                    if board[row_idx][cell_idx + 1] == X and board[row_idx][cell_idx + 2] == X:
                        return X
    return None

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[0][0] == board[0][1] == board[0][2]:
        if board[0][0] != EMPTY:
            return board[0][0]
    if board[0][0] == board[1][0] == board[2][0]:
        if board[0][0] != EMPTY:
            return board[0][0]
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] != EMPTY:
            return board[0][0]
    if board[0][1] == board[1][1] == board[2][1]:
        if board[0][1] != EMPTY:
            return board[0][1] 
    if board[0][2] == board[1][2] == board[2][2]:
        if board[0][2] != EMPTY:
            return board[0][2] 
    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] != EMPTY:
            return board[0][2]
    if board[1][0] == board[1][1] == board[1][2]:
        if board[1][0] != EMPTY:
            return board[1][0]
    if board[2][0] == board[2][1] == board[2][2]:
        if board[2][0] != EMPTY:
            return board[2][0]
    return None

print(winner(board))
