# Enemy class
# if you destroy this file, you make the game much easier
# obs: bunch of methods are same as player, could the both of them inherit from a parent class??
#      propably yes, but i have a deadline on my doorstep, salve mazzutti

import pygame
from pygame.math import Vector2
from settings import *



class Enemy:
    def __init__(self,pos):
        self.grid_pos = pos
        self.pixel_pos = self.get_pixel_pos()


    def get_pixel_pos(self):
        #   do the calculation to consider the top margin and size of each cell
        x = self.grid_pos.x*CELL_WIDTH + (CELL_WIDTH//2)
        y = self.grid_pos.y*CELL_HEIGHT+TOP_BUFFER + (CELL_HEIGHT//2)
        return Vector2(x,y)

    def update(self):
        pass

    def draw(self, screen):
        pygame.draw.circle(screen, RED, (self.pixel_pos.x, self.pixel_pos.y), CELL_WIDTH/2.5 )
