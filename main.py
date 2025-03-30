import pygame
import sys

# Works for the conda based python version

# Colors
WHITE = (255, 255, 255)
BLACK = (100, 100, 100)

# Config
BOARD_SIZE = 8
WINDOW_SIZE = 600
SQUARE_SIZE = WINDOW_SIZE // BOARD_SIZE

def draw_chessboard(screen):
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            rect = pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
            pygame.draw.rect(screen, color, rect)

# draw the pieces position onto the board. has the up
def draw_chess_pieces(screen, pieces):
    pass


def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption("Chessboard")

    running = True
    while running:
        screen.fill((0, 0, 0))
        draw_chessboard(screen)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
