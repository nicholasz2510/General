from sys import stdin

for tc in range(int(stdin.readline())):
    sounds = stdin.readline().split()
    descriptions = set()
    fox_sound = ""
    while True:
        line = stdin.readline()
        if line == "what does the fox say?\n":
            break
        descriptions.add(line.split()[2])
    for s in sounds:
        if s not in descriptions:
            fox_sound += s if fox_sound == "" else " " + s
    print fox_sound
