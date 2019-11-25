check_this = int(raw_input("Input your number to to check for primeness. This number must be larger than 1. "))
#check_this = 1

for x in range(2, check_this):
    if check_this % x == 0:
        print "The number is not prime"
        quit()
print "The number is prime"
