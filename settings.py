#
#   settings files, constants and stuff
#
from pygame.math import Vector2 as vec



FPS = 60 # only with RTX 3090

GREY = (110, 110, 110)
BLACK = (0,0,0)
YELLOW = (255, 255, 0)

TOP_BUFFER = 25 # space between the maze and the windows screen
MAZE_WIDTH = 560
MAZE_HEIGHT = 620
WIDTH = MAZE_WIDTH
HEIGHT = MAZE_HEIGHT + TOP_BUFFER
CELL_WIDTH = MAZE_WIDTH//28
CELL_HEIGHT = MAZE_HEIGHT//30

PLAYER_STARTING_POS = vec(1,1)
