from sys import stdin

for t in range(int(stdin.readline())):
    grades = [int(x) for x in stdin.readline().split()]
    students = grades[0]
    grades = grades[1:]
    total = 0
    over_average = 0
    for g in grades:
        total += g
    average = float(total) / float(students)
    for g in grades:
        if float(g) > average:
            over_average += 1
    print format(round(float(over_average) / float(students) * 100, 3), '.3f') + "%"
