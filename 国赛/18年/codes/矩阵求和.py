import math
N = int(1e3+7)
M = pow(10,9)+7
R = list(map(int,input().split()))
n = R[0]
a = [[0]*N]*N
for i in range(1,n+1):
    for j in range(1,n+1):
        k = math.gcd(i,j)
        a[i][j] = k*k
        print(a[i][j],end=" ")
    print()
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(a[i][j],end = ' ')
#     print()

"""
好吧，正解是莫比乌斯反演加杜教筛
属实是才疏学浅，run了
"""