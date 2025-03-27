import pygame
import sys
from constants import *
from board import is_valid_move, drop_piece, check_winner
from minimax import minimax
from display import draw_board
from client import *

def handle_events(screen, board, turn, server):
    winner = None

    if turn == PLAYER_1:
        col = server.get_move()
        if is_valid_move(board, col):
            row = drop_piece(board, col, PLAYER_1)
            draw_board(screen, board)
            server.send_move(col)
            if check_winner(board, row, col, PLAYER_1):
                winner = PLAYER_1
                print("Shutting down server...")
                server.close()
            return board, PLAYER_2, winner

    elif turn == PLAYER_2:
        col = server.get_move()
        if is_valid_move(board, col):
            row = drop_piece(board, col, PLAYER_2)
            draw_board(screen, board)
            server.send_move(col)
            if check_winner(board, row, col, PLAYER_2):
                winner = PLAYER_2
                print("Shutting down server...")
                server.close()
            return board, PLAYER_1, winner

    return board, turn, winner