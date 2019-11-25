from sys import stdin

votes = []

curr_line = stdin.readline()
while curr_line != "***":
    votes.append(curr_line)
    curr_line = stdin.readline()

nums_of_votes = {}
for vote in votes:
    if vote not in nums_of_votes.keys():
        nums_of_votes[vote] = 1
        continue
    nums_of_votes[vote] += 1

print nums_of_votes
