from sys import stdin

in_set = {int(x) for x in stdin.readline().split()}

sums = set()


def total(unused, ct):
    if unused == set():
        sums.add(ct)
        return

    for n in unused:
        total(unused.discard(n), ct + n)
        total(unused, ct)

print total(in_set, 0)
