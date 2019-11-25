import sys

shifts = int(sys.stdin[0])
file_ = sys.stdin[1]
overwritten = sys.stdin[2]
checker = []

for icmfcr in shifts:
    for i in file_:
        if i == "1":
            checker.append("0")
        elif i == "0":
            checker.append("1")

if str(checker) == overwritten:
    print "Deletion succeeded"
else:
    print "Deletion failed"
