#
#   settings files, constants and stuff
#
from pygame.math import Vector2
import pygame


# color customization
GREY = (110, 110, 110)
BLACK = (0,0,0)
YELLOW = (255, 255, 0)


# screen settings
TOP_BUFFER = 25 # space between the maze and the windows screen
MAZE_WIDTH = 560
MAZE_HEIGHT = 620
WIDTH = MAZE_WIDTH
HEIGHT = MAZE_HEIGHT + TOP_BUFFER
CELL_WIDTH = MAZE_WIDTH//28
CELL_HEIGHT = MAZE_HEIGHT//30

# game settings
PLAYER_STARTING_POS = Vector2(2,1)
FPS = 120 # only with RTX 3090
MOVE_KEYS = [
            pygame.K_RIGHT, # right
            pygame.K_LEFT,  # left
            pygame.K_UP,    # up
            pygame.K_DOWN   # down
             ]
