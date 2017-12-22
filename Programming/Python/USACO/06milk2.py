"""
ID: nichola64
LANG: PYTHON2
PROG: milk2
"""
fin = open('milk2.in', 'r')
fout = open('milk2.out', 'w')

original = []

for x in range(int(fin.readline())):
    original.append([int(n) for n in fin.readline().split()])

still_changing = True
new = []
find_start = True
start = 0
end = 0

while still_changing:
    for x in original:
        if find_start:
            start = x[0]
            find_start = False
            end = x[1]
        elif not find_start:
            end = x[1] if x[1] > end else end
            find_start = True
            new.append([start, end])
    original = new
    new = []


print new

fout.close()
