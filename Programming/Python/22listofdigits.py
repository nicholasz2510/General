def flip(list_to_flip):
    max_index = (len(list_to_flip) - 1)
    for x in range(max_index, -1, -1):
        list_to_flip.append(list_to_flip[x])
    for x in range(0, (max_index + 1)):
        list_to_flip.remove(list_to_flip[x])


def find_digits(number):
    num = str(number)
    digits = []
    for digit in num:
        digits.append(int(digit))
    return digits


def find_digits_mod_10(num):
    number = num
    digits = []
    if num == 0:
        digits.append(num)
    while number != 0:
        digits.append(number % 10)
        number -= number % 10
        number /= 10
    flip(digits)
    return digits


print find_digits(888999904)
print find_digits(0)
print find_digits(987095)

print find_digits_mod_10(888999904)
print find_digits_mod_10(0)
print find_digits_mod_10(987095)
