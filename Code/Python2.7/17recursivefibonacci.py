dic = {}

def fib(n):
    if n in dic:
        return dic[n]
    if n == 1 or n == 2:
        return 1
    dic[n] = fib(n-1) + fib(n-2)
    return dic[n]


print fib(30)
print fib(5)
print fib(10)
print fib(20)

print dic
