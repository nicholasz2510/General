n = int(raw_input("What would you like to use for n? "))

for x in range(1, n+1):
    if x % 3 == 0 or x % 5 == 0:
        print x,
