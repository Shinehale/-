"""
容易想到A是2次指数，B是3次指数，显然B增长更快，则考虑先尽可能增加B，使得d增量尽可能大
同时，应尽可能在后期增加A，使得d增量尽可能大
"""
import math

R = list(map(int, input().split()))
n1, n2 = R[0], R[1]
a1 = list(map(int, input().split()))
for i in range(int(n1)):
    a1[i] = (a1[i], i + 1)
a2 = list(map(int, input().split()))
for i in range(int(n2)):
    a2[i] = (a2[i], i + 1)
s = input()
a1.sort(key=lambda x: x[0])
a2.sort(key=lambda x: -x[0])
pos1, pos2 = 0, 0
for each in s:
    if each == '0':
        print('A%d' % (a1[pos1][1]))
        pos1 += 1
    elif each == '1':
        print("B%d" % (a2[pos2][1]))
        pos2 += 1
print('E')
