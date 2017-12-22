import sys

ans = 0

for line in sys.stdin:
    list_of_str_temps = line.split()

list_of_str_temps = map(int, list_of_str_temps)

for x in list_of_str_temps:
    if x < 0:
        ans += 1

print ans
