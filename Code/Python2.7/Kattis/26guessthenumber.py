guess = 500
pre_2_guess = 0
pre_guess = 0
print guess

for x in range(10):
    if raw_input("guess ")[:5] == "lower":
        print guess - (guess / 2)
        guess /= 2
    if raw_input("guess ")[:6] == "higher":
        print guess + (guess / 2)
        guess /= 2
    if raw_input("guess ")[:7] == "correct":
        break

quit()
