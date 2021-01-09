# Enemy class
# if you destroy this file, you make the game much easier
# obs: bunch of methods are same as player, could the both of them inherit from a parent class??
#      propably yes, but i have a deadline on my doorstep, salve mazzutti

from pygame.draw import circle as circle_draw
import pygame
from pygame.math import Vector2
from random import randint
from settings import *
from maze_data import walls



class Enemy:
    def __init__(self, game, pos, number):
        self.game = game
        self.grid_pos = pos
        self.pixel_pos = self.get_pixel_pos()
        self.radius = CELL_WIDTH/2.5
        self.number = number
        self.personality, self.color = self.set_personality()
        self.direction = Vector2(0 ,0)
        self.stored_dir = Vector2(0, 0)
        self.timer = 0


        self.able_to_move = True





    def get_pixel_pos(self):
        #   do the calculation to consider the top margin and size of each cell
        x = self.grid_pos[0]*CELL_WIDTH + (CELL_WIDTH//2)
        y = self.grid_pos[1]*CELL_HEIGHT+TOP_BUFFER + (CELL_HEIGHT//2)
        return Vector2(x,y)

    def set_personality(self):
        if self.number == 0:
            return "speedy", RED
        elif self.number == 1:
            return "slowy", PINK
        elif self.number == 2:
            return "randomy", CYAN
        else:
            return "scared", ORANGE


    def move(self):

        self.timer +=1
        next_pos = Vector2(self.grid_pos[0] + self.direction[0], self.grid_pos[1] + self.direction[1])


        if next_pos in walls:
            self.direction = self.get_random_direction()
            self.timer = 0

        if self.timer == 0 or self.timer >= 60:
            self.direction = self.get_random_direction()
            self.timer = 0


    def get_random_direction(self):
        while True: # not the best of practices
            case = randint(1,5)
            if case == 1:
                dir = Vector2(1,0)
            elif case == 2:
                dir =  Vector2(0,1)
            elif case == 3:
                dir =  Vector2(-1,0)
            else:
                dir =  Vector2(0,-1)

            #next_pos = dir + self.grid_pos # calculate the supposed next position
            next_pos = Vector2(self.grid_pos[0] + dir[0], self.grid_pos[1] + dir[1])
            if next_pos not in walls: # check if there is no walls on the path ahead
                break
        return dir

    def time_to_move(self):
        if int(self.pixel_pos[0]) % CELL_WIDTH == 10:
            if self.direction == Vector2(1, 0) or self.direction == Vector2(-1, 0)  or self.direction == Vector2(0, 0):
                return True
        if int(self.pixel_pos[1]+TOP_BUFFER//2) % CELL_HEIGHT == 10:
            if self.direction == Vector2(0, 1) or self.direction == Vector2(0, -1)  or self.direction == Vector2(0, 0):
                return True
        return False

    def change_grid_pos(self):
        self.grid_pos[0] = (self.pixel_pos[0])//CELL_WIDTH
        self.grid_pos[1] = (self.pixel_pos[1] - TOP_BUFFER)//CELL_HEIGHT


    def update(self):
        self.pixel_pos += self.direction
        if self.time_to_move():
            self.move()
        self.change_grid_pos()


    def on_player(self, player):
        if self.grid_pos == player.grid_pos:
            return True
        return False




    def draw(self, screen):
        circle_draw(screen, self.color, (self.pixel_pos[0], self.pixel_pos[1]), self.radius )
