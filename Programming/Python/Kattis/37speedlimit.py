from sys import stdin

while True:
    line = stdin.readline()
    if int(line) != -1:
        l_of_lines_in_sec = []
        total_miles = 0
        for x in range(int(line)):
            l_of_lines_in_sec.append([int(n) for n in stdin.readline().split()])
        hours_elapsed = 0
        for l in l_of_lines_in_sec:
            total_miles += l[0] * (l[1] - hours_elapsed)
            hours_elapsed = l[1]
        print str(total_miles) + " miles"
    else:
        break
