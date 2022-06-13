import math

N=int(input())
dp=[[0 for i in range(N+1)] for j in range(N+1)]
a=[[0 for i in range(N)]for k in range(N)]
for i in range(N):
    R=list(map(int,input().split()))
    for j in range(len(R)):
        a[i][j]=R[j]
dp[0][0]=a[0][0]
for i in range(0,N-1):
    for j in range(i+1):
        dp[i+1][j]=max(dp[i+1][j],dp[i][j]+a[i+1][j])
        dp[i+1][j+1]=max(dp[i+1][j+1],dp[i][j]+a[i+1][j+1])
if (N%2):
    print(dp[N-1][N//2])
else:
    print(max(dp[N-1][(N//2)-1]),dp[N-1][(N//2)])
"""
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
"""
"""
import os
import sys

n = int(input())
q = []
dp = [[0 for j in range(1,i+1)]for i in range(1,n+1)]
for i in range(n):
    q.append(list(map(int,input().split())))
dp[0][0] = q[0][0]
for i in range(1,n):
    for j in range(i+1):
        if j == 0 :
            dp[i][j] = dp[i-1][j]+q[i][j]
        elif i == j:
            dp[i][j] = dp[i-1][j-1]+q[i][j]
        else:
            dp[i][j] = q[i][j]+max(dp[i-1][j-1],dp[i-1][j])
if n%2 == 1:
  print(dp[n-1][n//2])
else:
  print(max(dp[n-1][(n//2)-1],dp[n-1][n//2]))
"""
