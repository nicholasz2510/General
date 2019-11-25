import sys

grid_size = [int(x) for x in sys.stdin.readline().split()]
total_seats = grid_size[0] * grid_size[1]
seats = []
combinations = []

for x in range(grid_size[0]):
    for i in sys.stdin.readline():
        seats.append(i)

if "." in seats:
    for seat in seats:
        break # Need to finish this
