import sys

answer = 0

num_of_lines = sys.stdin.readline()

for l in range(int(num_of_lines)):
    line = str(int(sys.stdin.readline()))
    num = int(line[:len(line) - 1])
    exponent = int(line[len(line) - 1])
    answer += num ** exponent

print answer
