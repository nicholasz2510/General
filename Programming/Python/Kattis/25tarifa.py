from sys import stdin

mb_per_month = int(stdin.readline())
n_of_months = int(stdin.readline())
current_num_of_mb = mb_per_month

for n in range(n_of_months):
    current_num_of_mb = (current_num_of_mb - int(stdin.readline())) + mb_per_month

print current_num_of_mb
