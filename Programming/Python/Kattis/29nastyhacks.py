from sys import stdin

for n in range(int(stdin.readline())):
    list_of_revenues = [int(i) for i in stdin.readline().split()]
    if list_of_revenues[0] < (list_of_revenues[1] - list_of_revenues[2]):
        print "advertise"
    if list_of_revenues[0] > (list_of_revenues[1] - list_of_revenues[2]):
        print "do not advertise"
    if list_of_revenues[0] == (list_of_revenues[1] - list_of_revenues[2]):
        print "does not matter"
