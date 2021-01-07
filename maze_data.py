
# Coins, walls, void and others things
# Could be maze_data.txt, but i'm too lazy to do: open("mazedata.txt", r)
# use CTRL+F to see through

from settings import *
from pygame import Vector2



# just for stetics porpose on maze_array
# so i dont have to mess with "" strings
C = "C" # coins
B = "B" # black tiles used for paint over walls
E = "E" # enemy 1
F = "F" # enemy 2
G = "G" # enemy 3
H = "H" # enemy 4
enemy_chars = [E, F, G, H] # enemy char list

maze_array = [
# the map of the game
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,C,C,C,C,C,C,C,C,C,C,C,C,1,1,C,C,C,C,C,C,C,C,C,C,C,C,1],
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
[1,1,1,1,1,1,C,1,1,C,1,E,0,0,0,0,F,1,C,1,1,C,1,1,1,1,1,1],
[1,1,1,1,1,1,C,C,C,C,1,0,0,0,0,0,0,1,C,C,C,C,1,1,1,1,1,1],
[1,1,1,1,1,1,C,1,1,C,1,G,0,0,0,0,H,1,C,1,1,C,1,1,1,1,1,1],
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
[1,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

walls = [] # walls coordenates
coins = [] # coins coordenates
enemies_pos = [] # enemies coordenates

# creating coordenates for entities in maze_array
for y, line in enumerate(maze_array):  # y
    for x, char in enumerate(line):    # x
        if char == 1:
            walls.append(Vector2(x, y))
        elif char == C:
            coins.append(Vector2(x, y))
        elif char in enemy_chars:
            enemies_pos.append(Vector2(x, y))


# obs: enumerate() returns an number and an element of the sequence
#      used here as an index and an element
