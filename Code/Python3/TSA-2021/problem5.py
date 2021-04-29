import sys

letter_to_num = ['', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

num_col = int(sys.stdin.readline())
num_row = int(sys.stdin.readline())
pos = sys.stdin.readline()
start_col = letter_to_num.index(pos[0])
start_row = int(pos[1])
curr_pos = [start_col, start_row]

directions = sys.stdin.readline()


def is_out_of_bounds():
    if curr_pos[0] < 1 or curr_pos[0] > num_col:
        return True
    if curr_pos[1] < 1 or curr_pos[1] > num_row:
        return True
    return False


for direction in directions:
    if direction == "N":
        curr_pos[1] -= 1
    elif direction == "E":
        curr_pos[0] += 1
    elif direction == "S":
        curr_pos[1] += 1
    elif direction == "W":
        curr_pos[0] -= 1
    if is_out_of_bounds():
        print("Out of bounds.")
        quit()

print(letter_to_num[curr_pos[0]] + str(curr_pos[1]))
