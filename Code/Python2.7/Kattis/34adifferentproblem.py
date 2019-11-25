from sys import stdin

while True:
    line = [int(n) for n in stdin.readline().split()]
    if line != []:
        if line[0] > line[1]:
            print line[0] - line[1]
        else:
            print line[1] - line[0]
    else:
        break
