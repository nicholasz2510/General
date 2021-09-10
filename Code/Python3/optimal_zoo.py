from collections import Counter

animals = ["lion", "giraffe", "camel", "seal", "cheetah", "cow", "monkey", "asian elephant", "african elephant",
           "reptile house", "hammerhead shark", "kangaroo", "tiger", "house of birds"]

values = [
    [1.5, 12.0, 4],
    [1.0, 4.0, 3],
    [0.5, 3.0, 2],
    [0.5, 3.0, 3],
    [1.0, 12.0, 1],
    [1.0 / 3.0, 1.0, 3],
    [0.5, 6.0, 4],
    [1.0, 8.0, 2],
    [3.0, 21.0, 3],
    [3.0, 30.0, 1],
    [0.5, 6.0, 3],
    [0.5, 2.5, 3],
    [1.0, 13.0, 2],
    [5.0, 30.0, 2]
]

varc_per_acre = {}
for animal in range(len(animals)):
    varc_per_acre[animals[animal]] = values[animal][1] / values[animal][0]

total_varc = 0.0
acres_used = 0.0
counts = Counter()

while acres_used < 30:
    curr_animal = max(animals, key=varc_per_acre.get)

    unit_acres = values[animals.index(curr_animal)][0]
    unit_varc = values[animals.index(curr_animal)][1]
    num_to_add = values[animals.index(curr_animal)][2]
    while unit_acres * num_to_add > 30.0 - acres_used:
        num_to_add -= 1

    counts[curr_animal] += num_to_add
    total_varc += unit_varc * num_to_add
    acres_used += unit_acres * num_to_add

    values[animals.index(curr_animal)][2] = 1
    values[animals.index(curr_animal)][1] /= 2
    varc_per_acre[curr_animal] = values[animals.index(curr_animal)][1] / values[animals.index(curr_animal)][0]

for curr_animal in animals:
    print(curr_animal + ": " + str(counts[curr_animal]))
print("\nTotal VARC: " + str(total_varc))
print("Total acreage: " + str(acres_used))
