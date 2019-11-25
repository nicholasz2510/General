from math import sqrt
import time

print "Hi! Welcome to my Pi from Squared Fractions (1/1, 1/4, 1/9, 1/16...) Generator!"

while True:
    amount_to_gen = raw_input("Please input the amount of squared fractions you want generated. ")
    try:
        amount_to_gen = int(amount_to_gen)
    except ValueError:
        print "Uh oh... you didn't input a number. Make sure the number was whole and not a floating point."
        continue
    break

denominator = 1.0
answer = 0.0
time.clock()
for x in range(amount_to_gen):
    answer += 1.0 / (denominator ** 2.0)
    denominator += 1

print "The result for Pi was: " + str(sqrt(answer * 6))
print "It took " + str(time.clock()) + " seconds"
