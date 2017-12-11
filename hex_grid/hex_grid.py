
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
