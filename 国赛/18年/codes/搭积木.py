n, m = map(int, input().strip().split())
mod = 1000000007

check = [[0 for j in range(m + 1)] for i in range(n + 1)]
dp = [[0 for j in range(m + 2)] for i in range(m + 1)]

for i in range(1, n + 1):
    G = input()
    for j in range(1, m + 1):
        check[i][j] = check[i][j - 1]
        if G[j - 1] == 'X':
            check[i][j] = check[i][j] + 1

ans = 1
for i in range(1, m + 1):
    for j in range(m, i - 1, -1):
        if check[n][j] - check[n][i - 1] == 0:
            ans = ans + 1
            dp[i][j] = dp[i][j + 1] + dp[i - 1][j] - dp[i - 1][j + 1] + 1
for t in range(n - 1, 0, -1):
    for i in range(1, m + 1):
        for j in range(m, i - 1, -1):
            if check[t][j] - check[t][i - 1] == 0:
                ans = (ans + dp[i][j]) % mod
                dp[i][j] = (dp[i][j] + dp[i - 1][j] + dp[i][j + 1] - dp[i - 1][j + 1]) % mod
            else:
                dp[i][j] = 0

print(ans)