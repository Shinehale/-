import math

INF = 2147483641


def dfs(x, y, val, step):
    if x == n - 1 and y == n - 1:
        global reach, ans
        reach = True
        ans = min(ans, step)
        return
    for each in direct:
        newX = x + each[0]
        newY = y + each[1]
        if newX < 0 or newY < 0 or newX >= n or newY >= n:
            continue
        if val>0:
            if mp[newX][newY] != '#':
                dfs(newX,newY,val-1, step + 1)
        if not vis[newX][newY]:
            if mp[newX][newY] == '.':
                vis[newX][newY] = True
                if val == 0:
                    dfs(newX, newY, 0, step + 1)
                else:
                    dfs(newX, newY, val - 1, step + 1)
                vis[newX][newY] = False
            elif mp[newX][newY] == '#':
                continue
            elif mp[newX][newY] == '%':
                vis[newX][newY] = True
                dfs(newX, newY, k, step + 1)
                vis[newX][newY] = False
            elif mp[newX][newY] == 'X':
                if val:
                    vis[newX][newY] = True
                    dfs(newX, newY, val - 1, step + 1)
                    vis[newX][newY] = False
                else:
                    continue


R = list(map(int, input().split()))
n, k = R[0], R[1]
vis = [[False for i in range(n) ] for j in range(n)]
reach = False
ans = INF
mp = []
direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]

for i in range(n):
    R = input()
    mp.append(R)

dfs(0, 0, 0, 0)

if not reach:
    print(-1)
else:
    print(ans)

"""
5 3
...XX
##%#.
...#.
.###.
.....

上述代码在
https://www.dotcpp.com/oj/problem2295.html
中只有36分
说明dfs仍有明显问题
最好的办法是写BFS但是我不想写了嘿嘿
"""
