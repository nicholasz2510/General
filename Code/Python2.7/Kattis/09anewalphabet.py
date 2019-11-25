import sys

ans = ""
convert = {"a": "@", "b": "8", "c": "(", "d": "|)", "e": "3", "f": "#", "g": "6", "h": "[-]", "i": "|", "j": "_|", "k": "|<", "l": "1", "m": "[]\/[]", "n": "[]\[]", "o": "0", "p": "|D", "q": "(,)", "r": "|Z", "s": "$", "t": "']['", "u": "|_|", "v": "\/", "w": "\/\/", "x": "}{", "y": "`/", "z": "2"}

for char in sys.stdin.readline():
    if char.isalpha():
        ans += convert[char.lower()]
    else:
        ans += char

print ans
