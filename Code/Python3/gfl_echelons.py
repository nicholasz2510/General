from itertools import permutations

cell_to_cardinal = {1: (-1, -1), 2: (0, -1), 3: (1, -1), 4: (-1, 0), 5: (1, 0), 6: (-1, 1), 7: (0, 1), 8: (1, 1)}

num_girls = 5
girls = []
print("For each cell that each girl buffs, type the number of the "
      "cell. (Example: 23578)\n"
      "[1] [2] [3]\n"
      "[4] [ ] [5]\n"
      "[6] [7] [8]\n"
      "Press [Enter] when at the end of each girl's buffs.\n")
for girl_num in range(num_girls):
    cells = input("For Girl #" + str(girl_num + 1) + ":\n")
    curr_girl_cells = []
    for cell in cells.strip():
        curr_girl_cells.append(cell_to_cardinal[int(cell)])
    girls.append(curr_girl_cells)

# print(girls)

slots = []


def gen_slots(curr):
    if len(curr) == num_girls + 1:
        slots.append(set(curr[1:]))
        return
    elif curr[-1] == 9:
        return
    for x in range(curr[-1] + 1, 10):
        gen_slots(curr + [x])


gen_slots([0])
permutes = list(permutations(range(num_girls)))

combos = []
for slot in slots:
    for permute in permutes:
        combo = [[5] * 3] + [[5] * 3] + [[5] * 3]
        curr_permute_i = 0
        for row in range(3):
            for col in range(3):
                if row * 3 + col + 1 in slot and curr_permute_i < 5:
                    combo[row][col] = permute[curr_permute_i]
                    curr_permute_i += 1
        combos.append(combo)

max_buffs = 0
max_combo = combos[0]
for combo in combos:
    buffs = 0
    for row in range(3):
        for col in range(3):
            if combo[row][col] < 5:
                for card in girls[combo[row][col]]:
                    if 0 <= col + card[0] < 3 and 0 <= row + card[1] < 3 and \
                            combo[row + card[1]][col + card[0]] is not None:
                        buffs += 1
    if buffs > max_buffs:
        max_buffs = buffs
        max_combo = combo

ans = ""
for row in max_combo:
    for cell in row:
        ans += "[" + str(cell + 1).replace("6", " ") + "] "
    ans += "\n"
print("\n\nOptimal placement:\n" + ans)
