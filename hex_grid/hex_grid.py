
def hex_grid(data):
    pos = [0, 0]
    for d in data:
        if d == 'n':
            pos[1] += 2
        elif d == 'e':
            pos[0] += 2
        elif d == 'w':
            pos[0] -= 2
        elif d == 's':
            pos[1] -= 2
        elif d == 'ne':
            pos[0] += 1
            pos[1] += 1
        elif d == 'nw':
            pos[0] -= 1
            pos[1] += 1
        elif d == 'se':
            pos[0] += 1
            pos[1] -= 1
        elif d == 'sw':
            pos[0] -= 1
            pos[1] -= 1

    print(pos)
    return (abs(pos[0]) + abs(pos[1]))/2


if __name__ == '__main__':

    with open('input.txt') as f:
        content = f.readline()
        _input = [x for x in content.strip().split(',')]
        print(hex_grid(_input))

# --- Day 11: Hex Ed ---
#
# Crossing the bridge, you've barely reached the other side of the stream when a program comes up to you, clearly in distress. "It's my child process," she says, "he's gotten lost in an infinite grid!"
#
# Fortunately for her, you have plenty of experience with infinite grids.
#
# Unfortunately for you, it's a hex grid.
#
# The hexagons ("hexes") in this grid are aligned such that adjacent hexes can be found to the north, northeast, southeast, south, southwest, and northwest:
#
#   \ n  /
# nw +--+ ne
#   /    \
# -+      +-
#   \    /
# sw +--+ se
#   / s  \
#
# You have the path the child process took. Starting where he started, you need to determine the fewest number of steps required to reach him. (A "step" means to move from the hex you are in to any adjacent hex.)
#
# For example:
#
#     ne,ne,ne is 3 steps away.
#     ne,ne,sw,sw is 0 steps away (back where you started).
#     ne,ne,s,s is 2 steps away (se,se).
#     se,sw,se,sw,sw is 3 steps away (s,s,sw).
#
# Your puzzle answer was 810.
