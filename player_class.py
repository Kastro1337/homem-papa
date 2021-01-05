from settings import *
import pygame
from pygame import Vector2
from maze_data import walls



#   The player class.
#   you cant go anywhere without this
class Player:
    def __init__(self, pos):
        #   Receives the position and modifies it, to be in one quadrant/sector
        #   considering the margin and the size of the cells that divide the map
        self.grid_pos = pos
        self.pixel_pos = self.get_pos()
        self.direction = Vector2(0,0)
        self.stored_dir = Vector2(0,0)
        self.able_to_move = True


    def get_pos(self):
        #   do the calculation to consider the top margin and size of each cell
        x = self.grid_pos.x*CELL_WIDTH + (CELL_WIDTH//2)
        y = self.grid_pos.y*CELL_HEIGHT+TOP_BUFFER + (CELL_HEIGHT//2)
        return Vector2(x,y)


    def move(self, key):
        if key == MOVE_KEYS[0]:     # right
            self.stored_dir = Vector2(1,0)

        elif key == MOVE_KEYS[1]:   # left
            self.stored_dir = Vector2(-1,0)

        elif key == MOVE_KEYS[2]:   # up
            self.stored_dir = Vector2(0,-1)

        else:                        # down
            self.stored_dir = Vector2(0,1)


    def lock_to_grid(self):
        #   Lock the player to the grid
        #   supostamente...

        # Horizontal
        if self.pixel_pos.x % CELL_WIDTH == CELL_HEIGHT//2: # ???? COMO ISSO FUNCIONA
            if self.stored_dir == Vector2(0,1) or self.stored_dir == Vector2(0,-1):
                self.direction = self.stored_dir

        #Vertical
        if (self.pixel_pos.y) % CELL_HEIGHT == CELL_WIDTH//2:
            if self.stored_dir == Vector2(1,0) or self.stored_dir == Vector2(-1,0):
                self.direction = self.stored_dir


    def can_move(self):
        # Check if there is no walls on the path ahead
        for each_wall in walls:
            #print("grid_pos = ",self.grid_pos)
            #print("direction =",self.direction)
            #print("wall =", each_wall)
            if Vector2(self.grid_pos + self.direction) == each_wall: # TODO: comment this one
                return False
        return True

    def change_grid_pos(self):
        # change grid position in reference of pixel position
        # for each 20 pixels to one directions, change the grid position
        # it depends on wich direction the player is moving

        if self.direction == Vector2(-1,0): #left
            self.grid_pos[0] = (self.pixel_pos[0]+CELL_WIDTH//2)//CELL_WIDTH
            self.grid_pos[1] = (self.pixel_pos[1] - TOP_BUFFER +CELL_HEIGHT//2)//CELL_HEIGHT -1

        elif self.direction == Vector2(1,0): #right
            self.grid_pos[0] = (self.pixel_pos[0]+CELL_WIDTH//2)//CELL_WIDTH -1
            self.grid_pos[1] = (self.pixel_pos[1] - TOP_BUFFER +CELL_HEIGHT//2)//CELL_HEIGHT -1

        elif self.direction == Vector2(0,1): #down
            self.grid_pos[0] = (self.pixel_pos[0]+CELL_WIDTH//2)//CELL_WIDTH -1
            self.grid_pos[1] = (self.pixel_pos[1] - TOP_BUFFER +CELL_HEIGHT//2)//CELL_HEIGHT -1

        elif self.direction == Vector2(0,-1): # up
            self.grid_pos[0] = (self.pixel_pos[0]+CELL_WIDTH//2)//CELL_WIDTH -1
            self.grid_pos[1] = (self.pixel_pos[1] - TOP_BUFFER +CELL_HEIGHT//2)//CELL_HEIGHT

        # thats complex AF
        # to regulate grid_pos, you need to change the "drag" of the position
        # depending on where the player is moving towards




    def update(self):
        if self.able_to_move:
            self.pixel_pos += self.direction
        self.change_grid_pos()
            #self.grid
        self.lock_to_grid()
        self.able_to_move = self.can_move()





    def draw(self, screen):
        #   Draw on screen the player's circle,
        #   with the corrected position and the diameter proportional to a quadrant
        pygame.draw.circle(screen, YELLOW, (self.pixel_pos.x, self.pixel_pos.y), CELL_WIDTH/2)
