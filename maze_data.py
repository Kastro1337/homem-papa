
# Coins, walls, void and others things
# Could be maze_data.txt, but i'm too lazy to do: open("mazedata.txt", r)
# use CTRL+F to see through

from pygame import Vector2

C = "C" # coins var, just to dont mess with "" strings

maze_array = [
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
[1,1,1,1,1,1,C,1,1,C,1,1,1,1,1,1,1,1,C,1,1,C,1,1,1,1,1,1],
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
[1,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

walls = []
coins = []

# creating coordenates for walls in maze_array
for y, line in enumerate(maze_array):  # y
    for x, char in enumerate(line):    # x
        if char == 1:
            walls.append(Vector2(x, y))
        elif char == C:
            coins.append(Vector2(x, y))

# obs: enumerated() returns an number and an element of the sequence
#      used here as an index and an element
