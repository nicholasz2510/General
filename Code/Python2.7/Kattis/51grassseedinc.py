from sys import stdin

one_metre_cost = float(stdin.readline())
num_lawns = int(stdin.readline())
total = 0.0

for i in range(num_lawns):
    curr_lawn = [float(x) for x in stdin.readline().split()]
    total_curr = (curr_lawn[0] * curr_lawn[1]) * one_metre_cost
    total += total_curr

print str("%.7f" % total)
