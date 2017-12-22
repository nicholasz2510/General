from sys import stdin

for x in range(int(stdin.readline())):
    num = int(stdin.readline())
    if num % 2 == 0:
        print str(num) + " is even"
    else:
        print str(num) + " is odd"

quit()
