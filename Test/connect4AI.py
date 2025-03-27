import pygame
import sys
from constants import *
from board import create_board
from display import draw_board
from handle_event import handle_events
from server import *
def main():
    pygame.init()
    font = pygame.font.SysFont(None, 75)

    server = Connect4Server()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Connect 4 - AI vs AI")

    board = create_board()
    turn, winner = PLAYER_1, None
    draw_board(screen, board)


    while True:
        board, turn, winner = handle_events(screen, board, turn, server)

        if winner is not None:
            screen.fill(BLACK, (0, 0, SCREEN_WIDTH, SQUARE_SIZE))
            mess = "Player 1 wins!" if winner == PLAYER_1 else "Player 2 wins!"
            text = font.render(mess, True, WHITE)
            screen.blit(text, (SCREEN_WIDTH // 3, 10))
            pygame.display.flip()

            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT or event.type == pygame.MOUSEBUTTONDOWN:
                        pygame.quit()
                        sys.exit()

if __name__ == "__main__":
    main()
