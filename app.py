# documentation: https://www.pygame.org/docs/

# imports
import pygame
import sys
import random

from objects.game_board import GameBoard
from objects.snake import Snake

# pygame setup
pygame.init()
pygame.display.set_caption('Python Snake -- MP')
screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()
running = True

# # use the game board class for setup of the game play area
# board = GameBoard()
# game_surface = board.draw_grid(screen)

# # initialize the snake character for the game
# snake = Snake()
# snake.draw(game_surface)

x = GameBoard()
s = Snake()


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP: s.direction = 'up'
            elif event.key == pygame.K_DOWN: s.direction = 'down'
            elif event.key == pygame.K_RIGHT: s.direction = 'right'
            elif event.key == pygame.K_LEFT: s.direction = 'left'

    # RENDER YOUR GAME HERE
    s.update_position()

    screen.fill('black')
    x.draw_grid(screen)
    s.draw(screen)


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
