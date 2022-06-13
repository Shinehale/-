import os
import sys
import math


# def gcd(x, y):
#     if x % y == 0:
#         return y
#     else:
#         return gcd(y, x % y)


ans = 0
for i in range(1, 2021, 1):
    for j in range(1, 2021, 1):
        if math.gcd(i, j) == 1:
            ans += 1

print(ans)
"""
math.gcd()调用速度明显比自己手写要快
可能是inline函数的缘故
反正需要系统学习一下math模块的用法
"""