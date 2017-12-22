import sys
import string

alphabet = list(string.ascii_lowercase)
alphabet.extend(list(string.ascii_uppercase))

for line in sys.stdin:
    iter_line = iter(line)
    next(iter_line)
    for x in line:
        for y in alphabet:
            if x == y:
                alphabet.remove(y.upper())
                alphabet.remove(y.lower())
    if len(alphabet) > 0:
        print "missing " + "".join(alphabet)
    else:
        print "pangram"
