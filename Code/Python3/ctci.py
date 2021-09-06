from collections import Counter


# CODE LIBRARY
class LinkedListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


# SOLUTIONS
def is_unique(string):
    return len(set(string)) == len(string)


def check_permutation(str_1, str_2):
    if len(str_1) != len(str_2):
        return False

    counter = Counter()
    for char in str_1:
        counter[char] += 1
    for char in str_2:
        if counter[char] == 0:
            return False
        counter[char] -= 1

    return True


def urlify(string, n):
    string_list = list(string)
    index = len(string_list)

    for i in range(n - 1, -1, -1):
        if string_list[i] == " ":
            string_list[index - 3:index] = "%20"
            index -= 3
        else:
            string_list[index - 1] = index[i]
            index -= 1
    return "".join(string_list[index:])


def palindrome_permutation(string):
    counter = set()

    for char in string:
        if char in counter:
            counter.remove(char)
        else:
            counter.add(char)

    if len(counter) > 1:
        return False

    return True


def remove_dups(head)
    visited = set()
    curr = head
    prev = None
    while curr is not None:
        if curr.value in visited:
            prev.next = curr.next
        else:
            set.add(curr.value)
            prev = curr
        curr = curr.next

    return head

def kth_to_last(head, k):
    if head is None:
        return 0

    n_from_last = kth_to_last(head.next, k) + 1
    if n_from_last == k:
        print(head.value)

    return n_from_last
