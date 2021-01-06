#
#   settings files, constants and stuff
#
from pygame.math import Vector2
import pygame

# game settings
PLAYER_STARTING_POS = Vector2(1,1)
FPS = 60 # only with RTX 3090
MOVE_KEYS = [
            pygame.K_RIGHT, # right
            pygame.K_LEFT,  # left
            pygame.K_UP,    # up
            pygame.K_DOWN   # down
             ]

DEBUG_KEYS = [
            pygame.K_1,     # draw grids
            pygame.K_2,     # draw walls
            pygame.K_3,     # draw player pos

]

# color customization
GREY = (110, 110, 110)
BLACK = (0,0,0)
YELLOW = (255, 255, 0)
PINK = (112,55,163)
RED = (255,0,0)
GOLDEN = (212, 175, 55)

# screen settings
TOP_BUFFER = 20 # space between the maze and the windows screen
MAZE_WIDTH = 560
MAZE_HEIGHT = 620
WIDTH = MAZE_WIDTH
HEIGHT = MAZE_HEIGHT + TOP_BUFFER
CELL_WIDTH = MAZE_WIDTH//28     # =20
CELL_HEIGHT = MAZE_HEIGHT//30   # =20
