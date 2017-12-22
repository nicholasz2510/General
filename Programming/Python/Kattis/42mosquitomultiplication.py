from sys import stdin

while True:
    nums_in = [int(x) for x in stdin.readline().split()]
    if nums_in == []:
        quit()
    mosquitoes, pupae, larvae, eggs_laid_by_one_mosquito, larvae_survival_rate, pupae_survival_rate, weeks = nums_in
    for n in range(weeks):
        
