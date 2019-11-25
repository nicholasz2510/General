import sys

gunnar = sys.stdin.readline().split()
emma = sys.stdin.readline().split()
gunnar_score = 0
emma_score = 0

for num in gunnar:
    gunnar_score += int(num)

for num in emma:
    emma_score += int(num)

if gunnar_score > emma_score:
    print "Gunnar"
elif emma_score > gunnar_score:
    print "Emma"
else:
    print "Tie"
