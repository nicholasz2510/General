def count_factors(n):
    ans = 0
    for num in range(1, n + 1):
        if n % num == 0:
            ans += 1
    return ans


def count_whitespace(s):
    ans = 0
    for c in s:
        if c.isspace():
            ans += 1
    return ans


def average_token_length(s):
    if len(s) == 0:
        return 0
    total_str_len = 0
    for string in s:
        total_str_len += len(string)
    return float(total_str_len) / float(len(s))


def contains_token(s, t):
    for x in s.split():
        if x == t:
            return True
    return False


def find_line_with_token(s, t):
    for x in s:
        if contains_token(x, t):
            return x
    return None


def is_palindrome(s):
    reverse = ""
    for x in range(len(s) - 1, -1, -1):
        reverse += s[x]
    return reverse == s


def find_smallest_factor(n):
    for num in range(2, n + 1):
        if n % num == 0:
            return num


def find_longest_palindrome(s):
    longest = ""
    there_is_pal = False
    for x in s:
        for y in x.split():
            if is_palindrome(y) and len(y) >= len(longest):
                longest = y
                there_is_pal = True
    if there_is_pal:
        return longest
    return None


def find_longest_line(s):
    longest = ""
    there_is_longer = False
    for x in s:
        if len(x) > len(longest):
            longest = x
            there_is_longer = True
    if there_is_longer:
        return longest
    return None


def find_most_whitespace(s):
    most_whitespace = ""
    there_is_more = False
    for x in s:
        if count_whitespace(x) > count_whitespace(most_whitespace):
            most_whitespace = x
            there_is_more = True
    if there_is_more:
        return most_whitespace
    return None


print count_factors(1)
print count_factors(6)
print count_factors(11)
print count_factors(30)
print
print count_whitespace("")
print count_whitespace("xyz")
print count_whitespace("one two  three   four    ")
print count_whitespace("one\ttwo\n\nthree   four\n\t")
print
print average_token_length([])
print average_token_length(["one", "two", "three"])
print
print contains_token("", "xyz")
print contains_token("xyz", "xyz")
print contains_token("xyx xyy xyz xya", "xyz")
print contains_token("xyx xyy xyZ xya", "xyz")
print
print find_line_with_token([], "hello")
print find_line_with_token(["hello world"], "world")
print find_line_with_token(["hello world"], "abc")
print find_line_with_token(["hello world", "this is a test", "this is another test"], "a")
print
print find_smallest_factor(17)
print find_smallest_factor(2)
print find_smallest_factor(169)
print
print is_palindrome("")
print is_palindrome("z")
print is_palindrome("xy")
print is_palindrome("abcddcba")
print is_palindrome("abcddbba")
print is_palindrome("abcdedcba")
print is_palindrome("abcdedbba")
print
print find_longest_palindrome([""])
print find_longest_palindrome(["I did something wrong"])
print find_longest_palindrome(["This is an apple"])
print find_longest_palindrome(["a bb xyz", "I heard a peep sis"])
print
print find_longest_line([""])
print find_longest_line(["hello"])
print find_longest_line(["Hello", "This is a test", "Goodbye"])
print
print find_most_whitespace([""])
print find_most_whitespace(["a b c"])
print find_most_whitespace(["a bb", "a bb\t\t", "xyz"])
