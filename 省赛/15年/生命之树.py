import sys

sys.setrecursionlimit(100000)
class Graph:
    def __init__(self, n):
        self.G = {}
        for i in range(n):
            self.G[i] = []
        self.size = n

    def add_edge(self, x, y):
        self.G[x].append(y)


ans = 0


def dfs(pos, fa):
    global ans
    dp[pos] = a[pos]
    for item in Gra.G[pos]:
        if item == fa:
            continue
        dp[item]=dfs(item, pos)
        if dp[item] > 0:
            dp[pos] = dp[pos] + dp[item]
    ans = max(ans, dp[pos])
    return dp[pos]


N = int(input())
a = list(map(int, input().split()))
Gra = Graph(N)
dp = [0 for i in range(N)]
for i in range(N - 1):
    R = list(map(int, input().split()))
    x, y = R[0] - 1, R[1] - 1
    Gra.add_edge(x, y)
    Gra.add_edge(y, x)
dfs(0, 0)
print(ans)
# //注意出现递归爆栈的情况
