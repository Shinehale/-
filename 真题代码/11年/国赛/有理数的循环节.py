"""
题目描述：
1/7 = 0.142857142 是个无限循环小数。
任何有理数都可以表示为无限循环小数的形式。
题目要求即是：给出一个数字的循环小数表示法。
输入：
1,7
输出：
0.[142857]
"""
import os
import sys

R = input().split(',')
a, b = int(R[0]), int(R[1])
s, tar = "", ""
flag = True
T_pos = 0
over = a // b
a = a % b
for i in range(100):
    p = a * 10 // b
    s = s + str(p)
    a = a * 10 % b
    if a == 0:
        flag = False
        break
pause = False
for i in range(100):
    for j in range(i):
        pos = s.find(s[j:i], i)
        if pos == i:
            tar = s[j:i]
            T_pos = j
            pause = True
            break
    if pause:
        break
if not flag:
    print(over, end=".")
    print(s)
else:
    print(over, end=".")
    print(s[0:T_pos], end="")
    print("[{:s}]".format(tar))

# 状态：1A
