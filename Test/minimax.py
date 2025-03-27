import random

import numpy as np
import math
from board import drop_piece, get_valid_moves, check_winner, is_game_tied
from constants import *


def evaluate_window(window, piece):
    score = 0
    opp_piece = RED_PLAYER if piece == YEL_PLAYER else YEL_PLAYER

    if window.count(piece) == 4:
        score += 100
    elif window.count(piece) == 3 and window.count(EMPTY) == 1:
        score += 5
    elif window.count(piece) == 2 and window.count(EMPTY) == 2:
        score += 2

    if window.count(opp_piece) == 3 and window.count(EMPTY) == 1:
        score -= 4

    return score


def evaluate(board, piece):
    score = 0
    center_array = [int(i) for i in list(board[:, NUM_COLS // 2])]
    score += center_array.count(piece) * 3

    for r in range(NUM_ROWS):
        row_array = [int(i) for i in list(board[r, :])]
        for c in range(NUM_COLS - 3):
            score += evaluate_window(row_array[c:c + WINNING_COUNT], piece)

    for c in range(NUM_COLS):
        col_array = [int(i) for i in list(board[:, c])]
        for r in range(NUM_ROWS - 3):
            score += evaluate_window(col_array[r:r + WINNING_COUNT], piece)

    for r in range(NUM_ROWS - 3):
        for c in range(NUM_COLS - 3):
            score += evaluate_window([board[r + i][c + i] for i in range(WINNING_COUNT)], piece)
            score += evaluate_window([board[r + 3 - i][c + i] for i in range(WINNING_COUNT)], piece)

    return score


def minimax(board, depth=12, turn=YEL_PLAYER):
    valid_moves = get_valid_moves(board)
    if depth == 0 or is_game_tied(board):
        return None, evaluate(board, turn)

    best_col = random.choice(valid_moves)
    if turn == YEL_PLAYER:
        max_eval = -math.inf
        for col in valid_moves:
            board_tmp = np.copy(board)
            row = drop_piece(board_tmp, col, YEL_PLAYER)
            if check_winner(board_tmp, row, col, YEL_PLAYER):
                return col, math.inf
            _, score = minimax(board_tmp, depth - 1, RED_PLAYER)
            if score > max_eval:
                max_eval = score
                best_col = col
        return best_col, max_eval
    else:
        min_eval = math.inf
        for col in valid_moves:
            board_tmp = np.copy(board)
            row = drop_piece(board_tmp, col, RED_PLAYER)
            if check_winner(board_tmp, row, col, RED_PLAYER):
                return col, -math.inf
            _, score = minimax(board_tmp, depth - 1, YEL_PLAYER)
            if score < min_eval:
                min_eval = score
                best_col = col
        return best_col, min_eval