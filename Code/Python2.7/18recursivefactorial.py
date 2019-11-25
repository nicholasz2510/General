dic = {}

def fac(l):
    if l in dic:
        return dic[l]
    if l == 1:
        return 1
    dic[l] = l * fac(l-1)
    return dic[l]

print fac(10)
print fac(20)
print fac(30)
