from sys import stdin

for tc in range(int(stdin.readline())):
    places = []
    for l in range(int(stdin.readline())):
        p = stdin.readline()
        if p not in places:
            places.append(stdin.readline())
    print len(places)
