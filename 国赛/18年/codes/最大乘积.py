import math
import itertools


def rule(x):
    for i in range(1, 10):
        if x.count(str(i)) != 1:
            return False
    return True


MAX = 0
x = list(itertools.permutations(range(1, 10), 9))
for each in x:
    number = ''.join(list(map(str, each)))
    for j in range(1, 8):
        a = int(number[:j])
        b = int(number[j:])
        c = str(a * b)
        if len(c) == 9:
            if rule(c):
                if int(c) > MAX:
                    MAX = int(c)
print(MAX)
# print(839542176)
