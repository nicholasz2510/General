import random

num_of_guesses = 0

random_num_start = int(raw_input("What would you like to be the start of the range of where the number can be? Example: 1 "))
random_num_end = int(raw_input("What would you like to be the end of the range of where the number can be? Example: 10 "))
total_guesses = int(raw_input("How many guesses would you like? "))

num = random.randint(random_num_start, random_num_end)
num_is_correct = False

while not num_is_correct and num_of_guesses < total_guesses:
    guess_num = int(raw_input("What is your guess? "))
    if guess_num == num:
        print "You got my number! Congrats! "
        quit()
    elif guess_num < num:
        print "Your number was too small."
        num_of_guesses += 1
    elif guess_num > num:
        print "Your number was too large."
        num_of_guesses += 1

print "Oh no! You ran out of guesses! The number was "+str(num)+"!"
