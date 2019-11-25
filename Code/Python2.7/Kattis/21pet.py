import sys

points = [[int(x) for x in sys.stdin.readline().split()], [int(x) for x in sys.stdin.readline().split()],
          [int(x) for x in sys.stdin.readline().split()], [int(x) for x in sys.stdin.readline().split()],
          [int(x) for x in sys.stdin.readline().split()]]
scores = []

for p in points:
    scores.append(p[0] + p[1] + p[2] + p[3])

winner_score = max(scores)

print str(scores.index(winner_score) + 1) + " " + str(winner_score)
