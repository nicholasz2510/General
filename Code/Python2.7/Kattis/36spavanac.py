from sys import stdin

normal_hour, normal_minute = [int(n) for n in stdin.readline().split()]
ans_hour = normal_hour
ans_minute = normal_minute

ans_minute -= 45
if ans_minute < 0:
    if ans_hour == 0:
        ans_hour = 23
    else:
        ans_hour -= 1
    ans_minute = 60 + ans_minute

print str(ans_hour) + ' ' + str(ans_minute)
