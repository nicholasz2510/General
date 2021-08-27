from sys import stdin

index = int(stdin.readline())
primes = "2"

curr = 3
for x in range(10005):
    while True:
        is_prime = True
        for y in range(2, curr):
            if curr % y == 0:
                is_prime = False
                break
        if is_prime:
            primes += str(curr)
            curr += 1
            break
        curr += 1

print(primes[index:index + 5])
