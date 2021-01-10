from settings import *
from pygame.draw import circle as circle_draw
from pygame import Vector2
from maze_data import *



#   The player class.
#   you wouldn't do anything without this
class Player:
    def __init__(self, game, pos):

        self.game = game                        # get the game objetct
        self.grid_pos = pos                     # grid position (example (13, 15))
        self.pixel_pos = self.get_pixel_pos()   # transform grid position in pixel position
        self.direction = Vector2(0,0)           # momvement direction
        self.stored_dir = Vector2(0,0)          # stored movement direction, in case player not able to move yet
        self.able_to_move = True                # boolean that let direction be stored_dir
        self.radius = CELL_WIDTH//2             # radius is half of a cell
                                                # so the player's diameter is a full cell
        self.score = 0                          # player's score



    def get_pixel_pos(self):
        #   Receives the position (Vector) and modifies it, to be in the center of a quadrant/sector
        #   considering the margin and the size of the cells that divide the map
        x = self.grid_pos[0]*CELL_WIDTH + (CELL_WIDTH//2)
        y = self.grid_pos[1]*CELL_HEIGHT+TOP_BUFFER + (CELL_HEIGHT//2)
        # the result is a pixel pos, often used to draw on screen objects
        #                            but also used to movement
        return Vector2(x,y)


    def move(self, key):
        # get pressed keys from event handler
        # and decides where the player should move towards
        if key == MOVE_KEYS[0]:     # right
            self.stored_dir = Vector2(1,0)

        elif key == MOVE_KEYS[1]:   # left
            self.stored_dir = Vector2(-1,0)

        elif key == MOVE_KEYS[2]:   # up
            self.stored_dir = Vector2(0,-1)

        else:                        # down
            self.stored_dir = Vector2(0,1)


    def can_move(self):
        # Check if there is no wall on the cell in front of the player
        for each_wall in walls:
            next_pos = self.grid_pos + self.direction
            if next_pos == each_wall:
                return False
        return True


    def lock_to_grid(self):
        # if the player is not on the center of a grid cell
        # and he decides to turn to another side, like from vertical moving to horizontal moving
        # than he will only be able to turn when he is on the exact center of a grid cell

        # Horizontal
        if self.pixel_pos[0] % CELL_WIDTH == CELL_HEIGHT//2:
            if self.stored_dir == Vector2(0,1) or self.stored_dir == Vector2(0,-1):
                self.direction = self.stored_dir

        #Vertical
        if (self.pixel_pos[1]) % CELL_HEIGHT == CELL_WIDTH//2:
            if self.stored_dir == Vector2(1,0) or self.stored_dir == Vector2(-1,0):
                self.direction = self.stored_dir


    def change_grid_pos(self):
        # change grid position in reference of pixel position
        # depends on wich direction the player is moving
        # needed to avoid change directions bug with walls
        # to regulate grid_pos, you need to change the "drag" of the position
        # depending on where the player is moving towards

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


    def on_coin(self):
        # if the player is on the same cell as a coin
        # the coin will dissapear
        if self.grid_pos in self.game.coins:
            self.game.coins.remove(self.grid_pos)
            return True


    def update(self):
        # call all the functions to make the player object work properly
        if self.able_to_move:
            # if there is no walls ahead
            # than the position is incremented by the direction (up down right left)
            self.pixel_pos += self.direction # actual moving
        self.change_grid_pos()
        self.lock_to_grid()
        self.able_to_move = self.can_move()

        if self.on_coin():
            # the score will go up if player is on a coin
            self.score += 1


    def draw(self, screen):
        #   Draw on screen the player's circle,
        #   with the corrected position and the diameter proportional to a quadrant
        x = self.pixel_pos[0]
        y = self.pixel_pos[1]
        circle_draw(screen, YELLOW, (x, y), self.radius)
