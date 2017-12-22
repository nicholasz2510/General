input_1 = ["Hello", "World", "in", "a", "frame"]
input_2 = []
input_3 = ["", ""]
input_4 = [""]
input_5 = ["b-day"]


def in_frame(l):
    top_bottom_frame = ""
    largest = ""
    for x in l:
        if len(x) > len(largest):
            largest = x
    for x in range(len(largest) + 2):
        top_bottom_frame += "*"
    print top_bottom_frame
    for x in l:
        for y in range(len(largest) - len(x)):
            x += " "
        print "*" + x + "*"
    print top_bottom_frame


in_frame(input_1)
print ""
in_frame(input_2)
print ""
in_frame(input_3)
print ""
in_frame(input_4)
print ""
in_frame(input_5)
