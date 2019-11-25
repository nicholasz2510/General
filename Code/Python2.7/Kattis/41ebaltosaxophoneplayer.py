from sys import stdin

notes_to_buttons = {"c": {2, 4, 7, 10}, "d": {2, 4, 7, 9}, "e": {2, 4, 7, 8}, "f": {2, 4, 7}, "g": {2, 4}, "a": {2, 3},
                    "b": {2}, "C": {3}, "D": {1, 4, 7, 9}, "E": {1, 4, 7, 8}, "F": {1, 4, 7}, "G": {1, 4}, "A": {1, 3},
                    "B": {1, 2}}

for n in range(int(stdin.readline())):
    times_fingers_pressed = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
    song = stdin.readline().strip("\n")
    pre_fingers = set()
    for note in song:
        fingers = notes_to_buttons[note]
        for f in fingers:
            if f not in pre_fingers:
                times_fingers_pressed[f] += 1
        pre_fingers = notes_to_buttons[note]
    print_this = ""
    for x in range(10):
        print_this += str(times_fingers_pressed[x + 1]) + " "
    print print_this[:- 1]
    # print times_fingers_pressed
