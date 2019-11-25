from sys import stdin

possibilities = [0, 11]

while True:
    line = stdin.readline().strip()
    if line == "0":
        break
    num = int(line)
    line = stdin.readline().strip()
    if line == "too high":
        if possibilities[1] > num:
            possibilities[1] = num
    if line == "too low":
        if possibilities[0] < num:
            possibilities[0] = num
    if line == "right on":
        if num > possibilities[0] and num < possibilities[1]:
            print "Stan may be honest"
        else:
            print "Stan is dishonest"
        possibilities = [0, 11]
