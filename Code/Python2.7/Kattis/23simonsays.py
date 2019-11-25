import sys

sentences = []

for x in range(int(sys.stdin.readline())):
    sentences.append(sys.stdin.readline())

for s in sentences:
    if s[:10] == "Simon says":
        print s[10:(len(s) - 1)]
