"""
ID: nichola64
LANG: PYTHON2
PROG: gift1
"""
fin = open('gift1.in', 'r')
fout = open('gift1.out', 'w')

names = []
for name_index in range(int(fin.readline().strip("\n"))):
    names.append(fin.readline().strip("\n"))

names_to_numbers = {}
for name in names:
    names_to_numbers[name] = 0

while True:
    giver = fin.readline().strip("\n")
    if len(giver) == 0:
        break
    amount, number_of_receivers = [int(x) for x in fin.readline().strip("\n").split()]
    if not number_of_receivers == 0:
        amount_given_per_receiver = int(float(amount) / float(number_of_receivers))
        receivers = []
        for x in range(number_of_receivers):
            receivers.append(fin.readline().strip("\n"))
        for receiver in receivers:
            names_to_numbers[receiver] += amount_given_per_receiver
        names_to_numbers[giver] -= amount_given_per_receiver * number_of_receivers

for name in names:
    fout.write(name + " " + str(names_to_numbers[name]) + "\n")

fout.close()
