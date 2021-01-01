#
#   creates the game class
#   basics stuff only
#
import sys
import pygame
from settings import *


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True # makes the game go *BRRRRRR*
        self.load() # load back gorund

    def run(self):
        while self.running:
            self.events()
            self.draw()
            self.clock.tick(FPS) # delta time in unity c#
        pygame.quit()
        sys.exit()

    def events(self):
        for event in pygame.event.get():
            # the right way to do it
            if event.type == pygame.QUIT:
                self.running = False

    # Load the background
    # And resize it
    def load(self):
        self.background = pygame.image.load('labirintite.png')
        self.background = pygame.transform.scale(self.background, (WIDTH, HEIGHT))

    def draw_grid(self):
        for x in range(WIDTH//CELL_WIDTH): # width/width/28
            pygame.draw.line(self.screen, GREY, (x*CELL_WIDTH,0), (x*CELL_WIDTH,HEIGHT))
        for x in range(HEIGHT//CELL_HEIGHT):
            pygame.draw.line(self.screen, GREY, (0, x*CELL_HEIGHT), (WIDTH, x*CELL_HEIGHT))


    def update(self):
        pass

    # Draw everything on screen
    def draw(self):
        self.screen.blit(self.background, (0,0))
        self.draw_grid()
        pygame.display.update()
