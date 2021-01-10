from pygame.draw import circle as circle_draw
import pygame
from pygame.math import Vector2
from random import randint
from settings import *
from maze_data import walls

# Enemy class
# if you destroy this file, you will make the game much easier
# obs: bunch of methods are same as player, could the both of them inherit from a parent class??
#      propably yes, but i have a deadline on my doorstep, salve mazzutti




class Enemy:
    def __init__(self, pos, number):
        # besides usual stuff like in player_class
        # each enemy has a unique number, and a pernality, used to diferenciate them
        # could be used to create differents movement patterns and so on
        self.grid_pos = pos
        self.pixel_pos = self.get_pixel_pos()
        self.radius = CELL_WIDTH/2.5
        self.number = number
        self.personality, self.color = self.set_personality()
        self.direction = Vector2(0 ,0)
        self.stored_dir = Vector2(0, 0)
        self.timer = 0 # timer is used to enforce longer random movement gap
        self.able_to_move = True


    def get_pixel_pos(self):
        #   do the calculation to return the center of a specified cell
        x = self.grid_pos[0]*CELL_WIDTH + (CELL_WIDTH//2)
        y = self.grid_pos[1]*CELL_HEIGHT+TOP_BUFFER + (CELL_HEIGHT//2)
        return Vector2(x,y)


    def set_personality(self):
        # set each ghost its owns personality and color
        if self.number == 0:
            return "speedy", RED
        elif self.number == 1:
            return "slowy", PINK
        elif self.number == 2:
            return "randomy", CYAN
        else:
            return "scared", ORANGE


    def move(self):
        # decides when its time for the enemy to change its direction
        # either when the timer reached 60 (with fps == 60, 1 second)
        # either when it hit a wall
        self.timer +=1
        next_pos = Vector2(self.grid_pos[0] + self.direction[0], self.grid_pos[1] + self.direction[1])

        if next_pos in walls:
            self.direction = self.get_random_direction()
            self.timer = 0

        if self.timer == 0 or self.timer >= 60:
            self.direction = self.get_random_direction()
            self.timer = 0


    def get_random_direction(self):
        # get a random (valid) direction for the enemy move to
        while True: # not the best of practices
            # attempt of switch case in python
            case = randint(1,5)
            if case == 1:
                dir = Vector2(1,0) # right
            elif case == 2:
                dir = Vector2(0,1) # down
            elif case == 3:
                dir = Vector2(-1,0) # left
            else:
                dir = Vector2(0,-1) # up

            # calculate the supposed next position
            next_pos = Vector2(self.grid_pos[0] + dir[0], self.grid_pos[1] + dir[1])
            if next_pos not in walls: # and check if there is no walls on supposed next position
                break
        return dir


    def time_to_move(self):
        # same as lock_to_grid method in player class
        # only change direction if on the center of a cell
        if int(self.pixel_pos[0]) % CELL_WIDTH == 10:
            if self.direction == Vector2(1, 0) or self.direction == Vector2(-1, 0)  or self.direction == Vector2(0, 0):
                return True
        if int(self.pixel_pos[1]+TOP_BUFFER//2) % CELL_HEIGHT == 10:
            if self.direction == Vector2(0, 1) or self.direction == Vector2(0, -1)  or self.direction == Vector2(0, 0):
                return True
        return False


    def change_grid_pos(self):
        # simplified version of change_grid_pos() in player class
        # this way dont seems to bug enemy for some reason
        # change the grid position in according to the pixel position
        self.grid_pos[0] = (self.pixel_pos[0])//CELL_WIDTH
        self.grid_pos[1] = (self.pixel_pos[1] - TOP_BUFFER)//CELL_HEIGHT


    def update(self):
        # call the other methods on enemy class
        self.pixel_pos += self.direction # the reak movement
        if self.time_to_move():
            self.move()
        self.change_grid_pos()


    def on_player(self, player):
        # check if enemy and player grid position are the same
        # method called in game class
        if self.grid_pos == player.grid_pos:
            return True
        return False


    def draw(self, screen):
        # draw the enemy as a circle
        x = self.pixel_pos[0]
        y = self.pixel_pos[1]
        circle_draw(screen, self.color, (x, y), self.radius)
