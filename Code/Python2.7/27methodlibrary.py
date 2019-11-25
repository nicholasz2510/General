def is_capitalized(word):
    return word[0].upper() == word[0] and word[0].isalpha()

def capitalize(word):
    return word[0].upper() + word[1:len(word)]

def get_life_stage(age):
    if age < 2:
        return "baby"
    elif age >= 2 and age <= 12:
        return "child"
    elif age >= 13 and age <= 17:
        return "teen"
    elif age >= 18 and age <= 64:
        return "adult"
    else:
        return "senior"

def is_vowel(c):
    return c in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

def first_vowel_index(s):
    if len([False for x in s if x not in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']]) == len(s):
        return -1
    return [x for x in range(len(s)) if s[x] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']][0]

def to_pig_latin(s):
    if len([False for x in s if x not in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']]) == len(s):
        return s
    elif s[0] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
        return s + "way"
    else:
        return s[first_vowel_index(s):len(s)] + s[:first_vowel_index(s)] + "ay"

def convert_to_pig_latin(words):
    final_words = ""
    for x in words.split():
        final_words += to_pig_latin(x) + " "
    return final_words

def make_line(edge, inner, width):
    return edge + (inner * (width - 2)) + edge

def make_rectangle(height, width):
    return make_line('+', '-', width) + (("\n" + "|" + (" " * (width - 2)) + "|") * (height - 2)) + "\n" + make_line('+', '-', width)

def next_hailstone(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1

def hailstones(n):
    hail = str(n) + " "
    pre = next_hailstone(n)
    while pre != 1:
        hail += str(pre) + " "
        pre = next_hailstone(pre)
    if hail != "1 ":
        hail += "1 "
    return hail

def count_tokens(words):
    return len(words.split())


print "is_capitalized:"
print is_capitalized("Hello"); print is_capitalized("hello"); print is_capitalized("0"); print is_capitalized("X")
print
print "capitalize:"
print capitalize("x"); print capitalize("hello"); print capitalize("hElLo"); print capitalize("123ab")
print
print "get_life_stage:"
print get_life_stage(0); print get_life_stage(1); print get_life_stage(2); print get_life_stage(10); print get_life_stage(13); print get_life_stage(16); print get_life_stage(21); print get_life_stage(60); print get_life_stage(70); print get_life_stage(80)
print
print "is_vowel:"
print is_vowel('a'); print is_vowel('e'); print is_vowel('i'); print is_vowel('o'); print is_vowel('u'); print is_vowel('A'); print is_vowel('E'); print is_vowel('I'); print is_vowel('O'); print is_vowel('U'); print is_vowel('x'); print is_vowel('h')
print
print "to_pig_latin:"
print to_pig_latin("slick"); print to_pig_latin("SLICK"); print to_pig_latin("strong"); print to_pig_latin("STRONG"); print to_pig_latin("xyzzy"); print to_pig_latin("orange")
print
print "convert_to_pig_latin:"
print convert_to_pig_latin("this is a test"); print convert_to_pig_latin("    this     is     a         test"); print convert_to_pig_latin(""); print convert_to_pig_latin("           "); print convert_to_pig_latin("The rain in Spain falls mainly in the plain")
print
print "make_rectangle:"
print make_rectangle(2, 2); print make_rectangle(3, 3); print make_rectangle(5, 4)
print
print "next_hailstone:"
print next_hailstone(1); print next_hailstone(5); print next_hailstone(33); print next_hailstone(2); print next_hailstone(16); print next_hailstone(2000000)
print
print "hailstones:"
print hailstones(1); print hailstones(16); print hailstones(7)
print
print "count_tokens:"
print count_tokens(""); print count_tokens("a b c"); print count_tokens("a b c d"); print count_tokens("The rain in Spain falls mainly in the plain")
