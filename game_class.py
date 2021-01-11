#
#   game class
#   handle all other classes and make the game happen
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
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))  # set the screen
        self.clock = pygame.time.Clock()                        # set the clock, used used to cap fps later
        self.load()                                             # load back gorund
        self.running = True                                     # makes the game go *BRRRRRR*
        self.state = "playing"                                  # there is 2 states of game: playing and over

        self.player = Player(self, copy.copy(PLAYER_STARTING_POS)) # create Player object and give its inital arguments
        self.enemies = []                                       # create enemies list
        self.enemies_starting_pos = []                          # and the enemies starting positions
        self.make_enemies()                                     # create the enmies and put into the enemies list
        self.walls = walls                                      # walls position
        self.coins = get_coins()                                # get coins positions

        self.grid_debug = False
        self.wall_debug = False
        self.player_debug = False


    def run(self):
        # keep the gaming going
        # call the functions in the game
        while self.running:
            if self.state == "playing":
                self.playing_update()
            elif self.state == "game-over":
                self.over_update()
        pygame.quit()
        sys.exit()


    def playing_events(self):
        # receive all playing state events and handle them
        # keys pressed and quitters
        for event in pygame.event.get():
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
        self.background = pygame.image.load('labirinto.png')
        self.background = pygame.transform.scale(self.background, (MAZE_WIDTH, MAZE_HEIGHT))


    def make_enemies(self):
        # pass the initial conditions for the instance of enemy object
        for enemy_number, each_enemy_pos in enumerate(enemies_pos):
            self.enemies_starting_pos.append(each_enemy_pos) # used to reset later
            self.enemies.append(Enemy(copy.copy(each_enemy_pos), enemy_number)) # create the object and put into the list


    def draw_text(self, words, screen, pos, centered = False,  size = 18, colour = WHITE, font_name= "arial black"):
        # draw text
        # padrao
        font = pygame.font.SysFont(font_name, size)
        text = font.render(words, False, colour)
        text_size = text.get_size()
        if centered: # centralize method
            pos[0] = pos[0]-text_size[0]//2
            pos[1] = pos[1]-text_size[1]//2
        screen.blit(text, pos)


    def draw_coins(self):
        # Draw the coins based on the maze map
        # simple way
        for each_coin in self.coins:
            x = (each_coin.x*CELL_WIDTH)+CELL_WIDTH//2                  # horizontal position
            y = ((each_coin.y*CELL_HEIGHT)+CELL_HEIGHT//2)+TOP_BUFFER   # vertical position
            r = CELL_WIDTH//5                                           # radius
            pygame.draw.circle(self.screen, GOLDEN, (x, y), r)


    def draw_grid(self):
        # debug function:
        # draw a visible grid, so we can see what is the cell width and cell height
        # and the calculations we made with them
        for x in range(WIDTH//CELL_WIDTH):
            pygame.draw.line(self.screen, GREY, (x*CELL_WIDTH,0), (x*CELL_WIDTH,HEIGHT))
        for y in range(HEIGHT//CELL_HEIGHT):
            pygame.draw.line(self.screen, GREY, (0, y*CELL_HEIGHT), (WIDTH, y*CELL_HEIGHT))


    def draw_walls(self):
        # debug function:
        # create a visible representation of the "real" wall
        # from the maze_data map array
        for wall in self.walls:
            x = wall.x*CELL_WIDTH
            y = wall.y* CELL_HEIGHT+TOP_BUFFER
            pygame.draw.rect(self.screen, PURPLE, (x, y, CELL_WIDTH, CELL_HEIGHT))


    def draw_entities_position(self):
        # debug function:
        # draw a red rectangle arround the player and enemies
        # show the real grid postion, whom the calculations are made with
        x = int(self.player.grid_pos[0]*CELL_WIDTH)
        y = int(self.player.grid_pos[1]*CELL_HEIGHT+TOP_BUFFER)
        pygame.draw.rect(self.screen, RED, (x, y, CELL_WIDTH,CELL_HEIGHT), 1)

        for each_enemy in self.enemies:
            x = int(each_enemy.grid_pos[0]*CELL_WIDTH)
            y = int(each_enemy.grid_pos[1]*CELL_HEIGHT+TOP_BUFFER)
            pygame.draw.rect(self.screen, RED, (x, y, CELL_WIDTH, CELL_HEIGHT), 1)


    def debug_mode(self, key):
        # turns debbuging on and off
        # TIL ternary operator in python
        if key == DEBUG_KEYS[0]:
            self.grid_debug = True if self.grid_debug == False else False
        elif key == DEBUG_KEYS[1]:
            self.wall_debug = True if self.wall_debug == False else False
        elif key == DEBUG_KEYS[2]:
            self.player_debug = True if self.player_debug == False else False


    def playing_update(self):
        # method update for playing state
        self.clock.tick(FPS) # higher the fps, higher the speed
        self.playing_events()
        self.playing_draw()
        self.player.update()
        for each_enemy in self.enemies:
            each_enemy.update()

            if each_enemy.on_player(self.player):
                self.state = "game-over"
                self.restart()


    def playing_draw(self):
        # method draw for playing state
        # paint the game, player enemies, pretty much everything
        self.screen.fill(BLACK)
        self.screen.blit(self.background, (0,TOP_BUFFER))
        self.draw_text(f"SCORE: {self.player.score}", self.screen, [60, TOP_BUFFER//2]) # score board

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
        # method for events in game-over state
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key in RETURN_KEY:
                    self.state = "playing"

                elif event.key in ESCAPE_KEY:
                    self.running = False


    def over_update(self):
        # in game-over update
        # call other game-over methods
        self.clock.tick(FPS)
        self.over_events()
        self.over_draw()


    def over_draw(self):
        # draw the game-over screen
        self.screen.fill(BLACK)
        self.screen.blit(self.screen, (0,TOP_BUFFER))
        quit_text = "Press the escape button to QUIT"
        again_text = "Press ENTER to PLAY AGAIN"
        self.draw_text("GAME OVER", self.screen, [WIDTH//2, 100], True)
        self.draw_text(again_text, self.screen, [WIDTH//2, HEIGHT//2], True)
        self.draw_text(quit_text, self.screen, [WIDTH//2, HEIGHT//1.5], True)

        pygame.display.update()


    def restart(self):
        # re-start all the inital positions, score, coins, and everyone movement
        # also all the copy.copy in the code is because of reset bugs
        # apparently, Vector2 is a list, and list are copied by reference (*pointers and stuff)
        self.player.grid_pos = Vector2(PLAYER_STARTING_POS) # reset player to starting position
        self.player.pixel_pos = self.player.get_pixel_pos() # and get its original pixel postion
        self.player.direction *= 0  # Nullifies direction
        self.player.score = 0       # nullifies score
        for index, each_enemy in enumerate(self.enemies):
            each_enemy.grid_pos = copy.copy(self.enemies_starting_pos[index]) # reset enemies starting pos
            each_enemy.pixel_pos = each_enemy.get_pixel_pos()                 # and get pixel-pos
            each_enemy.direction *= 0   # nullifies all enemies direction
        self.coins = get_coins() # and get the coins again
                                 # (thats why it has it's own function)
