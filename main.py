import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 100, 255)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame Starter")

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    
    # Fill the screen with white
    screen.fill(WHITE)
    
    # Draw a blue rectangle in the center
    pygame.draw.rect(screen, BLUE, (SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 - 50, 100, 100))
    
    # Update the display
    pygame.display.flip()
    
    # Control the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
