n = int(raw_input("What would you like to use for n? "))
sum_or_product = raw_input("Would you like to compute the sum or product of 1 through n? Please type sum or product. ")
one_through_n = []

for x in range(1, (n + 1)):
    one_through_n.append(x)

if sum_or_product == "sum":
    answer = 0
    for x in one_through_n:
        answer += x
elif sum_or_product == "product":
    answer = 1
    for x in one_through_n:
        answer *= x

print "Your answer is " + answer
