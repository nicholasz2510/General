import time

while True:
    amount_to_gen = raw_input("Please input the amount of prime fractions you want generated. ")
    try:
        amount_to_gen = int(amount_to_gen)
    except ValueError:
        print "Uh oh... you didn't input a number. Make sure the number was whole and not a floating point."
        continue
    break

#THIS CREATES THE PRIMES, PI CREATION ON LINE 43
def gen_primes():
    d = {}

    q = 2

    while True:
        if q not in d:
            yield q
            d[q * q] = [q]
        else:
            for p in d[q]:
                d.setdefault(p + q, []).append(p)
            del d[q]

        q += 1


prime_numbers = gen_primes()

primes = set()
y = 0
a = gen_primes()
while len(primes) <= amount_to_gen:
    primes |= {a.next()}
    y += 1

#THE CODE ABOVE CREATES PRIMES
#THE CODE BELOW CREATES PI

time.clock()
print str(2.0 / (reduce(lambda factor_a, factor_b: factor_a * factor_b, [1.0 + (1.0 / prime) if (prime - 1.0) % 4.0 == 0.0 else 1.0 - (1.0 / prime) for prime in sorted(list(primes))[1:]]))) + "\nIt took " + str(time.clock()) + " seconds"
