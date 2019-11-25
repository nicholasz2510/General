days_since_january_first_nineteen_hundred = 10

this_day = [((days_since_january_first_nineteen_hundred % 7) + 3) - 7 if (days_since_january_first_nineteen_hundred % 7) + 3 > 7 else (days_since_january_first_nineteen_hundred % 7) + 3][0]

print this_day