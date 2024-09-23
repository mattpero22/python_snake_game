# documentation: https://www.pygame.org/docs/

# imports
import pygame
import sys
import random

from objects.game_board import GameBoard

# constants/settings for game
SPEED = 10
SPACE_SIZE = 50
SNAKE_COLOR = "green"
BACKGROUND_COLOR = "white"


# pygame setup
pygame.init()
pygame.display.set_caption('Python Snake -- MP')
screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()
running = True

# use the game board class for setup of the game play area
board = GameBoard()
board.draw_grid(screen)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
