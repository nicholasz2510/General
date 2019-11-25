from sys import stdin
import time

start = time.process_time()

input_list = [int(x) for x in stdin.readline().strip()]

stack = [input_list[0]]


def what_to_push(curr_x):
    if not stack:
        return curr_x
    top_of_stack = stack[-1]
    if curr_x == top_of_stack:
        return curr_x
    stack.pop()
    return what_to_push((3 - curr_x) - top_of_stack)


for x in input_list[1:]:
    stack.append(what_to_push(x))

print(stack)
print("time taken: " + str(time.process_time() - start) + " seconds")
