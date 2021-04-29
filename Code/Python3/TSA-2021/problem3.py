import sys

pi = 3.14159

is_volume = sys.stdin.readline()[0] == "v"
value = float(sys.stdin.readline())

if is_volume:
    print("radius = " + str(round(((3 * value) / (4 * pi)) ** (1.0/3.0), 1)))
else:
    print("volume = " + str(round((4.0/3.0) * pi * (value ** 3), 1)))
