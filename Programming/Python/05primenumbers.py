def num_of_prime(range_start, range_stop):
    prime_numbers = []
    for num in range(range_start, range_stop):
        not_prime = False
        for x in range(2, num):
            if num % x == 0:
                not_prime = True
        if not not_prime:
            prime_numbers.append(num)
    print len(prime_numbers)
    print prime_numbers

num_of_prime(2, 100)
num_of_prime(100, 200)
num_of_prime(200, 300)
num_of_prime(300, 400)
num_of_prime(400, 500)
num_of_prime(500, 600)
num_of_prime(600, 700)
num_of_prime(700, 800)
num_of_prime(800, 900)
num_of_prime(900, 1000)
