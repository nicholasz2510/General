import time

print "Hi! Welcome to my Pi from Odd Fractions (1/1, 1/3, 1/5, 1/7...) Generator!"

while True:
    amount_to_gen = raw_input("Please input the amount of odd fractions you want generated. ")
    try:
        amount_to_gen = int(amount_to_gen)
    except ValueError:
        print "Uh oh... you didn't input a number. Make sure the number was whole and not a floating point."
        continue
    break

denominator = 1.0
answer = 0.0
time.clock()
for x in range(amount_to_gen / 2):
    answer += 1.0 / denominator
    denominator += 2.0
    answer -= 1.0 / denominator
    denominator += 2.0

print "The result for Pi was: " + str(answer * 4)
print "It took " + str(time.clock()) + " seconds"
