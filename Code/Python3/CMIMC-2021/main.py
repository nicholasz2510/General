from ast import literal_eval

# edit to the name of the input file
f = open('robotrecovery1.txt', 'r')


# change this function however you want: it takes in a character representing a cell
# of the maze and x/y coordinates and returns whatever representation you want
def rep(c, x, y):
    if c == '.':
        return c
    elif c == 'X':
        return c
    elif c == 'R':
        robots.append([x, y])
        return c
    elif c == 'E':
        entrance.append(x)
        entrance.append(y)
        return c


# you shouldn't need to edit lines 18-25
r, c, n = map(int, f.readline().strip().split())
robots = []
entrance = []
maze = []
instructions = []

for y in range(r):
    s = f.readline().strip()
    maze.append([rep(s[x], x, y) for x in range(c)])
heatmap = [[None for y in x] for x in maze]

checked = set()

# print(heatmap)

def has_value(x, y):
    return heatmap[y][x] is not None


def check_coordinate(x, y):
    if (x, y) in checked:
        return False
    checked.add((x, y))
    if x >= c or x < 0 or y >= r or y < 0:
        print("rejected in first conditional: " + str(x) + str(y))
        return False
    if maze[y][x] == 'X' or has_value(x, y):
        print("rejected in second conditional: " + str(x) + str(y))
        return False
    print("succeeded: " + str(x) + str(y))
    return True


def get_neighbors(x, y):
    return [[n[0], n[1]] for n in [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]] if check_coordinate(n[0], n[1])]


curr_heat = 0
curr_values = [entrance]
while len(curr_values) != 0:
    for v in curr_values:
        heatmap[v[1]][v[0]] = curr_heat

    next_values = []
    for v in curr_values:
        for n in get_neighbors(v[0], v[1]):
            next_values.append(n)
    curr_values = next_values
    curr_heat += 1

print(heatmap)
