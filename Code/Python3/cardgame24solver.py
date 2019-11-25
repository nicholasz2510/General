possible_values = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12,
                   "K": 13}


def valid_value(which_card):
    card = input("What is the value of your " + which_card + " card? (type a number, A, J, Q, or K)")
    while True:
        if card not in possible_values.keys():
            card = input(
                "Sorry, try that again. What is the value of your " + which_card + " card? (type a number, A, J, Q, or K)")
        else:
            return possible_values[card]


def cards_unique(shuffled):
    if not len(shuffled) > len(set(shuffled)):
        return shuffled


print("Welcome to Nick's 24 (the card game) cheat!")
card_1 = valid_value("first")
card_2 = valid_value("second")
card_3 = valid_value("third")
card_4 = valid_value("fourth")

cards = [card_1, card_2, card_3, card_4]
permutations = []

for first_card in cards:
    for second_card in cards:
        for third_card in cards:
            for fourth_card in cards:
                curr_shuffled = cards_unique([first_card, second_card, third_card, fourth_card])
                if curr_shuffled is not None:
                    permutations.append(curr_shuffled)

operands = []

print(permutations)
