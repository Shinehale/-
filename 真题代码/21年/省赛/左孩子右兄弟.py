import sys
sys.setrecursionlimit(1000000)
def dfs(x):
    size = len(Map[x])
    ans = 0
    for i in range(len(Map[x])):
        ans = max(ans, dfs(Map[x][i]))
    return ans + size


N = int(input())
Map = {}
for i in range(N):
    Map[i] = []
for i in range(1, N):
    x = int(input())
    Map[x - 1].append(i)
ret = dfs(0)
print(ret)

"""
11
1
1
1
2
2
6
6
6
4
4
"""
