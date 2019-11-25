from sys import stdin

input_string = stdin.readline()
input_string = input_string[0:len(input_string) - 1]
answer = []

for x in input_string:
    if x == "<":
        answer.pop(len(answer) - 1)
    else:
        answer.append(x)

print "".join(answer)
