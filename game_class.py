#
#   creates the game class
#   basics stuff only
#
import sys
import pygame
import copy
from settings import *
from player_class import *
from enemy_class import *
from maze_data import *

pygame.init()


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True # makes the game go *BRRRRRR*
        self.load() # load back gorund
        self.state = "game"

        self.player = Player(self, copy.copy(PLAYER_STARTING_POS))
        self.enemies = []
        self.enemies_starting_pos = []
        self.make_enemies()
        self.walls = walls
        self.coins = get_coins()

        self.grid_debug = False
        self.wall_debug = False
        self.player_debug = False


    def run(self):
        # keep the gaming going
        # call the functions in the game
        while self.running:
            if self.state == "game":
                self.game_update()
            elif self.state == "game-over":
                self.over_update()
        pygame.quit()
        sys.exit()

    def game_events(self):
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
        # could load other things if needed
        self.background = pygame.image.load('labirintite.png')
        self.background = pygame.transform.scale(self.background, (MAZE_WIDTH, MAZE_HEIGHT))
        BACKGROUND = self.background # just to draw black 2 tiles

    def make_enemies(self):
        # pass the initial conditions for the instance of enemy object
        for enemy_number, each_enemy_pos in enumerate(enemies_pos):
            self.enemies_starting_pos.append( each_enemy_pos)
            self.enemies.append(Enemy(self, copy.copy(each_enemy_pos), enemy_number))


    def draw_text(self, words, screen, pos, centered = False,  size = 18, colour = WHITE, font_name= "arial black"):
        font = pygame.font.SysFont(font_name, size)
        text = font.render(words, False, colour)
        text_size = text.get_size()
        if centered:
            pos[0] = pos[0]-text_size[0]//2
            pos[1] = pos[1]-text_size[1]//2
        screen.blit(text, pos)

    def draw_coins(self):
        # Draw the coins based on the maze map
        # simple way, no fancy pants
        for each_coin in self.coins:
            pygame.draw.circle(self.screen, GOLDEN, ((each_coin.x*CELL_WIDTH)+CELL_WIDTH//2, ((each_coin.y*CELL_HEIGHT)+CELL_HEIGHT//2)+TOP_BUFFER),CELL_WIDTH//5 )


    def draw_grid(self):
        for x in range(WIDTH//CELL_WIDTH): # width/width/28
            pygame.draw.line(self.screen, GREY, (x*CELL_WIDTH,0), (x*CELL_WIDTH,HEIGHT))
        for y in range(HEIGHT//CELL_HEIGHT):
            pygame.draw.line(self.screen, GREY, (0, y*CELL_HEIGHT), (WIDTH, y*CELL_HEIGHT))

    def draw_walls(self):
        for wall in self.walls:
            pygame.draw.rect(self.screen, PURPLE, (wall.x*CELL_WIDTH, wall.y* CELL_HEIGHT+TOP_BUFFER, CELL_WIDTH,CELL_HEIGHT))

    def draw_entities_position(self):
        pygame.draw.rect(self.screen, RED, (int(self.player.grid_pos[0]*CELL_WIDTH),int(self.player.grid_pos[1]*CELL_HEIGHT+TOP_BUFFER),CELL_WIDTH,CELL_HEIGHT), 1)
        for each_enemy in self.enemies:
            pygame.draw.rect(self.screen, RED, (int(each_enemy.grid_pos[0]*CELL_WIDTH), int(each_enemy.grid_pos[1]*CELL_HEIGHT+TOP_BUFFER), CELL_WIDTH, CELL_HEIGHT), 1)

    def debug_mode(self, key):
        # turns debbuging on and off
        if key == DEBUG_KEYS[0]:
            self.grid_debug = True if self.grid_debug == False else False
        elif key == DEBUG_KEYS[1]:
            self.wall_debug = True if self.wall_debug == False else False
        elif key == DEBUG_KEYS[2]:
            self.player_debug = True if self.player_debug == False else False


    def game_update(self):
        self.clock.tick(FPS) # higher the fps, higher the speed
        self.game_events()
        self.game_draw()
        self.player.update()
        for each_enemy in self.enemies:
            each_enemy.update()

            if each_enemy.on_player(self.player):
                self.state = "game-over"
                self.restart()






    def game_draw(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.background, (0,TOP_BUFFER))
        self.draw_text(f"SCORE: {self.player.score}", self.screen, [60, 0])

        if self.wall_debug:
            self.draw_walls()
        if self.grid_debug:
            self.draw_grid()
        if self.player_debug:
            self.draw_entities_position()
        self.draw_coins()
        self.player.draw(self.screen)
        for each_enemy in self.enemies:
            each_enemy.draw(self.screen)
        pygame.display.update()


    def over_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False


            if event.type == pygame.KEYDOWN:
                if event.key in RETURN_KEY:
                    self.state = "game"

                elif event.key in ESCAPE_KEY:
                    self.running = False


    def over_update(self):
        self.clock.tick(FPS)
        self.over_events()
        self.over_draw()


    def over_draw(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.screen, (0,TOP_BUFFER))
        quit_text = "Press the escape button to QUIT"
        again_text = "Press ENTER to PLAY AGAIN"
        self.draw_text("GAME OVER", self.screen, [WIDTH//2, 100], True)
        self.draw_text(again_text, self.screen, [WIDTH//2, HEIGHT//2], True)
        self.draw_text(quit_text, self.screen, [WIDTH//2, HEIGHT//1.5], True)

        pygame.display.update()

    def restart(self):
        self.player.grid_pos = Vector2(PLAYER_STARTING_POS)
        self.player.pixel_pos = self.player.get_pixel_pos()
        self.player.direction *= 0
        self.player.score = 0
        for index, each_enemy in enumerate(self.enemies):
            each_enemy.grid_pos = copy.copy(self.enemies_starting_pos[index])
            each_enemy.pixel_pos = each_enemy.get_pixel_pos()
            each_enemy.direction *= 0
        self.coins = get_coins()
