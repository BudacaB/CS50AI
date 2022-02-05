"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
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


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    board_unfilled = False
    for row in board:
        for cell in row:
            if cell == EMPTY:
                board_unfilled = True
    if board_unfilled and winner(board) == None:
        return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board) == True:
        return None
    if player(board) == X:
        return max_value(board)['action']
    elif player(board) == O:
        return min_value(board)['action']


def max_value(board):
    outcome = {'v': -1}
    if terminal(board) == True:
        outcome['v'] = utility(board)
        return outcome
    for action in actions(board):
        min_choice = min_value(result(board, action))['v']
        if outcome['v'] < min_choice:
            outcome['action'] = action
        outcome['v'] = max(outcome['v'], min_choice)
    return outcome


def min_value(board):
    outcome = {'v': 1}
    if terminal(board) == True:
        outcome['v'] = utility(board)
        return outcome
    for action in actions(board):
        max_choice = max_value(result(board, action))['v']
        if outcome['v'] > max_choice:
            outcome['action'] = action
        outcome['v'] = min(outcome['v'], max_choice)
    return outcome
