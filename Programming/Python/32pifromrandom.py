import math
import random

print "Hi! Welcome to my Pi from Pseudo-Random Numbers Generator!"

while True:
    least = raw_input("Please input the smallest number the random numbers can be. ")
    try:
        limit = int(limit)
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

for x in range(amount_to_gen):
    pair = []
    pair.append(random.randint(least, limit))
    pair.append(random.randint(least, limit))
