
# Coins, walls, void and others things
# Could be maze_data.txt, but i'm too lazy to do: open("mazedata.txt", r)
# use CTRL+F to see through the maze map

from settings import *
from pygame import Vector2



# just for stetics porpose on maze_array
# so i dont have to mess with "" strings
C = "C" # coins
E = "E" # enemy 1
F = "F" # enemy 2
G = "G" # enemy 3
H = "H" # enemy 4
enemy_chars = [E, F, G, H] # enemy char list

maze_array = [
# the map of the game
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,G,C,C,C,C,C,C,C,C,C,C,C,1,1,C,C,C,C,C,C,C,C,C,C,C,H,1],
[1,C,1,1,1,1,C,1,1,1,1,1,C,1,1,C,1,1,1,1,1,C,1,1,1,1,C,1],
[1,C,1,1,1,1,C,1,1,1,1,1,C,1,1,C,1,1,1,1,1,C,1,1,1,1,C,1],
[1,C,1,1,1,1,C,1,1,1,1,1,C,1,1,C,1,1,1,1,1,C,1,1,1,1,C,1],
[1,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,1],
[1,C,1,1,1,1,C,1,1,C,1,1,1,1,1,1,1,1,C,1,1,C,1,1,1,1,C,1],
[1,C,1,1,1,1,C,1,1,C,1,1,1,1,1,1,1,1,C,1,1,C,1,1,1,1,C,1],
[1,C,C,C,C,C,C,1,1,C,C,C,C,1,1,C,C,C,C,1,1,C,C,C,C,C,C,1],
[1,1,1,1,1,1,C,1,1,1,1,1,C,1,1,C,1,1,1,1,1,C,1,1,1,1,1,1],
[1,1,1,1,1,1,C,1,1,1,1,1,C,1,1,C,1,1,1,1,1,C,1,1,1,1,1,1],
[1,1,1,1,1,1,C,1,1,C,C,C,C,C,C,C,C,C,C,1,1,C,1,1,1,1,1,1],
[1,1,1,1,1,1,C,1,1,C,1,1,1,0,0,1,1,1,C,1,1,C,1,1,1,1,1,1],
[1,1,1,1,1,1,C,1,1,C,1,0,0,0,0,0,0,1,C,1,1,C,1,1,1,1,1,1],
[1,1,1,1,1,1,C,C,C,C,1,0,0,0,0,0,0,1,C,C,C,C,1,1,1,1,1,1],
[1,1,1,1,1,1,C,1,1,C,1,0,0,0,0,0,0,1,C,1,1,C,1,1,1,1,1,1],
[1,1,1,1,1,1,C,1,1,C,1,1,1,1,1,1,1,1,C,1,1,C,1,1,1,1,1,1],
[1,1,1,1,1,1,C,1,1,C,C,C,C,C,C,C,C,C,C,1,1,C,1,1,1,1,1,1],
[1,1,1,1,1,1,C,1,1,C,1,1,1,1,1,1,1,1,C,1,1,C,1,1,1,1,1,1],
[1,1,1,1,1,1,C,1,1,C,1,1,1,1,1,1,1,1,C,1,1,C,1,1,1,1,1,1],
[1,C,C,C,C,C,C,C,C,C,C,C,C,1,1,C,C,C,C,C,C,C,C,C,C,C,C,1],
[1,C,1,1,1,1,C,1,1,1,1,1,C,1,1,C,1,1,1,1,1,C,1,1,1,1,C,1],
[1,C,1,1,1,1,C,1,1,1,1,1,C,1,1,C,1,1,1,1,1,C,1,1,1,1,C,1],
[1,C,C,C,1,1,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,1,1,C,C,C,1],
[1,1,1,C,1,1,C,1,1,C,1,1,1,1,1,1,1,1,C,1,1,C,1,1,C,1,1,1],
[1,1,1,C,1,1,C,1,1,C,1,1,1,1,1,1,1,1,C,1,1,C,1,1,C,1,1,1],
[1,C,C,C,C,C,C,1,1,C,C,C,C,1,1,C,C,C,C,1,1,C,C,C,C,C,C,1],
[1,C,1,1,1,1,1,1,1,1,1,1,C,1,1,C,1,1,1,1,1,1,1,1,1,1,C,1],
[1,C,1,1,1,1,1,1,1,1,1,1,C,1,1,C,1,1,1,1,1,1,1,1,1,1,C,1],
[1,E,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,F,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

walls = [] # walls coordenates
#coins = [] # coins coordenates are generated separately
enemies_pos = [] # enemies coordenates

# creating coordenates for entities in maze_array
def create_coords():
    for y, line in enumerate(maze_array):
        for x, char in enumerate(line):
            if char == 1:
                walls.append(Vector2(x, y))
            elif char in enemy_chars:
                enemies_pos.append([x,y])
    # obs: enumerate() returns an number and an element of the sequence
    #      used here as an index and an element


def get_coins():
    # generate coins coords separately
    # because of reset bugs caused by anterior method
    lista = []
    for y, line in enumerate(maze_array):
        for x, char in enumerate(line):
            if char == C:
                lista.append(Vector2(x, y))
    return lista



create_coords()
