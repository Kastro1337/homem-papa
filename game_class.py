#
#   creates the game class
#   basics stuff only
#
import sys
import pygame
from settings import *
from player_class import *
from maze_data import walls


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True # makes the game go *BRRRRRR*
        self.load() # load back gorund
        self.player = Player(PLAYER_STARTING_POS)
        self.grid_debug = False
        self.wall_debug = False
        self.player_debug = False



    def run(self):
        while self.running:
            self.update()
        pygame.quit()
        sys.exit()

    def events(self):
        for event in pygame.event.get():
            # the right way to do it
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key in MOVE_KEYS:
                    self.player.move(event.key)
                elif event.key in DEBUG_KEYS:
                    self.debug_mode(event.key)



    def load(self):
        # Load the background
        # And resizes it
        self.background = pygame.image.load('labirintite.png')
        self.background = pygame.transform.scale(self.background, (MAZE_WIDTH, MAZE_HEIGHT))




    def draw_grid(self):
        for x in range(WIDTH//CELL_WIDTH): # width/width/28
            pygame.draw.line(self.screen, GREY, (x*CELL_WIDTH,0), (x*CELL_WIDTH,HEIGHT))
        for y in range(HEIGHT//CELL_HEIGHT):
            pygame.draw.line(self.screen, GREY, (0, y*CELL_HEIGHT), (WIDTH, y*CELL_HEIGHT))

    def draw_walls(self):
        for wall in walls:
            pygame.draw.rect(self.screen, PINK, (wall.x*CELL_WIDTH, wall.y* CELL_HEIGHT+TOP_BUFFER, CELL_WIDTH,CELL_HEIGHT))

    def draw_player_position(self):
        pygame.draw.rect(self.screen, RED, (int(self.player.grid_pos.x*CELL_WIDTH),int(self.player.grid_pos.y*CELL_HEIGHT+TOP_BUFFER),CELL_WIDTH,CELL_HEIGHT), 1)


    def debug_mode(self, key):
        # turns debbuging on and off
        if key == DEBUG_KEYS[0]:
            self.grid_debug = True if self.grid_debug == False else False
        elif key == DEBUG_KEYS[1]:
            self.wall_debug = True if self.wall_debug == False else False
        elif key == DEBUG_KEYS[2]:
            self.player_debug = True if self.player_debug == False else False


    def update(self):
        self.events()
        self.draw()
        self.player.update()
        #print(self.player.grid_pos)

        self.clock.tick(FPS) # higher the fps, higher the speed
                             # sdds do delta.time do unity

    # Draw everything on screen
    def draw(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.background, (0,TOP_BUFFER))
        if self.wall_debug:
            self.draw_walls()
        if self.grid_debug:
            self.draw_grid()
        if self.player_debug:
            self.draw_player_position()
        self.player.draw(self.screen)
        pygame.display.update()
