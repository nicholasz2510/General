import sys

positions = ["President", "Vice President", "Secretary", "Treasurer", "Reporter", "Sergeant-at-Arms"]

num_bal = int(sys.stdin.readline())

ballots = []

for x in range(num_bal):
    ballots.append(sys.stdin.readline().split())

votes = [{}, {}, {}, {}, {}, {}]

for ballot in ballots:
    for x in range(len(positions)):
        if ballot[x] in votes[x].keys():
            votes[x][ballot[x]] += 1
        else:
            votes[x][ballot[x]] = 1

# print(votes)

winners_all = []
nums_votes = []

for pos in votes:
    max_num = max(pos.values())
    winners = []
    for contestant in pos:
        if pos[contestant] == max_num:
            winners.append(contestant)
    winners_all.append(sorted(winners))
    nums_votes.append(max_num)

for x in range(len(positions)):
    tied = len(winners_all[x]) > 1
    print(positions[x] + ": " + ("-tie- " if tied else "") + " ".join(winners_all[x]) + ", " + str(nums_votes[x]))
