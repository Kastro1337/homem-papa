from settings import *
import pygame
from pygame import Vector2


#   The player class.
#   you cant go anywhere without this
class Player:
    def __init__(self,pos):
        #   Receives the position and modifies it, to be in one quadrant/sector
        #   considering the margin and the size of the cells that divide the map
        self.grid_pos = pos
        self.corrected_pos = self.get_pos()

        self.direction = Vector2(0,0)

    def get_pos(self):
        #   do the calculation to consider the top margin and size of each cell
        x = self.grid_pos.x*CELL_WIDTH+CELL_WIDTH//2
        y = self.grid_pos.y*CELL_HEIGHT+TOP_BUFFER+(CELL_HEIGHT//2)
        return Vector2(x,y)

    def move(self, key):
        if key == MOVE_KEYS[0]:     # right
            self.direction = Vector2(1,0)

        elif key == MOVE_KEYS[1]:   # left
            self.direction = Vector2(-1,0)

        elif key == MOVE_KEYS[2]:   # up
            self.direction = Vector2(0,-1)

        else:                        # down
            self.direction = Vector2(0,1)


    def draw(self, screen):
        #   Draw on screen the player's circle,
        #   with the corrected position and the diameter proportional to a quadrant
        pygame.draw.circle(screen, YELLOW, (self.corrected_pos.x, self.corrected_pos.y), CELL_WIDTH/2)

    def update(self):
        self.corrected_pos += self.direction