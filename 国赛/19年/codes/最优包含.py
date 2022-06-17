from cmath import inf

s = input().strip()
t = input().strip()
n = len(s)
m = len(t)

dp = [[inf for j in range(m + 1)] for i in range(n + 1)]
for i in range(n + 1):
    dp[i][0] = 0

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if s[i - 1] == t[j - 1]:
            dp[i][j] = dp[i - 1][j - 1]
        else:
            dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1] + 1)
print(dp[n][m])