"""
ID: nichola64
LANG: PYTHON2
PROG: beads
"""
fin = open('beads.in', 'r')
fout = open('beads.out', 'w')

num_of_beads = int(fin.readline())
beads = fin.readline()

already_found_first = False
on_first = True
largest = 0
current = 0
first = None


def is_first_bead(b, aff):
    return b != 'w' and not aff


for s_bead in range(num_of_beads):
    for bead_index in range(s_bead, num_of_beads + s_bead):
        bead = beads[bead_index % num_of_beads]
        if is_first_bead(bead, already_found_first):
            already_found_first = True
            first = bead
            if first == 'r':
                second = 'b'
            else:
                second = 'r'
        elif bead != first and on_first and bead != 'w':
            on_first = False
        elif bead == first and not on_first:
            break
        current += 1
    largest = max(largest, current)
    current = 0
    already_found_first = False
    on_first = True
    first = None

fout.write(str(largest) + "\n")

fout.close()
