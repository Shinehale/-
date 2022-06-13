# 牛顿迭代的基本思想是：
# 利用x(n+1)=x(n)-f(x(n))/g(x(n))
# 其中g(x)是f(x)的导函数
# 本题是用求解x^3-m=0这个方程的解作为蓝本

import os
import sys
import math

def f(x,m):
    return pow(x,3)-m
def g(x):
    return 3*pow(x,2)
T=int(input())
for i in range(T):
    N=int(input())
    x=5
    while abs(f(x,N))>=0.0000000001 :
        g_value=g(x)
        if g_value==0:
            x=2.0
            continue
        x=x-f(x,N)/g_value
    print("{:.3f}".format(x))

