def sum_for_loop(l):
    ans = 0
    for x in l:
        ans += x
    return ans

def sum_while_loop(l):
    ans = 0
    index = 0
    while len(l) > index:
        ans += l[index]
        index += 1
    return ans

def sum_recursion(l):
    if len(l) == 1:
        return l[0]
    i = l[0]
    l.pop(0)
    return i + sum_recursion(l)


print sum_for_loop([1, 2, 3])
print sum_for_loop([4, 5, 6])
print sum_for_loop([7, 8, 9])

print sum_while_loop([1, 2, 3])
print sum_while_loop([4, 5, 6])
print sum_while_loop([7, 8, 9])

print sum_recursion([1, 2, 3])
print sum_recursion([4, 5, 6])
print sum_recursion([7, 8, 9])
