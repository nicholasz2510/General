from sys import stdin

h, w, n = [int(x) for x in stdin.readline().split()]
bricks = [int(x) for x in stdin.readline().split()]

height = 0
width = 0

for b in bricks:
    if width < w and height < h:
        width += b
    if width == w:
        height += 1
        width = 0
    if width > w:
        print "NO"
        quit()

print "YES"
