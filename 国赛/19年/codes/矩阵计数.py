import sys


N, M = list(map(int, sys.stdin.readline().strip().split()))
numState = 2 ** M

stateAllowed = []
for i in range(numState):
    cnt, flag = 0, False
    temp = i
    while temp:
        if temp & 1:
            cnt += 1
        else:
            cnt = 0
        if cnt >= 3:
            flag = True
            break
        temp >>= 1
    if not flag:
        stateAllowed.append(i)

dp = [[[0 for _ in range(numState)] for __ in range(numState)] for ___ in range(N)]
for i in stateAllowed:
    dp[0][i][0] = 1
for i in range(1, N):
    for j in stateAllowed:
        for k in stateAllowed:
            for p in stateAllowed:
                if j & k & p == 0:
                    dp[i][j][k] += dp[i - 1][k][p]
ans = 0
for i in stateAllowed:
    ans += sum(dp[N - 1][i])
print(ans)

