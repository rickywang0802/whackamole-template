import pygame
import random

# Constants for grid size and colors
GRID_SIZE = 32  # Change this to 32 or 64 as needed
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 512
GRID_COLOR = (0, 0, 0)  # Black grid lines


def draw_grid(screen):
    """Draws grid lines on the screen."""
    for x in range(0, SCREEN_WIDTH, GRID_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (0, y), (SCREEN_WIDTH, y))


def move_mole():
    """Generates a random position for the mole within the grid."""
    x = random.randrange(0, SCREEN_WIDTH, GRID_SIZE)
    y = random.randrange(0, SCREEN_HEIGHT, GRID_SIZE)
    return x, y


def main():
    try:
        pygame.init()
        # Load mole image and set initial position
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        clock = pygame.time.Clock()

        # Initial mole position at the top-left corner
        mole_position = (0, 0)
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Check if the mole was clicked
                    if mole_image.get_rect(topleft=mole_position).collidepoint(event.pos):
                        mole_position = move_mole()  # Move mole to a new position

            # Clear screen and draw background
            screen.fill("light green")

            # Draw the grid
            draw_grid(screen)

            # Draw the mole at its current position
            screen.blit(mole_image, mole_image.get_rect(topleft=mole_position))

            pygame.display.flip()  # Update the screen
            clock.tick(60)  # 60 FPS
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
