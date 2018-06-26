from sys import stdin

variables = {}

def compare(one, comparer, two):
    if comparer == "=":
        return one == two
    if comparer == "<":
        return one < two
    if comparer == ">":
        return one > two

commands = stdin.readlines()

for c in commands:
    command = c.split()
    if command[0] == "define":
        variables[command[2]] = int(command[1])
        # print "Yay, defining works"
    if command[0] == "eval":
        one = command[1]
        two = command[3]
        if not (variables.has_key(one) and variables.has_key(two)):
            print "undefined"
            continue
        one = variables[one]
        two = variables[two]
        comparer = command[2]
        print str(compare(one, comparer, two)).lower()
