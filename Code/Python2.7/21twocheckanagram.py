def isAnagram(l1, l2):
    list_1 = []
    for x in l1:
        list_1.append(x)
    for x in l1:
        if l2.__contains__(x):
            list_1.remove(x)
            l2.remove(x)
    return not (len(list_1) > 0 or len(l2) > 0)

def sortedAnagrams(s1, s2):
    if len(s1) != len(s2):
        return False
    if len(s1) == 0 and len(s2) == 0:
        return True
    l1 = sorted(s1)
    l2 = sorted(s2)
    ans = False
    for x in range(0, len(s1)):
        ans = l1[x] == l2[x]
        if ans == False:
            return False
    return ans


print isAnagram([1, 2, 3], [1, 2, 3])
print isAnagram([4493, 47837843, "574"], [8433, 9394.27891])
print isAnagram([], [])
print isAnagram([9, 7], [])
print isAnagram([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1])

print sortedAnagrams([1, 2, 3], [1, 2, 3])
print sortedAnagrams([4493, 47837843, "574"], [8433, 9394.27891])
print sortedAnagrams([], [])
print sortedAnagrams([9, 7], [])
print sortedAnagrams([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
