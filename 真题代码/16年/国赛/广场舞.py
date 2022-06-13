import math
import sys


def toLeft(i, j, S):
    ret = P[i][0] * P[j][1] - P[i][1] * P[j][0] + \
          P[j][0] * S[1] - P[j][1] * S[0] + \
          S[0] * P[i][1] - S[1] * P[i][0]
    if ret > 0:
        return 1
    elif ret == 0:
        return 2
    else:
        return 0


def check(x, y):
    i, j = 0, N - 1
    S = (x, y)
    flag = toLeft(i, j, S)
    for times in range(N):
        value = toLeft(i, j, S)
        j = i
        i = i + 1
        if value == 2:
            continue
        if flag == 2:
            flag = value
            continue
        if flag != value:
            return False
    return True


N = int(input())
P = [[0 for j in range(2)] for i in range(N)]
ans = 0
max_x, max_y = -100000, -100000
min_x, min_y = 100000, 100000
for i in range(N):
    R = list(map(int, input().split()))
    P[i][0], P[i][1] = R[0], R[1]
    max_x = max(R[0], max_x)
    max_y = max(R[1], max_y)
    min_x = min(R[0], min_x)
    min_y = min(R[1], min_y)
"""
for i in range(min_x,max_x,1):
    for j in range(min_y,max_y,1):
        if check(i,j) and check(i+1,j) and check(i+1,j+1) and check(i,j+1):
            print(i,j)
            ans+=1
"""
print(check(2, 3))
print(ans)
"""
本题目不能使用toLeft测试，因为这个图形可能是凹多边形，不是凸多边形
"""
