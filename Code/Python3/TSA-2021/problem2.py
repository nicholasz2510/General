import sys

phrase = sys.stdin.readline().strip()
replace_this = sys.stdin.readline().strip()
replace_with = sys.stdin.readline().strip()

if replace_this == "":
    print(phrase)
else:
    print(phrase.replace(replace_this, replace_with))
