import time
from functools import reduce

time.clock()
max_prime = 5000
print(str(2.0 / (reduce(lambda factor_a, factor_b: factor_a * factor_b, [1.0 + (1.0 / prime) if (prime - 1.0) % 4.0 == 0.0 else 1.0 - (1.0 / prime) for prime in [n for n in range(2, max_prime) if n not in [factor_1 * factor_2 for factor_1 in range(2, n/2+1) for factor_2 in range(2, min(factor_1 + 1, n / factor_1 + 1))]][1:]]))) + "\nIt took " + str(time.clock()) + " seconds")
