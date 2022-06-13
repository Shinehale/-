import os
import sys

s = [[] for i in range(5)]
dt = {}
st = input()
R = input()
c = -1
pos = 0
ans = ""
for i in range(len(st)):
    if st[i] not in dt:
        dt[st[i]] = 1
    if pos % 5 == 0: c += 1
    s[c].append(st[i])
    pos += 1
for i in range(26):
    op = chr(ord("a") + i)
    if op not in dt:
        if pos % 5 == 0: c += 1
        if c == 5:
            break
        s[c].append(op)
        pos += 1
dic = {}
for i in range(5):
    for j in range(5):
        dic[s[i][j]] = (i, j)
for i in range(0, len(R) - 1, 2):
    x, y = R[i], R[i + 1]
    if x not in dic or y not in dic:
        ans += x + y
    elif x == y:
        ans += x + x
    else:
        tup1, tup2 = dic[x], dic[y]
        if tup1[0] == tup2[0] or tup1[1] == tup2[1]:
            ans += y + x
        else:
            ans += s[tup1[0]][tup2[1]] + s[tup2[0]][tup1[1]]
if len(R) % 2 == 1:
    ans += R[-1]
print(ans)
