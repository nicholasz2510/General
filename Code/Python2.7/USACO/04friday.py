"""
ID: nichola64
LANG: PYTHON2
PROG: friday
"""
fin = open('friday.in')
fout = open('friday.out', 'w')

years = int(fin.readline())
delta = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30,
         12: 31}
current_year = 1900
thirteenths = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}
days_since_start = 0


def is_leap_year(m, y):
    if m != 3:
        return False
    if y % 400 == 0:
        return True
    if y % 100 == 0:
        return False
    if y % 4 == 0:
        return True
    return False


def days_to_add(m):
    if m == 1:
        return delta[12]
    else:
        return delta[m - 1]


if years == 0:
    print "0 0 0 0 0 0 0"
    quit()

for year in range(1900, 1900 + years):
    for month in range(1, 13):
        if not is_leap_year(month, year):
            if days_since_start == 0:
                days_since_start += 12
                thirteenths[1] += 1
                continue
            days_since_start += days_to_add(month)
            weekday = (days_since_start % 7) + 3
            this_day = weekday - 7 if weekday > 7 else weekday
            thirteenths[this_day] += 1
            continue
        days_since_start += 29
        weekday = (days_since_start % 7) + 3
        this_day = weekday - 7 if weekday > 7 else weekday
        thirteenths[this_day] += 1

for x in range(1, 8):
    fout.write(str(thirteenths[x]))
    if x != 7:
        fout.write(" ")
    else:
        fout.write("\n")

fout.close()
