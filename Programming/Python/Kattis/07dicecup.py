import sys

line1 = sys.stdin.readline()

dice1 = int(line1.split()[0])
dice2 = int(line1.split()[1])


"""
outputs = []

for x in range(1, dice1 + 1):
    for y in range(1, dice2 + 1):
        outputs.append(x + y)

output_counter = {}
for o in outputs:
    if o in output_counter:
        output_counter[o] += 1
    else:
        output_counter[o] = 1
"""
most_times = 0
for x in output_counter:
    if output_counter[x] > most_times:
        most_times = output_counter[x]
for x in output_counter:
    if output_counter[x] == most_times:
        print x
