fibonacci = [1, 1]
pre_num_1 = 1
pre_num_2 = 1
index = 2

for x in range(3, 101):
    fibonacci.append(pre_num_1 + pre_num_2)
    pre_num_2 = pre_num_1
    pre_num_1 = fibonacci[index]
    index += 1

print fibonacci
