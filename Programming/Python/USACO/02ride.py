"""
ID: nichola64
LANG: PYTHON2
PROG: ride
"""
fin = open('ride.in', 'r')
fout = open('ride.out', 'w')


letters_to_numbers = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12,
                      "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22, "W": 23,
                      "X": 24, "Y": 25, "Z": 26}

first_str = fin.readline().strip("\n")
second_str = fin.readline().strip("\n")
str_one_num = 1
str_two_num = 1

for c in first_str:
    str_one_num *= letters_to_numbers[c]

for c in second_str:
    str_two_num *= letters_to_numbers[c]

if str_one_num % 47 == str_two_num % 47:
    fout.write("GO\n")
else:
    fout.write("STAY\n")

fout.close()
