from settings import *
import pygame


#   The player class.
#   you cant go anywhere without this
class Player:
    def __init__(self,pos):
        #   Receives the position and modifies it, to be in one quadrant/sector
        #   considering the margin and the size of the cells that divide the map
        self.grid_pos = pos
        x = self.grid_pos.x*CELL_WIDTH+CELL_WIDTH//2
        y = self.grid_pos.y*CELL_HEIGHT+TOP_BUFFER+(CELL_HEIGHT//2)
        self.correct_pos = vec(x, y)


    def draw(self, screen):
        #   Draw on screen the player's circle,
        #   with the corrected position and the diameter proportional to a quadrant
        pygame.draw.circle(screen, YELLOW, (self.correct_pos.x, self.correct_pos.y), CELL_WIDTH/2)
