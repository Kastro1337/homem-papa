#
#   creates the game class
#   basics stuff only
#
import sys
import pygame
from settings import *
from player_class import *


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True # makes the game go *BRRRRRR*
        self.load() # load back gorund
        self.player = Player(PLAYER_STARTING_POS)
        print(self.player.grid_pos)


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


    # Load the background
    # And resizes it
    def load(self):
        self.background = pygame.image.load('labirintite.png')
        self.background = pygame.transform.scale(self.background, (MAZE_WIDTH, MAZE_HEIGHT))

    def draw_grid(self):
        for x in range(WIDTH//CELL_WIDTH): # width/width/28
            pygame.draw.line(self.background, GREY, (x*CELL_WIDTH,0), (x*CELL_WIDTH,HEIGHT))
        for x in range(HEIGHT//CELL_HEIGHT):
            pygame.draw.line(self.background, GREY, (0, x*CELL_HEIGHT), (WIDTH, x*CELL_HEIGHT))


    def update(self):
        self.events()
        self.draw()
        self.player.update()
        self.clock.tick(FPS) # higher the fps, higher the speed
                             # sdds do delta.time do unity

    # Draw everything on screen
    def draw(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.background, (0,TOP_BUFFER))
        self.draw_grid()
        self.player.draw(self.screen)
        pygame.display.update()
