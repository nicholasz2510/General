from math import sqrt
from fractions import gcd
from random import randint
import time


def is_coprime(a, b):
    return gcd(a, b) == 1


print "Hi! Welcome to my Pi from Pseudo-Random Numbers Generator!"

while True:
    least = raw_input("Please input the smallest number the random numbers can be. ")
    try:
        least = int(least)
    except ValueError:
        print "Uh oh... you didn't input a number. Make sure the number was whole and not a floating point."
        continue
    break

while True:
    limit = raw_input("Please input the largest number the random numbers can be. ")
    try:
        limit = int(limit)
    except ValueError:
        print "Uh oh... you didn't input a number. Make sure the number was whole and not a floating point."
        continue
    break

while True:
    amount_to_gen = raw_input("Please input the amount of PAIRS of numbers you want generated. ")
    try:
        amount_to_gen = int(amount_to_gen)
    except ValueError:
        print "Uh oh... you didn't input a number. Make sure the number was whole and not a floating point."
        continue
    break

coprime = 0
cofactor = 0

time.clock()

for x in range(amount_to_gen):
    a = randint(least, limit)
    b = randint(least, limit)
    if is_coprime(a, b):
        coprime += 1
        continue
    cofactor += 1

print "My result for finding Pi was : " + str(sqrt(6 / (float(coprime) / amount_to_gen)))
print "It took " + str(time.clock()) + " seconds"
