import pygame
import random

# Constants
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
BLOCK_SIZE = 30
FPS = 60

# Colors
COLORS = [
    (0, 0, 0),       # Black
    (255, 0, 0),     # Red
    (0, 255, 0),     # Green
    (0, 0, 255),     # Blue
    (255, 255, 0),   # Yellow
    (255, 165, 0),   # Orange
    (128, 0, 128),   # Purple
    (0, 255, 255)    # Cyan
]

# Tetromino shapes: I, J, L, O, S, T, Z
SHAPES = [
    [[1, 1, 1, 1]],
    [[1, 0, 0], [1, 1, 1]],
    [[0, 0, 1], [1, 1, 1]],
    [[1, 1], [1, 1]],
    [[0, 1, 1], [1, 1, 0]],
    [[0, 1, 0], [1, 1, 1]],
    [[1, 1, 0], [0, 1, 1]]
]

# Game class
class Tetris:
    def __init__(self):
        self.board = [[0] * (SCREEN_WIDTH // BLOCK_SIZE) for _ in range(SCREEN_HEIGHT // BLOCK_SIZE)]
        self.current_piece = self.new_piece()
        self.score = 0
    
    def new_piece(self):
        shape = random.choice(SHAPES)
        color = random.randint(1, len(COLORS) - 1)
        return {'shape': shape, 'color': color, 'x': SCREEN_WIDTH // BLOCK_SIZE // 2 - len(shape[0]) // 2, 'y': 0}

    def move(self, dx):
        self.current_piece['x'] += dx

    def rotate(self):
        self.current_piece['shape'] = [list(row) for row in zip(*self.current_piece['shape'][::-1])]

    def drop(self):
        self.current_piece['y'] += 1
    
    def clear_lines(self):
        # Check for filled lines and clear them
        pass

    def is_game_over(self):
        # Check if game is over
        return False

# Main function
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    game = Tetris()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    game.move(-1)
                elif event.key == pygame.K_RIGHT:
                    game.move(1)
                elif event.key == pygame.K_DOWN:
                    game.drop()
                elif event.key == pygame.K_UP:
                    game.rotate()

        screen.fill(COLORS[0])
        # Render game board and current piece
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()