from sys import stdin

n_times = int(stdin.readline())
intervals = []
for x in range(n_times):
    intervals.append([int(n) for n in stdin.readline().split()])

possibilities = range(intervals[0][0], intervals[0][1] + 1)
for i in intervals[1:]:
    if (i[1] < possibilities[0] or i[0] > possibilities[len(possibilities) - 1]):
        print "edward is right"
        quit()
    for ps in possibilities:
        if not ps > i[0] and ps < i[1]:
            possibilities.remove(ps)
print "gunilla has a point"
