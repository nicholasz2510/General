import sys

for first_line in sys.stdin:
    split_list = first_line.split()
    x = int(split_list[0])
    y = int(split_list[1])
    n = int(split_list[2])

for num in range(1, n+1):
    if num % x == 0 and num % y == 0:
        print "FizzBuzz"
    elif num % x == 0:
        print "Fizz"
    elif num % y == 0:
        print "Buzz"
    else:
        print num
