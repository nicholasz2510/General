from sys import stdin

words = sorted(stdin.readline().split())
prev = ""
for word in words:
    if word == prev:
        print "no"
        quit()
    else:
        prev = word
print "yes"