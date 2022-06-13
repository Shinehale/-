N = int(input())
R1 = list(map(int, input().split()))
R2 = list(map(int, input().split()))
ins = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def check():
    for i in range(N):
        if S1[i] != R1[i]:
            return False
        if S2[i] != R2[i]:
            return False
    return True


def calc(item):
    ans = item[0] * N + item[1]
    return ans


def dfs(x, y):
    if x == N - 1 and y == N - 1:
        if check():
            for item in ans:
                print(calc(item), end=" ")
        return
    for each in ins:
        new_x = x + each[0]
        new_y = y + each[1]
        if new_x >= N or new_y >= N or new_x < 0 or new_y < 0:
            continue
        if vis[new_x][new_y]:
            continue
        if S1[new_y] > R1[new_y]:
            continue
        if S2[new_x] > R2[new_x]:
            continue
        vis[new_x][new_y] = True
        S1[new_y] += 1
        S2[new_x] += 1
        ans.append((new_x, new_y))
        dfs(new_x, new_y)
        vis[new_x][new_y] = False
        S1[new_y] -= 1
        S2[new_x] -= 1
        ans.pop()


S1 = [0 for i in range(N)]
S2 = [0 for i in range(N)]
vis = [[False for i in range(N)] for j in range(N)]
ans = [(0, 0)]
S1[0] = 1
S2[0] = 1
vis[0][0] = True
dfs(0, 0)

# C语言网过了，但是蓝桥杯的网站好像大家都超时